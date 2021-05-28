import numpy as np
dim = input().split()

for x in range(len(dim)):    #converting dimensions into integer in the list
    dim[x] = int(dim[x])
    
values = [input().split() for _ in range(dim[0])] #getting values for 2-d array

arr = np.array(values, dtype=int)   #converting into array
print(np.prod(np.sum(arr,axis=0)))
