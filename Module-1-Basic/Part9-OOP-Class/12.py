
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

name = input("Tovar nomi: ")
price = float(input("Narxi: "))

product = Product(name, price)
if product.price > 50:
    tax = product.price * 0.08
else:
    tax = product.price * 0.05

final_price = product.price + tax
print(f"Yakuniy narx (soliq bilan): ${final_price:.2f}")
