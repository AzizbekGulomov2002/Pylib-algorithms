
class ShoppingList:
    def __init__(self, name, items):
        self.name = name
        self.items = items

name = input("Mijoz ismi: ")
items = input("Xaridlar (vergul bilan ajratilgan): ").split(',')

customer = ShoppingList(name, items)
if not customer.items or customer.items == ['']:
    print("Xaridlar kiritilmagan")
else:
    print(f"{customer.name} mijozning xaridlari: {', '.join(customer.items)}")
