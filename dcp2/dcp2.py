#!/bin/python3
#-*- encoding: utf-8 -*-
import unittest

"""
This aplay divs to caculate the respective product
"""
def productArrDiv(list):
    """docstring for productArrDiv"""
    acom = 1
    for element in list:
        acom *= element

    for i in range(0, len(list)):
        list[i] = acom / list[i]
    return list;

"""
This apply observers to generate the
acomulated product skiping the i
index, not use div
"""
def productArrNoDiv(list):
    n = len(list)
    lsub1 = []
    lsub2 = []
    leftRightObserver = 1;
    rightLeftObserver = 1;
    resl = [1]*n  
    for i in range(n):
        if (i > 0):
            leftRightObserver *= list[i-1]
            rightLeftObserver *= list[n-i]

            resl[i] *= leftRightObserver
            resl[n-i-1] *= rightLeftObserver
    return resl

"""
TESTING
"""
class TestProdArrDiv(unittest.TestCase):
    def test_1(self):
        self.assertEqual( productArrDiv([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24] )

    def test_2(self):
        self.assertEqual( productArrDiv([3, 2, 1]), [2, 3, 6] )


    def test_3(self):
        self.assertEqual( productArrNoDiv([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24] )
        self.assertEqual( productArrNoDiv([2, 3, 4, 5, 6]), [360, 240, 180, 144, 120] )

    def test_4(self):
        self.assertEqual( productArrNoDiv([3, 2, 1]), [2, 3, 6] )

"""
Main Call
"""
if __name__ == '__main__':
    unittest.main()
