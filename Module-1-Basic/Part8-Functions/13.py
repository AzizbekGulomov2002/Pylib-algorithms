



def check_password(password):
    if password == "python123":
        return "Parol to'g'ri"
    else:
        return "Xato parol"

password = input("parol kiriting = ")
result = check_password(password)
print(result)