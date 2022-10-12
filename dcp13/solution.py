#!/bin/python3
# -*- encoding: utf-8 -*-

"""
This is the function that wait a str 's' and int 'k'
return the longest substring with k distinct characters

The solution use dynamic programming to save the occurence
if characters inside of an string to remove them in future
"""
def lstwkdc(s: str, k: int) -> str:
    letterOccurence = [0]*27  # 27 letters of latam alphabet (with ñ)
    lessVal = ord('a')
    maxStr = ''
    actualStr = ''
    diffCount = 0
    for charact in s:
        actualStr += charact  
        if letterOccurence[ord(charact) - lessVal] != 0:
            if (len(actualStr) > len(maxStr)):
                maxStr = actualStr
            letterOccurence[ord(charact) - lessVal] +=1
        else:
            diffCount += 1 
            letterOccurence[ord(charact) - lessVal] = 1
            if (diffCount > k):
                firstChar = actualStr[0]
                #noRepIndx = 0
                #for actChar in actualStr:
                #    if actChar == firstChar:
                #        noRepIndx += 1
                #    else:
                #        break
                #actualStr = actualStr[noRepIndx:]
                actualStr = actualStr[ letterOccurence[ord(charact) - lessVal]]
                diffCount -= 1
                letterOccurence[ord(firstChar) - lessVal] = 0
                pass
            else:
                # test if len of max
                if (len(actualStr) > len(maxStr)):
                    maxStr = actualStr
    return maxStr


print(lstwkdc("abcba", 2))
print(lstwkdc("cbbbbaac", 2))
print(lstwkdc("abcde", 2))

