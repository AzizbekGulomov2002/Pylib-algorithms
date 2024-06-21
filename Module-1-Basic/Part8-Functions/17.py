


def max_min_difference(numbers):
    if not numbers:
        return "Ro'yxat mavjud emas"
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num-min_num

my_list = [10,4,8,3,15,6]
result = max_min_difference(my_list)
print(f"Eng katta va eng kichik sonlar farqi: {result}")