import subprocess
from typing import List

from credentials import IDRAC_PWD, IDRAC_USER, IDRAC_IP


def execute_ipmi_subcommand(subcommand: str) -> str:
    if IDRAC_IP is None or IDRAC_USER is None or IDRAC_PWD is None:
        print("Error: no credentials filled. Set them in credentials.py")
        exit(-1)

    cmd = f'ipmitool -I lanplus -H {IDRAC_IP} -U {IDRAC_USER} -P {IDRAC_PWD} {subcommand}'
    return str(subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True).stdout.read())


def get_temperatures() -> str:
    return execute_ipmi_subcommand("sdr type temperature")


def get_cpu_temperatures() -> List[int]:
    output = execute_ipmi_subcommand("sdr type temperature | cut -d'|' -f5 | cut -d' ' -f2 | tr '\n' ' '")
    return [int(temp) for temp in output.split(" ")[2:4]]


def set_manual_mode() -> None:
    execute_ipmi_subcommand("raw 0x30 0x30 0x01 0x00")


def set_auto_mode() -> None:
    execute_ipmi_subcommand("raw 0x30 0x30 0x01 0x01")


def set_fan_speed(percent: int) -> None:
    if percent < 0 or percent > 100:
        raise Exception(f"Incorrect value '{percent}'")

    print(f"Set fan speed at {percent}%")
    set_manual_mode()
    execute_ipmi_subcommand(f"raw 0x30 0x30 0x02 0xff {hex(percent)}")
