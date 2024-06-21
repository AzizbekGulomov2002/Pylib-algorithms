


users = {'admin':'admin123', 'aziz':'qwerty','charlie':'abc123'}
login= input("Loginni kiriting = ")
password = input("Parolni kiriting = ")

if login in users and users[login] == password:
    print("Xush kelibsiz")
else:
    print("Login yoki parolda xatolik")