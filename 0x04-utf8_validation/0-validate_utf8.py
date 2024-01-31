#!/usr/bin/python3

"""This module consist of a function that
    detect a valid utf-8 encoding in a data
"""


def validUTF8(data):
    """Detect a valid utf-8 encoding"""

    if not data:
        return False

    for byte in data:

        # Check if byte is a start byte for a single byte character
        if (byte & 0b10000000) == 0:
            continue

        # Check if byte is a multibyte character
        count = 1
        while count < 8 and byte & (0b10000000 >> count) != 0:
            count += 1

        # Check for invalid byte
        if count == 1 or count > len(data):
            return False

        for i in range(1, count):
            if i >= len(data) or (data[i] & 0b11000000) != 0b10000000:
                return False
    return True
