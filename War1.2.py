import random

suits = ("hearts", "diamonds", "spades", "clubs")
ranks = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace")
values = {"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, 
          "jack":11, "queen":12, "king":13, "ace":14}

class Card:
    
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
    
class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards=[]
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self,):
        return f"Player {self.name} has {len(self.all_cards)} cards."

#game setup
player1 = Player('one')
player2 = Player('two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())

round_num = 0
game_on = True

while game_on:
    round_num += 1
    print(f"Round {round_num}.")
    
    if len(player1.all_cards) == 0:
        print("Player 1 out of cards! Player 2 wins!")
        game_on = False
        break
    elif len(player2.all_cards) == 0:
        print("Player 2 out of cards! Player 2 wins!")
        game_on = False
        break
        
    #start new round
    player_one_cards = []
    player_one_cards.append(player1.remove_one())
    player_two_cards = []
    player_two_cards.append(player2.remove_one())
    
    at_war = True
    
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player1.add_cards(player_one_cards)
            player1.add_cards(player_two_cards)
            at_war = False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player2.add_cards(player_one_cards)
            player2.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR!")
            if len(player1.all_cards) < 5:
                print("Player 1 unable to declare war! Player 2 wins!")
                game_on=False
                break
            elif len(player2.all_cards) < 5:
                print("Player 2 unable to declare war! Player 1 wins!")
                game_on=False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player1.remove_one())
                    player_two_cards.append(player2.remove_one())
                