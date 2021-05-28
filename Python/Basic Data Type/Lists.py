if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        c = input().split()
        for x in range(1,len(c)):
            c[x] = int(c[x])
        if c[0] == "insert":
            arr.insert(c[1],c[2])
        elif c[0] == "remove":
            arr.remove(c[1])
        elif c[0] == "append":
            arr.append(c[1])
        elif c[0] == "sort":
            arr.sort()
        elif c[0] == "pop":
            arr.pop()
        elif c[0] == "reverse":
            arr.reverse()
        else:
            print(arr)
        
