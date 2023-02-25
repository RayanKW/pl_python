"""
    in this example we will create a card game in structural programing. THe game goes like this-
    we have 8 cards. one card is chosen at random and shown face up. the user is supposed to guess if the 
    card is either lower or higher of value than the shown card. if the value is higher and the user
    had said so then he is awrded 20points if the value is llower and the user had said higher then he
    is wrong and is deducted 15 points.
    in the second part we'll implement this example using the concepts of OOP.
    
    Data representation
    
    The programm needs to represent a deck of 52 cards which we'll buil into a list. the elements of the
    list will be in a dictionary, i.e key:value pairs. To represent each card will contain three key
    value pairs i.e rank, suit and value. rank is name of the card. eg rank would be Ace, 1, Jack, 3, King etc
    suit would be Clubs, spade etc and the value of course is 1-13 and it's an integer used to compare the cards
    e.g {'rank': 'Jack', 'suit': 'clubs', 'value': 11} this is one of the elements in the list.
    """
#implimentation
import random
#setting the card constants

suit_tupple = ('Spades', 'hearts', 'Clubs', 'Diamonds')
rank_tupple = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King' )
no_cards = 8

def getCard(deckListIn):
    thisCard = deckListIn.pop() #removes the top of the deck and returns
    return  thisCard

def shuffle(deckListIn):
    deckListOut = deckListIn.copy() #makes a copy of the start deck and stores it in the deckListOut
    random.shuffle(deckListOut)
    return deckListOut
print("Welcome To The Game!!!!!")
print('You May Choose Whether The Next Card To Be Show Will Be Higher Or LOwer Than The currently Shown')
print('If YoU Get It Right Then You\'re Awarded 20 Points Else If You\'re Wrong You\'re Deducted 15 POints! ! !')
print(' You Have 50 Points To Start With')
print()
startingDeckList = []
for suit in suit_tupple:
    for thisValue, rank in enumerate(rank_tupple):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue+1}
        startingDeckList.append(cardDict)
score =50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    #2
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting Card is:', currentCardRank + ' of ' + currentCardSuit)
    print()
    #3
    for cardNumber in range(0, no_cards):
        answer = input('Will The Next NUmber Be HIgher Or Lower Than The ' + currentCardRank + ' of ' + currentCardSuit+ '?enter H)igh or L)ower: ')
        #4
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next Card Is: ', nextCardRank + ' of ' + nextCardSuit)
        #5
        if answer == 'h' or answer == 'H':
            if nextCardValue > currentCardValue:
                print('You Got It Right, The Card is HIgher')
                score +=20
            else:
                print("You Got It Wrong, The Card Is Lower")
                score+=15
        elif answer == 'l' or answer == 'L':
            if nextCardValue < currentCardValue:
                print('You Got It Right, The Card is HIgher')
                score +=20
            else:
                print("You Got It Wrong, The Card Is Lower")
                score-=15
        else:
            print('Sorry Wrong Input')
        print('Your Score Is', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue =nextCardValue
    #6 
        goAgain = input('To Play Again, Press Enter, or "Q" to Quit: ')
        if goAgain =="q":
            break
        print("Bye Bye")
