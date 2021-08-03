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
arr= list(map(float,input().split()))

#probability of boys
p=arr[0]/sum(arr)
#probability of girls
q=arr[1]/sum(arr)

#number of trials required
x=3
#total number of trials
n=6

ans = 0
for i in range(x,n+1):
    ans = ans + binomial(i,n,p)
    
print(round(ans,3))
