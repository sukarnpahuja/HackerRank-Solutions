# Enter your code here. Read input from STDIN. Print output to STDOUT

#input the number of test cases
T = int(input())

#applying for loop to take inputs of sets A and B
for i in range(T):
    size_a = int(input())
    A = set(map(int,input().split()))
    size_b = int(input())
    B = set(map(int,input().split()))
    
    #checking for subset
    print(A.issubset(B))
