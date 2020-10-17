# usage : python3 set-fan-speed.py --percent 20

import argparse

from utils import set_fan_speed

parser = argparse.ArgumentParser()
parser.add_argument('--percent', type=int, help='fan speed, in percent', required=True)

if __name__ == "__main__":
    args = parser.parse_args()

    if args.percent < 10 and \
            input("Warning! You are willing to set fan speed to a low value. Continue ? (y/n) : ") != "y":
        exit(0)

    elif args.percent > 100:
        print("Input value > 100%. Exit.")
        exit(-1)

    set_fan_speed(args.percent)
