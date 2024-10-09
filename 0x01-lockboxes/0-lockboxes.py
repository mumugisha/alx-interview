#!/usr/bin/python3
"""Lockbox files."""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    Args:
        boxes (list of list of int): List of boxes with keys inside.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    length = len(boxes)
    keys = set()
    open_boxes = []
    a = 0

    while a < length:
        olda = a
        open_boxes.append(a)
        keys.update(boxes[a])

        for key in keys:
            if key != 0 and key < length and key not in open_boxes:
                a = key
                break

        if olda != a:
            continue
        else:
            break

    for a in range(length):
        if a not in open_boxes and a != 0:
            return False

    return True
