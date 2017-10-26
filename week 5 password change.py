not_allowed_passwords = ["Password", "password", "sesame", "Sesame", "Letmein", "LetMeIn", "Qwerty", "Cheese"]
print("Enter a password that is between 6 and 12 characters")
password1 = ""
while len(password1) < 6 or len(password1) > 12:
    password1 = str(input("Input a password: "))
    if password1 in not_allowed_passwords:
        password1 = "hello"
password2 = input("Input the password again: ")
if password1 == password2:
    print("Password changed!")
else:
    print("Two passwords don't match")
