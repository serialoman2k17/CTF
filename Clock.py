def clock():
    a = int(input("Enter time: "))
    days = a // (60 * 24)
    hours = a % (60 * 24) // 60
    minutes = a % 60
    print(days, hours, minutes, sep=':')


clock()
