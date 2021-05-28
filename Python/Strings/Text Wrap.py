import textwrap

def wrap(string, max_width):
    if len(string)>0 and len(string)<1000 and max_width>0 and max_width<len(string):
        return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
