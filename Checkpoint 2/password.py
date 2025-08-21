def main():
    import getpass
    password = getpass.getpass("Enter a new password: ")
    check_password(password)

def check_password(check):
    print("You have three tries to guess the password")
    tries = 3
    while tries > 0:
        checkpass = input("Guess: ")
        if check == checkpass:
            print("The password is correct. The progran will end now")
            break
        if check != checkpass:
            print("The password is incorrect")
            tries = tries - 1
            if tries == 0:
                print("You didn't guess it! The program will end now")
                break
        
main()

