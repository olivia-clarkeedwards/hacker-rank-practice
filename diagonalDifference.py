#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diagonals = [0, 0]

    for row in range(len(arr)):
        col = row
        diagonals[0] += arr[row][col]

    col = len(arr) - 1
    for row in range(len(arr)):
        diagonals[1] += arr[row][col]
        col -= 1

    diagonals.sort()
    return abs(diagonals[0] - diagonals[1])


print(diagonalDifference([
[1, 2, 3],
[4, 5, 6],
[9, 8, 9]]))