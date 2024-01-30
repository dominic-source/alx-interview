#!/usr/bin/python3

"""This module consist of a function that
    detect a valid utf-8 encoding in a data
"""


def validUTF8(data):
    """Detect a valid utf-8 encoding"""
    byte = data[0]
    data_s = data[1:]
    if byte <= 0b01111111:
        # single byte
        for i in data_s:
            if not (i <= 0b01111111):
                return False
    elif byte >= 0b11000000:
        # two bytes
        for i in data_s:
            if (i & 0b1000000) == 0:
                return False
    return True
