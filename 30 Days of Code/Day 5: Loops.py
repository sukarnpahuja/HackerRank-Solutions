#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n>=2 and n<=20:
        for i in range(1,11):
            print(f"{n} x {i} = {n*i}")
