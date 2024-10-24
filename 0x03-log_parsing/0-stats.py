#!/usr/bin/python3
"""
The Script that reads stdin line by line and computes metrics.
"""
import sys

file_total_size = [0]
code_count = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
counter = 0


def print_stats():
    """Print statistics."""
    print("File size: {}".format(file_total_size[0]))
    for key, value in sorted(code_count.items()):
        if value != 0:
            print("{}: {}".format(key, value))


def parse_line(line):
    """
    Check if the line matches the expected format.
    """
    try:
        line = line[:-1]
        status_list = line.split(" ")
        file_total_size[0] += int(status_list[-1])
        status_code = status_list[-2]
        if status_code in code_count:
            code_count[status_code] += 1
    except BaseException:
        pass


if __name__ == '__main__':
    listnumber = 1
    try:
        for line in sys.stdin:
            parse_line(line)
            """Print after every 10 lines"""
            if listnumber % 10 == 0:
                print_stats()
            listnumber += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
