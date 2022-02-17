import login_page 
import random
import time
import datetime

# login menu
print("WELCOME TO THE COLOR CARD GAME")
print("CAN 2 PLAYERS LOGIN TO THE SYSTEM?")

# asking both players to login
player1 = login_page.showLoginScreen(1)
login_page.loggedInPlayers.append(player1)

player2 = login_page.showLoginScreen(2)
login_page.loggedInPlayers.append(player2)

# sample login info for testing:
# username: admin, password: password
# username: rilmar, password: cat123


# title screen
def mainMenu():
        print("")
        choices = ["1", "2", "3"]
        choice = input("(1) PLAY A MATCH, (2) CHECK PAST GAME RECORDS, (3) HOW TO PLAY >> ")
        
        # execute different options
        if choice == "1":
                startGame()

        if choice == "2":
                print("")
                print("PAST GAMES:")

                # display info from past games
                past_games = open("past_games.txt", "r")

                for line in past_games.readlines():
                        print(line)

                past_games.close()
                print("")

                mainMenu()

        if choice == "3":
                print("RULES:")
                print("-TO PLAY, 2 PLAYERS MUST BE LOGGED INTO AN ACCOUNT")
                print("-EACH TURN, BOTH PLAYERS TAKE A CARD FROM THE DECK")
                print("-THE CARDS IN THE DECK HAVE DIFFERENT VALUES BASED ON COLOR AND NUMBER")
                print("-WHOEVER'S CARD IS WORTH MORE WINS THE TURN")
                print("-THIS IS REPEATED UNTIL THE DECK IS EMPTY")
                print("")

                mainMenu()

        if not choice in choices:
                print("ERROR: INVALID COMMAND!")
                print("")
                mainMenu()


# card game
def startGame():
        # define all card colors needed
        colors = ["red", "black", "yellow"]
        deck = []

        # create 4 colored decks that each contain 10 cards
        class Card:
            def __init__(self, color, number):
                self.color = color
                self.number = number

        
        for color in colors:
                for x in range(1, 10 + 1):
                        deck.append(Card(color, x))


        # randomizing deck:
        # making new deck to keep random cards
        randomizeDeck = []

        while len(deck) != 0:
                # pick a random card, add it to the "random" deck, then destroy it from the old deck
                getCard = random.choice(deck)
                randomizeDeck.append(getCard)
                deck.pop(deck.index(getCard))


        deck = randomizeDeck

        # defining rules
        print("")
        print("GAME RULES:")
        print("RED > BLACK > YELLOW >")
        
        # setup game variables
        turn = 0
        player1Points = 0
        player2Points = 0

        timeGameWasBegun = time.time()
        
        # game loop
        def startRound():
                # setup turn variables
                nonlocal turn, player1Points, player2Points
                
                player1Card = None
                player2Card = None
                
                turn += 1

                print("")
                print("TURN:", turn)
                
                # both players pick cards:
                # player 1 picks a random card from the deck
                print("PLAYER 1 CHOOSE FROM THE TOP OR THE BOTTOM OF THE DECK")
                input("(1) TOP, (2) BOTTOM >> ")
                
                player1Card = random.choice(deck)                
                deck.remove(player1Card)
                
                # announce the random card
                print("PLAYER 2 CHOOSE FROM THE TOP OR THE BOTTOM OF THE DECK")
                input("(1) TOP, (2) BOTTOM >> ")
                print("")
                
                
                # player 2 picks a random card from the deck
                player2Card = random.choice(deck)
                deck.remove(player2Card)
                
                # announce the random card
                print("PLAYER 1 HAS PICKED", player1Card.color, player1Card.number)
                print("PLAYER 2 HAS PICKED", player2Card.color, player2Card.number)
                print("")

                
                # evaluating cards
                # colors = red, black and yellow
                # color values: red beats black, black beats yellow, yellow beats red
                card1Color = player1Card.color
                card2Color = player2Card.color
                
                # compare color of each if they aren't the same, otherwise compare their numbers
                # better color or higher number wins
                if card1Color != card2Color: 
                        # comparing colours...
                        if card1Color == "yellow":
                                if card2Color == "black":
                                        print("PLAYER 2 WINS")
                                        player2Points += 1
                                else:
                                        print("PLAYER 1 WINS")
                                        player1Points += 1

                        if card1Color == "black":
                                if card2Color == "red":
                                        print("PLAYER 2 WINS")
                                        player2Points += 1
                                else:
                                        print("PLAYER 1 WINS")
                                        player1Points += 1

                        if card1Color == "red":
                                if card2Color == "yellow":
                                        print("PLAYER 2 WINS")
                                        player2Points += 1
                                else:
                                        print("PLAYER 1 WINS")
                                        player1Points += 1
                        print("BY COLOUR")
                else:
                        # comparing numbers...
                        if player1Card.number > player2Card.number:
                                print("PLAYER 1 WINS")
                                player1Points += 1
                        else:
                                print("PLAYER 2 WINS")
                                player2Points += 1
                        print("WITH A HIGHER NUMBER")


        # keep starting new turns until there are no more cards left
        while len(deck) > 0:
                startRound()


        # record how long the game lasted
        timeGameWasEnded = time.time()
        timeGameLasted = round(timeGameWasEnded - timeGameWasBegun)
        
        # format this into a readable string
        timeGameLasted = str(timeGameLasted) + " seconds"

        # decide the winner
        print("")
        print("THE RESULTS OF THE GAME ARE...")
        time.sleep(1)

        winner = None
        
        if player1Points == player2Points:
                # player points are equal
                print("THE GAME WAS A TIE")
                winner = "Tie"
        else:
                if player1Points > player2Points:
                        # player 1 has more points
                        print("PLAYER 1 WINS THE GAME")
                        winner = player1 + " was the winner"
                else:
                        # player 2 has more points
                        print("PLAYER 2 WINS THE GAME")
                        winner = player2 + " was the winner"


        # reading how many past games there are
        past_games = open("past_games.txt", "r")
        past_games_count = len(past_games.readlines())
        past_games.close()

        # format the current time as a readable string
        x = datetime.datetime.now()
        timeFormat =str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " " + "(" + str(x.hour) + ":" + str(x.minute) + ")"

        # writing game record to past games file
        past_games = open("past_games.txt","a")
        recordFormat = "Game #" + str(past_games_count + 1) + ", " + player1 + " vs. " + player2 + ", Result: " + winner + ", Time lasted : " + timeGameLasted + ", Date: " + timeFormat + " " + "\n"
        past_games.write(recordFormat)
        

# run program
print("WELCOME TO THE MAIN MENU. DO YOU WANT TO...")
mainMenu()
