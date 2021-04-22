def clock(time):
    days = time // (60 * 24)
    hours = time % (60 * 24) // 60
    minutes = time % 60
    print(days, hours, minutes, sep=':')


clock(int(input("Enter time: ")))
