import random

class Sazka():




def sportka(self):
    list_of_rounds = []
    counter = 0
    while counter < 10:
        pick = []
        for i in range(6):
            x = random.randint(1, 49)
            pick.append(x)
            final_pick = sorted(pick)
        if len(set(final_pick)) == len(final_pick):
            list_of_rounds.append(final_pick)
            counter += 1
        else:
            continue
    return list_of_rounds

def euromiliony(self):
    list_of_first_rounds = []
    counter = 0
    while counter < 6:
        round_one = []
        for i in range(5):
            x = random.randint(1, 50)
            round_one.append(x)
            final_round_one = sorted(round_one)
        if len(set(final_round_one)) == len(final_round_one):
            list_of_first_rounds.append(final_round_one)
            counter += 1
        else:
            continue

    counter = 0
    list_of_second_rounds = []
    while counter < 6:
        round_two = []
        for i in range(2):
            y = random.randint(1, 10)
            round_two.append(y)
            final_round_two = sorted(round_two)
        if len(set(final_round_two)) == len(final_round_two):
            list_of_second_rounds.append(final_round_two)
            counter += 1
        else:
            continue
    return list(zip(list_of_first_rounds, list_of_second_rounds))

ticket = Sazka()
#print(ticket.sportka())
#print(ticket.euromiliony())
print("SPORTKA")
for row in ticket.sportka():
    print(row)
print(80*"-")
print("EUROMILIONY")
for one, two in ticket.euromiliony():
    print(one, two)