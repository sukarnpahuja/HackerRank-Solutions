import numpy as np

#Input of dimensions and conversion into integer
dim = input().split()
for i in range(len(dim)):
    dim[i] = int(dim[i])
 
#Input of values of 2 matrices
matrix1 = [input().split() for _ in range(dim[0])]
matrix2 = [input().split() for _ in range(dim[1])]

#conversion of matrices values into integer form
for x in range(dim[0]):
    for y in range(dim[2]):
        matrix1[x][y] = int(matrix1[x][y])
        
for a in range(dim[1]):
    for b in range(dim[2]):
        matrix2[a][b] = int(matrix2[a][b])

#conversion to array
arr_1 = np.array(matrix1)
arr_2 = np.array(matrix2)

#concatenation
print(np.concatenate((arr_1,arr_2),axis=0))
