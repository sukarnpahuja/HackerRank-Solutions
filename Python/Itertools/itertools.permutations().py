# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

input_list = input().split()
s = input_list[0]
k = int(input_list[1])

if k>0 and k<len(s) and s.isupper()==True:
    s= sorted(s)
    output = list(permutations(s,k))
    for i in output:
        output_list = list(i)
        print("".join(output_list))
