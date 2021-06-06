#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip()) #input
    
#converting to binary (inbuild funvtion)
'''
    if there is no built in function:
        while n>0:
            remainder = n%2
            n=n/2
            store rem in a list and join\
'''
bin_num = str(bin(n))

output = 0    # for final output
state = 0    #to check the consecutive length continuously
curr_len = 0 #to store current length

#checking each element in number
for i in bin_num:
    if i == '1':
        #increases with every consecutive 1
        state += 1
        curr_len = state       #stores the lates length of consecutive 1s
    else:
        state = 0      #becomes 0 as soon as 0 occurs
        output = max(state,curr_len)   #output stored is max of new length vs prev lenth
        
print(output)
