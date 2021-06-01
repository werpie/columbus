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
            elif place == "q":
                if self.board[0,0] == 0:
                    self.board[0,0] = 1

    def show_board(self):
        print(self.board)


def do():
    x = tic_tac_toe()
    x.show_board()
    x.player_move()
