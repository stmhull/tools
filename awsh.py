#!/usr/bin/env python3
import sys
import subprocess
import argparse

STAGING = "54.197.32.199"
PROD = "54.172.55.226"

parser = argparse.ArgumentParser(description="SSH into one of the EC2 instances.", prog="awsh")
parser.add_argument('environment', help="Environment, either staging or production",
                    nargs="?", default="production", choices=["production", "staging", "ip"])
parser.add_argument('--keygen', help="Generate a new key for when the host key changes", 
                    nargs="?", choices=["production", "staging"])
args = vars(parser.parse_args())

command = "ssh -i ~/.ssh/amazon-linux.pem ec2-user@"

print(args['keygen'])

if args['keygen'] == "staging":
  subprocess.run(("ssh-keygen -R " + STAGING).split(" "))
elif args['keygen'] == "production":
  subprocess.run(("ssh-keygen -R " + PROD).split(" "))

if args["environment"] == "production":
    subprocess.run((command + PROD).split(" "))
else:
    subprocess.run((command + STAGING).split(" "))