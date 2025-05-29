#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    for word in line.strip().split():
        res = re.sub(r'[^a-zA-Z0-9]', '', word)
        if res:
            print(f"{res}\t1")
        