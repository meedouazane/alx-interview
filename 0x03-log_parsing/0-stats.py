#!/usr/bin/python3
"""  reads stdin line by line and computes metrics """
import sys
from collections import Counter

status = []
elements = {}
sortlist = []
size = 0

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            data = line.rstrip()
            parts = data.split()
            status.append(parts[7])
            elements = Counter(status)
            size += int(parts[8])
            if len(status) == 10:
                print(f"File size: {size}")
                sortlist = sorted(elements.items(), key=lambda x: x[0])
                for i, k in sortlist:
                    print(f"{i}: {k}")
                status.clear()
    except KeyboardInterrupt:
        print(f"File size: : {size}")
        for i, k in sortlist:
            print(f"{i}: {k}")
