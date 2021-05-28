import numpy as  np

dim = input().split()
for i in range(len(dim)):
    dim[i] = int(dim[i])
    
values = [input().split() for _ in range(dim[0])]
for x in range(dim[0]):
    for y in range(dim[1]):
        values[x][y] = int(values[x][y])
    
arr = np.array(values,float)

print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(np.around(np.std(arr,axis=None),11))
