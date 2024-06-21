


def check_even_odd(num):
    if num%2 == 0:
        return "Juft son"
    else:
        return "Toq son"

number = int(input("Son kiriting = "))
result = check_even_odd(number)
print(f"Kiritilgan son: {result}")