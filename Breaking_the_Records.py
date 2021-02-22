#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    best = 0
    worst = 0
    highest = scores[0]
    lowest = scores[0]

    for i in scores:
        if i > highest:
            highest = i
            best += 1
        if i < lowest:
            lowest = i
            worst += 1

    return best, worst
    

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)