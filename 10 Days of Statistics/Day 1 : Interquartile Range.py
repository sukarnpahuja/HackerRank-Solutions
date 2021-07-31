#input the number of values
n = int(input())
# input values
values = list(map(int,input().split(" ")))
#input frequencies
freq = list(map(int,input().split(" ")))

#define median function
def median(arr):
    medval = 0
    if len(arr)%2==1:
        medval = arr[len(arr)//2]
    else:
        medval = (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) // 2
        
    return medval

#define interquartile function
def interQuartileRange(values, freq):
    a = []
    # replicating values
    for i in range(n):
        v = values[i]
        f = freq[i]
        while(f>=1):
            a.append(v)
            f-=1
    a = sorted(a)
    
    q1 = round(median(a[:len(a)//2]),1)
    q2 = median(a)
    q3 = round(median(a[(len(a)+1)//2:]),1)
    
    #printing with a decimal point
    print("%0.1f" % (q3 - q1))
    
#function calling
interQuartileRange(values, freq)
