#! /usr/bin/python3

import argparse
import datetime
import time

from utils import get_cpu_temperatures, set_fan_speed, set_auto_mode


def range_limit(arg):
    try:
        f = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Percentage must be an integer")
    if f < 0 or f > 100:
        raise argparse.ArgumentTypeError("Percentage must be < 0 and > 100")
    return f


parser = argparse.ArgumentParser()

parser.add_argument("--first_threshold", type=int, help="Your max temp for threshold 1", default=40)
parser.add_argument("--fan_speed_under_first_threshold", type=range_limit,
                    help="Fan speed (percent) when temps are under threshold 1", default=15)

parser.add_argument("--second_threshold", type=int, help="Your max temp for threshold 2", default=45)
parser.add_argument("--fan_speed_under_second_threshold", type=range_limit,
                    help="Fan speed (percent) when temps are under threshold 2", default=20)

parser.add_argument("--sleep_time", type=int, help="Sleep time (in seconds) between each execution", default=60)


def main():
    print("Reading temperatures sensors for CPUs")
    cpu_temps = get_cpu_temperatures()

    for i, cpu_temp in enumerate(cpu_temps):
        print(f"Temperature on CPU {i}: {cpu_temp} celsius degrees")

    max_temp = max(cpu_temps)

    if max_temp < TEMP_THRESHOLD_1:
        print(f"Temperatures are under threshold 1 ({TEMP_THRESHOLD_1}). "
              f"Set manual mode, {FAN_SPEED_UNDER_THRESHOLD_1_PERCENT}%")
        set_fan_speed(FAN_SPEED_UNDER_THRESHOLD_1_PERCENT)

    elif max_temp < TEMP_THRESHOLD_2:
        print(f"Temperatures are under threshold 2 ({TEMP_THRESHOLD_2}). "
              f"Set manual mode, {FAN_SPEED_UNDER_THRESHOLD_2_PERCENT}%")
        set_fan_speed(FAN_SPEED_UNDER_THRESHOLD_2_PERCENT)

    else:
        print("Max temperature excedeed. Switch to auto mode")
        set_auto_mode()


if __name__ == "__main__":
    args = parser.parse_args()

    TEMP_THRESHOLD_1 = args.first_threshold
    TEMP_THRESHOLD_2 = args.second_threshold

    FAN_SPEED_UNDER_THRESHOLD_1_PERCENT = args.fan_speed_under_first_threshold
    FAN_SPEED_UNDER_THRESHOLD_2_PERCENT = args.fan_speed_under_second_threshold

    SLEEP_TIME = args.sleep_time

    while True:
        print(f"Start at {datetime.datetime.now()}")
        main()

        print(f"Sleeping for {SLEEP_TIME} sec")
        time.sleep(SLEEP_TIME)
