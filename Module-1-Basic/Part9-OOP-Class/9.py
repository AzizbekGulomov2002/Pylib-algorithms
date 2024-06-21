


class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

model = input("Avtomobil modeli: ")
year = int(input("Avtomobil yili: "))

car = Car(model, year)
if car.year <= 2010:
    print("Eski avtomobil")
else:
    print("Yangi avtomobil")
