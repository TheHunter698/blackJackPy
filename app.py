
class Game:
    players = []
    turn = 0
    history = []
    deck = []

    def mode(self): #Sets the mode of the game, with that it generates decks or deck and customizes player names
        mode = input('Single player or Multiplayer \n')
    
        if mode == 'Multiplayer':
            self.multiPlayer()
        else:
            self.singlePlayer()

    def start (self):
        if self.players[self.turn] == self.userName:
            self.playerTurn()
        elif self.turn > self.players:
            self.passRound()
        elif self.exit == true:
            return 'Exited the game'
        else:
            self.npcTurn()

        return self.start()
       
    def singlePlayer(self): #Here you should append objects but you are appending strings, ask how to do this cuz dynamic variables are not ez
        players = input('How many players? \n')
        userName = input('What is your name?')

        for x in range(0,int(players)):
           if(x == 0):
               self.players.append(Player())
               self.players[x].name = 'House'
           elif(x == 1):
               self.players.append(RealPlayer())
               self.players[x].name = userName
           else:
               self.players.append(Player())
               self.players[x].name = 'Player' + str(x)
        
        self.currentPlayer = players[0] ##Set initial player

        if int(players)/3 > 1:
            deckNumber = math.floor(int(players)/3) ##If the number of players is more than 3 we take how many decks wee need with math floor 
            ##And append them
            for x in range(0, deckNumber):
                for y in range(0,4):
                    for z in range(0,14):
                        if z == 0:
                            self.deck.append('A')
                        elif z == 11:
                            self.deck.append('J')
                        elif z == 12:
                            self.deck.append('Q')
                        elif z == 13:
                            self.deck.append('K')
                        else:
                            self.deck.append(str(z))

        ##If there is less than 3 players we only append 1 deck
        else:
            for y in range(0,4): #4 types of card, 13 cards per each type
                for y in range(0,14):
                    if y == 0:
                        self.deck.append('A')
                    elif y == 11:
                        self.deck.append('J')
                    elif y == 12:
                        self.deck.append('Q')
                    elif y == 13:
                        self.deck.append('K')
                    else:
                        self.deck.append(str(y))

    ##The game will be reset, along with scores and the initial player

    def multiPlayer(self):
        return 'Under construction :3'
    
    def runStatistics(self):
        history = self.history
        

    def playerTurn(self): ##Turn for users
        whatNext = input('This is your turn, write Hit me to take a card.\n Write pass to give the turn to the next player.\n Write save game to save your game.')
        current = self.players[self.turn]

        if current.score > 21: #Score goes first
            return 'You are busted with a score of ' + current.score + '!'
        elif current.score == 21:
            current = self.players[self.turn]
            current.wins += 1
            self.passRound() #Passes round if 21
        elif whatNext.lower() == 'hit me':
            card = current.throwCard()
            print 'You got a ' + str(card)
            print 'Your total score is' + Player.score
            return self.playerTurn() #Ez recursion
         elif whatNext.lower() == 'save game':
            self.saveGame()
            return 'Game saved :D'
        elif whatNext.lower() == 'exit':
            self.exit()
        elif whatNext.lower() == 'pass':
            current.passTurn()
            return 'You passed turn!'
        else:
    
        maxScore = max(wins)
        maxIndex = wins.index(maxScore)
        winner = self.players[maxIndex]
        return winner.name

    def npcTurn(self):
        index = self.turn

        card = drawCard() #We get a card
        print currentPlayer + 'got a ' + card #Show the card
        scores[index] += card #Assign it to the right player (the current one)

        if scores[index] == 21: #We pass round if its 21
            print currentPlayer + 'wins with a blackJack!'
            isWin()
            self.passRound()
        elif scores[index] > 21: #We pass turn if its more than 21 and its busted
            print currentPlayer + 'got busted!'
            passTurn()
        elif scores[index] <= 16: #We draw again if its less than 16
            return drawCard()
        else: #We pass turn if its more than 16 (17 or more)
            passTurn()

    def exit():
        return 'Exited the game succesfully'
    

    def passRound(): #We pass round, reset scores, THIS DOES NOT CHECK WHO WINS
    for number in range(1, len(scores)):
        scores[number] = 0

    currentPlayer = playerNames[0]

class Player:
    score = 0
    name = ''
    wins = 0

    def throwCard(self):
        deck = Game.deck
        card = deck[math.floor(math.random()*len(deck))]
        if card == 'A':
            if self.score <= 10:
                self.score += 11
            else:
                self.score += 1
        elif card == 'J':
            self.score += 1
        elif card == 'Q':
            self.score += 2
        elif card == 'K':
            self.score += 3
        else:
            self.score += int(card)
        
        Game.history.append(card)
        return int(card)
        
    def passTurn(self):
        Game.turn += 1

            
    def isWin(): #Method to give a win directly to a player
        wins[wins.index(currentPlayer)] += 1 

    
class RealPlayer(Player):
    name = Game.userName     

    def throwCard(self):
        deck = Game.deck
        card = deck[math.floor(math.random()*len(deck))]
        if card == 'A':
            value = askAs()
            self.score += int(value)
            card = value
        elif card == 'J':
            card = 1
            self.score += 1
        elif card == 'Q':
            self.score += 2
            card = 2
        elif card == 'K':
            self.score += 3
            card = 3
        else:
            self.score += int(card)
        
        return card
    
    def passTurn(self):
        Game.turn += 1

    def split(self): ##Under construction, please hold still, it'll be done in a jiffy


def askAs():
    value = input('Yo got an Ace, choose if you want a 11 or a 1')
    return value


Game.mode() #Sets game mode
Game.start()

