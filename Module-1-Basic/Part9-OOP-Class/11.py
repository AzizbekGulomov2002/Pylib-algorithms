class Invoice:
    def __init__(self, item, price):
        self.item = item
        self.price = price

item = input("Tovar nomi: ")
price = float(input("Narxi: "))

invoice = Invoice(item, price)
if invoice.price > 10:
    discounted_price = invoice.price * 0.9
    print(f"Chegirmadan keyingi narx: ${discounted_price:.2f}")
else:
    print(f"Narx: ${invoice.price:.2f}")
