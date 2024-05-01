#!/usr/bin/python3
import sys
from collections import Counter

status = []
elements = {}
size = 0
try:
    for _ in range(10000):
        i = 0
        for line in sys.stdin:
            i += 1
            data = line.rstrip()
            parts = data.split()
            size += int(parts[8])
            status.append(parts[7])
            elements = Counter(status)
            if i == 10:
                break
        print(f"File size: {size}")
        for i, k in elements.items():
            print(f"{i}: {k}")
        status.clear()
except KeyboardInterrupt:
    print(f"File size: : {size}")
    for i, k in elements.items():
        print(f"{i}: {k}")
