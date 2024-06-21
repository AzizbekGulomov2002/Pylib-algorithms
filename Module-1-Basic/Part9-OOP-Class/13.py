

class MovieTicket:
    def __init__(self, age, showtime):
        self.age = age
        self.showtime = showtime

age = int(input("Yosh: "))
showtime = input("Seans vaqti: ")

ticket = MovieTicket(age, showtime)
if ticket.age < 18:
    price = 5  # 50% chegirma
else:
    price = 10

print(f"Yosh: {ticket.age}, Seans: {ticket.showtime}, Bilet narxi: ${price}")
