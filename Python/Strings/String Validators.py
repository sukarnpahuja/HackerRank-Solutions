if __name__ == '__main__':
    s = input()
    if len(s)>0 and len(s)<=1000:
        print(any(a.isalnum() for a in s))
        print(any(a.isalpha() for a in s))
        print(any(a.isdigit() for a in s))
        print(any(a.islower() for a in s))
        print(any(a.isupper() for a in s))
        
        #ANY FUNCTION: RETURNS TRUE FOR ANY ONE TRUE VALUE
                    
