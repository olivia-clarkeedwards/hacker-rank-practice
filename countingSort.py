#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # result = []
    
    count = [0 for _ in range(100)]
    for int in arr:
        count[int] += 1

    return count
    
    # for index in range(len(count)):
    #     while count[index] != 0:
    #         result.append(index)
    #         count[index] -= 1

    # return result 
            
            
        
    
        

countingSort([1, 4, 3])