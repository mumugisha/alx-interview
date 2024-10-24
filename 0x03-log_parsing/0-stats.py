#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys

code_count = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}
file_total_size = 0
counter = 0

try:
    for line in sys.stdin:
        status_list = line.split(" ")

        if len(status_list) > 4:
            code = status_list[-2]
            size = int(status_list[-1])

            if code in code_count.keys():
                code_count[code] += 1
                file_total_size += size

            counter += 1
            if counter == 10:
                counter = 0
                print("File size: {}".format(file_total_size))
                for key, value in sorted(code_count.items()):
                    if value != 0:
                        print("{}: {}".format(key, value))
except Exception:
    pass

finally:
    print("File size: {}".format(file_total_size))
    for key, value in sorted(code_count.items()):
        if value != 0:
            print("{}: {}".format(key, value))
