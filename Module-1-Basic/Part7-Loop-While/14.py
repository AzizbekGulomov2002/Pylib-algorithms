

total = 0
number_list = []
while True:
    number = int(input("Son kiriting (to'xtatish uchun 0 bosing) : "))
    if number == 0:
        break
    number_list.append(number)
total = sum(number_list)
print(f"Yig'indi: {total}")