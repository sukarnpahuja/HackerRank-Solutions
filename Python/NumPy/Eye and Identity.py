import numpy as np
np.set_printoptions(legacy='1.13')
dim = input().split()
for x in range(len(dim)):
    dim[x] = int(dim[x])
arr = np.eye(dim[0],dim[1],k=0)
print(arr)

