import random

class Sazka:
    def __init__(self, rounds):
        self.rounds = rounds

    def sportka(self):
        list_of_rounds = []
        for i in range(0, self.rounds):
            rounds = random.sample(range(1, 51), 6)
            list_of_rounds.append(sorted(list(rounds)))
        return list_of_rounds

    def euromiliony(self):
        list_of_rounds = []
        list_of_osudi = []
        for j in range(0, self.rounds):
            osudi = random.sample(range(1, 6), 2)
            list_of_osudi.append(sorted(list(osudi)))
        for i in range(0, self.rounds):
            rounds = random.sample(range(1, 36), 7)
            list_of_rounds.append(sorted(list(rounds)))
        return list(zip(list_of_rounds, list_of_osudi))

    def extra_renta(self):
        list_of_rounds = []
        for i in range(0, self.rounds):
            rounds = random.sample(range(1, 34), 7)
            list_of_rounds.append(sorted(list(rounds)))
        return list_of_rounds


tah_1 = Sazka(3)

print(tah_1.sportka())
print(tah_1.euromiliony())
print(tah_1.extra_renta())
