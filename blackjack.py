import random

def setup():
    global playerAces, playerCards, drawnCards
    drawnCards = []
    dealerCards = []
    playerCards = []
    dealerAces = 0
    playerAces = 0
    input("Welcome to BlackJack!\nClick enter to begin. ")

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

def getPlayerValue():
    global playerAces, playerCards, drawnCards
    playerValue = sum(playerCards)
    if ((playerAces > 0) or (playerAces > 1)) and ((playerValue + 11 > 21)):
        playerValue = playerValue + 1
    elif playerAces > 0:
        playerValue = playerValue + 11
    return playerValue

def deal():
    drawPlayerCard()
    drawPlayerCard() 
    
setup()
deal()
print("Aces", playerAces)
print(getPlayerValue())
print(drawnCards)
