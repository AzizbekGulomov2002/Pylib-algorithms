


baza = {'Ali': 85, 'Vali': 60, 'Soli': 45}
student_name = input("Talaba ismini kiriting: ")
if student_name in baza:
    grade = baza[student_name]
    print(f"{student_name} ning bahosi: {grade}")
    if grade >= 80:
        print("A'lochi")
    elif grade>=50:
        print("O'rtacha")
    else:
        print("Qoniqarsiz")
else:
    print("Talaba bazadan topilmadi")