def main():
    name = input("What's you name? ")
    price = 50
    total_paid = 0
    vending_machine(price, total_paid, name)


def vending_machine(price, total_paid, name):
    while price > 0:
        print(f"Amount due: {price}")
        pay = int(input("Insert Coin: "))

        if pay == 25 or pay == 10 or pay == 5:
            total_paid = total_paid + pay
            price = price - pay
        else: 
            print("Not a coin")
    if total_paid > 50:
        print(f"Thanks! Here's your coke {name}")
        print(f"Here's your change: {total_paid - 50}")


main()eep it