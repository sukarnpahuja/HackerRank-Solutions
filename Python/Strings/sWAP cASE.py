def swap_case(s):
    #if len(s)>0 and len(s)<=100:
    final = ''
    for x in range(len(s)):
        if s[x].isupper()==True:
            final = final + s[x].lower()
        elif s[x].islower() == True:
            final = final + s[x].upper()
        else:
            final = final + s[x]

    return final
        
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
