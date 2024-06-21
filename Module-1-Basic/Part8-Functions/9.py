


def check_number(num):
    if num>0:
        return "Musbat son"
    elif num<0:
        return "Manfiy son"
    else:
        return "Nol"

number = float(input("Son kiriting : "))
result = check_number(number)
print(f"Kiritilgan son: {result}")