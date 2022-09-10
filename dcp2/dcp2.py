#!/bin/python3
#-*- encoding: utf-8 -*-
import unittest


def productArrDiv(list):
    """docstring for productArrDiv"""
    acom = 1
    for element in list:
        acom *= element

    for i in range(0, len(list)):
        list[i] = acom / list[i]
    return list;


def productArrNoDiv(list):
    n = len(list)
    lsub1 = []
    lsub2 = []
    resl = [1]*n  
    for i in range(n):
        lsub1.append(1)
        lsub2.append(1)
        if (i > 0):
            lsub1[i] = lsub1[i-1] * list[i-1]
            lsub2[i] = lsub2[i-1] * list[n-i]

            resl[i] *= lsub1[i]
            resl[n-i-1] *= lsub2[i] 
    return resl

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

if __name__ == '__main__':
    unittest.main()
