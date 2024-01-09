#!/usr/bin/python3

"""Module to practice python dsa using lockboxes algorithm"""


def canUnlockAll(boxes):
    """find boxes that cannot be unlocked"""

    numOfBoxes = len(boxes)

    setOfKeys = set([0])
    lockedBoxes = set(range(1, numOfBoxes))

    queue = list(boxes[0])

    while queue:
        key = queue.pop(0)
        if key not in setOfKeys:
            setOfKeys.add(key)
            if key in lockedBoxes:
                lockedBoxes.remove(key)
            queue.extend(boxes[key])

    return len(setOfKeys) == numOfBoxes
