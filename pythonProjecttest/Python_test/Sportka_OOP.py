from random import randint

# def sportka():
#     for i in range(2):
#         tah = set()
#         while len(tah) < 6:
#             tah.add(randint(1, 49))
#     return tah
#
# print(sportka())

class Sazka:
    def __init__(self, tah):
        self.tah = set(tah)

    def sportka(self):
        for _ in range(10):
            while len(self.tah) < 6:
                self.tah.add(randint(1, 49))
        return sorted(list(self.tah))

    def euromiliony(self, osudi):
        self.osudi = osudi
        while len(self.tah) < 7:
            self.tah.add(randint(1, 35))
        while len(self.osudi) < 1:
            self.osudi.add(randint(1, 5))
        return sorted(list(self.tah)), self.osudi

tah_1 = Sazka()
tah_1.sportka()


