def main():
    number = input("Enter a positive integer: ")
    while not number.isdigit():
        number = input("Nah dude enter a positive integer: ")
    while int(number) < 0:
        number = input("Nah dude enter a positive integer: ")
    multiply(number)
    
def multiply(num):
    first = 1
    while first <= int(num):
        second = 1
        while second <= int(num):
            multiply = first * second
            print(f"{first} x {second} = {multiply}")
            second += 1
        first += 1

main()