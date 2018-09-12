#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 12:24:07 2018

@author: prasad
"""

# Simple game of Tic-Tac-Toe built for Reinforcement Learning applications

# Board - the game board is represented by a list of size 9
def main():
    board = [" " for x in range(9)]  
    game(board)


# Prints a properly formatted board
def printBoard(board):
    print("%s | %s | %s"%(board[0],board[1],board[2]))
    print("_________")
    print("%s | %s | %s"%(board[3],board[4],board[5]))
    print("_________")
    print("%s | %s | %s"%(board[6],board[7],board[8]))
    
    
# Inserts the player's piece into the given position in the board
# GIVEN: pos - position on the board where the piece is to be inserted
#        player - the piece that represents the current player (X or O)
#        board - the board in which the piece is to be inserted
def insertBoard(pos, player, board):
    board[pos] = player
    
    
# Returns True if and only if the given position is free .i.e. it does not have
# a piece at the given position
# Else returns False
def spaceFree(pos, board):
    return board[pos] == " "


# Main execution method of the game
# GIVEN: board - board on which the game is to be played
def game(board):
    print("TIC TAC TOE\n")
    printBoard(board)
    player = "X"
    while not boardFull(board):
        oldplayer = player
        player = playerMove(player, board)
        printBoard(board)            
        
        if checkWinner(board, oldplayer): 
            print("%s won this match!"%oldplayer)
            break
        
    if boardFull(board):
        printBoard(board)
        print("Match ended in a draw!")


# Performs the current player's move and
# Returns the player whose turn it is next to play
# Prints warnings to extract valid input from the user
def playerMove(player, board):
    run = True
    
    while run:
        choice = input("Please enter a position to play: ")
        
        try:
            choice = int(choice)
            if not checkChoice(choice, board):
                raise Exception("Number out of range")
        except:
            print("Please enter a valid number between 0 and 8")
            continue
        
        if spaceFree(choice, board):
            insertBoard(choice, player, board)
            player = turnDecider(player)
            run = False
        else:
            print("Slot is full choose another slot")
            
    return player
   
    
# Returns True if the given position is within the board size(0 to 8)
# Else returns False
def checkChoice(pos, board):
    return not (pos >= len(board) or pos < 0)


# Returns True if the board is full
# Else returns False
def boardFull(board):
    if board.count(' ') > 0:
        return False
    else:
        return True


# Returns the piece of the player whose turn it is next to play
def turnDecider(player):
    player1 = "X"
    player2 = "O"
    
    if player == player2:
        return player1
    else:
        return player2
        
    
# Returns True if any winning condition for the given player is satisfied
# Else returns False
# GIVEN: board - the board on which current game is being played
#        player - piece of the player whose turn it is to play 
        
## NEEDS to be improved later on 
def checkWinner(b, player):
    return ((b[0] == player and b[1] == player and b[2] == player) or
            (b[3] == player and b[4] == player and b[5] == player) or
            (b[6] == player and b[7] == player and b[8] == player) or
            (b[0] == player and b[3] == player and b[6] == player) or
            (b[1] == player and b[4] == player and b[7] == player) or
            (b[2] == player and b[5] == player and b[8] == player) or
            (b[0] == player and b[4] == player and b[8] == player) or
            (b[2] == player and b[4] == player and b[6] == player))
    

if __name__ == '__main__':
    main()
    