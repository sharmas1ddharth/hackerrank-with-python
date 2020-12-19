#!/bin/python3

import sys


S = input().strip()

try:
    conversion = int(S)
    print(conversion)
except:
    print("Bad String")