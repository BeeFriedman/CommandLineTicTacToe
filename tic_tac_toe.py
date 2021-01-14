class Players:
    n = ""
    w = 0
    lo = 0
    dr = 0
    p = 0.0

    def __init__(self, name, wins, losses, draw, percentage):
        self.n = name
        self.w = wins
        self.l0 = losses
        self.dr = draw
        self.p = percentage

    def __str__(self):
        s = "{:10s}{:<10d}{:<10d}{:<10d}{:<10.2f}"
        return s.format(self.n, self.w, self.lo,self.dr, self.p)

class TicTacToe:
    playerList = []
    boardList = []
    player1 = ""
    player2 = ""
    boardSize = 3
    symbol1 = "O"
    symbol2 = "X"
    currentPlayer = ""
    currentSymbol = ""
    sq = []

    def __init__(self, ):
        self.playerList = []
        self.boardsize = 3
        self.currentPlayer = self.player1
        self.currentSymbol = self.symbol2

    def menu(self):
        while True:
            print("Welcome to Tic-Tac-Toe! Please choose an option from the menu.")
            print("---------------------------")
            print("0) Quit")
            print("1) Start Game")
            print("2) Choose Players")
            print("3) Change Board Size")
            print("4) View Scoreboard")
            print("5) Reset Scoreboard")
            try:
                self.number = int(input())

                if self.number < 0 or self.number > 5:
                    print("Error! Out of range!\n")
                elif self.number == 0:
                    print("Hope to see you soon!")
                    return
                elif self.number == 1:
                    self.run()
                elif self.number == 2:
                    self.choosePlayer()
                elif self.number == 3:
                    self.changeBoard()
                elif self.number == 4:
                    self.scoreBoard()
                else:
                    self.reset()
            except:
                print("Error! Please enter an integer!\n")

    def choosePlayer(self):
        try:
            self.choice = int(input("Please choose one of the following:\n1) Choose an existing player\n2) Add a new player\n"))

            if self.choice < 1 or self.choice > 2:
                print("Error! Out of range!\n")
            elif self.choice == 1:
                l = len(self.playerList)

                for self.n in range(l - 1):
                    for self.num in range(l - 1):
                        if self.playerList[self.num + 1].p > self.playerList[self.num].p:
                            base = self.playerList[self.num]
                            self.playerList[self.num] = self.playerList[self.num + 1]
                            self.playerList[self.num + 1] = base
                for self.pl in self.playerList:
                    print(self.playerList.index(self.pl) + 1, self.pl)
                self.choice1 = int(input("Enter the number of the first player you want to choose.\n"))
                self.player1 = self.playerList[self.choice1 - 1].n
                self.choice2 = int(input("Enter the number of the second player you want to choose.\n"))
                if self.choice2 == self.choice1:
                    print("Error! You can't have the same player twice!\n")
                    return
                self.player2 = self.playerList[self.choice2 - 1].n
            else:
                self.addPlayer()
        except:
            print("Error! Please enter an integer!\n")

    def addPlayer(self):
        try:
            self.choice3 = str(input("Please enter the first player's name\n")).strip().capitalize()
            for self.pl in self.playerList:
                if self.pl.n == self.choice3:
                    print("Error! This name already exists!\n")
                    return
            self.playerItem = Players(self.choice3, 0, 0, 0, round(0.0, 2))
            self.playerList.append(self.playerItem)
            self.player1 = self.choice3
            self.choice4 = str(input("Please enter the second player's name\n")).strip().capitalize()
            for self.pl in self.playerList:
                if self.pl.n == self.choice4:
                    print("Error! This name already exists!\n")
                    return
            self.playerItem = Players(self.choice4, 0, 0, 0, 0.0)
            self.playerList.append(self.playerItem)
            self.player2 = self.choice4
        except:
            print("Error! Please enter a name!\n")

    def changeBoard(self):
        try:
            self.choice5 = int(input("Enter the board size (3 for a 3x3, 4 for a 4x4 etc.)\n"))

            if self.choice5 < 3 or self.choice5 > 6:
                print("Error! Out of range!\n")
            else:
                self.boardSize = self.choice5
                print("The board size was updated")
        except:
            print("Error! Please enter an integer!\n")

    def scoreBoard(self):
        s = "{:10s}{:10s}{:10s}{:10s}{:10s}"
        print(s.format("Name", "Wins", "Losses","Draws", "Percentage"))
        print("--------------------------------------------------")

        if len(self.playerList) > 10:
            l = 10
        else:
            l = len(self.playerList)

        for self.n in range(l - 1):
            for self.num in range(l - 1):
                if self.playerList[self.num + 1].p > self.playerList[self.num].p:
                    base = self.playerList[self.num]
                    self.playerList[self.num] = self.playerList[self.num + 1]
                    self.playerList[self.num + 1] = base

        for self.sc in self.playerList:
            print(self.sc)
        print()

    def updateScore(self, name, action):
        for pl in self.playerList:
            if name == pl.n:
                if action == "w":
                    pl.w += 1
                    total = (pl.w + pl.lo + pl.dr)
                    if pl.w != 0:
                        pl.p = round(100*pl.w/total, 2)
                elif action == "d":
                    pl.dr += 1
                    total = (pl.w + pl.lo + pl.dr)
                    if pl.w != 0:
                        pl.p = round(100*pl.w/total, 2)
                else:
                    pl.lo += 1
                    total = (pl.w + pl.lo + pl.dr)
                    if pl.w != 0:
                        pl.p = round(100*pl.w/total, 2)
                return

    def reset(self):
        for self.pl in self.playerList:
            self.pl.w = 0
            self.pl.lo = 0
            self.pl.dr = 0
            self.pl.p = round(0.0, 2)
        print("The board was reset!\n")

    def run(self):
        self.currentPlayer = self.player1
        self.boardList = []
        self.sq = [["       ", "|"],
                   ["   ", " ", "   ", "|"],
                   ["       ", "|"],
                   ["-------", "|"]]

        def board(self):
            if len(self.boardList) == 0:
                for x in range(1, self.boardSize * self.boardSize + 1):
                    self.boardList.append(x)

            x = 1
            for i in range(self.boardSize):
                if i != self.boardSize - 1:
                    for row in self.sq:
                        for j in range(self.boardSize):
                            if (row == self.sq[1]) and ((len(str(x)) == 1) or (len(str(self.boardList[x - 1])) == 1)):
                                self.sq[1][2] = "   "
                                self.sq[1][1] = self.boardList[x - 1]
                                x += 1
                                for slot in row:
                                    if j != self.boardSize - 1:
                                        print(slot, end="")
                                if j == self.boardSize - 1:
                                    for slot in row[:-1]:
                                        print(slot, end="")
                            elif (row == self.sq[1]) and ((len(str(x)) != 1) or (len(str(self.boardList[x - 1])) != 1)):
                                self.sq[1][2] = "  "
                                self.sq[1][1] = self.boardList[x - 1]
                                x += 1
                                for slot in row:
                                    if j != self.boardSize - 1:
                                        print(slot, end="")
                                if j == self.boardSize - 1:
                                    for slot in row[:-1]:
                                        print(slot, end="")

                            else:
                                for slot in row:
                                    if j != self.boardSize - 1:
                                        print(slot, end="")
                                if j == self.boardSize - 1:
                                    for slot in row[:-1]:
                                        print(slot, end="")
                        print()

                else:
                    for row in self.sq[:3]:
                        if row == self.sq[1]:
                            for j in range(self.boardSize):
                                if (len(str(x)) == 1) or (len(str(self.boardList[x - 1])) == 1):
                                    self.sq[1][2] = "   "
                                    self.sq[1][1] = self.boardList[x - 1]
                                    x += 1
                                    for slot in row:
                                        if j != self.boardSize - 1:
                                            print(slot, end="")
                                    if j == self.boardSize - 1:
                                        for slot in row[:-1]:
                                            print(slot, end="")
                                else:
                                    self.sq[1][2] = "  "
                                    self.sq[1][1] = self.boardList[x - 1]
                                    x += 1
                                    for slot in row:
                                        if j != self.boardSize - 1:
                                            print(slot, end="")
                                    if j == self.boardSize - 1:
                                        for slot in row[:-1]:
                                            print(slot, end="")
                            print()
                        else:
                            for j in range(self.boardSize):
                                for slot in row:
                                    if j != self.boardSize - 1:
                                        print(slot, end="")
                                if j == self.boardSize - 1:
                                    for slot in row[:-1]:
                                        print(slot, end="")
                            print()

        def changePlayer(self):
            if self.currentPlayer == self.player1:
                cPlayer = self.player2
            else:
                cPlayer = self.player1
            if self.currentSymbol == self.symbol1:
                cSymbol = self.symbol2
            else:
                cSymbol = self.symbol1
            return [cPlayer, cSymbol]

        def checkDraw(self):
            for listItem in self.boardList:
                if (listItem == "X") or (listItem == "O"):
                    continue
                else:
                    return False
            return True

        def checkWin(self):
            x = 0
            u = -1
            bl = []
            for _ in range(self.boardSize):
                bl.append([])
            for r in bl:
                u += 1
                for q in range(self.boardSize):
                    bl[u].append(self.boardList[x])
                    x += 1
            test = "y"
            for n in range(self.boardSize):
                for item in bl[n]:
                    if item == "X":
                        test = "y"
                    else:
                        test = "n"
                        break
                if test == "y":
                    return True
            for n in range(self.boardSize):
                for item in bl[n]:
                    if item == "O":
                        test = "y"
                    else:
                        test = "n"
                        break
                if test == "y":
                    return True

            for c in range(self.boardSize):
                for g in range(self.boardSize):
                    if bl[g][c] == "X":
                        test = "y"
                    else:
                        test = "n"
                        break
                if test == "y":
                    return True
            for c in range(self.boardSize):
                for g in range(self.boardSize):
                    if bl[g][c] == "O":
                        test = "y"
                    else:
                        test = "n"
                        break
                if test == "y":
                    return True

            for a in range(self.boardSize):
                if bl[a][a] == "X":
                    test = "y"
                else:
                    test = "n"
                    break
            if test == "y":
                return True
            for a in range(self.boardSize):
                if bl[a][a] == "O":
                    test = "y"
                else:
                    test = "n"
                    break
            if test == "y":
                return True

            i = self.boardSize - 1
            for a in range(self.boardSize):
                if bl[a][i] == "X":
                    test = "y"
                else:
                    test = "n"
                    break
                i -= 1
            if test == "y":
                return True
            i = self.boardSize - 1
            for a in range(self.boardSize):
                if bl[a][i] == "O":
                    test = "y"
                else:
                    test = "n"
                    break
                i -= 1
            if test == "y":
                return True

        while self.player1 == "" or self.player2 == "":
            print("You need to choose two players in order to play!\n")
            self.addPlayer()
        self.currentPlayer = self.player1

        print("Welcome to Tic-Tac-Toe! When you are promted, choose one of the avaliable boxs.")

        while True:
            print()
            board(self)
            print()
            try:
                choice = int(input(self.currentPlayer + " Choose a box: "))

                if choice > self.boardSize * self.boardSize or choice < 1:
                    print("sorry, your selection out of bounds!")
                elif (self.boardList[choice - 1] == self.symbol1) or (self.boardList[choice - 1] == self.symbol2):
                    print("Sorry, this box is not empty!")
                else:
                    playerChangeResult = changePlayer(self)
                    self.currentSymbol = playerChangeResult[1]
                    self.boardList[choice - 1] = self.currentSymbol
                    if checkDraw(self):
                        print()
                        board(self)
                        print()
                        print("The board is full, it's a draw!\n")
                        TicTacToe.updateScore(self, self.currentPlayer, "d")
                        playerChangeResult = changePlayer(self)
                        TicTacToe.updateScore(self, playerChangeResult[0], "d")
                        break
                    if checkWin(self):
                        print()
                        board(self)
                        print()
                        print(self.currentPlayer, "You Won!!\n")
                        TicTacToe.updateScore(self, self.currentPlayer, "w")
                        playerChangeResult = changePlayer(self)
                        TicTacToe.updateScore(self, playerChangeResult[0], "l")
                        break
                    self.currentPlayer = playerChangeResult[0]
            except:
                print("Error! Please enter an integer!\n")

ttt = TicTacToe()
ttt.menu()