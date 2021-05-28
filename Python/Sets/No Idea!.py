# Enter your code here. Read input from STDIN. Print output to STDOUT

#Input the size of array(n) and set A and B (m)
sizes = list(map(int,input().split()))
n = sizes[0]    #size of array
m = sizes[1]    #size of sets A and B

#input elements of array
arr = list(map(int,input().split()))

#input sets A and B
A = set(map(int,input().split()))
#list_A = list(A)
B = set(map(int,input().split()))
#list_B = list(B)

#assigning happiness value
happiness = 0

for x in arr:
    if x in A:
        happiness+=1
    if x in B:
        happiness-=1
    else:
        happiness = happiness
        
print(happiness)
