#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
   
#creating variables --> count : to calculate sum; output_list: to store sums.
count=0
output_list = []

#double for loop for 2D array to extract each element
for x in range(6):
    for y in range(6):
        if x+2<6 and y+2<6:  #condition for hourglass
            count = arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x+1][y+1]+arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2]
        output_list.append(count)

#printing the max value of the list
print(max(output_list))
