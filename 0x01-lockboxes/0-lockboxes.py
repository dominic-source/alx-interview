#!/usr/bin/python3

"""Module to practice python dsa using lockboxes algorithm"""


def canUnlockAll(boxes):
    """find boxes that cannot be unlocked"""

    numOfBoxes = len(boxes)

    unlockedBoxes = {0}
    lockedBoxes = set(range(1, numOfBoxes))

    queue = list(boxes[0])

    while queue:
        key = queue.pop(0)
        if key not in unlockedBoxes:
            unlockedBoxes.add(key)
            if key in lockedBoxes:
                lockedBoxes.remove(key)
            keys = boxes[key])
            for newKey in keys:
                if newKey not in unlockedBoxes:
                    queue.append(newKey)

    return len(unlockedBoxes) == numOfBoxes
