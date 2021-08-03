# Enter your code here. Read input from STDIN. Print output to STDOUT

#creating function geometric distribution
def g(n,p):
    q = 1-p
    out = (q**(n-1))*p
    
    return out

#input the array of numerator and denominator
arr = list(map(int,input().split()))

#determining probability
p = arr[0]/arr[1]
#first success trial
n = 5

print(round(g(n,p),3))
