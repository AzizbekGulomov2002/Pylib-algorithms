


class Circle:
    def __init__(self, radius):
        self.radius = radius

radius = float(input("Radius: "))

circle = Circle(radius)
if circle.radius > 0:
    area = 3.14 * circle.radius ** 2
    print(f"Aylaning yuzasi: {area}")
else:
    print("Noto'g'ri radius")
