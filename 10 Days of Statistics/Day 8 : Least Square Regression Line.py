********************************
# METHOD -1 :
# Using the formula method
********************************

#define MEAN function
def mean(arr):
    out = sum(arr)/len(arr)
    return out
    
#define Regression Function
def Regression(X,Y):
    final = []           #list to declare a,b values
    n = 5                #total number of values
    
    #calculate mean of X and Y arrays
    Xmean = mean(X)
    Ymean = mean(Y)
    
    #summation of X and Y arrays
    Xi = sum(X)
    Yi = sum(Y)
    
    #Calculation of summation of Xi**2
    Xi2 = 0 
    for i in range(n):
        Xi2 = Xi2 + (X[i]**2)
        
    #Calculation of summation of XiYi
    XiYi = 0
    for j in range(n):
        XiYi = XiYi + (X[j]*Y[j])
        
    #calculating b valye by applying the formulae
    num = (n*XiYi) - (Xi*Yi)
    den = (n*Xi2) - (Xi**2)
    b = num/den
    
    #calculation of a value by formula
    a = Ymean - (b*Xmean)
    
    #appening in the list [a,b]
    final.append(a)
    final.append(b)
    
    return final

#INPUTS
n = 5           #number of values
X = []          #X array
Y = []          # Y array
for i in range(n):
    l = list(map(int,input().split()))
    X.append(l[0])
    Y.append(l[1])
 
# a and b coefficient --> Regression Line
regCoeff = Regression(X,Y)
x = 80
#calculating the value of y given valuue of x=80
y = regCoeff[0] + regCoeff[1]*x

print(round(y,3))


*******************************
# METHOD - 2:
# Using library Scikit Learn 
*******************************

from sklearn import linear_model
import numpy as np
xl = [95, 85, 80, 70, 60]
x = np.asarray(xl).reshape(-1, 1)
y = [85, 95, 70, 65, 70]
lm = linear_model.LinearRegression()
lm.fit(x, y)
X = 80
Y = lm.intercept_ + X*lm.coeff_[0]
print(round(Y,3))
