#TICTACTOE1v1 FINAL VERSION
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
    displayingforfirstime()

def asknamePlayer1():
    #Player 1 name is asked in this function for 2 Player mode
    playername = input("\nEnter your name, Player 1: ")
    return playername

def asknamePlayer2():
    #Player 2 name is asked in this function for 2 Player mode
    playername= input("\nEnter your name, Player 2: ")
    return playername


def movemaker(question, low, high):
    #Ask for a number within a range. This kind of asking a question to get a number is done multiple times, so it is more efficient to make a function which takes the question and range as an input to give back a response letting us know if it is in the range
    #function is  made for efficiency
    response = None
    while response not in range (low, high):
        response = int(input(question))
    return response

def rand_game_starter():
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


def create_newboard():
    #Creating new game board with 9 squares in a function so that when it gets called from a different function, the board that is blank is sent.
    board = []
    for square in range(totalsquares):
        board.append(nothing)
    return board


def displayingforfirstime():
    #Displaying board on screen for only one time as in the beginning, it ties with the tutorial to make show the players the corresponding values that they have to enter to show it on the board. OR a simplified version of the tutorial
    print("\n\t", 0, "|", 1, "|", 2)
    print("\t", "_________")
    print("\t", 3, "|", 4, "|", 5)
    print("\t", "_________")
    print("\t", 6, "|", 7, "|", 8, "\n")

def displaying(board):
    #Displaying board on screen.

    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "_________")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "_________")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")



def moves(board):
    #Creates a list of moves that would be used in the main functions of the game that allows the players to actually move.
    moves = []
    for square in range(totalsquares):
        if board[square] == nothing:
            moves.append(square)
    return moves



def winning(board):
    #Determine the game winner by using the logic of the game where if one gets 3 in a row horizontally, vertically or slanted, they win. returns a winner to main function if either of the two players won
    wincombinations = ((0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6))

    for row in wincombinations:
        if board[row[0]] == board[row[1]] == board[row[2]] != nothing:
            winner = board[row[0]]
            return winner

    if nothing not in board:
        return tie

    return None



def player1_move(board, player1):
#To Get player 1's move from 0 to 9
#also used to check if the move the player has selected can be made and that it is in the left over squares where there does not exist an x or an o

    squarescompleted = moves(board)
    move = None
    while move not in squarescompleted:
        move = movemaker("Where will "+p1+ " move? (0 - 8):", 0, totalsquares)
        if move not in squarescompleted:
            print("\nThis square's already occupied. Choose another square, " + p1 +".\n")
    #returning move to the main function where based on turn, the moves are given to the respective players.
    return move


def player2_move(board, player2):
#To Get player 2's move from 0 to 9
#also used to check if the move the player has selected can be made and that it is in the left over squares where there does not exist an x or an o

    squarescompleted = moves(board)
    move = None
    while move not in squarescompleted:
        move = movemaker("Where will "+p2+ " move? (0 - 8):", 0, totalsquares)
        if move not in squarescompleted:
            print("\nThat square's already occupied. Choose another square, " + p2 +".\n")
    #returning move to the main function where based on turn, the moves are given to the respective players.
    return move

def nexturn(turn):
    #Switching of turns function that is returned to main accordingly to help change the turn each time a player plays
    if turn == X:
        return O
    else:
        return X

def winningscreen(board, player2, player1):
    #Congratulating the winner accordingly.
    winner1 = winning(board)

    if winner1 == player1:
        print("Congratulations " + p1 + ". You are the winner!")

    elif winner1 == player2:
        print("Congratulations " + p2 + ". You are the winner!")

    elif winner1 == tie:
        print("It is a tie")

    restart()

def restart():
    restart = input(("\nIf y'all want to play again, press r or press any other key to quit."))
    if restart == "r":
        main()
    else:
        print("\nGAME OVER\n")


def main():
    #main function which brings together the game
    Tutorial()
    global p1
    global p2
    p1 = asknamePlayer1()
    p2 = asknamePlayer2()
    player2, player1 = rand_game_starter()
    turn = X
    board = create_newboard()
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
    winningscreen(board, player2, player1)


main()
