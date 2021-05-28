import numpy as np

size = int(input())
values = [list(map(float,input().split())) for _ in range(size)]

arr = np.array(values)

print(round(np.linalg.det(arr),2))
