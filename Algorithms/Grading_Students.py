#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    for g in grades:
        if g < 38:
            pass
        elif math.ceil(g/5)*5 - g < 3:
            i = grades.index(g)
            grades[i] = math.ceil(g/5)*5
    return grades

    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()