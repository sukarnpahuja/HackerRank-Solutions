if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    if (n>=2 and n<=10):
            arr_set = set(arr)
          
            print(sorted(arr_set)[-2])
