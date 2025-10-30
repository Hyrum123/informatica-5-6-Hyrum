foods = {
    "milk": 73, "greek yogurt": 77, "egg": 75, "blue cheese": 119, "butter": 113, "almonds": 170, "sunflower seeds": 165, "salmon": 175, "shrimp": 28, "watermelon": 11
}

def main():
    choices = input("What two foods do you want? ").lower().split(", ")
    print(calories(choices[0], choices[1]))

def calories(food1, food2):
    add = foods[food1] + foods[food2]
    return add

main()
