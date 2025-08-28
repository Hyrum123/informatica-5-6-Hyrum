def main():
    num = input("Enter a number my guy: ")
    num = test(num)
    num = int(num)
    step = input("Enter a step size my guy: ")
    step = test(step)
    step = int(step)
    step = testzero(step)
    step = int(step)
    math_loop(num, step)

def test(a):
    while not a.isdigit():
        a = input("Enter an integer fool: ")
    return a

def testzero(i):
    while i == 0 or i == "0":
        i = input("Enter something other than zero fool: ")
        test(i)
    return i

def math_loop(number, steps):
    start = steps
    while start < number:
        print(start)
        start += steps

main()