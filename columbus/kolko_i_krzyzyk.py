import pygame, numpy as np,random
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,200)
RED = (200,0,0)
SCREEN_SIZE = (600,600)

"""
Zwraca "player","computer","remis", zależnie, kto wygrał
"""

def init_display(): #Making display and bacground for game
    global screen,background
    screen = pygame.display.set_mode((SCREEN_SIZE))
    background = pygame.Surface(screen.get_size())
    background.fill(BLACK)
    font = pygame.font.SysFont("Times",20)
    moves1 = ["q", "w", "e"], ["a", "s", "d"], ["z", "x", "c"]
    for row, line in enumerate(moves1):
        for column, element in enumerate(line):
            text1 = font.render(element, True, WHITE)
            screen.blit(text1,(column*200+20,row*200+10))

class tic_tac_toe(): #Main game rules, restricting moves for player and making moves for pc

    def __init__(self):
        self.board = np.zeros((3, 3))
        self.possible_moves = ["q","w","e","a","s","d","z","x","c"]

    def win_checker(self):
        skos1 = self.board[0, 0] + self.board[1, 1] + self.board[2, 2]
        skos2 = self.board[2, 0] + self.board[1, 1] + self.board[0, 2]
        for row in range(3):
                if abs(np.sum(self.board[row,:])) == 3 or abs(np.sum(self.board[:,row])) == 3 \
                        or abs(skos1) == 3 or abs(skos2) == 3:
                    return True
        return False

    def filling_board(self,place,who):
        if place in self.possible_moves:
            if place == "q":
                self.board[0, 0] = who
                self.possible_moves.remove("q")
                return True
            if place == "w":
                self.board[0, 1] = who
                self.possible_moves.remove("w")
                return True
            if place == "e":
                self.board[0, 2] = who
                self.possible_moves.remove("e")
                return True
            if place == "a":
                self.board[1, 0] = who
                self.possible_moves.remove("a")
                return True
            if place == "s":
                self.board[1, 1] = who
                self.possible_moves.remove("s")
                return True
            if place == "d":
                self.board[1, 2] = who
                self.possible_moves.remove("d")
                return True
            if place == "z":
                self.board[2, 0] = who
                self.possible_moves.remove("z")
                return True
            if place == "x":
                self.board[2, 1] = who
                self.possible_moves.remove("x")
                return True
            if place == "c":
                self.board[2, 2] = who
                self.possible_moves.remove("c")
                return True
        else:
            return False

    def computer_move(self):
        move = random.choice(self.possible_moves)
        drawing_circle(move)
        self.filling_board(move,1)


    def player_move(self,place):
        return self.filling_board(place,-1)

    def show_board(self):
        print(self.board)



def drawing_x(letter):
    moves1 = ["q", "w", "e"], ["a", "s", "d"], ["z", "x", "c"]
    s = 30
    for row,line in enumerate(moves1):
        for column,element in enumerate(line):
            if element == letter:
                y = 200*row+s
                x = 200*column+s
                ye = 200*(row+1)-s
                xe = 200*(column+1)-s
                position1 = (x,y)
                position2 = (xe,y)
                position3 = (xe,ye)
                position4 = (x,ye)
    pygame.draw.line(screen,BLUE,position1,position3,10)
    pygame.draw.line(screen,BLUE,position2,position4,10)

def drawing_circle(letter):
    moves1 = ["q", "w", "e"],["a", "s", "d"],["z", "x", "c"]
    s = 100
    rad = 70
    for row,line in enumerate(moves1):
        for column,element in enumerate(line):
            if element == letter:
                x = 200*row+s
                y = 200*column+s
                pygame.draw.circle(screen,RED,(y,x),rad,10)


def tic_tac_toeing():
    global screen,background,licznik
    init_display()
    x = tic_tac_toe()
    licznik = 0
    pygame.draw.line(screen, WHITE, (200, 0), (200, 600), 10)
    pygame.draw.line(screen, WHITE, (400, 0), (400, 600), 10)
    pygame.draw.line(screen, WHITE, (0, 200), (600, 200), 10)
    pygame.draw.line(screen, WHITE, (0, 400), (600, 400), 10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if x.player_move("q"):
                        drawing_x("q")
                        pygame.display.update()
                        pygame.time.wait(300)
                        licznik += 1
                        if x.win_checker():
                            return "player won"
                        if licznik == 5:
                            return "remis"
                        x.computer_move()
                elif event.key == pygame.K_w:
                    if x.player_move("w"):
                        drawing_x("w")
                        pygame.display.update()
                        pygame.time.wait(300)
                        licznik += 1
                        if x.win_checker():
                            return "player won"
                        if licznik == 5:
                            return "remis"
                        x.computer_move()
                elif event.key == pygame.K_e:
                    if x.player_move("e"):
                        drawing_x("e")
                        pygame.display.update()
                        pygame.time.wait(300)
                        licznik += 1
                        if x.win_checker():
                            return "player won"
                        if licznik == 5:
                            return "remis"
                        x.computer_move()
                elif event.key == pygame.K_a:
                    if x.player_move("a"):
                        drawing_x("a")
                        pygame.display.update()
                        pygame.time.wait(300)
                        licznik += 1
                        if x.win_checker():
                            return "player won"
                        if licznik == 5:
                            return "remis"
                        x.computer_move()
                elif event.key == pygame.K_s:
                    if x.player_move("s"):
                        drawing_x("s")
                        pygame.display.update()
                        pygame.time.wait(300)
                        licznik += 1
                        if x.win_checker():
                            return "player won"
                        if licznik == 5:
                            return "remis"
                        x.computer_move()
                elif event.key == pygame.K_d:
                    if x.player_move("d"):
                        drawing_x("d")
                        pygame.display.update()
                        pygame.time.wait(300)
                        licznik += 1
                        if x.win_checker():
                            return "player won"
                        if licznik == 5:
                            return "remis"
                        x.computer_move()
                elif event.key == pygame.K_z:
                    if x.player_move("z"):
                        drawing_x("z")
                        pygame.display.update()
                        pygame.time.wait(300)
                        licznik += 1
                        if x.win_checker():
                            return "player won"
                        if licznik == 5:
                            return "remis"
                        x.computer_move()
                elif event.key == pygame.K_x:
                    if x.player_move("x"):
                        drawing_x("x")
                        pygame.display.update()
                        pygame.time.wait(300)
                        licznik += 1
                        if x.win_checker():
                            return "player won"
                        if licznik == 5:
                            return "remis"
                        x.computer_move()
                elif event.key == pygame.K_c:
                    if x.player_move("c"):
                        drawing_x("c")
                        pygame.display.update()
                        pygame.time.wait(300)
                        licznik += 1
                        if x.win_checker():
                            return "player won"
                        if licznik == 5:
                            return "remis"
                        x.computer_move()
                if event.key == pygame.K_r:
                    x.show_board()
        if x.win_checker():
            return "computer"

        pygame.display.update()