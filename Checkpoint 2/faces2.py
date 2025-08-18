def main():
    emoji = input("Write something with emotion my guy: ").strip().replace(":)", "🙂").replace(":(", "🙁")
    print(convert(emoji))

def convert(copy):
    return copy

main()