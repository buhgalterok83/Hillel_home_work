email = input("Enter your email adress: ")

if "@" not in email or "." not in email:
    print(False)
else:
    if email.index("@") < email.index("."):
        if email[0] != "@" and email[-1] != ".":
            print(True)
        else:
            print(False)

    else:
        print(False)