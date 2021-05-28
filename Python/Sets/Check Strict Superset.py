# Enter your code here. Read input from STDIN. Print output to STDOUT

#input set A
A = set(map(int,input().split()))

#input other sets
s = int(input())
output = True
for _ in range(s):
    n = set(map(int,input().split()))
    
    # for a flase conditin, either n is not a subset of A or n and A are exactly equal
    if n.issubset(A)==False or len(n)==len(A):
        output = False
        break
        
print(output)
