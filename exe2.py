mail = input("Enter an e-mail address to see if it's valid or not:")
if "@" in mail:
    if "." in mail:
        print("It is a valid e-mail address!")
    else:
        print("It is not an e-mail address!")
else:
    print("It is not an email address!")