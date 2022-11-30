from classes import card
from classes import player
import math, random

class Deck:
    def __init__(self):
        suits = ["spades", "hearts", "clubs", "diamonds"]
        self.cards = []
        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append(card.Card(s, i, str_val))

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def show_abrvs(self):
        for card in self.cards:
            print(card.get_abrv())

    def get_num_cards(self):
        return len(self.cards)
    
    def get_order(self):
        for card in self.cards:
            print(card.suit)

    def shuffle(self):
        shuffled = []
        while len(self.cards) > 0:
            shuffled.append(self.cards.pop(math.floor(random.randrange(0, len(self.cards)))))
        self.cards = shuffled

    def deal(self, player1, player2):
        for i in range(len(self.cards)):
            if i%2 == 1:
                player1.add_card(self.cards[i])
            else:
                player2.add_card(self.cards[i])

