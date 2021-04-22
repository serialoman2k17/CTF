from random import randint


def mini_max():
    a = [randint(0, 20) for i in range(5)]
    maxim = 0
    minim = 100
    for i in range(0, len(a)):
        if a[i] > maxim:
            maxim = a[i]
        if a[i] < minim:
            minim = a[i]
    print(a)
    for i in range(len(a)):
        if a[i] == maxim:
            a[i] = minim
        elif a[i] == minim:
            a[i] = maxim
    print(a)


mini_max()
