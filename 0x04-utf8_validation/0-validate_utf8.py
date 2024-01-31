#!/usr/bin/python3

"""This module consist of a function that
    detect a valid utf-8 encoding in a data
"""


def validUTF8(data):
    """Detect a valid utf-8 encoding"""
    length = len(data)
    j = 0

    while j < length:
        byte = data[j]

        # Check if byte is a start byte for a single byte character
        if (byte & 0b10000000) == 0:
            j += 1
            continue

        # Check if byte is a multibyte character
        count = 0
        while count < 8 and byte & (0b10000000 >> count) != 0:
            count += 1

        # Check for invalid byte
        if count == 1 or count > length:
            return False

        # check for continuation byte
        for i in range(0, count):
            j += 1
            if j >= len(data) or (data[j] & 0b11000000) != 0b10000000:
                return False
        if (data[count + j - 1] & 0b11000000) == 0b10000000:
            return False
        j += 1
    return True
