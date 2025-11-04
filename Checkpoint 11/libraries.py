# import random

# coin = random.choice(["Heads", "Tails"])
# print(coin)

# number = random.randint(1, 10)
# print(number)

# cards = ["Jack", "Queen", "King", "Ace"]
# random.shuffle(cards)
# for card in cards:
#     print(card)

# import statistics
# print(statistics.mean([100, 6]))

# In the terminal type cd "Checkpoint 11"
# Then type python libraries.py Hyrum 5 125

import statistics
import sys
try:    
    print("Hello, my name is", sys.argv[0], sys.argv[1])
    print(statistics.mean([int(sys.argv[2]), int(sys.argv[3])]))
except IndexError:
    print("Too few arguments")
    sys.exit("Too few arguments")

import sys
import cowsay
try:
    cowsay.cow("Hello my name is " + sys.argv[1])
except IndexError:
    print("Too few arguments")
    