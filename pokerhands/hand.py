from card import Card 
from deck import Deck 


#WRITE YOUR HAND CLASS BELOW
class Hand:
    def __init__(self):
      self.hand = []
    
    def add_card(self,card):
        self.hand.append(card)
    
    def __str__(self):
        ret = ""
        for card in self.hand:
            ret += str(card) + "\n"
        return ret

    def add_cards_from_deck(self,deck,num):
        for i in range(num):
            self.add_card(deck.get_next_card())

    def get_rank_dictionary(self):
        d = {}
        for card in self.hand:
            if card.get_rank_name() not in d:
                d[card.get_rank_name()] = 0
            d[card.get_rank_name()] += 1
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
        return d

    def check_one_pair(self):
        d = self.get_rank_dictionary()
        pair_count = 0
        three_check = False
        for card in d:
            if d[card] == 2:
                pair_count += 1
            elif d[card] == 3:
                three_check = True
        if pair_count == 1 and not three_check:
            return True
        return False

    def check_two_pair(self):
        d = self.get_rank_dictionary()
        pair_count = 0
        for card in d:
            if d[card] == 2:
                pair_count += 1
        if pair_count == 2:
            return True
        return False

    def check_three_of_a_kind(self):
        d = self.get_rank_dictionary()
        set_count = 0
        pair_check = False
        for card in d:
            if d[card] == 3:
                set_count +=1
            elif d[card] == 2:
                pair_check = True
        if set_count == 1 and not pair_check:
            return True
        return False

    def check_four_of_a_kind(self):
        d = self.get_rank_dictionary()
        for card in d:
            if d[card] == 4:
                return True
        return False

    def check_full_house(self):
        d = self.get_rank_dictionary()
        three_count = 0
        two_count = 0
        for card in d:
            if d[card] == 3:
                three_count += 1
            elif d[card] == 2:
                two_count += 1
        if three_count == two_count == 1:
            return True
        return False

    def check_flush(self):
        l = []
        for card in self.hand:
            l.append(card.suit)
        
        for i in range(len(l)-1):
            if l[i] != l[i+1]:
                return False
        return True

    def check_straight(self):
        l = []
        for card in sorted(self.hand):
            l.append(card.rank)
        
        for i in range(len(l)-1,0,-1):
            if l[i] != l[i-1] + 1:
                return False
        return True

    def get_hand_type(self):
        if self.check_straight() and self.check_flush():
            return "Straight Flush"
        elif self.check_one_pair():
            return "One Pair"
        elif self.check_two_pair():
            return "Two Pair"
        elif self.check_three_of_a_kind():
            return "Three of a kind"
        elif self.check_four_of_a_kind():
            return "Four of a kind"
        elif self.check_flush():
            return "Flush"
        elif self.check_full_house():
            return "Full House"
        elif self.check_straight():
            return "Straight"
        else:
            return "High Card"
