#!/usr/bin/python3

import sys

file = sys.argv[1]

countline=0
with open(file) as fd:
    for line in fd:
        countline=countline+1

print(countline)
