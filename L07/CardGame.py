'''
    CardGame
'''

from Card import *
from Hand import *
from Deck import *


class CardGame(Deck):
    '''  a framework for a multiplayer card game
         this simple game just gives a point if they select a face card!
         the game ends when someone picks the queen of spades (12,3)
    '''

    def __init__(self, num_players):
        # create an empty hand for each player
        super().__init__()  # create a Deck with no jokers
        self.shuffle()
        self.hands = [Hand('player'+str(i),[]) for i in range(num_players)]
        self.points = [0 for i in range(num_players)]
        self.round = 1

    def play(self):
        '''
            play multiple rounds until the game is over
        '''
        game_over=False
        while not game_over:
            game_over = self.play_one_round()
            self.round += 1

        print("game over!")

    def play_one_round(self):
        ''' every one takes a turn and possibly ending the game '''
        print('\n\nROUND',self.round)
        print('score',self.points)
        print('hands')
        for h in self.hands:
            print(h)
        for i in range(len(self.hands)):
            game_over = self.take_turn(i)
            if game_over:
                return True
        input("press return to continue")
        return False

    def take_turn(self,i):
        ''' we need to override this to make it a game '''
        card = self.pick_card(0)
        if card.get_rank()>10:
            self.hands[i].add_card(card)
        print('picked',card)
        if card.get_rank()==12 and card.get_suit()==3:
            return True
        if card.get_rank()>10:
            self.points[i] +=1
        return False
        
        pass


if __name__=='__main__':
    game = CardGame(3)
    game.play()
    print("hello world")




    

