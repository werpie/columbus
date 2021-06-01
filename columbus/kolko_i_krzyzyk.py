import pygame
import random
import numpy as np

class tic_tac_toe():

    def __init__(self):
        self.board = np.zeros((3,3))

    def player_move(self):
        while True:
            place = input("q,w,e\na,s,d\nz,x,c")
            if place == "q":
                if self.board[0,0] == 0:
                    self.board[0,0] = 1
                    return
            elif place == "w":
                if self.board[0,1] == 0:
                    self.board[0,1] = 1
                    return
                    
            elif place == "e":
                if self.board[0,2] == 0:
                    self.board[0,2] = 1
                    return

            elif place == "a":
                if self.board[1,0] == 0:
                    self.board[1,0] = 1
                    return

            elif place == "s":
                if self.board[1,1] == 0:
                    self.board[1,1] = 1
                    return

            elif place == "d":
                if self.board[1,2] == 0:
                    self.board[1,2] = 1
                    return

            elif place == "z":
                if self.board[2,0] == 0:
                    self.board[2,0] = 1
                    return

            elif place == "x":
                if self.board[2,1] == 0:
                    self.board[2,1] = 1
                    return

            elif place == "c":
                if self.board[2,2] == 0:
                    self.board[2,2] = 1
                    return
                

    def show_board(self):
        print(self.board)


def do():
    x = tic_tac_toe()
    x.show_board()
    x.player_move()
