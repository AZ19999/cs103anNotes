'''
Examples of Python classes
'''


class BankAccount():
    def __init__(self,name,starting_balance):
        self.name = name
        self.balance = starting_balance

    def __str__(self):
        return "["+self.name+","+str(self.balance)+"]"

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def transfer(self, account, amount):
        self.balance -= amount
        account.balance += amount


class Card():
    ''' This is a standard playing card with suit and rank '''

    ranks = "Joker A 2 3 4 5 6 7 8 9 10 J Q K".split()
    suits = "Hearts Clubs Diamonds Spades".split()
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def __str__(self):
        return Card.ranks[self.rank]+":"+Card.suits[self.suit]


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

    def remove_match(self,c):
        ''' remove the cards with the same rank and same color suit
              hearts and diamonds are red (0,2)
              clubs and spades are black (1,3)
        '''
        suit = c.get_suit()
        matching_suit = (suit+2)%4
        for i in range(len(self.cards)):
            b = self.cards[i]
            if b.get_rank() == c.get_rank() and b.get_suit()==matching_suit:
                del self.cards[i]
                return b


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

    


        

    
