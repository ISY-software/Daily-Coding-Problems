#!/bin/python3
# -*-encoding: utf-8 -*-

def climbR(stepsList: list, stairCase: int) -> int:
    if (len(stepsList) == 1):
        return 1
    if (stairCase == 0):
        return 1
    ways = 0
    for stp in stepsList:
        if stp <= stairCase:
            ways += climbR(stepsList, stairCase - stp)
    return ways

def climb(stepsList: list, stairCase: int) -> int:
    restStairs = [stairCase]
    ways = 0
    for isc in restStairs:
        if isc == 0:
            ways +=1
        for stp in stepsList:
            if stp <= isc:
                restStairs.append(isc - stp)
        
    return ways

#print(climbR([1,2], 4))

print(climb([1,2], 5))
