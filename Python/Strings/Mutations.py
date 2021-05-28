def mutate_string(string, position, character):
    output = ''
    my_list = list(string)
    my_list[position] = character
    output = "".join(my_list)
    return output

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
