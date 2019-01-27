print 'Wellcome to BlackJack Python, please choose a modality, single player or multiplayer, by writing that.'

mode = raw_input('Write multiplayer or single player')

if mode == 'multiplayer' or mode == 'Multiplayer':
    startSinglePlayer();
else:
    startMultiPlayer();


def startSinglePlayer():
    players = raw_input('How many players?')
    userName = raw_input('What is your name')
    playerNames = []
    scores = []
    deck = []
    currentPlayer = playerNames[0]


    for x in range(0, int(players)):
        playerNames.append('Player' + x)
        scores.append(0)
    
    playerNames[0] = 'House'
    playerNames[1] = userName

    for x in range(0,14):
        if x == 0:
            deck.append('A')
        elif x === 11:
            deck.append('J')
        elif x === 12:
            deck.append('Q')
        elif x === 13:
            deck.append('K')
        else:
            deck.append(x)

    

def drawCard(deck):

    return card;
def skipTurn(currentPlayer):
    return something;
def askAs(currentPlayer):
    return algo;


