import os

loggedInPlayers = []

# start-up login screen
def showLoginScreen(playerNumber):
        print("")
        print("PLAYER", playerNumber)
        print("PLEASE LOGIN OR CREATE AN ACCOUNT...")

        retrievedPlayer = None

        # keep trying to retrieve a player if an attempt is unsuccessful
        while retrievedPlayer == None:
             retrievedPlayer = selectOptions(playerNumber)

        return retrievedPlayer


def selectOptions(playerNumber):
        choices = ["1", "2"]
        choice = input("(1) Enter Login, (2) Make an Account >> ")
        
        if choice == "1":
                user = validateLogin()
                if user == "unsuccessful":
                    return None
                else:
                    return user
        if choice == "2":
            user = createAccount()
            return user

        if not choice in choices:
            print("ERRROR INVALID COMMAND")
            print("")

            return None


# choice 1: logging into an account
def validateLogin():
        enteredUser = input("ENTER USERNAME >> ")
        enteredPassword = input("ENTER PASSWORD >> ")

        if enteredUser in loggedInPlayers:
             print("ERROR: THE USER IS ALREADY SIGNED IN")
             return "unsuccessful"

               
        if checkUserPassword(enteredUser) == enteredPassword:
                print("LOGGED IN SUCCESSFULLY!")
                print("")
                return enteredUser
        else:
                print("ERROR: INVALID LOGIN")
                return "unsuccessful"


def checkUserPassword(username):
     user_records = open("user_records.txt", "r")

     # return user's password if the user exists, otherwise return nothing     
     for record in user_records.readlines():
          # loginInfo (username, password)
          loginInfo = record.split(" ")

          if loginInfo[0] == username:
               return loginInfo[1]

     return None


# choice 2: creating an account
def createAccount():
        username = input("ENTER USERNAME >> ")

        if usernameIsInUse(username) == False and textContainsLetters(username):
                password = input("ENTER PASSWORD >> ")

                if textContainsLetters(password) == False:
                     print("ERROR: PASSWORD NEEDS TO BE MADE UP OF LETTERS, NUMBERS OR SYMBOLS!!!")
                     return None
                
                # write login info to the server
                user_records = open("user_records.txt", "a")
                user_records.write(" " + "\n")
                format_logininfo = username + " " + password
                user_records.write(format_logininfo)
                user_records.close()

                print("CREATED ACCOUNT SUCCESSFULLY")

                return username
        else:
                print("ERROR: USERNAME IS IN USE OR INVALID!!!")
                print("")
                
                return None


def usernameIsInUse(username):
     user_records = open("user_records.txt", "r")
     
     for record in user_records.readlines():
          # loginInfo (username, password)
          loginInfo = record.split(" ")
          
          if loginInfo[0] == username:
               return True

     return False


def textContainsLetters(txt):
     if txt == "":
          return False

     # count number of unique letters in the txt
     lettersUsed = {" "}

     for x in txt:
          lettersUsed.add(x)


     # if it's made up of just spaces then return false
     if len(lettersUsed) == 1 and lettersUsed[0] == " ":
          return False

     return True
