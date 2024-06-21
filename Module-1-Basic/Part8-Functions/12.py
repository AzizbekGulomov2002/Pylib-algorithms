


def find_larger(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return "Ikkalasi teng"

a = float(input("birinchi son : "))
b = float(input("ikkinchi son : "))
result = find_larger(a,b)
print(f"Katta son: {result}")