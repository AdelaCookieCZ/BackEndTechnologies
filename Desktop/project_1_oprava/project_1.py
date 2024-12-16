"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Adéla Michl
email: kolackova.adela@gmail.com
"""
from collections import Counter

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

user_password = {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}
user = str(input("Zadejte vase username: "))
password = str(input("Zadejte vase heslo: "))
capital_word_count = 0
upper_case_word_count = 0
lower_case_word_count = 0
numeric_string_count = 0
number_sum = 0

print(f"{'-' * 40}")

if user_password.get(user) == password:
    print(f"Welcome to the app, {user}\n"
          f"We have 3 texts to be analyzed.\n"
          f"{'-' * 40}")
    text_number = input("Enter a number btw. 1 and 3 to select: " )
    if not text_number.isnumeric():
        print("Zadana hodnota neni platna.")
    elif int(text_number) not in range(1,4):
        print("Zadane cislo textu neexistuje.")
    else:
        text_number = int(text_number) - 1
        text_length = len(TEXTS[text_number].split())
        for word in TEXTS[text_number].split():
            if word[0].isupper():
                capital_word_count += 1
            if word.isupper() and word.isalpha():
                upper_case_word_count += 1
            if word.islower():
                lower_case_word_count += 1
            if word.isnumeric():
                numeric_string_count += 1
            if word.isnumeric():
                number_sum += int(word)

        #graph variables
        word_lengths = [len(word.strip('.,!?')) for word in TEXTS[text_number].split()]
        length_counts = Counter(word_lengths)
        length_counts = dict(sorted(length_counts.items()))
        max_length = max(length_counts.keys(), default=0)
        max_count = max(length_counts.values(), default=0)

        print(f"{'-' * 40}\n"
              f"There are {text_length} words in the selected text.\n"
              f"There are {capital_word_count} titlecase words.\n"
              f"There are {upper_case_word_count} uppercase words.\n"
              f"There are {lower_case_word_count} lowercase words.\n"
              f"There are {numeric_string_count} numeric strings.\n"
              f"The sum of all the numbers {number_sum}\n"
              f"{'-' * 40}\n"
              f"{'LEN':>4}| {'OCCURENCES':^{max_count-1}}| {'NR.':<3}\n"
              f"{'-' * 40}")
        #graph creation
        for length in range(1, max_length + 1):
            count = length_counts.get(length, 0)
            print(f"{length:>4}|{'*' * count:<{max_count}}|{count:<3}")
else:
    print(f"Unregistered user, terminating the program..")