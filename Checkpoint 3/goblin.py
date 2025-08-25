import random
print("Welcome to the goblin game!")
print("The best game ever!")
player_name = input("What's your name? ")
print(f"{player_name}, can you find the goblin?")
print("|_|_|_|_|_|")
goblin_position = random.randint(1, 5)
keep_trying = True
while keep_trying:
    guess_position = int(input("Can you guess where the goblin is? "))
    if guess_position == goblin_position:
        print("Good job! You found the goblin")
        keep_trying = False
    else: print("Try again, the goblin is still hiding")