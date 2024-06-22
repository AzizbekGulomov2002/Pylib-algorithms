def print_customer_info(name, **kwargs):
    print(f"Mijozning ismi: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Test qilish
print_customer_info("John", age=30, city="New York", email="john@example.com")