#!/usr/bin/env python3

import subprocess

subprocess.run(["ip", "link", "show", "up"])
print("This program will check your interfaces.")
interface = input("Enter an interface,like, ens3: ")
subprocess.run(["ip", "addr", "show", "dev", "interface"])
subprocess.run(["ip", "route", "show", "dev", "interface"])