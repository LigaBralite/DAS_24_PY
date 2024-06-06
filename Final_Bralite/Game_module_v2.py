from cards import Deck

scoreS = 0
scoreD = 0
deck = Deck()
deck.shuffle_deck()
BJ = 21

def card_value(card):
    if rank in "JQK":
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)

while scoreS < BJ and scoreD < BJ:
    card = deck.deal_self()[0] 
    print(card)
    rank, suit = card
    scoreS += card_value(card)
    print(f"Your current score: {scoreS}")
    if scoreS == BJ:
        print("Blackjack!")
        break
    elif scoreS > BJ:
        print(f"You are bust! Score {scoreS}")
        break
    else:
        card = deck.deal_dealer()[0] 
        print(card)
        rank, suit = card
        scoreD += card_value(card)
        print(f"Dealer's current score: {scoreD}")
        if scoreD == BJ:
            print("Blackjack!")
            break
        elif scoreD > BJ:
            print(f"Dealer bust! Score {scoreD}")
            break
        
        choice = input("Do you want another card? (y/n)")
        while choice.lower() not in ["y", "n"]:
            print("Please enter a valid value - 'Y' for Yes and 'N' for No")
            choice = input("Do you want another card? (y/n)")

        if choice.lower() == "n":
            print("As you wish, let's see what I have 🃏")
            card = deck.deal_dealer()[0] 
            print(card)
            rank, suit = card
            scoreD += card_value(card)
            print(f"Dealer's current score: {scoreD}")
            if scoreD == BJ:
                print("Blackjack!")
                break
            elif scoreD > BJ:
                print(f"Dealer busted! Score {scoreD}")
                break 
            elif scoreD > scoreS:
                print(f"Dealer wins with score {scoreD} VS Your score {scoreS}")
                break
            else:
                print(f"You win! Score {scoreS}")
            break

# REMARK: Game made assuming that after player stops dealer gets only one hand and wins player with biggest score
# Initial version, planned TODO changes before final submission deadline:
            # 1. DONE Optimize few blocks that are repeated in several blocks (score calculation for card)
            # 2. DONE Validate input (Y/N) and throw error in case another value given
# Potential changes if more time
            # 1. Try another way of code (without While loop)
            # 2. Could be improved giving dealer option to play several hands
            # 3. Several player mode
