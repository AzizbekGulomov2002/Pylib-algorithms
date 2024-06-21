
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Yetarli mablag' mavjud emas!")

    def get_balance(self):
        return self.__balance

# Test
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print(f"Hisobdagi mablag': {account.get_balance()} $")
