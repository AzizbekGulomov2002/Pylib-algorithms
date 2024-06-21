
class CinemaVisitor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input("Tomoshabin ismi: ")
age = int(input("Yoshi: "))

visitor = CinemaVisitor(name, age)

if visitor.age >= 18:
    print(f"{visitor.name} kattalar uchun kinoga ruxsat berilgan.")
else:
    print(f"{visitor.name} bolalar uchun kinoga ruxsat berilgan.")
