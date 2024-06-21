

name = input("Ismingizni kiriting: ")
while True:
    age = int(input("Yoshingizni kiriting: "))
    if age >= 18:
        print(f"{name}, siz voyaga yetgansiz.")
    else:
        print(f"{name}, siz voyaga yetmagansiz.")
    break
