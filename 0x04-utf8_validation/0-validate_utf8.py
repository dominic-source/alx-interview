#!/usr/bin/python3

"""This module consist of a function that
    detect a valid utf-8 encoding in a data
"""


def validUTF8(data):
    """Detect a valid utf-8 encoding"""

    for i in data:
        test = i & 0xFF
        if test == 0:
            return False
    return True
