from card import Card 
from deck import Deck 
from hand import Hand

# card1 = Card("Three", "Hearts")
# card2 = Card(3, 3)
# print(card1)
# print(card2)

# print(card1 > card2)

# deck = Deck()
# print(deck)

# h = Hand()
# h.add_card(Card("Ten", "Hearts"))
# h.add_card(Card("Jack", "Clubs"))
# print(h)

# d = Deck()
# h = Hand()
# h.add_cards_from_deck(d, 12)
# print(h)

# d = Deck()
# h = Hand()
# h.add_cards_from_deck(d, 10)
# print(h)
# print(h.get_rank_dictionary())

# h = Hand()
# h.add_card(Card("Ten", "Hearts"))
# h.add_card(Card("Jack", "Clubs"))
# h.add_card(Card("Ten", "Spades"))
# h.add_card(Card("Ace", "Clubs"))
# h.add_card(Card("King", "Hearts"))
# s = h.check_one_pair()

# print(h.hand[2])
# print(h)
# print(s)  #should print True
# print("-------")

# h = Hand()
# h.add_card(Card("Ten", "Hearts"))
# h.add_card(Card("Nine", "Clubs"))
# h.add_card(Card("Eight", "Spades"))
# h.add_card(Card("Seven", "Clubs"))
# h.add_card(Card("Six", "Hearts"))
# s = h.check_straight()
# print(h)
# print(s)  #should print True
# print("-------")


def five_card_draw():
    d = Deck()
    p1 = Hand()
    p2 = Hand()
    p1.add_cards_from_deck(d,5)
    print("It is Player 1's turn: ")
    print(p1)
    counter = 0
    while counter < 3:
        choice = input("Which card would you like to trade in? Type n to stop trading. \n")
        if choice.lower() == "n":
            break
        choice = int(choice)
        p1.hand.pop(choice-1)
        p1.hand.insert(choice-1,d.get_next_card())
        print(p1)
        counter += 1
    print(f"Player 1's final hand is: \n{str(p1)}")
    p2.add_cards_from_deck(d,5)
    print("It is Player 2's turn: ")
    print(p2)
    counter = 0
    while counter < 3:
        choice = input("Which card would you like to trade in? Type n to stop trading. \n")
        if choice.lower() == "n":
            break
        choice = int(choice)
        p2.hand.pop(choice-1)
        p2.hand.insert(choice-1,d.get_next_card())
        print(p2)
        counter += 1
    print(f"Player 2's final hand is: \n{str(p2)}")
    hand_type_rank = ["straight flush","four of a kind","full house","flush","straight","three of a kind","two pair","one pair","high card"]
    p1_rank = hand_type_rank.index(p1.get_hand_type().lower())
    p2_rank = hand_type_rank.index(p2.get_hand_type().lower())
    if p1_rank < p2_rank:
        print(f"Player 1 wins with the hand\n{str(p1)}Their hand was {p1.get_hand_type()}")
    elif p1_rank > p2_rank:
        print(f"Player 2 wins with the hand\n{str(p2)}Their hand was {p2.get_hand_type()}")
    else:
        print(f"The game ends in a tie!\nBoth Players hands were {p1.get_hand_type()}\n")

        
    
# five_card_draw()

### This code semi-works.
### When it comes to determining the winner, it prints out a list (sometimes more than 2) 
### I never tell it to do this which is confusing me