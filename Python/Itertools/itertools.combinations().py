# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

i = input().split()
s = i[0]
k= int(i[1])

for x in range(1,k+1):
    for c in combinations(sorted(s),x):
        print("".join(list(c)))
