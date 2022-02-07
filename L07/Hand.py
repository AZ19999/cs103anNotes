'''
   Hand class represents a named list of playing cards with suit and rank
'''

from Card import *


class Hand():
    ''' this is a named list of cards '''

    def __init__(self,name,cards):
        self.name = name
        self.cards =cards

    def __str__(self):
        return self.name+":"+str([c.__str__() for c in self.cards])

    def get_name(self):
        return self.name

    def get_cards(self):
        return self.cards

    def set_cards(self,new_cards):
        self.cards = new_cards

    def pick_card(self,n):
        c = self.cards[n]
        del self.cards[n]
        return c

    def add_card(self,c):
        self.cards.append(c)



        


def test_hand():

    c1 = Card(1,0)
    c2 = Card(5,2)
    c3 = Card(13,0)
    c4 = Card(1,2)
    print("here is a hand")
    h = Hand("Tim",[c1,c2,c3,c4])
    print(h)
    c = Card(5,0)
    print("Let's remove any cards that match",c,'from',h)
    d=h.remove_match(c)
    print('here is the card removed',d,'and the new hand',h)


    


        

    
