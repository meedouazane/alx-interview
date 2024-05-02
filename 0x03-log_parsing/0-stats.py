#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """

import sys
from collections import Counter


def parse_line(line):
    """ Parses a line and returns IP, status code, and file size """
    parts = line.split()
    if (len(parts) != 9 or parts[4] != "\"GET" or
            parts[5] != "/projects/260" or parts[6] != "HTTP/1.1\""):
        return None, None, None
    ip = parts[0]
    status_code = parts[7]
    try:
        status_code = int(status_code)
    except ValueError:
        return None, None, None
    if status_code not in {200, 301, 400, 401, 403, 404, 405, 500}:
        return None, None, None
    file_size = int(parts[8])
    return ip, status_code, file_size


def print_metrics(total_size, status_counts):
    """ Prints the computed metrics """
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def main():
    status_counts = Counter()
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            ip, status_code, file_size = parse_line(line.strip())
            if ip is None:
                continue
            total_size += file_size
            status_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)
                status_counts.clear()
    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)


if __name__ == "__main__":
    main()
