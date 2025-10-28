while True:
    try:
        fraction = input("Enter a fraction from 0 to 1. It must be in x/y format: ").split("/")
        fraction[0] = int(fraction[0])
        fraction[1] = int(fraction[1])
        if fraction[0] > fraction[1]:
            print("The numerator must be smaller than the denominator")
            continue
        fuel_lvl = fraction[0] / fraction[1]
        if fuel_lvl <= 0.01:
            print("YOUR FUEL IS EMPTY")
            break
        elif fuel_lvl >= 0.99:
            print("Your fuel is full man. Fullfuel. Fuelfull")
            break
        else:
            print(f"Your fuel level is at {fuel_lvl:.2f}")
            break
    except ZeroDivisionError:
        print("You can't divide by zero fool")
        pass
    except ValueError:
        print("You must enter an integer fool")
        pass