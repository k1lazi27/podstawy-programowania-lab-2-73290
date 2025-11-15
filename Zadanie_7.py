password = "pk47!jy0893"
password_length = len(password)
print(password_length)
if password_length < 11:
    print("Hasło jest za krótkie !!!")
elif "!" not in password:
    print("Hasło nie zawiera znaku specjalnego !!!")
else:
    print("Hasło jest poprawne :)")