def perform_operation(operation, *args):
    if operation == 'add':
        result = sum(args)
    elif operation == 'multiply':
        result = 1
        for num in args:
            result *= num
    else:
        return "Noto'g'ri amal"

    return result

# Test qilish
print(perform_operation('add', 1, 2, 3))  # Natija: 6
print(perform_operation('multiply', 2, 3, 4))  # Natija: 24