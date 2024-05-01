#!/usr/bin/python3
import sys
from collections import Counter

status = []
for _ in range(10000):
    elements = []
    size = 0
    try:
        for _ in range(10):
            data = input()
            parts = data.split()
            size += int(parts[8])
            status.append(parts[7])
            elements = Counter(status)
        print(f"File size: {size}")
        for i, k in elements.items():
            print(f"{i}: {k}")
        status.clear()
    except KeyboardInterrupt:
        print(f"File size: : {size}")
        for i, k in elements.items():
            print(f"{i}: {k}")
