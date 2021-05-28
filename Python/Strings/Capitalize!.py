#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
    '''
    if len(s)>0 and len(s)<1000 and s.isalnum()==True:
        new_list = s.split()
        for i in range(len(new_list)):
            if new_list[i][0].isalpha() ==True:
                new_list[i].capitalize()
                print(" ".join(new_list))
            else:
                print(" ".join(new_list))
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
