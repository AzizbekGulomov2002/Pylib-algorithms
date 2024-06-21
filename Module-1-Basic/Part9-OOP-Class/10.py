
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

length = float(input("Uzunlik: "))
width = float(input("Kenglik: "))

rectangle = Rectangle(length, width)
if rectangle.length > 0 and rectangle.width > 0:
    perimeter = 2 * (rectangle.length + rectangle.width)
    print(f"To'rtburchak perimetri: {perimeter}")
else:
    print("Noto'g'ri o'lchamlar")
