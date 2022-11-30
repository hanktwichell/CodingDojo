class Card:
    def __init__(self, suit, point_val, string_val):
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

    def card_info(self):
        print(f"{self.string_val} of {self.suit} : {self.point_val} points")

    def get_abrv(self):
        abrv = ""
        if (self.point_val == 1):
            abrv = "A"
        elif (self.point_val < 11):
            abrv = str(self.point_val)
        else:
            abrv = self.string_val[0]
        abrv += "o" + self.suit[0].upper()
        return abrv
    
    # def get_int(self):
    #     base = 0
    #     if (self.suit == "clubs"):
    #         base = 13
    #     if (self.suit == "diamonds"):
    #         base = 26
    #     if (self.suit == "spades"):
    #         base = 39
    #     return self.point_val + base
