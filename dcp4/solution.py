#!/bin/bash
#-*- encoding: utf-8 -*-


def missingSequence(squence: list):
    for i in range(len(squence)):
        squence[i] = abs(squence[i])

    for i in range(len(squence)):
        inx = abs(squence[i])
        if (inx > 0):
            squence[inx-1] = - abs(squence[inx-1])

    for i in range(len(squence)):
        if squence[i] > 0 :
            return i+1
    return len(squence) 
        
print(missingSequence([3, 4, -1, 1 ]))
print(missingSequence([1, 2, 0]))
