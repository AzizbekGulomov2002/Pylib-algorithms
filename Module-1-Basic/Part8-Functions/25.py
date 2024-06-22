def create_product(name, **kwargs):
    product = {'name': name}
    product.update(kwargs)
    return product

# Foydalanuvchi kiritgan ma'lumotlar
name = input("Mahsulot nomini kiriting: ")
price = float(input("Mahsulot narxini kiriting: "))
quantity = int(input("Mahsulot miqdorini kiriting: "))
product = create_product(name, price=price, quantity=quantity)
print("Mahsulot:", product)
