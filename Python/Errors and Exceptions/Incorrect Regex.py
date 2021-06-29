# Enter your code here. Read input from STDIN. Print output to STDOUT
import re;

n = int(input())
for i in range(n):
    x = input()
    try:
        re.compile(x)
        result = True
    except re.error:
        result = False
    
    print(result)
