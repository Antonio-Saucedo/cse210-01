"""
Assignment: W02 Prove
Author: Antonio Saucedo
"""

from colorama import Fore
from colorama import Style

def main():
    player_turn = "o"
    size = int(input("What board size would you like? 3 or 4? "))
    print()

    while (size != 3) & (size != 4):
        print("Invalid Size!")
        size = input("What board size would you like? 3 or 4? ")
        print()

    board = board_values(size)

    winner = "draw"
    while (not end(board, size)) & (winner != "x") & (winner != "o"):
        display_board(board, size)
        player_turn = player(player_turn)
        turn(player_turn, board, size)
        winner = win(board, size)
        print()

    display_board(board, size)
    print()

    if winner != "draw":
        print(f"{winner} is the winner!")
    else:
        print("It was a draw!")
    print(f"Good game! Thanks for playing!\n")

def board_values(size):
    if size == 3:
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    else:
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
    return board

def color_text(text):
    if text == "x":
        return Fore.RED + Style.BRIGHT + str(text) + " " + Style.RESET_ALL
    elif text == "o":
        return Fore.BLUE + Style.BRIGHT + str(text) + " " + Style.RESET_ALL
    else:
        return Fore.GREEN + Style.BRIGHT + str(text) + " " + Style.RESET_ALL

def display_board(board, size):
    if size == 3:
        print(color_text(board[0]) + color_text("|") + color_text(board[1]) + color_text("|") + color_text(board[2]))
        print(color_text("--+---+--"))
        print(color_text(board[3]) + color_text("|") + color_text(board[4]) + color_text("|") + color_text(board[5]))
        print(color_text("--+---+--"))
        print(color_text(board[6]) + color_text("|") + color_text(board[7]) + color_text("|") + color_text(board[8]))
    else:
        print(color_text(board[0]) + color_text("|") + color_text(board[1]) + color_text("|") + color_text(board[2])+ color_text("|") + color_text(board[3]))
        print(color_text("--+---+---+--"))
        print(color_text(board[4]) + color_text("|") + color_text(board[5]) + color_text("|") + color_text(board[6])+ color_text("|") + color_text(board[7]))
        print(color_text("--+---+---+--"))
        print(color_text(board[8]) + color_text("|") + color_text(board[9]) + color_text("|") + color_text(board[10])+ color_text("|") + color_text(board[11]))
        print(color_text("--+---+---+--"))
        print(color_text(board[12]) + color_text("|") + color_text(board[13]) + color_text("|") + color_text(board[14])+ color_text("|") + color_text(board[15]))

def player(player_turn):
    if player_turn == "o":
        return "x"
    else:
        return "o"

def turn(player_turn, board, size):
    print()
    if size == 3:
        move = int(input(f"{player_turn}'s turn to choose a square (1-9): "))
        while (move < 1) | (move > 9):
            print()
            print("Invalid Entry!")
            move = int(input(f"{player_turn}'s turn to choose a square (1-9): "))
    else:
        move = int(input(f"{player_turn}'s turn to choose a square (1-16): "))
        while (move < 1) | (move > 16):
            print()
            print("Invalid Entry!")
            move = int(input(f"{player_turn}'s turn to choose a square (1-16): "))
    board[move - 1] = player_turn

def win(board, size):
    if size == 3:
        if ((board[0] == "x") & (board[1] == "x") & (board[2] == "x")) | ((board[3] == "x") & (board[4] == "x") & (board[5] == "x")) |\
            ((board[6] == "x") & (board[7] == "x") & (board[8] == "x")) | ((board[0] == "x") & (board[3] == "x") & (board[6] == "x")) |\
                ((board[0] == "x") & (board[1] == "x") & (board[2] == "x")) | ((board[1] == "x") & (board[4] == "x") & (board[7] == "x")) |\
                    ((board[2] == "x") & (board[5] == "x") & (board[8] == "x")) | ((board[0] == "x") & (board[4] == "x") & (board[8] == "x")) |\
                        ((board[2] == "x") & (board[4] == "x") & (board[6] == "x")):
            return "x"
        elif ((board[0] == "o") & (board[1] == "o") & (board[2] == "o")) | ((board[3] == "o") & (board[4] == "o") & (board[5] == "o")) |\
            ((board[6] == "o") & (board[7] == "o") & (board[8] == "o")) | ((board[0] == "o") & (board[3] == "o") & (board[6] == "o")) |\
                ((board[0] == "o") & (board[1] == "o") & (board[2] == "o")) | ((board[1] == "o") & (board[4] == "o") & (board[7] == "o")) |\
                    ((board[2] == "o") & (board[5] == "o") & (board[8] == "o")) | ((board[0] == "o") & (board[4] == "o") & (board[8] == "o")) |\
                        ((board[2] == "o") & (board[4] == "o") & (board[6] == "o")):
            return "o"
        else:
            return "draw"
    else:
        if ((board[0] == "x") & (board[1] == "x") & (board[2] == "x") & (board[3] == "x")) | ((board[4] == "x") & (board[5] == "x") & (board[6] == "x") &\
            (board[7] == "x")) | ((board[8] == "x") & (board[9] == "x") & (board[10] == "x") & (board[11] == "x")) | ((board[12] == "x") & (board[13] == "x") &\
                (board[14] == "x") & (board[15] == "x")) | ((board[0] == "x") & (board[4] == "x") & (board[8] == "x") & (board[12] == "x")) | ((board[1] == "x") &\
                    (board[5] == "x") & (board[9] == "x") & (board[13] == "x")) | ((board[2] == "x") & (board[6] == "x") & (board[10] == "x") & (board[14] == "x")) |\
                    ((board[3] == "x") & (board[7] == "x") & (board[11] == "x") & (board[15] == "x")) | ((board[0] == "x") & (board[5] == "x") & (board[10] == "x") &\
                        (board[15] == "x")) | ((board[3] == "x") & (board[6] == "x") & (board[9] == "x") & (board[12] == "x")):
            return "x"
        elif ((board[0] == "o") & (board[1] == "o") & (board[2] == "o") & (board[3] == "o")) | ((board[4] == "o") & (board[5] == "o") & (board[6] == "o") &\
            (board[7] == "o")) | ((board[8] == "o") & (board[9] == "o") & (board[10] == "o") & (board[11] == "o")) | ((board[12] == "o") & (board[13] == "o") &\
                (board[14] == "o") & (board[15] == "o")) | ((board[0] == "o") & (board[4] == "o") & (board[8] == "o") & (board[12] == "o")) | ((board[1] == "o") &\
                (board[5] == "o") & (board[9] == "o") & (board[13] == "o")) | ((board[2] == "o") & (board[6] == "o") & (board[10] == "o") & (board[14] == "o")) |\
                    ((board[3] == "o") & (board[7] == "o") & (board[11] == "o") & (board[15] == "o")) | ((board[0] == "o") & (board[5] == "o") & (board[10] == "o") &\
                        (board[15] == "o")) | ((board[3] == "o") & (board[6] == "o") & (board[9] == "o") & (board[12] == "o")):
            return "o"
        else:
            return "draw"

def end(board, size):
    for value in range(size * size):
        if (board[value - 1] != "x") & (board[value - 1] != "o"):
            return False
    return True

continue_playing = True
while continue_playing:
    main()
    play_again = input("Would you like to play again? ")

    while (play_again.lower() != 'y') & (play_again.lower() != 'yes') & (play_again.lower() != 'n') & (play_again.lower() != 'no'):
        print("Invalid Input!")
        play_again = input("Would you like to play again? ")

    if (play_again.lower() == 'y') | (play_again.lower() == 'yes'):
        continue_playing = True
    elif (play_again.lower() == 'n') | (play_again.lower() == 'no'):
        continue_playing = False