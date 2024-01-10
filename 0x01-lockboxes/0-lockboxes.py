#!/usr/bin/python3

"""Module to practice python dsa using lockboxes algorithm"""


def canUnlockAll(boxes):
    """find boxes that cannot be unlocked"""

    setOfKeys = set([0])
    lockedBoxes = set()

    for idx, box in enumerate(boxes):
        if idx not in setOfKeys:
            lockedBoxes.add(idx)
        elif idx in setOfKeys:
            setOfKeys.update(box)
        for locked in lockedBoxes:
            if locked in setOfKeys:
                setOfKeys.update(boxes[locked])
    return len(setOfKeys) == len(boxes)
