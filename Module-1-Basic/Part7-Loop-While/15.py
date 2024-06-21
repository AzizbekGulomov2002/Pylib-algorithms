numbers = []
while len(numbers) < 5:
    number = int(input("Son kiriting: "))
    numbers.append(number)

for num in numbers:
    if num % 2 == 0:
        print(f"{num} juft son")
    else:
        print(f"{num} toq son")
