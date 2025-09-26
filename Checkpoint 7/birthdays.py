birthdays = {
    "Gabo T": "12/27/2007",
    "Gabo F": "7/28/2008",
    "Alyssa": "6/20/2008"
}

name = input("What person would you like to see their birthday? ").title()
while name != "":
    if name in birthdays:
        print(birthdays[name])
    else:
        new_birthday = input("I don't have a birthday for that person, what's their birthday? ")
        birthdays[name] = new_birthday
        print("Birthdays updated")
    name = input("Want another name? (if not press enter) ")
print(birthdays)

with open("birthday.txt", "a") as file:
    for item in birthdays:
        file.write(f"{item} was born {birthdays[item]}\n")