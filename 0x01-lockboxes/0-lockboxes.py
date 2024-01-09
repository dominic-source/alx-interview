#!/usr/bin/python3

"""Module to practice python dsa using lockboxes algorithm"""


def canUnlockAll(boxes):
    """find boxes that cannot be unlocked"""

    unlockedBoxes = 0
    setOfKeys = set([0])
    lockedBoxes = set()

    for idx, box in enumerate(boxes):
        if idx not in setOfKeys:
            lockedBoxes.add(idx)
        elif idx in setOfKeys:
            unlockedBoxes += 1
            setOfKeys.update(box)
            for locked in lockedBoxes:
                if locked in setOfKeys:
                    unlockedBoxes += 1
                    setOfKeys.add(locked)
    return unlockedBoxes == len(boxes)
