def main():
    text = input("Enter a secret message: ").strip().lower()
    encode_message(text)

def encode_message(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    letter_loc = 0
    while letter_loc < len(text):
        if text[letter_loc] in alphabet:
            alphabet_loc = alphabet.find(text[letter_loc])
            print(cipher[alphabet_loc], end="")
        else:
            print(text[letter_loc], end="")
        letter_loc += 1
    print("")

main()

