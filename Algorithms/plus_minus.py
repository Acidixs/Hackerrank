import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr, n):
    positive = len([x for x in arr if x > 0])/n
    negative = len([x for x in arr if x < 0])/n
    zeros = len([x for x in arr if x == 0])/n

    print(("{:.6f}".format((positive))))
    print("{:.6f}".format((negative)))
    print("{:.6f}".format((zeros)))

    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
