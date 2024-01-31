#!/usr/bin/python3

"""This module consist of a function that
    detect a valid utf-8 encoding in a data
"""


def validUTF8(data):
    """Detect a valid utf-8 encoding"""
    count = 0
    for i in data:

        # Check for continuation byte
        if (i & 0b10000000) != 0 and (i & 0b01000000) == 0 and count > 0:
            count -= 1
            continue
        elif (i & 0b10000000) != 0 and (i & 0b01000000) == 0 and count <= 0:
            return False
        elif (i & 0b10000000) == 0 and count == 0:
            continue
        elif (i & 0b10000000) == 0 and count > 0:
            return False

        # count the number of initial 1 bit bits
        start_bin = 0b10000000
        while (i & start_bin) and count < 5:
            count += 1
            start_bin >>= 1

    return True
