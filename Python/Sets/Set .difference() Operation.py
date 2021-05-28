# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set_A = set(map(int,input().split()))
b = int(input())
set_B = set(map(int,input().split()))

print(len(set_A-set_B))
