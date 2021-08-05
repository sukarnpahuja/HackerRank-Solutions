# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
def clt(wt,n,mean,sd):
    m = n*mean
    nsd = (math.sqrt(n))*sd
    #normal distribution
    return round(0.5 * (1 + math.erf((wt - m) / (nsd * (math.sqrt(2))))),4)

wt = int(input())
n = int(input())
mean = int(input())
sd = int(input())

print(clt(wt,n,mean,sd))
