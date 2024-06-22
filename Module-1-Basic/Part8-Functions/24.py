
def sum_numbers(*args):
    return sum(args)

# Foydalanuvchi kiritgan sonlar
numbers = list(map(float, input("Sonlarni kiriting (vergul bilan ajrating): ").split(',')))
print("Yig'indi:", sum_numbers(*numbers))
