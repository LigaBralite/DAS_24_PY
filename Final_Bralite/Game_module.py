from cards import Deck

scoreS = 0
scoreD = 0
deck = Deck()
deck.shuffle_deck()
BJ = 21

while scoreS < BJ and scoreD < BJ:
    card = deck.deal_self()[0] 
    print(card)
    rank, suit = card
    if rank in "JQK":
        scoreS += 10
    elif rank == "A":
        scoreS += 11
    else:
        scoreS += int(rank)
    print(f"Your current score: {scoreS}")
    if scoreS == BJ:
        print("Blackjack!")
        break
    elif scoreS > BJ:
        print("Bust!")
        break
    else:
        card = deck.deal_dealer()[0] 
        print(card)
        rank, suit = card
        if rank in "JQK":
            scoreD += 10
        elif rank == 'A':
            scoreD += 11
        else:
            scoreD += int(rank)
        print(f"Dealer's current score: {scoreD}")
        if scoreD == BJ:
            print("Blackjack!")
            break
        elif scoreD > BJ:
            print("Bust!")
            break
        choice = input("Do you want another card? (y/n)")
        if choice.lower() != "y":
            print("As You wish, let's see what I have 🃏")
            card = deck.deal_dealer()[0] 
            print(card)
            rank, suit = card
            if rank in "JQK":
                scoreD += 10
            elif rank == "A":
                scoreD += 11
            else:
                scoreD += int(rank)
            print(f"Dealer's current score: {scoreD}")
            if scoreD == BJ:
                print("Blackjack!")
                break
            elif scoreD > BJ:
                print("Dealer busted!")
                break
            elif scoreD > scoreS:
                print("Dealer wins!")
                break
            else:
                print("You win!")
            break

# REMARK: Game made assuming that after player stops dealer gets only one hand
# Initial version, planned TODO changes before final submission deadline:
            # 1. Optimize few blocks that are repeated in several blocks (score calculation for card; score comparison with BJ value)
            # 2. Validate input (Y/N) and throw error in case another value given
# Potential changes if more time
            # 1. Try another way of code (without While loop)
            # 2. Could be improved giving dealer option to play several hands
            # 3. Several player mode
