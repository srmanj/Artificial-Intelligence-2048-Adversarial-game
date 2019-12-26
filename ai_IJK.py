#!/usr/local/bin/python3

"""
This is where you should write your AI code!

Authors: PLEASE ENTER YOUR NAMES AND USER ID'S HERE

Based on skeleton code by Abhilash Kuhikar, October 2019
"""

from logic_IJK import Game_IJK
import copy
import random
import numpy as np
import operator
mapping = { "A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16 ,
                "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, " ":0}
            
MIN, MAX = -10000,10000
# Suggests next move to be played by the current player given the current game
#
# inputs:
#     game : Current state of the game 
#
# This function should analyze the current state of the game and determine the 
# best move for the current player. It should then call "yield" on that move.
#Heuristics
def heuristic(board,typeofplayer):
    #calculating heuristic for board
    h1=empty_tile(board)
    #h2=corner_tile(board)
    h2=quantify(board,typeofplayer)
    h1_m =h1/(h1+h2)
    h2_m = h2/(h1+h2)
    h=0.3*h1_m+0.7*h2_m
    return h

def empty_tile(board):
    h1 = str(board.getGame()).count("' '")
    return h1


def quantify(board,player):
    maxi =mini= 0
    board = board.getGame()
    for i in range(len(board)): 
        for j in range(len(board)):
            if (ord(board[i][j])>64 and ord(board[i][j])<91):
                maxi += mapping[board[i][j]] * (mapping[board[i][j]]*10)
            elif (ord(board[i][j])>96 and ord(board[i][j])<123):
                mini += mapping[board[i][j]] * (mapping[board[i][j]]*10)
    if player == 'max':
        return maxi
    else:
        return mini



#Function to generate children for a given dictionary entry
def generateChildren(board,key,depth):
    dic={}
    for j in ['U','D','L','R']:
#        print(str(i+j+str(iter)))
        temp = copy.deepcopy(board) #Create a copy of that game
        tmp = str(key)+str(j)+str(depth)
        dic[tmp] = temp.makeMove(j) #perform move j on it and append to the dictionary
        #temp.printGame()        
    return dic



#Generating children of specified depth
def return_dict(board,depth):
   children_list=[]
   child={}
   child["0"]=board
   children_list.append(child)
   for i in range(1,depth):
      dict_to_iterate=children_list[i-1]
      flag1={}
      for key,value in dict_to_iterate.items():
         flag=generateChildren(value,key,i)
         flag1.update(flag)
      children_list.append(flag1)
   return children_list

def non_det_choice(board,typeofplayer):
    children_list=return_dict(board,2)
    heu_values=[]
    heu_keys = []
    for key,value in children_list[1].items():
        heu_values.append(heuristic(value,typeofplayer))
        heu_keys.append(key)
    return heu_keys[heu_values.index(max(heu_values))][1]


def choice(board,typeofplayer,depth):
    children_list=return_dict(board,depth)
    heu_values=[]
    heu_keys = []
    for key,value in children_list[depth-1].items():
        heu_values.append(heuristic(value,typeofplayer))
        heu_keys.append(key)
    #Read the best leaf available
    optimal_choice = maxplayer(0, 0, heu_values, -10000, 10000,depth)
    my_choice = heu_keys[heu_values.index(optimal_choice)][1]
    
    return my_choice


#Begin - The following code was designed using the pseudo code from - https://www.cs.cornell.edu/courses/cs312/2002sp/lectures/rec21.htm
#Minimax with alpha beta implementation
def maxplayer(depth, nodeIndex, values, alpha, beta,d):
    if depth == d:  
        return values[nodeIndex-1] 
    else:
        best = MIN
        # Recur for left and right children  
        for i in range(0, 4):  #We have 4 children 
            childnode= nodeIndex * 2 + i
            val = minplayer(depth + 1,childnode,values, alpha, beta,d)  
            best = max(best, val)  
            alpha = max(alpha, best)  
  
            # Alpha Beta Pruning   
            if beta <= alpha:
                break            
        return best
    
def minplayer(depth, nodeIndex, values, alpha, beta,d):
    if depth==d:
        return values[nodeIndex-1]
    else:
        best = MAX 
  
        # Recur for left and right children  
        for i in range(0, 4):
            childnode=nodeIndex*2+i
            val = maxplayer(depth + 1,childnode ,values, alpha, beta,d)  
            best = min(best, val)  
            beta = min(beta, best)  
  
            # Alpha Beta Pruning  
            if beta <= alpha:  
                break 
           
        return best
#End of code that was designed using the pseudo code from https://www.cs.cornell.edu/courses/cs312/2002sp/lectures/rec21.htm


def next_move(game: Game_IJK)-> None:

    '''board: list of list of strings -> current state of the game
       current_player: int -> player who will make the next move either ('+') or -'-')
       deterministic: bool -> either True or False, indicating whether the game is deterministic or not
    '''

    board = game.getGame()
    player = game.getCurrentPlayer()
    deterministic = game.getDeterministic()
    
    print(player)

    # You'll want to put in your fancy AI code here. For right now this just 
    # returns a random move.
    
    if player == '+':
       temp = 'max'
    else:
       temp = 'min'
    
    if deterministic == True:
        yield choice(game,temp,4)#random.choice(['U', 'D', 'L', 'R'])
    else:
        yield choice(game,temp,5)#random.choice(['U', 'D', 'L', 'R'])
    
    
    
 ##Extra stuff
#Create a gradient matrix to reward the behavior of saving higher valued pieces towards the edges
   #  lt_heu=[[5,4,3,2,1,0],[4,3,2,1,0,-1],[3,2,1,0,-1,-2],[2,1,0,-1,-2,-3],[1,0,-1,-2,-3,-4],[0,-1,-2,-3,-4,-5]]
   #  rt_heu=[[0,1,2,3,4,5],[-1,0,1,2,3,4],[-2,-1,0,1,2,3],[-3,-2,-1,0,1,2],[-4,-3,-2,-1,0,1],[-5,-4,-3,-2,-1,0]]
   #  lb_heu=[[0,-1,-2,-3,-4,-5],[1,0,-1,-2,-3,-4],[2,1,0,-1,-2,-3],[3,2,1,0,-1,-2],[4,3,2,1,0,-1],[5,4,3,2,1,0]]
   #  rb_heu=[[-5,-4,-3,-2,-1,0],[-4,-3,-2,-1,0,1],[-3,-2,-1,0,1,2],[-2,-1,0,1,2,3],[-1,0,1,2,3,4],[0,1,2,3,4,5]]
    
   #  h2 = max(sum(sum(np.multiply(lt_heu,h_temp))), sum(sum(np.multiply(lb_heu,h_temp))), sum(sum(np.multiply(rt_heu,h_temp))), sum(sum(np.multiply(rb_heu,h_temp))))   
