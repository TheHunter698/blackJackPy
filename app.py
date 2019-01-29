
def startMultiPlayer():
    print 'your mom gay'

def startSinglePlayer():
    players = raw_input('How many players? \n')
    userName = raw_input('What is your name? \n')
    playerNames = []
    scores = []
    deck = []
    wins = []
   

    for x in range(0, len(players)):
        playerNames.append('Player' + str(x))
        scores.append(0);
    
    playerNames[0] = 'House'
    playerNames[1] = userName
    currentPlayer = playerNames[0]

    for x in range(0,14):
        if x == 0:
            deck.append('A')
        elif x == 11:
            deck.append('J')
        elif x == 12:
            deck.append('Q')
        elif x == 13:
            deck.append('K')
        else:
            deck.append(x)

    startGame() #Starts game in single player
#Stop Function here


def startGame():
    if currentPlayer != userName:
        npcTurn()
    else:
        playerTurn()
        
            
def npcTurn():
    index = playerNames.index(currentPlayer)

    card = drawCard() #We get a card
    print currentPlayer + 'got a ' + card #Show the card
    scores[index] += card #Assign it to the right player (the current one)

    if scores[index] == 21: #We pass round if its 21
        print currentPlayer + 'wins with a blackJack!'
        isWin()
        passRound()
    elif scores[index] > 21: #We pass turn if its more than 21 and its busted
        print currentPlayer + 'got busted!'
        passTurn()
    elif scores[index] <= 16: #We draw again if its less than 16
        return drawCard()
    else: #We pass turn if its more than 16 (17 or more)
        passTurn()

def drawCard(): #Draw card

    card = deck[math.floor(math.radint(1,len(deck)))] #Random card
    if card == 'J':
        card = 1;
    elif card == 'Q':
        card = 2;
    elif card == 'K':
        card = 3;
    else:
        card = card;

    return int(card); #Return value of the card, in integer 

def passTurn(): #Pass the turn to the next player
    if currentPlayer == playerNames[len(playerNames)]: #If last player, we check who wins and passRound
       checkWin() #We check who wins
       passRound()
    else:   
        currentPlayer = playerNames[playerNames.index(currentPlayer) + 1] #Next player if its not the last 1

def passRound(): #We pass round, reset scores, THIS DOES NOT CHECK WHO WINS
    for number in range(1, len(scores)):
        scores[number] = 0

    currentPlayer = playerNames[0]

def isWin(): #Method to give a win directly to a player
    wins[wins.index(currentPlayer)] += 1
    
def checkWin(): 
    scoresArr = scores
    highest = 0

    for number in scoresArr: #We take the highest number
        holder = number
        if number > higher:
            higher = number
    
    wins[socres.index(highest)] += 1 #Add a win to a player that has the index of the highest score


print 'Wellcome to BlackJack Python, please choose a modality, single player or multiplayer, by writing that.'

mode = raw_input('Write multiplayer or single player ')

if mode == 'multiplayer' or mode == 'Multiplayer':
     startMultiPlayer();
else:
    startSinglePlayer();

