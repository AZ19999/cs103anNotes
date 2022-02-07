'''
   Card class represents a playing card with suit and rank
'''


class Card():
    ''' This is a standard playing card with suit and rank '''

    ranks = "Joker A 2 3 4 5 6 7 8 9 10 J Q K".split()
    standard_ranks = ranks[1:]  # remove the jokers
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

    def __repr__(self):
        return 'Card('+str(self.rank)+","+str(self.suit)+')' 

    def __cmp__(self,c):
        ''' returns 0 if self==c, -1 if self<c and +1 if self>c '''
        if (self.rank == c.rank) and (self.suit==c.suit):
            return 0
        elif self.rank != c.rank:
            return self.rank - c.rank
        else:
            return self.suit-c.suit



        

    
