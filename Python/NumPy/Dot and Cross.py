import numpy as np

size = int(input())
arr_1 = np.array([list(map(int,input().split())) for _ in range(size)])
arr_2 = np.array([list(map(int,input().split())) for _ in range(size)])

print(np.dot(arr_1,arr_2))

