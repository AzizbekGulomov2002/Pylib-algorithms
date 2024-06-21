
# Berilgan numbers ro'yxatdagi toq sonlarning kvadratini hisoblang va natijani chiqaring.


input = [1, 2, 3, 4, 5]
output = []

for i in input:
    if i%2!=0:
        output.append(i**2)
print(output)