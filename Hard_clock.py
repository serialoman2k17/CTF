def Hard_clock(h, m, s):
    print(h * 30 + m * 30 / 60 + s * 30 / 3600)


Hard_clock(int(input('Enter hour: ')), int(input('Enter minutes: ')), int(input('Enter seconds: ')))
