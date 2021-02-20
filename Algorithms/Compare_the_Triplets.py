import math
import os
import random
import re
import sys
import itertools

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    aScore = 0
    bScore = 0
    for (x,y) in zip(a,b):
      if x > y:
          aScore += 1
      elif x < y:
          bScore += 1
      elif aScore == bScore:
          pass

    return aScore, bScore  



if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)