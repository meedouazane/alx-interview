#!/usr/bin/python3
"""  reads stdin line by line and computes metrics """
import sys
from collections import Counter


def validate_ip(ip):
    """ verify if ip address is valid"""
    a = ip.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


def verify_format(Line):
    """ format must be <IP Address> -
    [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
    """
    valid_status = [200, 301, 400, 401, 403, 404, 405, 500]
    if (validate_ip(Line[0]) is False or
            len(Line) != 9 or Line[5] != "/projects/260" or
            Line[1] != "-" or Line[4] != "\"GET" or
            Line[7] not in valid_status or
            Line[6] != "HTTP/1.1\""):
        return False
    try:
        int(Line[8])
    except ValueError:
        return False
    return True


status = []
elements = {}
sortlist = []
size = 0

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            data = line.rstrip()
            parts = data.split()
            if verify_format(parts):
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
