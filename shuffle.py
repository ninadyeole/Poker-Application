import random
#Building a Deck of Cards
suits = list(range(4))
value = list(range(13))
deck_of_cards = list()
 
for i in suits:
    for j in value:
        deck_of_cards.append((i,j))
 
#shuffle the deck: random.shuffle time complexity = O(n)
random.shuffle(deck_of_cards)

#shuffled deck of cards
print(deck_of_cards)

#deal two cards
[print(deck_of_cards[i]) for i in range(2)]
