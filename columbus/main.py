import numpy as np
from planet_choosing import *
from klasy import *
from planeta_zero import *
from planeta1 import *
from kolko_i_krzyzyk import *
from Labirynt import *
from Paprociara import *
from chodzenie import *
from Zakonczenie import *
from Ksiezyc import *

def main():
    planeta_zero()
    loop = True
    input()
    while loop:
        temp = planet_choosing()
        if temp == 1:
            chodzenie()
            planeta1()
        if temp == 2:
            chodzenie()
            #wstep do labiryntu
            Labirynt()
    Ksiezyc()
if __name__ == '__main__':
    main()
