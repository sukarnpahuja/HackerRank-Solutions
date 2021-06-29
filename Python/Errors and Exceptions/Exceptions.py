# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for i in range(T):
    values = input().split()
    a = values[0]
    b = values[1]
    
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as e:
        print('Error Code:',e)
