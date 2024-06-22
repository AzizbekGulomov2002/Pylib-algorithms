def calculate_total(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total += value
    return total

# Test qilish
print(calculate_total(apples=10, oranges=5, bananas=7))  # Natija: 22
