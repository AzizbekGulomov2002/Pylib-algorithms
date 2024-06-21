# Berilgan numbers ro'yxatdagi eng kichik elementni toping va natijani chiqaring.

input = [3, 5, 7, 2, 8, 1]
min = input[0]

for i in input:
    if i<min:
        min = i
print(min)