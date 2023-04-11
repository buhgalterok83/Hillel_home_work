email = input("Enter your email adress: ")

if email.count('@') == 1 and email.count('.') == 1:
    if email.index("@") < email.index('.'):
        if email[0] != "@" and email[-1] != ".":
            print(True)
        else:
            print(False)
    else:
        print(False)
else:
    print(False)
