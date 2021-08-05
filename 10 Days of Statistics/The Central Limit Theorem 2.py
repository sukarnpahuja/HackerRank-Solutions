# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
def clt(tickets,strength,mean,sd):
    m = strength*mean
    nsd = (math.sqrt(strength))*sd
    #normal distribution
    return round(0.5 * (1 + math.erf((tickets - m) / (nsd * (math.sqrt(2))))),4)

tickets = int(input())
strength = int(input())
mean = float(input())
sd = float(input())

print(clt(tickets,strength,mean,sd))
