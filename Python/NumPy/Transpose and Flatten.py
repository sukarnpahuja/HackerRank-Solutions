import numpy as np

dim = input().split()
for i in range(2):
    dim[i] = int(dim[i])
values = [input().split() for _ in range(dim[0])]

for x in range(dim[0]):
    for y in range(dim[1]):
        values[x][y] = int(values[x][y])
        
arr = np.array(values)
trans = np.transpose(arr)
print(trans)
print(arr.flatten())
