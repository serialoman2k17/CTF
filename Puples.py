def puples(a):
    b = [a]
    sum = 0
    for i in range(2):
        a = int(input(f'Enter quantity puples in {i + 2} class: '))
        b.append(a)
    for i in range(len(b)):
        if b[i] % 2 != 0:
            b[i] += 1
            b[i] /= 2
            sum += b[i]
        else:
            b[i] /= 2
            sum += b[i]
    return sum


print(int(puples(int(input('Enter quantity puples in 1 class: ')))))
