#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    totalswaps = 0
    for i in range(0,n):
        swapsinround = 0
        for j in range(0,n-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
                swapsinround+=1
                
        totalswaps = totalswaps + swapsinround
        if swapsinround == 0:
            break
        
    print('Array is sorted in ' + str(totalswaps) + ' swaps.')
    print('First Element: ' + str(a[0]))
    print('Last Element: ' + str(a[n-1]))
    
         
