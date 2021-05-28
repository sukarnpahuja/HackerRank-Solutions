def split_and_join(line):
    split_list = line.split(" ")
    output = "-".join(split_list)
    return output
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
