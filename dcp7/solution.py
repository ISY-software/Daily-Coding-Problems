#!/bin/python3
#-*- encoding: utf-8 -*-


def decodeWays(num:str) ->int:
    lnn = len(num)
    if (lnn == 0 or lnn == 1):
        return 1
    rslt = decodeWays(num[1:]) 
    if (int(num[0:2]) < 26):
        rslt += decodeWays(num[2:])
    return rslt

def decodeWaysNoRec(num:str) ->int:
    branchs = [num]
    acom = 0
    while(len(branchs) != 0):
        tempNum = branchs.pop(0)
        lnn = len(tempNum)
        if (lnn == 0 or lnn == 1):
            acom +=1
        else:
            branchs.append(tempNum[1:])
            if (int(tempNum[0:2]) < 26):
                branchs.append(tempNum[2:])
    return acom



print(decodeWays('111'))
print(decodeWaysNoRec('111'))
print(decodeWays('11111'))
print(decodeWaysNoRec('11111'))

# vim: foldlevel=9
