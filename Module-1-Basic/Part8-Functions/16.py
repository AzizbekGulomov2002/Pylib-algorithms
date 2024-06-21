



def is_ascending(a,b,c):
    if a<b<c:
        return "Sonlar orib borish tartibida"
    elif a>b>c:
        return "Sonlar kamayib borish tartibida"
    else:
        return "Sonlar ortib borish tartibida emas"

a = float(input("Birinchi son: "))
b = float(input("Ikkinchi son: "))
c = float(input("Uchinchi son: "))

result = is_ascending(a,b,c)
print(result)