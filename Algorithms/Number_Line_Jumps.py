import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    try:
        jumps = (x1 - x2) / (v2-v1) # amount of moves required to make both of kangaroos position equal
    except ZeroDivisionError: # Cannot divide number by zero. Both kangaroos start at different places with same jump distance. They can never meet.
        return "NO"

    print("jumps" , jumps)
    k1 = (jumps*v1) + x1 # kangaroo1 startingPos + jumpDistance * jumps
    k2 = (jumps*v2) + x2 # kangaroo2 startingPos + jumpDistance * jumps
    print(k1, k2)

    # If the second kangaroo's jump distance is larger than the first, there is no way for the first kangaroo to catch up
    if v2 > v1:
        return "NO"

    # The operator '%' returns the remainder. If the moves required to match position is a decimal, then the kangaroo would be in the air, because it wouldn't be a complete jump.
    # If the move is a integer and complete jumps
    elif (x1 - x2) % (v2-v1) == 0:
        return "YES"

    # If the moves required is an decimal and not an complete jump
    elif (x1 - x2) % (v2-v1) != 0:
        return "NO"

if __name__ == '__main__':
    x1, v1, x2, v2 = map(int, input().split())
    result = kangaroo(x1, v1, x2, v2)
    print(result)
