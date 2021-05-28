# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
#new_list = []

#new_list.append(A)
#new_list.append(B)
output = (list(product(A,B)))

for i in range(len(output)):
    print(output[i],end=" ")
