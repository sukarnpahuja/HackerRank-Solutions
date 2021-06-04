# Enter your code here. Read input from STDIN. Print output to STDOUT
#enter number of etries 
n = int(input())

#taking names and phone numbers and storing in a list
phone_list = []
for _ in range(n):
    input_list = input().split(" ")
    #storing each value seperately in a list
    for x in input_list:
        phone_list.append(x)
#conveting phone numbers to integer
for y in range(1,len(phone_list),2):
    phone_list[y] = int(phone_list[y])
    
#creating a phoneBook using dictionary comprehension
phoneBook = {phone_list[i]:phone_list[i+1] for i in range(0,len(phone_list),2)}
    
#taking queries
while True:
    try:
        query = input()
        if query in phoneBook:
            print(query,'=',phoneBook[query],sep="")
        else:
            print('Not found')
    except:
           break 
            
