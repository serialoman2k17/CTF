def frame(digit, char):
    a = [[char for j in range(digit)]for i in range(digit)]
    for i in range(digit):
        print()
        for j in range(digit):
            if 0 < i < digit - 1 and 0 < j < digit - 1:
                print(' ', end=' ')
            else:
                print(a[i][j], end=' ')


frame(int(input("Enter the size: ")), input("Enter the symbol: "))
