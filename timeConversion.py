#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    suffix = s[-2:]
    hour = int(s[0:2])

    if suffix == 'AM' and hour == 12:
        return f'0{hour - 12}{s[2:-2]}'
    elif suffix == 'PM' and 1 <= hour and hour <= 11:
        return f'{hour + 12}{s[2:-2]}'
    elif hour < 10:
        return f'0{hour}{s[2:-2]}'
    else:
        return f'{hour}{s[2:-2]}' 

print(timeConversion('12:01:00PM'))
print(timeConversion('12:01:00AM'))
print(timeConversion('12:05:39AM'))
print(timeConversion('12:40:22AM') == '00:40:22')


