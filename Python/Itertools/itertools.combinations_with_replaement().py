# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

i = input().split()
s = i[0]
k= int(i[1])

for c in combinations_with_replacement(sorted(s),k):
    print("".join(list(c)))
