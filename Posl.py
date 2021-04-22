def posl(numbers):
    tmp = 0
    maxim = 0
    a = [numbers]
    while numbers != 0:
        numbers = int(input("Enter your number: "))
        a.append(numbers)
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            tmp += 1
        if a[i] != a[i - 1]:
            if tmp > maxim:
                maxim = tmp
            tmp = 0
    print(maxim + 1)


posl(int(input('Enter your number: ')))
