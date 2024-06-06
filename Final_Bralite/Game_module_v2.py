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
    
def result(score):
    if score == BJ:
        print("Blackjack!")
    elif score > BJ:
        print("Bust!")
    else:
        return None

while scoreS < BJ or scoreD < BJ:
    card = deck.deal_self()[0] 
    print(card)
    rank, suit = card
    scoreS += card_value(card)
    resultS = result(scoreS)
    if resultS:
        print(f"End of game! Your score {scoreS} - {resultS}")
        break
    else:
        print(f"Your current score: {scoreS}")   
    card = deck.deal_dealer()[0] 
    print(card)
    rank, suit = card
    scoreD += card_value(card)
    resultD = result(scoreD)
    if resultD:
        print(f"End of game! Dealer score {scoreD} - {resultD}")
        break
    else:
        print(f"Dealer's current score: {scoreD}")

    while True:
        choice = input("Do you want another card? (y/n)")
        if choice.lower() == "n":
            print("As You wish, let's see what I have 🃏")
            while scoreD < 17:
                card = deck.deal_dealer()[0] 
                print(card)
                scoreD += card_value(card)
                if scoreD >= BJ or scoreD > scoreS:
                    break
            
            if scoreD == BJ:
                print("Dealer gets Blackjack!")
            elif scoreD > BJ:
                print(f"Dealer busted! Score {scoreD}")
            elif scoreD > scoreS:
                print(f"Dealer wins! Score {scoreD}")
            else:
                print(f"You win! Score {scoreS}")
            break
        elif choice == "y":
            break
        else:
            print("Please enter 'y' for Yes or 'n' for No.")


# REMARK: Game made assuming that after player stops dealer gets only one hand and wins player with biggest score
# Initial version, planned TODO changes before final submission deadline:
            # 1. DONE Optimize few blocks that are repeated in several blocks (score calculation for card; score comparison with BJ value)
            # 2. DONE Validate input (Y/N) and throw error in case another value given
# Potential changes if more time
            # 1. Try another way of code (without While loop)
            # 2. DONE Could be improved giving dealer option to play several hands
            # 3. Several player mode
