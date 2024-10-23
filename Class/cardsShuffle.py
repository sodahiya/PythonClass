import random
# a list of all the suits
Suits = ["\u2663", "\u2665",
         "\u2666", "\u2660"]
# a list of all the ranks
Ranks = ['A', '2', '3', '4', '5',
         '6', '7', '8', '9', '10',
         'J', 'Q', 'K']
cards = []

for i in Ranks:
    for j in Suits:
        cards.append(f"{i} of {j}")

random.shuffle(cards)

for i  in range(4):
    print(f"Player {i+1}: ", end = ' ')
    for j in range(13):
        print(cards[i*13 + j], end = ' ')
    print()