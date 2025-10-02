def main():
    assign_letters()

def assign_letters():
    import random
    letters = []
    for letter in range(13):
        letters.append((random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])))
    print(f"Your letters are", end=" ")
    for item in letters:
        print(item, end=", ")
    print()

main()