#!/usr/local/bin/python3
"""
This implements a keyboard interface where humans can enter their
IJK moves.

Based on skeleton code by Abhilash Kuhikar, October 2019
"""

import random
from logic_IJK import Game_IJK

# Suggests next move to be played by the current player given the current game
#
# game : Current state of the game 
#
# This function should analyze the current state of the game and determine the 
# best move for the current player. It should then call "yield" on that move.

def next_move(game: Game_IJK)-> None:
    ''' game: current-state of game
        yield a single character as one of the following moves - 'U', 'L', 'R', 'D', 'S'
    '''
    '''board: list of list of chars -> current state of the game
       current_player: int -> player who will make the next move either 1('+') or -1('-')
    '''

    print('Please enter move for player %s (U, D, L, R): ' % game.getCurrentPlayer())
    move = input().strip().upper()
    while(move not in "UDLR"):
        print('Bad move! Please try again and enter move for player %s (U, D, L, R): ' % turn)
        move = input().strip()

    yield move
