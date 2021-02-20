#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    leftRight = sum([arr[x][x] for x in range(n)])
    rightLeft = sum([arr[x][n-1-x] for x in range(n)])

    diff = abs(leftRight - rightLeft)
    return diff

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)

    