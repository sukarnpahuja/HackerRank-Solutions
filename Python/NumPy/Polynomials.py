import numpy as np

values = list(map(float,input().split()))
x = int(input())

arr = np.array(values)

print(np.polyval(arr,x))
