def main(): #main function
    text = input("Enter a secret message: ").strip().lower() #ask the user for a message
    encode_message(text) #run the encode_message function

def encode_message(text): #define encode_message function
    alphabet = "abcdefghijklmnopqrstuvwxyz" #alphabet variable
    cipher = "zyxwvutsrqponmlkjihgfedcba" #cipher variable
    letter_loc = 0 #letter location tracker variable
    while letter_loc < len(text): #while the letter location is less than the length of the text then...
        if text[letter_loc] in alphabet: #if the letter in the letter location is in the alphabet then...
            alphabet_loc = alphabet.find(text[letter_loc]) #it finds where the letter in the alphabet is that is in the text and that is the alphabet location variable
            print(cipher[alphabet_loc], end="") #it prints that location in the cipher variable
        else: #if the letter in the letter location is not in the alphabet then...
            print(text[letter_loc], end="") #it prints whatever that symbol was
        letter_loc += 1 #adds one to the letter location
    print("") #end line

main() #runs the main function