def main():
    num = input("Enter a number my guy: ")
    num = test(num)
    step = input("Enter a step size my guy: ")
    step = test(step)
    num = int(num)
    step = int(step)
    math_loop(num, step)

def test(a):
    while not a.isdigit():
        a = input("Enter an integer fool: ")
    return a

def math_loop(number, steps):
    start = steps
    while start < number:
        if start == 0:
            steps = int(input("Enter a new step size, not zero: "))
        print(start)
        start += steps

main()