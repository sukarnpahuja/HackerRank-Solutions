import numpy
numpy.set_printoptions(legacy='1.13')

values = input().split()
for i in range(len(values)):
    values[i] = float(values[i])
    
arr = numpy.array(values)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
