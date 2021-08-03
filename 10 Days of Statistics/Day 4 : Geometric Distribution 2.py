# Enter your code here. Read input from STDIN. Print output to STDOUT

arr = list(map(int,input().split()))
p = arr[0]/arr[1]
q = 1-p
n=5

ans = 0
for i in range(1,n+1):
    ans = ans + (q**(n-i))*p 
    
print(round(ans,3))
    
