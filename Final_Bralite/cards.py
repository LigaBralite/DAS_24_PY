import random
import itertools 

def get_deck(suits="♦♣♥♠", ranks=tuple("JQKA23456789")+("10",)): 
    return list(itertools.product(suits, ranks))

def get_shuffled_deck(suits="♦♣♥♠", ranks=tuple("JQKA23456789")+("10",)):
    deck = get_deck(suits, ranks)
    random.shuffle(deck) 
    return deck

class Deck:
    def __init__(self, suits="♦♣♥♠", ranks=tuple("JQKA23456789")+("10",)):
        self.suits = suits
        self.ranks = ranks
        self.cards = self._gen_deck() 
    def __init__(dealer, suits="♦♣♥♠", ranks=tuple("JQKA23456789")+("10",)):
        dealer.suits = suits
        dealer.ranks = ranks
        dealer.cards = dealer._gen_deck() 

    def _gen_deck(self):
        return list(itertools.product(self.ranks, self.suits))
    def _gen_deck(dealer):
        return list(itertools.product(dealer.ranks, dealer.suits))
    
    def get_deck(self):
        return self.cards
    def get_deck(dealer):
        return dealer.cards
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
        return self.cards 
    
    def shuffle_deck(dealer):
        random.shuffle(dealer.cards)
        return dealer.cards
    
    # Deal methods for Player and Dealer
    def deal_self(self, n=1):
        dealt_self = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt_self
    
    def deal_dealer(dealer, n=1):
        dealt_dealer = dealer.cards[:n]
        dealer.cards = dealer.cards[n:]
        return dealt_dealer
    