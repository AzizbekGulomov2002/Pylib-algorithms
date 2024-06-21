
class Student:
    def __init__(self, name, course, grade):
        self.name = name
        self.course = course
        self.grade = grade

name = input("Talabaning ismi: ")
course = input("Talabaning kursi: ")
grade = int(input("Talabaning bahosi: "))

student = Student(name, course, grade)
if student.grade >= 50:
    print(f"{student.name} muvaffaqiyatli bo'ldi.")
else:
    print(f"{student.name} muvaffaqiyatli bo'lmadi.")
