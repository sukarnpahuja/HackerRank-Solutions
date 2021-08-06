# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def sd(arr):
    num = 0
    mean = sum(arr)/len(arr)
    for i in range(len(arr)):
        num = num + (arr[i]-mean)**2
    den = len(arr)
    out = math.sqrt(num/den)
    
    return out
        
    
def pearson(n,x,y):
    mean_x = sum(x)/n
    mean_y = sum(y)/n
    sd_x = sd(x)
    sd_y = sd(y)
    num = 0 
    for i in range(n):
        num =  num + ((x[i]-mean_x)*(y[i]-mean_y))
    den = n*sd_x*sd_y
    out = num/den
    
    return out
    
    
n = int(input())
X = list(map(float,input().split()))
Y = list(map(float,input().split()))
print(round(pearson(n,X,Y),3))
