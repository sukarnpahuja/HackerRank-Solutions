# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def p(k,l):
    a = (l**k)*(2.71828**-l)
    b = factorial(k)
    out = a/b
    
    return out

mean  = float(input())
prob = int(input())
print(round(p(prob,mean),3))


