# Enter your code here. Read input from STDIN. Print output to STDOUT

#creating factorial function
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
   
#creating binomial function
def binomial(x,n,p):
    q = 1-p
    a = factorial(n)/(factorial(x)*factorial(n-x))
    b = p**x
    c = q**(n-x)
    out = a*b*c

    return out

# input of ratio values boys:girls
arr= list(map(int,input().split()))

#probability of reject
p=arr[0]/100
#probability of accept
q=1-p

#number of trials required
x=2
#total number of trials
n=10

ans1 = 0
for i in range(0,x+1):
    ans1 = ans1 + binomial(i,n,p)
    
ans2 = 0
for j in range(x,n+1):
    ans2 = ans2 + binomial(j,n,p)
    
print(round(ans1,3))
print(round(ans2,3))
