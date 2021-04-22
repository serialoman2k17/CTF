from random import randint


def sdvig(a=0, b=20):
    a = [randint(a, b) for i in range(5)]
    print(a)
    a = a[-1:] + a[:-1]
    print(a)


sdvig()
