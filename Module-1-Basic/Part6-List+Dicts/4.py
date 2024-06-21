
# Berilgan numbers ro'yxatdagi 3 ga qoldiqsiz bo'linadigan sonlarni olib, yangi ro'yxatga joylashtiring.


input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = []
for i in input:
    if i % 3 == 0:
        output.append(i)
print(output)