def main():
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            break
        except ValueError:
            print("Enter an integerrrr")
            pass
    print(factorial(number))


def factorial(num):
    if num < 0:
        raise ValueError("Enter a positive integer fool")
    elif num == 0:
        return 1
    result = num
    while num > 1:
        num = num - 1
        result = num * result
    return result
    
main()