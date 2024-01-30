#!/usr/bin/python3

"""This module consist of a function that
    detect a valid utf-8 encoding in a data
"""


def validUTF8(data):
    """Detect a valid utf-8 encoding"""

    if not data:
        return False

    for i in data:
        if not (i <= 0b01111111):
            return False
    return True
