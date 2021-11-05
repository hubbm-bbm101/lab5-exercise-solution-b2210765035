mail = input("Enter an e-mail address to see if it's valid or not:")
def email_check():
    at=False
    dot=False
if "@" in mail:
    at=True
    if "." in mail:
        dot=True
        print("It's an email!")
    else:
        print("Not an email!")
else:
    print("Not an email!")