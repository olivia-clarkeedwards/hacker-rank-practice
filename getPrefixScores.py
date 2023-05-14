#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getPrefixScores' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getPrefixScores(arr):
    result = []
    size_of_array = len(arr)

    for end_of_prefix in range(1, size_of_array + 1):
        prefix_array = arr[:end_of_prefix]
        
        for index in range(len(prefix_array)):
            prefix_array[index] += max(prefix_array)

        result.append(sum(prefix_array) % (10**9 + 7))

    return result

print(getPrefixScores([1, 2, 1]))
print(getPrefixScores([1, 2, 3]))








