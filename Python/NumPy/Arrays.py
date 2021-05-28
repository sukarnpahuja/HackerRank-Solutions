import numpy

def arrays(arr):
    # complete this function
    c = numpy.array(arr,float)
    return numpy.flip(c)
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
