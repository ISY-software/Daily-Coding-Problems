#!/bin/python3
# -*- encoding: utf-8 -*-

class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def counNodes(treeNode : Node) -> int:
    nodeCount = 0
    nodeList = [treeNode]
    for tempNode in nodeList:
        if isinstance(tempNode,Node):
            nodeCount+=1
            nodeList.append(tempNode.left)
            nodeList.append(tempNode.right)
        
    return  nodeCount

treeNode1 = Node('a',
                 Node('b',
                      Node('f'),
                      Node('g')
                      ),
                 Node('c',
                      Node('h'),
                      Node('i')
                      )
                 )

treeNode2 = Node('a',
                 Node('b',
                      Node('f'),
                      ),
                 Node('c',
                      Node('h',
                           Node('j'),
                           Node('k',None, Node('l'))
                           ),
                      Node('i')
                      )
                 )

def testAssert ( testVal, spectedVal):
    assert  testVal == spectedVal, f"should be: {spectedVal}, got: {testVal}"

testAssert (counNodes(treeNode1), 7)
testAssert (counNodes(treeNode2), 9)
