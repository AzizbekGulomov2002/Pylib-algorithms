

def reward(grade):
    if grade >= 90:
        return "A'lo baho"
    elif grade >= 75:
        return "Yaxshi baho"
    elif grade >= 50:
        return "Qoniqarli"
    else:
        return "Qoniqarsiz"

grade = int(input("Bahoni kiriting = "))
result = reward(grade)
print(result)