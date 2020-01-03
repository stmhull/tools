#!/usr/local/bin/python3

import argparse
import time
from datetime import datetime

parser = argparse.ArgumentParser(description="Simple date conversion", prog="sdate")
parser.add_argument("-d", help="Date to epoch", nargs="?")
parser.add_argument("-e", help="Epoch to date", nargs="?")

args = vars(parser.parse_args())

if args["e"] is not None:
  print(datetime.fromtimestamp(int(args["e"])))

if args["d"] is not None:
  year, month, day = args["d"].split("-")
  print(int(datetime(int(year), int(month), int(day), 0, 0, 0).timestamp()))
