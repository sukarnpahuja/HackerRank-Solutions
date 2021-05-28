def count_substring(string, sub_string):
    ct = 0
    if len(string)>=1 and len(string)<=200:
        string.upper()
        for i in range((len(string)-len(sub_string))+1):
            if string[i:i+len(sub_string)] == sub_string:
                ct += 1
            else:
                pass
        
    return ct

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
