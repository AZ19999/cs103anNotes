'''
   Deck - a standard 52 card deck
'''

from Hand import *
from Card import *
import random

class Deck(Hand):
    ''' a deck of 52 cards '''

    def __init__(self,name='deck',num_jokers=0):
        self.name = name
        self.cards=[]

        for rank in range(1,14):
            for suit in range(0,4):
                card = Card(rank,suit)
                self.cards.append(card)

        for i in range(num_jokers):
            self.cards.append(Card(0,i))

    def shuffle(self):
        random.shuffle(self.cards)


            

