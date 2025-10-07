import random

alphabet = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
    'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
    }


letters = []

for letter in range(13):
    letters.append((random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])))
print(f"Your letters given are:", end=" ")
for item in letters:
    print(item, end=", ")
print()
print("Each point for letter is: ", end="")
for item in letters:
    if item in alphabet:
        print(alphabet[item], end=", ")
print()

word = input("Enter a word: ").lower()
if set(word).issubset(set(letters)):
    print("simon")

