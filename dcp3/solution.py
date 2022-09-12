#!/bin/python3
# -*- encoding: utf-8 -*-

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return self.jsonnice(self)

    def jsonnice (self, node) -> str:
        if node != None :
            return 'val:' + node.val + ', left: {' + self.jsonnice(node.left) + '}' + ', right: {' + self.jsonnice(node.left) + '}'
        return 'NONE'


def serialize(root: Node)-> str:
    rl = [root];
    rslt = ''
    while len(rl) != 0:
        current_noe = rl.pop(0);
        if current_noe != None:
            rslt += current_noe.val + ','
            rl.append(current_noe.left)
            rl.append(current_noe.right)
        else:
            rslt += 'None'
    return str(rslt)


def deserialize(s: str)->Node :
    # s = s[1:len(s)-1]
    listOfS = s.split(',')
    rsltNode = Node(listOfS.pop(0))
    parenth =  [rsltNode]
    while(len(parenth) != 0 and len(listOfS) != 0):
        tempNode = parenth.pop(0)
        if tempNode != None :
            lVal = listOfS.pop(0)
            rVal = listOfS.pop(0)
            if lVal != 'None':
                lNode = Node(lVal)
                parenth.append(lNode)
                tempNode.left = lNode
            if rVal != 'None':
                rNode = Node(rVal)
                parenth.append(rNode)
                tempNode.right = rNode
    
    return rsltNode


node = Node('root', 
        Node('left', 
            Node('left.left')), 
        Node('right')
        )
node2 = Node('root',
        Node('rl',
            Node('rl.l',
                Node('rl.l.l'),
                Node('rl.l.r')
                ),
            Node('rl.r',
                Node('rl.r.l'),
                Node('rl.r.r')
                )
            ),
        Node('rr',
            Node('rr.l',
                None,
                Node('rr.l.r')
                ),
            Node('rr.r',
                Node('rr.r.l'),
                )
            ),
        )
assert deserialize(serialize(node)).left.left.val == 'left.left'
