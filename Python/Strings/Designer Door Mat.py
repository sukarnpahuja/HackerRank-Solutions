# Enter your code here. Read input from STDIN. Print output to STDOUT

#Input and conversion into integer and assihnment
dim = list(map(int,input().split()))
n = dim[0]
m = dim[1]

#condition check
if(n>5 and n<101 and n%2 != 0  and m>15 and m<303):
    
    #FIRST HALF
    for i in range(1,n,2):
        print("-"*((m-(3*(i)))//2) + ".|."*(i) + "-"*((m-(3*(i)))//2))
        
    #CENTRE LINE
    print("-"*((m-7)//2) +  "WELCOME" + "-"*((m-7)//2))
    
    #SECOND HALF
    for j in range(n-2,0,-2):
        print("-"*((m-(3*(j)))//2) + ".|."*(j) + "-"*((m-(3*(j)))//2))
