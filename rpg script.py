running_battle = []

class side():
    def __init__(self, players):
        self.characters = []
        
        if len(players) == 1:
            team = players.Team
            self.characters.append(team[0], team[1])

        if len(players) > 1:
            for p in players:
                startingChar = p.Team[1]
                self.characters.append(startingChar)


# if there is one player on a side, he controls both characters
# if there are two, control over each character is split up
# if there is three, the same also applies
def returnControllers(players):
    if len(players) == 1:
        return [players[0], players[0]]

    if len(players) == 2:
        return [players[0], players[1]]

    if len(players) == 3:
        return [players[0], players[1], players[2]]


class battle():
    def __init__(self, sideAPlayers, sideBPlayers):
        self.turn = 0
        self.sideAPlayers = returnControllers(sideAPlayers)
        self.sideBPlayers = returnControllers(sideBPlayers)
        self.sides = []

    def setupBattle(self):
        # create sides
        createSideA = side(self.sideAPlayers)
        self.sides.append(createSideA)

        createSideB = side(self.sideBPlayers)
        self.sides.append(createSideB)

        # start battle
        self.continueTurn(self)


    def continueTurn(self):
        self.turn += 1
