while True:
    greeting = input("Respond to a customer to get cash $$$: ").strip().lower()
    if greeting == "hello":
        print("$0")
    elif greeting.startswith("h") == True:
        print("$20")
    else:
        print("$100")
        break