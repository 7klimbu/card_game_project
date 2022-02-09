import login_page 
import random
import time
import datetime

# login menu
print("WELCOME TO THE COLOR CARD GAME")
print("CAN 2 PLAYERS LOGIN TO THE SYSTEM?")

# sample login info:
# username: admin, password: password
# username: rilmar, password: cat123

player1 = login_page.showLoginScreen(1)
login_page.loggedInPlayers.append(player1)

player2 = login_page.showLoginScreen(2)
login_page.loggedInPlayers.append(player2)


# title screen
def mainMenu():
        print("")
        choices = ["1", "2", "3"]
        choice = input("(1) PLAY A MATCH, (2) CHECK PAST GAME RECORDS, (3) HOW TO PLAY >> ")

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


        # randomizing deck
        randomizeDeck = []

        while len(deck) != 0:
                getCard = random.choice(deck)
                randomizeDeck.append(getCard)
                deck.pop(deck.index(getCard))


        deck = randomizeDeck

        # defining rules
        print("")
        print("GAME RULES:")
        print("RED > BLACK > YELLOW >")

        turn = 0
        player1Points = 0
        player2Points = 0

        timeGameWasBegun = time.time()

        def startRound():
                nonlocal turn, player1Points, player2Points
                
                player1Card = None
                player2Card = None
                
                turn += 1

                print("")
                print("TURN:", turn)
                
                # each player picks a random card
                print("PLAYER 1 CHOOSE FROM THE TOP OR THE BOTTOM OF THE DECK")
                input("(1) TOP, (2) BOTTOM >> ")
                
                player1Card = random.choice(deck)                
                deck.remove(player1Card)

                print("PLAYER 2 CHOOSE FROM THE TOP OR THE BOTTOM OF THE DECK")
                input("(1) TOP, (2) BOTTOM >> ")
                print("")
                
                player2Card = random.choice(deck)
                deck.remove(player2Card)

                print("PLAYER 1 HAS PICKED", player1Card.color, player1Card.number)
                print("PLAYER 2 HAS PICKED", player2Card.color, player2Card.number)
                print("")

                # evaluating cards
                # red beats black, black beats yellow, yellow beats red
                colours = ["red", "black", "yellow"]
                card1Colour = player1Card.color
                card2Colour = player2Card.color
        
                if card1Colour != card2Colour: 
                        # compare colours if they aren't the same
                        if card1Colour == "yellow":
                                if card2Colour == "black":
                                        print("PLAYER 2 WINS")
                                        player2Points += 1
                                else:
                                        print("PLAYER 1 WINS")
                                        player1Points += 1

                        if card1Colour == "black":
                                if card2Colour == "red":
                                        print("PLAYER 2 WINS")
                                        player2Points += 1
                                else:
                                        print("PLAYER 1 WINS")
                                        player1Points += 1

                        if card1Colour == "red":
                                if card2Colour == "yellow":
                                        print("PLAYER 2 WINS")
                                        player2Points += 1
                                else:
                                        print("PLAYER 1 WINS")
                                        player1Points += 1
                        print("BY COLOUR")
                else:
                        # compare numbers (bigger one wins)
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
        timeGameLasted = str(timeGameLasted) + " seconds"

        # decide the winner
        print("")
        print("THE RESULTS OF THE GAME ARE...")
        time.sleep(1)

        winner = None

        if player1Points == player2Points:
                print("THE GAME WAS A TIE")
                winner = "Tie"
        else:
                if player1Points > player2Points:
                        print("PLAYER 1 WINS THE GAME")
                        winner = player1 + " was the winner"
                else:
                        print("PLAYER 2 WINS THE GAME")
                        winner = player2 + " was the winner"


        # reading how many past games there are
        past_games = open("past_games.txt", "r")
        past_games_count = len(past_games.readlines())
        past_games.close()

        # format the current time as a string
        x = datetime.datetime.now()
        timeFormat =str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " " + "(" + str(x.hour) + ":" + str(x.minute) + ")"

        # writing game record to past games file
        past_games = open("past_games.txt","a")
        recordFormat = "Game #" + str(past_games_count + 1) + ", " + player1 + " vs. " + player2 + ", Result: " + winner + ", Time lasted : " + timeGameLasted + ", Date: " + timeFormat + " " + "\n"
        past_games.write(recordFormat)
        

# run program
print("WELCOME TO THE MAIN MENU. DO YOU WANT TO...")
mainMenu()
