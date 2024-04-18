#!/usr/bin/python3
''' Opening Lockboxes '''


def canUnlockAll(boxes):
    """ determines if all the boxes can be opened"""
    checked = [False] * len(boxes)

    def dfs(box):
        """ Depth First Search """
        if checked[box]:
            return
        checked[box] = True
        for i in boxes[box]:
            dfs(i)
    dfs(0)
    return all(checked)
