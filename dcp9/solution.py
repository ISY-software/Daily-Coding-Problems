#!/bin/python3
# -*-encoding: utf-8 -*-

def findMaxSum(arr):
    if len(arr) == 0 :
        return 0
    acom = arr[0]
    arr[0] = 0
    for i in range(1, len(arr)):
        arr[i], acom = max(arr[i-1], acom), arr[i-1] + arr[i]
    return max(arr[-1], acom)

# Complex O(N) and space constant: is the seam of data
def findMaxSum2(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    acom = arr[0]
    arr[1], arr[0] = arr[0], arr[1]

    for i in range(2, len(arr)):
        arr[i], arr[i-1] = max(arr[i-1], arr[i-2]), arr[i-1] + arr[i]
    return max(arr[-1], arr[-2])


print(findMaxSum([5, 5, 10, 100, 10, 5]))
print(findMaxSum2([5, 5, 10, 100, 10, 5]))
print(findMaxSum([5, 1, 1, 5]))
print(findMaxSum2([5, 1, 1, 5]))
print(findMaxSum([2, 4, 6, 2, 5]))
print(findMaxSum2([2, 4, 6, 2, 5]))
print(findMaxSum([5, 2, 1, 5]))
print(findMaxSum2([5, 2, 1, 5]))
print('----')
print(findMaxSum([5, 2, 1]))
print(findMaxSum2([5, 2, 1]))
print(findMaxSum([2, 5, 1]))
print(findMaxSum2([2, 5, 1]))

print(findMaxSum([5, 2]))
print(findMaxSum2([5, 2]))
print(findMaxSum([2, 5]))
print(findMaxSum2([2, 5]))

print(findMaxSum([3]))
print(findMaxSum2([3]))
print(findMaxSum([]))
print(findMaxSum2([]))
