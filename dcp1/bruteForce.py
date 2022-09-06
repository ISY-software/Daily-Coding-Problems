#!/bin/python3
# -*- encoding: utf-8 -*-

def addinlist(lst:list, k:int)->bool:
    for i in range(0, len(lst)):
        if( k - lst[i]  ) in lst[i+1:] :
            return True
    return False
    
print(addinlist([10, 15, 3, 7], 17))
