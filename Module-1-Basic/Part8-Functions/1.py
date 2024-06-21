


# Berilgan ro'yxat elementlarini yig'indisini hisoblaydigan funktsiya tuzing.


def sum_list(numbers):
    total = 0
    for i in numbers:
        total+=i
    return total

list = [1,2,3,4,5]
result = sum_list(list)
print(f"Ro'yxat yig'indisi : {result}")