#!/bin/python3
# -*- encoding: utf-8 -*-
import time
# traversing a matrix in sperital


def spiralMatrix(mtrx: list):
    hSteps = len(mtrx[0])
    vSteps = len(mtrx)-1
    jPos = -1
    iPos = 0
    iIncrease = 1
    jIncrease = 1

    while hSteps > 0 or vSteps > 0:
        for _ in range(hSteps):
            jPos += jIncrease
            print(mtrx[iPos][jPos])
            time.sleep(0.51)
        if (vSteps == 0):
            break
        for _ in range(vSteps):
            iPos += iIncrease
            print(mtrx[iPos][jPos])
            time.sleep(0.51)

        jIncrease *= -1
        iIncrease *= -1
        hSteps -= 1
        vSteps -= 1


matrix_temp = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

matrix_temp2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
        ]
#1 2 3 4 8 12 11 10 9 5 6 7 

matrix_temp3 = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
        [17,18,19,20]
        ]
#1 2 3 4 8 12 16 20 19 18 17 13 9 5 6 7 11 15 14 10

#spiralMatrix(matrix_temp)
spiralMatrix(matrix_temp2)
#spiralMatrix(matrix_temp3)
