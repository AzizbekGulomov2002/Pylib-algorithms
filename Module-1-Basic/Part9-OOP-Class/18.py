


class Appliance:
    def __init__(self, name, power, hours):
        self.name = name
        self.power = power
        self.hours = hours

name = input("Qurilma nomi: ")
power = float(input("Quvvat (vattlarda): "))
hours = float(input("Ishlash vaqti (soatlarda): "))

appliance = Appliance(name, power, hours)
energy_consumption = appliance.power * appliance.hours

if energy_consumption > 1000:
    print(f"{appliance.name} yuqori energiya sarfiga ega.")
else:
    print(f"{appliance.name} normal energiya sarfiga ega.")

print(f"Umumiy energiya sarfi: {energy_consumption} Vatt-soat")

