# Enter your code here. Read input from STDIN. Print output to STDOUT
s = int(input())
A = set(map(int,input().split()))

inputs = int(input())
for i in range(inputs):
    operation_size = input().split()
    N = set(map(int,input().split()))
        
        
    if 'intersection_update' in operation_size:
        A.intersection_update(N)
    elif 'difference_update' in operation_size:
        A.difference_update(N)
    elif 'symmetric_difference_update' in operation_size:
        A.symmetric_difference_update(N)
    else:
        A.update(N)
            
print(sum(A))
