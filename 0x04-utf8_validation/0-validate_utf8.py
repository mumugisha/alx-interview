#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validate if the data set represents a valid UTF-8 encoding.
    """
    data_byte_count = 0

    for byte in data:
        if data_byte_count == 0:
            if byte >> 5 == 0b110:
                data_byte_count = 1
            elif byte >> 4 == 0b1110:
                data_byte_count = 2
            elif byte >> 3 == 0b11110:
                data_byte_count = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            data_byte_count -= 1

    return data_byte_count == 0
