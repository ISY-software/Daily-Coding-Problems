#!/bin/python3
# -*- encoding: utf-8 -*-

import math

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
    # maxStrLen = 0
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
    # print(mxln)
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

# get the K pointer of level
def lvlK(lvl):
    if lvl <= 0:
        return 0
    return (2**(lvl))-1

def phelper2(lst, mxln):
    lenLst = len(lst)-1
    k = mxln
    #charFillNode = '*'
    charFillNode = ' '
    #charFillInitSpaces = '·'
    charFillInitSpaces = ' '
    #charFillBetween = '`'
    charFillBetween = ' '
    charTLeft='\u250c'
    charTRight='\u2510'
    charTUp='\u2534'
    charTSeparator='\u2500'

    for i in range(lenLst):
        #print(i,i-1, lvlK(i-1))
        initSpaces = lvlK(lenLst - i -1)
        betweenSpaces = (initSpaces*2) +1
        betweenString = charFillBetween*(betweenSpaces*k) 
        treeStringUp = ''
        treeStringDown = ''
        flagSide = 'L' # 'L' or 'R'
        actualList = lst[i] 

        # Print up chars
        if i != 0:
            # print init spaces
            print(charFillInitSpaces*(initSpaces*k),end='') # print init spaces
            for j in range( len(actualList)):
                nodej = actualList[j]
                hk = (k-1) / 2
                if (flagSide == 'L'):
                    flagSide = 'R'
                    if nodej is None:
                        print(charFillBetween*k, end='')
                    else:
                        print(charFillBetween*(math.floor(hk)),end='' )
                        #print(str(charTLeft).center(k, charFillNode), end='')
                        print(charTLeft, end='')
                        print(charTSeparator*(math.ceil(hk)),end='' )
                else: 
                    flagSide = 'L'

                    if nodej is None:
                        print(charFillBetween*k, end='')
                    else:
                        print(charTSeparator*(math.floor(hk)),end='' )
                        #print(str(charTRight).center(k, charFillNode), end='')
                        print(charTRight, end='')
                        print(charFillBetween*(math.ceil(hk)),end='' )
            
                if (j != (len(actualList) -1)):

                    if nodej is None:
                        print(charFillBetween*betweenSpaces, end='')
                    else:
                        if (flagSide == 'R'):
                            print(charTSeparator*(initSpaces*k), end='')
                            print(str(charTUp).center(k, charTSeparator), end='')
                            print(charTSeparator*(initSpaces*k), end='')
                        else:
                            print(betweenString, end='')
                else:
                    print()
        # print nodes
        print(charFillInitSpaces*(initSpaces*k),end='') # print init spaces
        for j in range(len(actualList)):
            nodej =  actualList[j]
            #print(nodej, end='')
            if (nodej is None):
                print(charFillBetween*k, end='')
            else:
                print(str(nodej).center(k, charFillNode), end='')
            if j != (len(actualList)-1):
                print(betweenString, end='')
            else:
                print()
            # Print bottom chars

#        lvlMount = (2**(lenLst-i-1)) - 1
#
#        initSpaces = lvlMount * mxln
#        betweenSpaces = ((lvlMount*2)+1) * mxln
#        # # printing the init spaces
#        print(" "*initSpaces, end='')
#        # printing the betweenSpaces and the nodes
#        lvlElmts = lst[i]
#
#        for i in lvlElmts:
#            if i is None:
#                i = "#"
#            print(str(i).center(mxln, '´'), end='')
#            print(' '*betweenSpaces, end='')
#        print()
#
#        # print(lvlMount, (lvlMount*2)+1, initSpaces, betweenSpaces)
#    pass


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
tree2 = Node('Ñ', 
        Node('g',
            Node('e',
                Node('a'),
                Node('b')
                ),
            Node('f',
                Node('c'),
                Node('d')
                )
            ),
        Node('n',
            Node('l',
                Node('h'),
                Node('i')
                ),
            Node('m',
                Node('j'),
                Node('k')
                )
            )
        )


tree3 = Node('Ñ', 
        Node('g',
            Node('e',
                Node('a'),
                Node('b')
                ),
            Node('f',
                Node('c'),
                Node('d')
                )
            ),
        Node('n',None,
            Node('m',
                Node('j'),
                Node('k')
                )
            )
        )

tree4 = Node('Ñ', 
        Node('g',
            Node('e',
                Node('a'),
                Node('b')
                ),
            Node('f',
                Node('c'),
                Node('d')
                )
            ),
        Node('n',
            Node('l',
                Node('h'),
                Node('i')
                )
        )
        )

#printTrzee(treee)
#printTrzee(tree2)
printTrzee(tree4)
