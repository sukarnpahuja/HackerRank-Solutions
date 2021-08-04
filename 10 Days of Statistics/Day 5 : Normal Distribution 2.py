# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def nd(x,m,sd):
    return round(0.5 * 100 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5)))),3)

arr = list(map(int,input().split()))
mean = arr[0]
sd = arr[1]

x1 = int(input())
x2 = int(input())

print(round(100 - nd(x1,mean,sd),2))
print(round(100 - nd(x2,mean,sd),2))
print(round(nd(60,mean,sd),2))
