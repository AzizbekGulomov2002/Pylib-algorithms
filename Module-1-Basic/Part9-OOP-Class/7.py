


class Employee:
    def __init__(self, name, hours_worked):
        self.name = name
        self.hours_worked = hours_worked

name = input("Ishchining ismi: ")
hours_worked = int(input("Haftalik ish soatlari: "))

employee = Employee(name, hours_worked)
if employee.hours_worked > 40:
    overtime = employee.hours_worked - 40
    salary = (40 * 10) + (overtime * 15)
else:
    salary = employee.hours_worked * 10

print(f"{employee.name}ning umumiy maoshi: ${salary}")
