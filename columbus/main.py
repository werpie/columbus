import numpy as np
from planet_choosing import *
from klasy import *
from planeta_zero import *
from kolko_i_krzyzyk import *
from Labirynt import *
from Paprociara import *
from chodzenie import *
from Zakonczenie import *
from Ksiezyc import *

def main():
    #laneta_zero()
    loop = True
    Ksiezyc()
    Zakonczenie()
    input()
    while loop:
        temp = planet_choosing()
        if temp == 1:
            chodzenie()
            Game()
        if temp == 2:
            chodzenie()
            tic_tac_toeing()

if __name__ == '__main__':
    main()