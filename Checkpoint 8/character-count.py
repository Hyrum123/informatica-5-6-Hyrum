def main():
    message = input("Enter a message: ")
    count(message)

def count(message):
    dictionary = {}
    for character in message:
        dictionary.setdefault(character, 0)
        dictionary[character] += 1

    print(dictionary)
    print(len(message))
    # key = dictionary.index(max(list(dictionary.values())))
    print(f"The character {list(dictionary.keys())[list(dictionary.values()).index(max(list(dictionary.values())))]} has {max(list(dictionary.values()))} chartacters")

main()