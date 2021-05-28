# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
s = set()
if N>0 and N<1000:
    for x in range(N):
        i = input()
        s.add(i)
        
    print(len(s))
