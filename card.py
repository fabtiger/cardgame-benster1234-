

suit = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

face = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

 



 

from random import *

current = 1

def card_game(current=1):

while current in range(1, 11):
suit_random = suit[randrange(0, 3)]

face_random = face[randrange(0, 12)]

 

used_suit = []

used_face = []

 

if suit_random not in used_suit and face_random not in used_face:

    print '%s of %s' % (face_random, suit_random)

        else:

        card_game()

 

        used_suit.append(suit_random)

        used_face.append(face_random)

 

     current = current + 1

 

card_game()
