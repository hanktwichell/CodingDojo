from classes import card
class Player:
    def __init__(self):
        self.cards = []
        self.prizecards = []

    def play_top_card(self):
        return self.cards.pop(0)
    
    def add_card(self, card):
        self.cards.append(card)

    def reveal_hand(self):
        for card in self.cards:
            print(card.get_abrv())

    def get_hand_size(self):
        return len(self.cards)

    def add_prizecard(self, card):
        self.prizecards.append(card)

    def reveal_prizecards(self):
        for prizecard in self.prizecards:
            print(prizecard.get_abrv())

    def num_prizecards(self):
        return len(self.prizecards)
