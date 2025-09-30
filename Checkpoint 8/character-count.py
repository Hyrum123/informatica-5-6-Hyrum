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
    print(max(dictionary))

main()