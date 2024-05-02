#!/usr/bin/python3
"""  reads stdin line by line and computes metrics """
import sys
from collections import Counter
from datetime import datetime


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


def validate_date(Year, time):
    """ Verifying if date is valid"""
    date_y = str(Year)
    date_t = str(time)
    time_clean = date_t.replace(']', '')
    year_clean = date_y.replace('[', '')
    try:
        datetime.strptime(time_clean, '%H:%M:%S.%f')
        datetime.strptime(year_clean, '%Y-%m-%d')
    except ValueError:
        return False


def verify_format(Line):
    """ format must be <IP Address> -
    [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
    """
    valid_status = [200, 301, 400, 401, 403, 404, 405, 500]
    try:
        int(Line[8])
        int(Line[7])
    except ValueError:
        return False
    if (validate_ip(Line[0]) is False or
            len(Line) != 9 or Line[5] != "/projects/260" or
            Line[1] != "-" or Line[4] != "\"GET" or
            validate_date(Line[2], Line[3]) is False or
            int(Line[7]) not in valid_status or
            Line[6] != "HTTP/1.1\""):
        return False
    return True


if __name__ == "__main__":
    status = []
    elements = Counter()
    size = 0
    c = 0
    try:
        for line in sys.stdin:
            c += 1
            data = line.rstrip()
            parts = data.split()
            if verify_format(parts):
                status.append(parts[7])
                elements.update([parts[7]])
                size += int(parts[8])
            if c % 10 == 0:
                print(f"File size: {size}")
                for code, count in sorted(elements.items()):
                    print(f"{code}: {count}")
            if c % 10 == 0 or line.strip() == "":
                status.clear()
    except KeyboardInterrupt as err:
        print(f"File size: {size}")
        for code, count in sorted(elements.items()):
            print(f"{code}: {count}")
        raise
