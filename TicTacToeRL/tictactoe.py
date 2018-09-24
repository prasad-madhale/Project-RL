#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 12:24:07 2018

@author: prasad
"""
import random

# Class TicTacToe represents a simple game of Tic-Tac-Toe built for Reinforcement 
# Learning applications
# It has following attributes:
#     board - the game board is represented by a list of strings of size 9
#     player - represents the player whose turn it is to play next (by default 'X' player plays first)
class TicTacToe:
    
    def __init__(self):
        self.board = [" " for x in range(9)]  
        self.player = 'X'
    
    
    # Prints a properly formatted board
    def printBoard(self, board):
        print("%s | %s | %s"%(board[0],board[1],board[2]))
        print("_________")
        print("%s | %s | %s"%(board[3],board[4],board[5]))
        print("_________")
        print("%s | %s | %s"%(board[6],board[7],board[8]))


        
    # Inserts the player's piece into the given position in the board
    # GIVEN: pos - position on the board where the piece is to be inserted
    #        player - the piece that represents the current player (X or O)
    #        board - the board in which the piece is to be inserted
    def insertBoard(self, pos, player, board):
        board[pos] = player
        
        
    # Returns True if and only if the given position is free .i.e. it does not have
    # a piece at the given position
    # Else returns False
    def spaceFree(self, pos, board):
        return board[pos] == " "
    
    
    # Main execution method of the game
    # GIVEN: board - board on which the game is to be played
    def game(self, board):
        print("TIC TAC TOE\n")
        self.printBoard(board)
        done = False
        
        while not self.boardFull(board):
            oldplayer = self.player
            self.player = self.playerMove(self.player, board)
            self.printBoard(board)            
            
            if self.checkWinner(board, oldplayer): 
                print("%s won this match!"%oldplayer)
                done = True
                break
            
            oldplayer = self.player
            self.player = self.compMove(self.player, board)
            print("\nAI's move\n")
            self.printBoard(board) 
            
            if self.checkWinner(board, oldplayer): 
                print("%s won this match!"%oldplayer)
                done = True
                break        
            
        if self.boardFull(board) and not done:
            self.printBoard(board)
            print("Match ended in a draw!")
    
    
    # Performs the current player's move and
    # Returns the player whose turn it is next to play
    # Prints warnings to extract valid input from the user
    def playerMove(self, player, board):
        run = True
        
        while run:
            choice = input("Please enter a position to play: ")
            
            try:
                choice = int(choice)
                if not self.checkChoice(choice, board):
                    raise Exception("Number out of range")
            except:
                print("Please enter a valid number between 0 and 8")
                continue
            
            if self.spaceFree(choice, board):
                self.insertBoard(choice, player, board)
                player = self.turnDecider(player)
                run = False
            else:
                print("Slot is full choose another slot")
                
        return player
       
        
    def compMove(self, player, board):
        run = True
        
        while run:
            # Call the RL class to predict the move
            choice = random.randint(0,8)
            
            try:
                if not self.checkChoice(choice, board):
                    raise Exception("Number out of range")
            except:
                print("Please enter a valid number between 0 and 8")
                continue
            
            if self.spaceFree(choice, board):
                self.insertBoard(choice, player, board)
                player = self.turnDecider(player)
                run = False
            else:
                print("Slot is full choose another slot")
                
        return player
        
        
    # Returns True if the given position is within the board size(0 to 8)
    # Else returns False
    def checkChoice(self, pos, board):
        return not (pos >= len(board) or pos < 0)
    
    
    # Returns True if the board is full
    # Else returns False
    def boardFull(self, board):
        if board.count(' ') > 0:
            return False
        else:
            return True
    
    
    # Returns the piece of the player whose turn it is next to play
    def turnDecider(self, player):
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

    def checkWinner(self, board, player):

        combos = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

        for line in combos:
            lineState = board[line[0]] + board[line[1]] + board[line[2]]

            if lineState == "XXX" or lineState == "OOO":
                return True

        return False


    def getState(self, board):
        boardState = ""

        for chars in board:
            boardState += chars

        return boardState


    def nextState(self,board,pos,player):
        board2 = board.copy()
        board2[pos] = player
        result = self.getState(board2)
        return result


def main():
    tic = TicTacToe()
    tic.game(tic.board)


if __name__ == '__main__':
    main()
    