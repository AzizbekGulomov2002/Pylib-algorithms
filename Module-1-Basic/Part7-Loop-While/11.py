


total = 0
while True:
    number = input("Son kiriting (to'xtatish uchun 'stop' yozing): ")
    if number.lower() == "stop":
        break
    total += int(number)
print(f"Yig'indi: {total}")