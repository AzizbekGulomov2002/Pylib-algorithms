
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name, int(salary))

# Test
emp_str = "John Doe-50000"
employee = Employee.from_string(emp_str)
print(f"Ism: {employee.name}, Maosh: {employee.salary}")
