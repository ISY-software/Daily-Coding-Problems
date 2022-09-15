#!/bin/python3
# -*- encoding: utf-8 -*-


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTrzee(tree):
    lst = []
    phelper(tree, lst, 0)
    print(lst)


def phelper(tree, lst, lvl):
    lvl = 0
    rootPath = [tree]
    rsltL = [[]]
    loopT = 1
    count = 0
    expand = True
    while expand:
        expand = False
        for i in range(loopT):
            tmpTree = rootPath.pop(0)
            if tmpTree is None:
                rootPath.append(None)
                rootPath.append(None)
                rsltL[lvl].append(None)
                continue
            expand = True
            rsltL[lvl].append(tmpTree.val)
            rootPath.append(tmpTree.left)
            rootPath.append(tmpTree.right)
        lvl+=1
        rsltL.append([])
        loopT *=2

    print(rsltL)

treee = Node('a',
             Node('b',
                  Node('C'),
                  Node('d',
                       Node ('I'),
                       Node ('J'))
                  ),
             Node('e',
                  Node('f',
                       Node('H')
                       ),
                  Node('g',
                       None,
                       Node ('K'))
                  )
             )
printTrzee(treee)
