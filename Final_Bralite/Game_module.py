from cards import Deck

scoreS = 0
scoreD = 0
deck = Deck()
deck.shuffle_deck()
BJ = 21

while scoreS < BJ or scoreD < BJ:
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

# I know code can be optimised, this is first version using While loop
# Game made assuming that after player stops dealer gets only one hand
# Could be improved giving dealer option to play several hands