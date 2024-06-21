
class Athlete:
    def __init__(self, name, trainings):
        self.name = name
        self.trainings = trainings

name = input("Sportchi ismi: ")
trainings = input("Mashg'ulotlar (vergul bilan ajratilgan): ").split(',')

athlete = Athlete(name, trainings)
if not athlete.trainings or athlete.trainings == ['']:
    print("Mashg'ulotlar kiritilmagan")
else:
    print(f"{athlete.name}ning mashg'ulotlari: {', '.join(athlete.trainings)}")
