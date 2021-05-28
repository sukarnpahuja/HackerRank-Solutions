import numpy as np
dim = input().split()
for x in range(len(dim)):
    dim[x] = int(dim[x])

values = [input().split() for _ in range(dim[0])]

arr = np.array(values,dtype=int)
min_value = np.min(arr,axis=1)
print(np.max(min_value))
