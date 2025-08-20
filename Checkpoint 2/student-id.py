def main():
    print('')
    print('Please enter the following information to create your ID Card.')
    input('Press enter to continue.')

    fname = input("What is your first name? ").title().strip()
    lname = input("What is your last name? ").upper().strip()
    email = input("What is your email address? ").strip()
    phone = input("What is your phone number? ").strip
    idnum = input("What is your student ID number? ").strip().title()
    thing = input("What is your FPT class? ").strip().title()
    gyear = int(input("What is your expected graduation year? ").strip())
    fasub = input("What is your favorite subject? ").strip().title()
    extra = input("Do you have any extracurricular activities? ").strip().title()
    yearsleft = gyear - 2025
    line = "-" * 40

    print(f"Your ID card is: \n{line}\n{lname}, {fname}\nStudent\nID: {idnum}\n\n{email}\n{phone}\n\nFPT Class: {thing}\tFavorite Subject: {fasub}\nExpected Graduation: {gyear}\tYears left: {yearsleft}")    
	
main()