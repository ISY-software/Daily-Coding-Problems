#!/bin/python3
#-*- encoding: utf-8 -*-

import random


def montecarloMethod(decimals=3):
    iterations = 0
    insidePoints = 0
    #for _ in range(iterations):
    while(True):
        iterations +=1
        randNumX = random.random()
        randNumY = random.random()
        if (randNumX**2 + randNumY**2) < 1:
            insidePoints += 1
        result = insidePoints/iterations

montecarloMethod()  
