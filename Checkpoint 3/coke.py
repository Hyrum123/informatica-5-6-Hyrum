def main():
    name = input("What's you name? ")
    coins = int(input("Pay with 25, 10, or 5: "))
    while total <= 50:
        if coins == 25 or coins == 10 or coins == 5:
            total = total + coins
        else:
            print("Not a coin")


main()