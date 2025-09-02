def main():
    text = input("Enter a secret message: ").strip().lower()
    output = encode_message(text)
    print(output)

def encode_message(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    letter_loc = 0
    while letter_loc < len(text):
        if text[letter_loc] in alphabet:
                alphabet_loc = alphabet.find(text[letter_loc])
                print(cipher[alphabet_loc])
        letter_loc += 1

main()

