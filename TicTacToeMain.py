# Tic-Tac-Toe - FINAL Version W BOTH 1v1 AND CPU MODES
#importing random function for its usage below in the game
import random

# Variables used in the game
X = "X"
O = "O"
nothing = " "
tie = "TIE"
totalsquares = 9

def Tutorial():
        #tutorial for the game which describes what they are playing and how to play it
    print("\n\nWelcome to Tic-Tac-Toe. I will now be letting you know that this is not a GUI based program and you will have to type in numbers to fill in the squares as follows:\n\n\n0-Top-Left, 1-Top-Middle, 2-Top-Right\n\n3-Middle-Left, 4-Middle-Middle, 5-Middle-Right\n\n6-Bottom-Left, 7-Bottom-Middle, 8-Bottom-right")
    #displayingfirsttime would call the function which would show a sample or like the 9 squares with the corresponding numbers within them
    displayingfirstime()


def asknameCPU():
    #For the Computer-Player Mode
    #Asks for player name and it is used only in Computer version as if it was the same for 2player, the prompt would get all messed up
    playername = input("\n\nEnter your name Human ")
    return playername

def asknamePlayer1():
    #Player 1 name is asked for 2 Player mode
    playername1 = input("\nEnter your name Player 1 ")
    return playername1

def asknamePlayer2():
    #Player 2 name is asked for 2 Player mode
    playername2= input("\nEnter your name Player 2 ")
    return playername2


def movemaker(question, low, high):
    #Ask for a number within a range. This kind of asking a question to get a number is done multiple times, so it is more efficient to make a function which takes the question and range as an input to give back a response letting us know if it is in the range
    #function is  made for efficiency
    response = None
    while response not in range (low, high):
        response = int(input(question))
    return response


def randomCPU():
    #Determine if player or computer goes first using the random function.
    #usage of random function
    choice = random.choice([0,1])
    if choice == 0:

        print("\n"+p+" Goes First")
        player = X
        computer = O
    else:
        print("\nComputer Goes First")
        computer = X
        player = O
    return computer, player


def randomfriend():
    #Determine if player1 or player2 goes first.
    #usage of random function
    choice = random.choice([0,1])

    if choice == 0:
        print("\n"+ p1+" Goes First")
        player1 = X
        player2 = O
    else:
        print("\n"+ p2+" Goes First")
        player2 = X
        player1 = O
    return player2, player1

def newboard():
    #Creating new game board with 9 squares in a function so that when it gets called from a different function, the board that is blank is sent.
    board = []
    for square in range(totalsquares):
        board.append(nothing)
    return board

def displayingfirstime():
    #Displaying board on screen for only one time as in the beginning, it ties with the tutorial to make show the players the corresponding values that they have to enter to show it on the board. OR a simplified version of the tutorial
    print("\n\t", 0, "|", 1, "|", 2)
    print("\t", "---------")
    print("\t", 3, "|", 4, "|", 5)
    print("\t", "---------")
    print("\t", 6, "|", 7, "|", 8, "\n")

def displaying(board):
    #Displaying board on screen.
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def moves(board):
    #Create list of moves that would be used in the main functions of the game that allows the players to actually move.
    moves = []
    for square in range(totalsquares):
        if board[square] == nothing:
            moves.append(square)
    return moves


def winning(board):
    #Determine the game winner by using the logic of the game where if one gets 3 in a row horizontally, vertically or slanted, they win.
    wincombinations = ((0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6))

    for row in wincombinations:
        if board[row[0]] == board[row[1]] == board[row[2]] != nothing:
            winner = board[row[0]]
            return winner

    if nothing not in board:
        return tie

    return None




def player_move(board, player):
    #To Get player's move in the CPU version of the game with the prompt.
    #used to check if the move the player has selected can be made and that it is in the left over squares
    squarescompleted = moves(board)
    move = None
    while move not in squarescompleted:
        move = movemaker("Where will "+p+ " move? (0 - 8):", 0, totalsquares)
        if move not in squarescompleted:
            print("\nThis square's already occupied. Choose another square, " + p +".\n")
    #returning move to the main function where based on turn, the moves are given to the respective players.
    return move

def computer_move(board, computer, player):
    #AVANISH's Tic Tac Toe tactics
    # the best positions to have, in order
    bestsquares = (4, 0, 2, 6, 3, 8, 1, 5, 7)

    print("Computer chooses to move to", end=" ")
    #used when computer is about to win
    # To take the winning move by the computer where it first checks the move, checks if it is the computers move, then checks if it is in winning combination, then it returns it accordingly.
    for move in moves(board):
        board[move] = computer
        if winning(board) == computer:
            print(move)
            return move
        board[move] = nothing
    #used when player is about to win
    # To block the measly opponent by checking if the player can win in the next move by doing the same as winnning in the previous function with only changing the check of computer's move to player's move.
    for move in moves(board):
        board[move] = player
        if winning(board) == player:
            print(move)
            return move
        board[move] = nothing
    #this function is used when no one has clear cut opportunity to win
    # picking the best open square by using the list created in the beginning of the function, best squares. it is the middle, top left, top right, bottom left, bottom right, top middle, left middle, right middle and bottom middle. It does not really matter affter a point as only really the first two or three moves really matter, and as far as comp doesnt make move to the middles, it will definetely draw
    #usage of for loop where it runs through the whole of the best squares list and return best possible move
    for move in bestsquares:
        if move in moves(board):
            print(move)
            return move


def player1_move(board, player1):
  #To Get player's move in the CPU version of the game with the prompt.
  #used to check if the move the player has selected can be made and that it is in the left over squares

    squarescompleted = moves(board)
    move = None
    while move not in squarescompleted:
        move = movemaker("Where will "+p1+ " move? (0 - 8):", 0, totalsquares)
        if move not in squarescompleted:
            print("\nThis square's already occupied. Choose another square, " + p1 +".\n")
    #returning move to the main function where based on turn, the moves are given to the respective players.
    return move

def player2_move(board, player2):
 #To Get player's move in the CPU version of the game with the prompt.
#used to check if the move the player has selected can be made and that it is in the left over squares

    squarescompleted = moves(board)
    move = None
    while move not in squarescompleted:
        move = movemaker("Where will "+p2+ " move? (0 - 8):", 0, totalsquares)
        if move not in squarescompleted:
            print("\nThat square's already occupied. Choose another square, " + p2 +".\n")
    #returning move to the main function where based on turn, the moves are given to the respective players.
    return move




def nexturn(turn):
    #Switching of turns function that is returned to main accordingly
    if turn == X:
        return O
    else:
        return X


def congratwinnerCPU(winner, computer, player):
    #Congratulating the winner accordingly.

    if winner == computer:
        print("You lost, but it was expected. Nice try? Not ")

    elif winner == player:
        print("You beat the unbeatable, YOU ARE THE CHAMPIONNN, bUt wAiT a MiNutE, YoU wIlL nEvEr SeE thIs cAuSe I Am UnBeAtAbLe.oofieoffiegoofiedhatchigondo9-5job")

    elif winner == tie:
        print("It is a tie")

def congratwinnerfriend(winner, player2, player1):
    #Congratulating the winner accordingly.

    if winner == player2:
        print(p2 +" WON!")

    elif winner == player1:
        print(p1+" WON!")

    elif winner == tie:
        print("It is a tie and no one has won")


def mainfor1v1():
    #main function just for the 2 player game. ADD ON TO ORIGINAL GAME
    Tutorial()
    global p1
    global p2
    p1 = asknamePlayer1()
    p2 = asknamePlayer2()
    player2, player1 = randomfriend()
    turn = X
    board = newboard()
    displaying(board)

    while not winning(board):
        if turn == player1:
            move = player1_move(board, player1)
            board[move] = player1
        else:
            move = player2_move(board, player2)
            board[move] = player2
        displaying(board)
        turn = nexturn(turn)

    winner = winning(board)
    congratwinnerfriend(winner, player2, player1)


def mainforCPU():
    #main function just for the computer game. DONE FIRST
    Tutorial()
    global p
    p = asknameCPU()
    computer, player = randomCPU()
    turn = X
    board = newboard()
    displaying(board)

    while not winning(board):
        if turn == player:
            move = player_move(board, player)
            board[move] = player
        else:
            move = computer_move(board, computer, player)
            board[move] = computer
        displaying(board)
        turn = nexturn(turn)

    winner = winning(board)
    congratwinnerCPU(winner, computer, player)


# start the program
def main():
    #main program where user lets us know what kind of challenge he or she wants
    i = input("If you want to play against a friend, press 1 for 2 Player Mode, If you want an actual challenge, press 2 for Player-Computer Mode ")
    if i == "1":
        mainfor1v1()
    if i == "2":
        mainforCPU()
    else:
        main()
    breaking = input("\n\nPress the enter key to quit or n key to start another game.")
    if breaking == "n":
        main()

main()
