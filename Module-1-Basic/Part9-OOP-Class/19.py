
class Car:
    def __init__(self, model, distance, time):
        self.model = model
        self.distance = distance
        self.time = time

model = input("Avtomobil modeli: ")
distance = float(input("Masofa (kilometrda): "))
time = float(input("Vaqt (soatda): "))

car = Car(model, distance, time)
speed = car.distance / car.time
if speed > 100:
    print(f"{car.model} tez yuradi (Tezlik: {speed} km/soat).")
else:
    print(f"{car.model} oddiy tezlikda yuradi (Tezlik: {speed} km/soat).")
