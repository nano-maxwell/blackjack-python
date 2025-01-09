import random

def setup():
    global playerAces, playerCards, dealerAces, dealerCards, drawnCards
    drawnCards = []
    dealerCards = []
    playerCards = []
    dealerAces = 0
    playerAces = 0
    input("Welcome to BlackJack!\nClick enter to begin. ")
    deal()
    deal()
    print("Your total:", getPlayerValue())
    print("Dealer's total:", getDealerValue())
    checkCondition()
    turn()

def drawPlayerCard():
    global playerAces, playerCards, drawnCards
    drawn = random.randint(1, 12)
    if drawnCards.count(drawn) == 3:
        return drawPlayerCard()
    drawnCards.append(drawn)
    if drawn > 10:
        drawn = 10
    if drawn == 1:
        playerAces = playerAces + 1
    else:
        playerCards.append(drawn)
    return drawn

def drawDealerCard():
    global dealerAces, dealerCards, drawnCards
    drawn = random.randint(1, 12)
    if drawnCards.count(drawn) == 3:
        return drawDealerCard()
    drawnCards.append(drawn)
    if drawn > 10:
        drawn = 10
    if drawn == 1:
        dealerAces = dealerAces + 1
    else:
        dealerCards.append(drawn)
    return drawn

def getPlayerValue():
    global playerAces, playerCards, drawnCards
    playerValue = sum(playerCards)
    for _ in range(playerAces):
        if (playerValue + 11 > 21):
            playerValue = playerValue + 1
        else:
            playerValue = playerValue + 11
    return playerValue

def getDealerValue():
    global dealerAces, dealerCards, drawnCards
    dealerValue = sum(dealerCards)
    for _ in range(dealerAces):
        if (dealerValue + 11 > 21):
            dealerValue = dealerValue + 1
        else:
            dealerValue = dealerValue + 11
    return dealerValue

def deal():
    drawPlayerCard()
    drawDealerCard()

def turn():
    global playerAces, playerCards, dealerAces, dealerCards, drawnCards
    move = input("Would you like to hit or stand? ")
    if move.lower() == "hit":
        drawPlayerCard()
        print("\nYour total:", getPlayerValue())
        print("Dealer's total:", getDealerValue())
        checkCondition()
    elif move.lower() == "stand":
        drawDealerCard()
        print("\nYour total:", getPlayerValue())
        print("Dealer's total:", getDealerValue())
        checkCondition()
    else:
        return turn()

def checkCondition():
    global playerAces, playerCards, dealerAces, dealerCards, drawnCards
    if (getPlayerValue() == 21 and (getDealerValue() != 21)):
        print("You win!")
        playAgain()
    elif (getDealerValue() == 21):
        print("You lose.")
        playAgain()
    elif (getDealerValue() > 21):
        print("You win!")
        playAgain()
    elif (getPlayerValue() > 21):
        print("You lose.")
        playAgain()
    else:
        return turn()

def playAgain():
    again = input ("Do you want to play again? Yes or no. ")
    if again.lower() == "yes":
        print("\n")
        return setup()
    elif again.lower() == "no":
        exit()
    else:
        return playAgain()

setup()
