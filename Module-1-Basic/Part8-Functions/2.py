

def even_nums(numbers):
    evens = []
    for num in numbers:
        if num%2==0:
            evens.append(num)
    return evens

list_numbers = [1,2,3,4,5,6,7,8,9,10]
result = even_nums(list_numbers)
print(f"Juft sonlar: {result}")