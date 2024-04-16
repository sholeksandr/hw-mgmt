#!/usr/bin/python
# pylint: disable=line-too-long
# pylint: disable=C0103
# pylint: disable=W0718
# pylint: disable=R0913:

########################################################################
# Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES.
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

import os
import sys
import time
import pdb

atttrib_list = {
    "NVLink_Switch_Scaleout": [
        {"fin": "/sys/devices/platform/mlxplat/mlxreg-io/hwmon/{}/fan1",
         "fn": "run_cmd",
         "arg": ["/usr/bin/hw-management-chassis-events.sh hotplug-event FAN1 {arg1}"],
         "poll": 5, "ts": 0},
        {"fin": "/sys/devices/platform/mlxplat/mlxreg-io/hwmon/{}/fan2",
         "fn": "run_cmd",
         "arg":["/usr/bin/hw-management-chassis-events.sh hotplug-event FAN2 {arg1}"],
         "poll": 5, "ts": 0},
        {"fin": "/sys/devices/platform/mlxplat/mlxreg-io/hwmon/{}/fan3",
         "fn": "run_cmd",
         "arg": ["/usr/bin/hw-management-chassis-events.sh hotplug-event FAN3 {arg1}"],
         "poll": 5, "ts": 0},
        {"fin": "/sys/devices/platform/mlxplat/mlxreg-io/hwmon/{}/fan4",
         "fn": "run_cmd",
         "arg": ["/usr/bin/hw-management-chassis-events.sh hotplug-event FAN4 {arg1}"],
         "poll": 5, "ts": 0},
        {"fin": "/sys/devices/platform/mlxplat/mlxreg-io/hwmon/{}/fan5",
         "fn": "run_cmd",
         "arg": ["/usr/bin/hw-management-chassis-events.sh hotplug-event FAN5 {arg1}"],
         "poll": 5, "ts": 0},
        {"fin": "/sys/devices/platform/mlxplat/mlxreg-io/hwmon/{}/fan6",
         "fn": "run_cmd",
         "arg": ["/usr/bin/hw-management-chassis-events.sh hotplug-event FAN6 {arg1}"],
         "poll": 5, "ts": 0},
        {"fin": "/sys/devices/platform/mlxplat/mlxreg-io/hwmon/{}/leakage1",
         "fn": "run_cmd",
         "arg": ["/usr/bin/hw-management-chassis-events.sh hotplug-event LEAKAGE1 {arg1}"],
         "poll": 2, "ts": 0},
        {"fin": "/sys/devices/platform/mlxplat/mlxreg-io/hwmon/{}/leakage1",
         "fn": "run_cmd",
         "arg": ["/usr/bin/hw-management-chassis-events.sh hotplug-event LEAKAGE2 {arg1}"],
         "poll": 2, "ts": 0},
        {"fin": "/sys/devices/platform/mlxplat/mlxreg-io/hwmon/{}/leakage_rope1",
         "fn": "run_cmd",
         "arg": ["/usr/bin/hw-management-chassis-events.sh hotplug-event LEAKAGE_ROPE1 {arg1}"],
         "poll": 2, "ts": 0},
        {"fin": "/sys/devices/platform/mlxplat/mlxreg-io/hwmon/{}/leakage_rope2",
         "fn": "run_cmd",
         "arg": ["/usr/bin/hw-management-chassis-events.sh hotplug-event LEAKAGE_ROPE2 {arg1}"],
         "poll": 2, "ts": 0},
        {"fin": "/sys/devices/platform/mlxplat/mlxreg-io/hwmon/{}/power_button",
         "fn": "run_cmd",
         "arg": ["/usr/bin/hw-management-chassis-events.sh hotplug-event POWER_BUTTON {arg1}"],
         "poll": 1, "ts": 0},
        
        {"fin": "/sys/module/sx_core/asic0/temperature/input",
         "fn": "asic_temp_populate",
         "arg" : ["asic"],
         "poll": 3, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/temperature/input",
         "fn": "asic_temp_populate",
         "arg" : ["asic2"],
         "poll": 3, "ts": 0},
        
        {"fin": "/sys/module/sx_core/asic0/module0/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module1"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module1/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module2"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module2/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module3"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module3/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module4"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module4/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module5"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module5/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module6"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module6/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module7"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module7/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module8"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module8/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module9"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module9/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module10"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module10/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module11"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module11/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module12"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module12/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module13"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module13/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module14"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module14/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module15"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module15/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module16"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module16/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module17"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module17/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module18"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module18/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module19"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module19/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module20"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module20/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module21"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module21/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module22"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module22/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module23"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module23/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module24"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module24/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module25"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module25/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module26"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module26/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module27"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module27/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module28"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module28/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module29"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module29/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module30"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module30/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module31"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module31/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module32"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module32/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module33"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module33/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module34"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module34/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module35"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic0/module35/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module36"], "poll": 20, "ts": 0},
        
        {"fin": "/sys/module/sx_core/asic1/module0/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module37"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module1/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module38"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module2/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module39"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module3/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module40"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module4/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module41"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module5/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module42"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module6/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module43"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module7/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module44"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module8/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module45"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module9/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module46"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module10/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module47"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module11/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module48"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module12/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module49"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module13/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module50"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module14/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module51"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module15/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module52"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module16/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module53"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module17/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module54"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module18/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module55"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module19/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module56"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module20/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module57"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module21/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module58"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module22/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module59"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module23/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module60"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module24/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module61"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module25/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module62"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module26/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module63"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module27/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module64"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module28/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module65"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module29/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module66"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module30/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module67"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module31/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module68"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module32/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module69"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module33/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module70"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module34/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module71"], "poll": 20, "ts": 0},
        {"fin": "/sys/module/sx_core/asic1/module35/temperature/input",
         "fn": "module_temp_populate", "arg" : ["module72"], "poll": 20, "ts": 0}
        
    ],
    "test": [
        {"fin": "/tmp/hwmon/{}/fan1",
         "cmd": "/usr/bin/hw-management-chassis-events.sh hotplug-event FAN1 {arg1}",
         "poll": 5, "ts": 0}
    ]
}

# ----------------------------------------------------------------------
def run_cmd(cmd_list, arg):
    for cmd in cmd_list:
        cmd = attr_prop["cmd"] + " 2> /dev/null 1> /dev/null"
        os.system(cmd.format(arg1=arg))

# ----------------------------------------------------------------------
def asic_temp_populate(arg_list, arg):
    ''
    val = arg * 125
    f_name = "/var/run/hw-management/thermal/{}".format(arg_list[0])
    with open(f_name, 'w', encoding="utf-8") as f:
        f.write(arg)

    f_name = "/var/run/hw-management/thermal/{}_temp_trip_crit".format(arg_list[0])
    if not os.path.isfile(f_name):
        with open(f_name, 'w', encoding="utf-8") as f:
            f.write("105000")

        f_name = "/var/run/hw-management/thermal/{}_temp_emergency".format(arg_list[0])
        with open(f_name, 'w', encoding="utf-8") as f:
            f.write("120000")

        f_name = "/var/run/hw-management/thermal/{}_temp_crit".format(arg_list[0])
        with open(f_name, 'w', encoding="utf-8") as f:
            f.write("85000")

        f_name = "/var/run/hw-management/thermal/{}_temp_norm".format(arg_list[0])
        with open(f_name, 'w', encoding="utf-8") as f:
            f.write("75000")

# ----------------------------------------------------------------------
def module_temp_populate(arg_list, arg):
    ''
    val = arg * 125
    f_name = "/var/run/hw-management/thermal/{}".format(arg_list[0])
    with open(f_name, 'w', encoding="utf-8") as f:
        f.write(arg)

    f_name = "/var/run/hw-management/thermal/{}_temp_crit".format(arg_list[0])
    if not os.path.isfile(f_name):
        with open(f_name, 'w', encoding="utf-8") as f:
            f.write("70000")

        f_name = "/var/run/hw-management/thermal/{}_temp_emergency".format(arg_list[0])
        with open(f_name, 'w', encoding="utf-8") as f:
            f.write("75000")

        f_name = "/var/run/hw-management/thermal/{}_temp_fault".format(arg_list[0])
        with open(f_name, 'w', encoding="utf-8") as f:
            f.write("0")

        f_name = "/var/run/hw-management/thermal/{}_temp_trip_crit".format(arg_list[0])
        with open(f_name, 'w', encoding="utf-8") as f:
            f.write("120000")


# ----------------------------------------------------------------------
def update_attr(attr_prop):
    """
    @summary: Update hw-mgmt attributes and invoke cmd per attr change
    """
    ts = time.time()
    if ts >= attr_prop["ts"]:
        # update timestamp
        attr_prop["ts"] = ts + attr_prop["poll"]
        # update file
        fin = attr_prop["fin"].format(attr_prop["hwmon"])
        if  os.path.isfile(fin):
            with open(fin, 'r', encoding="utf-8") as f:
                val = f.read().rstrip('\n')
            if "oldval" not in attr_prop.keys() or attr_prop["oldval"] != val:
                attr_prop["oldval"] = val
                fn_name = attr_prop["fn"]
                argv = attr_prop["arg"]
                try:
                    globals()[fn_name](argv, val)
                except:
                    pass


def init_attr(attr_prop):
    if "hwmon" in attr_prop["fin"]:
        path = attr_prop["fin"].split("hwmon")[0]
        try:
            flist = os.listdir(os.path.join(path, "hwmon"))
            hwmon_name = [fn for fn in flist if "hwmon" in fn]
            attr_prop["hwmon"] = hwmon_name[0]
        except Exception as e:
            attr_prop["hwmon"] = ""

def main():
    """
    @summary: Update attributes
    arg1: system type
    """

    args = len(sys.argv) - 1

    if args < 1:
        try:
            f = open("/sys/devices/virtual/dmi/id/product_name", "r")
            system_type = f.read()
        except Exception as e:
            system_type = ""
    else:
        system_type = sys.argv[1]

    if system_type not in atttrib_list.keys():
        print("Not supported system type: {}".format(system_type))
        sys.exit(1)

    sys_attr = atttrib_list[system_type]
    for attr in sys_attr:
        init_attr(attr)

    while True:
        for attr in sys_attr:
            update_attr(attr)
        time.sleep(1)

if __name__ == '__main__':
    main()