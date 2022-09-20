#!/bin/python3
# -*- encoding: utf-8 -*-


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTrzee(tree):
    lst, mxln = lhelper(tree)
#   phelper(lst, mxln)
    phelper2(lst, mxln)


def lhelper(tree):
    lvl = 0
    rootPath = [tree]
    rsltL = []
    loopT = 1
    expand = True
    maxStrLen = 4
    while expand:
        expand = False
        rsltL.append([])
        for _ in range(loopT):
            tmpTree = rootPath.pop(0)
            if tmpTree is None:
                rootPath.append(None)
                rootPath.append(None)
                rsltL[lvl].append(None)
                continue
            expand = True
            rsltL[lvl].append(tmpTree.val)
            if maxStrLen < len(str(tmpTree.val)):
                maxStrLen = len(str(tmpTree.val))
            rootPath.append(tmpTree.left)
            rootPath.append(tmpTree.right)
        lvl += 1
        loopT *= 2

    return rsltL, maxStrLen


def phelper(lst, mxln):
    print(mxln)
    initSpaces = 2 ** (len(lst)-2)
    betweenSpaces = (initSpaces*2) - 1
    for i in range(len(lst)-1):
        elem = lst[i]
        print(" "*initSpaces, end="")
        for i in range(len(elem)):
            if elem[i] is None:
                print("#", end='')
            else:
                print(elem[i], end='')
            print(" "*(betweenSpaces), end='')
        print()
        initSpaces = int(initSpaces/2)
        betweenSpaces = (initSpaces*2) - 1


def phelper2(lst, mxln):
    lenLst = len(lst)-1
    # beetwrspaces = 1
    for i in range(lenLst):
        initSpaces = (2**(lenLst-i)) - 1
        betweenSpaces = (initSpaces * 2) + 1
        print(initSpaces, betweenSpaces)
    pass


treee = Node('a',
             Node('b',
                  Node('C'),
                  Node('d',
                       Node('I'),
                       Node('J'))
                  ),
             Node('e',
                  Node('f',
                       Node('H')
                       ),
                  Node('g',
                       None,
                       Node('K'))
                  )
             )

printTrzee(treee)
