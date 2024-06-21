

products = {"olma":3, "banan":2.5, "shaftoli":4}
product_name = input("Mahsulot nomini kiriting = ")
if product_name in products:
    print(f"{product_name.capitalize()} narxi: {products[product_name]} $")
else:
    print("Mahsulot topilmadi")
