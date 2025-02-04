#!/bin/bash
##################################################################################
# Copyright (c) 2020 - 2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the names of the copyright holders nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# Alternatively, this software may be distributed under the terms of the
# GNU General Public License ("GPL") version 2 as published by the Free
# Software Foundation.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

# Description: hw-management pre execution script.
#              Checks if service is already running. Just in case, it should
#              be done internally by systemd.
#              Check if by some reason /var/run/hw-management exist.
#              If yes, remove it.
#              Waits in loop until hw-management service can be started.
#              Report start of hw-management service to console and logger.

source hw-management-helpers.sh
[ -f "$board_type_file" ] && board_type=$(< $board_type_file) || board_type="Unknown"
[ -f "$sku_file" ] && product_sku=$(< $sku_file) || product_sku="Unknown"

if systemctl is-active --quiet hw-management; then
        echo "Error: HW management service is already active."
        logger -t hw-management -p daemon.error "HW management service is already active."
        exit 1
fi

if [ -d /var/run/hw-management ]; then
	rm -fr /var/run/hw-management
fi

# If the BSP emulation is not available for the platforms that run in the SimX
# environment, TC need to be stopped. Otherwise enabling TC.
if check_simx; then
    if ! check_if_simx_supported_platform; then
	    if systemctl is-enabled --quiet hw-management-tc; then
		    echo "Stopping and disabling hw-management-tc on SimX"
		    systemctl stop hw-management-tc
		    systemctl disable hw-management-tc
	    fi
	    echo "Start Chassis HW management service."
	    logger -t hw-management -p daemon.notice "Start Chassis HW management service."
	    exit 0
    else
	    if ! systemctl is-enabled --quiet hw-management-tc; then
		    echo "Enabling and starting hw-management-tc"
		    systemctl enable hw-management-tc
		    systemctl start hw-management-tc
	    fi
    fi
fi

case $board_type in
VMOD0014)
	if [ ! -d /sys/devices/pci0000:00/0000:00:1f.0/NVSN2201:00/mlxreg-hotplug/hwmon ]; then
		timeout 180 bash -c 'until [ -d /sys/devices/pci0000:00/0000:00:1f.0/NVSN2201:00/mlxreg-hotplug/hwmon ]; do sleep 0.2; done'
	fi
	;;
*)
	arch=$(uname -m)
	if [ "$arch" = "aarch64" ]; then
		plat_path=/sys/devices/platform/MLNXBF49:00
	else
		plat_path=/sys/devices/platform/mlxplat
	fi
	if [ -d ${plat_path}/mlxreg-hotplug ]; then
		if [ ! -d ${plat_path}/mlxreg-hotplug/hwmon ]; then
			export plat_path
			timeout 180 bash -c 'until [ -d ${plat_path}/mlxreg-hotplug/hwmon ]; do sleep 0.2; done'
		fi
	elif [ ! -d ${plat_path}/mlxreg-io/hwmon ]; then
		export plat_path
		timeout 180 bash -c 'until [ -d ${plat_path}/mlxreg-io/hwmon ]; do sleep 0.2; done'
	fi
	;;
esac
echo "Start Chassis HW management service."
logger -t hw-management -p daemon.notice "Start Chassis HW management service."
