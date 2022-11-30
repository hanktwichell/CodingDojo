from classes.deck import Deck
from classes.deck2 import Deck2
from classes.player import Player

# Prizecard War
bicycle = Deck()
player1 = Player()
player2 = Player()
bicycle.shuffle()
bicycle.deal(player1, player2)

def prizecard_war():
    while (player1.get_hand_size() > 0 and player2.get_hand_size() > 0):
        in_play = []
        c1 = 0
        c2 = 0
        while (c1 == c2):
            if (player1.get_hand_size() == 0 or player2.get_hand_size() == 0):
                return
            card1 = player1.play_top_card()
            card2 = player2.play_top_card()
            in_play.append(card1)
            in_play.append(card2)
            c1 = card1.point_val
            c2 = card2.point_val
        if (c1 > c2):
            while len(in_play) > 0:
                player1.add_prizecard(in_play.pop(0))
        else:
            while len(in_play) > 0:
                player2.add_prizecard(in_play.pop(0))
    if (player1.num_prizecards() == player2.num_prizecards()):
        print(f"It's a tie! {player1.num_prizecards()}-{player2.num_prizecards()}!")
    elif (player1.num_prizecards() > player2.num_prizecards()):
        print(f"Player 1 Won {player1.num_prizecards()}-{player2.num_prizecards()}! Congratulations!")
    else:
        print(f"Player 2 Won {player2.num_prizecards()}-{player1.num_prizecards()}! Congratulations!")

prizecard_war()


# Egyptian Rat Slap

tricycle = Deck2()
player3 = Player()
player4 = Player()
tricycle.shuffle()
tricycle.deal(player3, player4)

def check_doubles(in_play, last_turn):
    if ((len(in_play) > 1 and in_play[0].point_val == in_play[1].point_val) or (len(in_play) > 2 and in_play[0].point_val == in_play[2].point_val)):
        if (last_turn == 1):
            while len(in_play) > 0:
                player3.add_card(in_play.pop(0))
            return True
        else:
            while len(in_play) > 0:
                player4.add_card(in_play.pop(0))
            return True
    return False

def no_cards(player):
    return player.get_hand_size() == 0

def egyptian_rat_slap():
    honors = 1
    rounds = 0
    while (player3.get_hand_size() > 0 and player4.get_hand_size() > 0):
        in_play = []
        facecard = False
        countdown = 0
        rounds += 1
        turns = 0
        print(f"-- Round {rounds} | Cards: P3-{player3.get_hand_size()} P4-{player4.get_hand_size()} --")
        while facecard == False:
            if ((turns + honors) % 2 == 1):
                if (no_cards(player3)):
                    return "Player 4 Wins!"
                in_play.insert(0, player3.play_top_card())
                print(f"P3 T{turns} {in_play[0].get_abrv()}")
                
            else:
                if (no_cards(player4)):
                    return "Player 3 Wins!"
                in_play.insert(0, player4.play_top_card())
                print(f"P4 T{turns} {in_play[0].get_abrv()}")
            if (check_doubles(in_play, (turns + honors) % 2)):
                if ((turns + honors) % 2 == 1):
                    honors =  1
                else:
                    honors = 0
                break
            if (in_play[0].point_val > 10):
                facecard = True
                countdown = in_play[0].point_val - 10
            turns += 1
        while facecard == True and countdown > 0:
            if ((turns + honors) % 2 == 1):
                if (no_cards(player3)):
                    return "Player 4 Wins!"
                in_play.insert(0, player3.play_top_card())
                print(f"P3 T{turns} {in_play[0].get_abrv()} *")
            else:
                if (no_cards(player4)):
                    return "Player 3 Wins!"
                in_play.insert(0, player4.play_top_card())
                print(f"P4 T{turns} {in_play[0].get_abrv()} *")
            if (check_doubles(in_play, (turns + honors)%2)):
                if ((turns + honors) % 2 == 1):
                    honors = 1
                else: 
                    honors = 0
                break
            if (in_play[0].point_val > 10):
                countdown = in_play[0].point_val - 10
                turns += 1
            else:
                countdown -= 1
        if (countdown == 0):
            if ((turns + honors) % 2 == 1):
                while len(in_play) > 0:
                    player4.add_card(in_play.pop(0))
                honors = 0
            else:
                while len(in_play) > 0:
                    player3.add_card(in_play.pop(0))
                honors = 1
    if (player3.get_hand_size() > player4.get_hand_size()):
        return "Player 3 Wins!"
    return "Player 4 Wins!"

print(egyptian_rat_slap())
