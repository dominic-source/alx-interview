#!/usr/bin/python3

"""Module to practice python dsa using lockboxes algorithm"""


def canUnlockAll(boxes):
    """find boxes that cannot be unlocked"""

    setOfKeys = set([0])
    lockedBoxes = set()
    length = len(boxes)

    for idx, box in enumerate(boxes):
        if idx not in setOfKeys:
            lockedBoxes.add(idx)
        elif idx in setOfKeys:
            lockedBoxes.discard(idx)
            setOfKeys.update(box)
        for locked in set(lockedBoxes):
            if locked in setOfKeys:
                lockedBoxes.discard(locked)
                setOfKeys.update(boxes[locked])
    return len(lockedBoxes) == 0
