

class Exam:
    def __init__(self, total_questions, correct_answers):
        self.total_questions = total_questions
        self.correct_answers = correct_answers

    def calculate_score(self):
        return self.correct_answers * 3.1

total_questions = int(input("Savollar soni: "))
correct_answers = int(input("To'g'ri javoblar soni: "))

exam = Exam(total_questions, correct_answers)
score = exam.calculate_score()
passing_score = (total_questions * 3.1) * 0.7  # 70% of the total possible score

if score >= passing_score:
    print("Muvaffaqiyatli")
else:
    print("Muvaffaqiyatsiz")

print(f"To'plangan ball: {score}")

