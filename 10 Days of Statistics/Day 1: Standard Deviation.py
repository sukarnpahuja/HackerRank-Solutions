#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = round(sum(arr)/len(arr),1)
    rounded = []
    for i in arr:
        rounded.append((i-mean)**2)
    
    final = math.sqrt(sum(rounded)/len(rounded))
    print(round(final,1))
    

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
