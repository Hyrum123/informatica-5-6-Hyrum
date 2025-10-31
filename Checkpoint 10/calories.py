foods = {
    "milk": 73, "greek yogurt": 77, "egg": 75, "blue cheese": 119, "butter": 113, "almonds": 170, "sunflower seeds": 165, "salmon": 175, "shrimp": 28, "watermelon": 11
}

def main():
    choices = input("What two foods do you want? (seperated by a comma) ").lower().split(", ")
    while True:
        try:
            print(f"The number of calores total is: {calories(choices[0], choices[1])}")
            break
        except IndexError:
            choices = input("Enter TWO foods: ").lower().split(", ")
            pass

def calories(food1, food2):
    try:
        if (food1 == "milk" or food2 == "milk") and (food1 == "watermelon" or food2 == "watermelon"):
            raise ValueError("DON'T EVER MIX THOSE")
        add = foods[food1] + foods[food2]
        return add
    except KeyError:
        print("Bro, that isn't part of the food list")

main()
