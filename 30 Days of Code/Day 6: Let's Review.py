# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for i in range(T):
    S = str(input())
    print(S[::2], S[1::2])
'''

METHOD-2

t = int(input())
if t>=1 and t<=10:
    for i in range(t):
        s = input()
        if len(s)>=2 and len(s)<=1000:
            s_list = list(s)
            even_list = []
            odd_list = []
            for x in range(len(s_list)):
                if x%2 == 0:
                    even_list.append(s_list[x])
                else:
                    odd_list.append(s_list[x])
            str1 = "".join(even_list)
            str2 = "".join(odd_list)
            print(f"{str1}  {str2}")
'''
