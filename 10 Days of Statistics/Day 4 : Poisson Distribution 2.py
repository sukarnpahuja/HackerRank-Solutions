"""
X = random variable
k = trial 
lemda = mean

**if K is not given**
E[X] = lemda
Var[X] = lemda

IMPORTANT:
E[X**2] = X**2 = lemda + lemda**2
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

arr = list(map(float,input().split()))
ma = arr[0]
mb = arr[1]

cost_A = 160 + 40*(ma+ma**2)
cost_B = 128 + 40*(mb+mb**2)

print(round(cost_A,3))
print(round(cost_B,3))
