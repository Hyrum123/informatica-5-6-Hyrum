def main():
    number = input("Enter a positive integer: ")
    while not number.isdigit():
        number = input("Nah dude enter a positive integer: ")
    while int(number) < 0:
        number = input("Nah dude enter a positive integer: ")
    multiply(number)
    
def multiply(num):
    start = 1
    while start <= 10:
        multiply = int(num) * int(start)
        print(f"{num} x {start} = {multiply}")
        start += 1

main()