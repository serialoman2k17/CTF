def joint(separator, list_string):
    for i in range(len(list_string)):
        if i != len(list_string) - 1:
            print(list_string[i], end=separator)
        else:
            print(list_string[i], end='')


joint(input("Enter your separator: "), input("Enter your string: "))