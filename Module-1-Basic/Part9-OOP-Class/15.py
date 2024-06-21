
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

title = input("Kitob nomi: ")
author = input("Muallif ismi: ")

book = Book(title, author)
if not book.title or not book.author:
    print("Noto'g'ri ma'lumotlar")
else:
    print(f"Kitob nomi: {book.title}, Muallif: {book.author}")
