from collections import *

#input number of elments in an array
n = int(input())

#input array alements
numbers =  input().split(" ")

#converting to integers
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
    
#calculating MEAN
mean = round(sum(numbers)/len(numbers),1)
print(mean)

#calculating  MEDIAN
sorted_num=sorted(numbers)
median=0
if len(sorted_num)%2!=0:
    median=sorted_num[(len(sorted_num)//2)+1]   
else:
    median=sum(sorted(numbers)[(n//2)-1:(n//2)+1])/2
print(median)

#calculating MODE
mode_values= Counter(numbers)
maxVal=max(mode_values.values())
modes=[]

for i in mode_values.keys():
    if mode_values[i]==maxVal:
        modes.append(i)
        
if len(modes)==1: 
    mode= modes[0]
else:
    mode=min(modes)

print(mode)
