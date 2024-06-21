# Berilgan numbers ro'yxatdagi eng katta elementni toping va natijani chiqaring.

input = [3, 5, 7, 2, 8, 1]
max = input[0]
for i in input:
    if i > max:
        max = i
print(max)