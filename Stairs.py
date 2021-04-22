a = int(input("Enter the number of steps: "))
b = input("Enter the symbol of steps: ")
c = input("Which way will the stairs go (left, right): ")
if c == "left":
    # Left
    for i in range(1, a+1):
        print(b * i)
elif c == "right":
    # Right
    for i in range(1, a + 1):
        print((" " * (a - i)), b * i)
else:
    print("Your enter invalid, please enter again")
