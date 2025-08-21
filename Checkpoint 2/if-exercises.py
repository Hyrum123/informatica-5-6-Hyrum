def main():
    numbers = input("Enter a calculation: ").split(" ")
    print(numbers)
    calculation(float(numbers[0]), numbers[1], float(numbers[2]))

def calculation(a, b, c):
    result = 0
    if b == "+":
        result = a + c
    elif b == "-":
        result = a - c
    elif b == "*":
        result = a * c
    elif b == "/":
        result = a / c
    print(f"{result:.1f}")

main()

