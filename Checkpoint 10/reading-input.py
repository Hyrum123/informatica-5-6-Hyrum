def main():
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)

def read_input(prompt, start, finish):
    while True:
        try:
            num = int(input(prompt))
            if int(num) >= start and int(num) <= finish:
                print(num)
                return num
            elif int(num) < start:
                print(f"The input was too low. The lowest number available is {start}")
            elif int(num) > finish:
                print(f"The input was too high. The highest number available is {finish}")
        except ValueError:
            print("Invalid input")
            pass

main()