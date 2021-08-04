# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def nd(x,m,sd):
    return round(0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5)))),3)

arr = list(map(int,input().split()))
mean = arr[0]
sd = arr[1]

x = float(input())
arr_x = list(map(int,input().split()))
x1 = arr_x[0]
x2 = arr_x[1]

print(nd(x,mean,sd))
print(nd(x2,mean,sd)-nd(x1,mean,sd))
