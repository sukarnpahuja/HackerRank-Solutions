# taking input of number of values
n = int(input())
#taking array values
value = input().split(" ")

#converting into integer form
for i in range(n):
    value[i] = int(value[i])

#defining median function
def median(arr):
    medval = 0
    if len(arr)%2==1:
        medval = arr[len(arr)//2]
    else:
        medval = (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) // 2
        
    return medval

#quartile function
def quartiles(data):
    a = sorted(data)
    q1 = median(a[:len(data)//2])
    q2 = median(a)
    q3 = median(a[(len(data)+1)//2:])
    print(q1)
    print(q2)
    print(q3)
    
quartiles(value)
        
