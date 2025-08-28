num = int(input("Enter a number my guy: "))
step = int(input("Enter a step size my guy: "))
start = step


while start < num:
    if start == 0:
        step = int(input("Enter a new step size, not zero: "))
    print(start)
    start += step