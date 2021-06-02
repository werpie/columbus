import pygame
import random
import numpy as np


class tic_tac_toe():

    def __init__(self):
        self.board = np.zeros((3, 3))
        self.possible_moves = ["q","w","e","a","s","d","z","x","c"]

    def filling_board(self,place):
        if place == "q":
            if self.board[0, 0] == 0:
                self.board[0, 0] = 1
                self.possible_moves.remove("q")
                return True
        elif place == "w":
            if self.board[0, 1] == 0:
                self.board[0, 1] = 1
                self.possible_moves.remove("w")
                return True

        elif place == "e":
            if self.board[0, 2] == 0:
                self.board[0, 2] = 1
                self.possible_moves.remove("e")
                return True

        elif place == "a":
            if self.board[1, 0] == 0:
                self.board[1, 0] = 1
                self.possible_moves.remove("a")
                return True

        elif place == "s":
            if self.board[1, 1] == 0:
                self.board[1, 1] = 1
                self.possible_moves.remove("s")
                return True

        elif place == "d":
            if self.board[1, 2] == 0:
                self.board[1, 2] = 1
                self.possible_moves.remove("d")
                return True

        elif place == "z":
            if self.board[2, 0] == 0:
                self.board[2, 0] = 1
                self.possible_moves.remove("z")
                return True

        elif place == "x":
            if self.board[2, 1] == 0:
                self.board[2, 1] = 1
                self.possible_moves.remove("x")
                return True

        elif place == "c":
            if self.board[2, 2] == 0:
                self.board[2, 2] = 1
                self.possible_moves.remove("c")
                return True
        else:
            return False

    def computer_move(self):
        move = random.choice(self.possible_moves)
        self.filling_board(move)
        print(move)

    def player_move(self):
        while True:
            place = input("q,w,e\na,s,d\nz,x,c")
            if self.filling_board(place) == True:
                return


    def show_board(self):
        print(self.board)


def do():
    x = tic_tac_toe()
    while True:
        x.show_board()
        x.player_move()
        x.computer_move()
        print(x.possible_moves)
        if input() == 1:
            return
