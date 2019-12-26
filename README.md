# B551 Assignment 2: Games and Bayes
##### Submission by Sri Harsha Manjunath - srmanj@iu.edu; Vijayalaxmi Bhimrao Maigur - vbmaigur@iu.edu; Disha Talreja - dtalreja@iu.edu
###### Fall 2019


## Part 1: IJK
IJK is a sliding tile game played on a 4x4 board by two players, lowercase (also known as -) and uppercase
(+). The players take turns, starting with uppercase. At the start of each turn, a tile labeled a is added
randomly somewhere on the board if it is lowercase’s turn, and an A is added if it is uppercase’s turn. A
player’s turn consists of making one of five possible moves: Up, Down, Left, Right. All tiles are slid in the direction that
the player selected until there are no empty spaces left in that direction. Then, pairs of letters that are the
same, of the same case, and adjacent to each other in the direction of the movement are combined together
to create a single tile of the subsequent letter and the same case. For example, if an A slides down and hits
another A, the two merge and become a single B. Similarly, pairs of B’s merge to become a single C, and so
on. For pairs of letters that are the same but with opposite case, e.g. A and a, the tiles merge to become
the letter B if it is uppercase’s turn, or b if it is lowercase’s turn. The game ends when a K or k appears on
the board, and the player of that case wins the game. </br>

The game has two specific variants. </br> In Deterministic IJK, the new a or A at the beginning of each turn
is added to a predictable empty position on the board (which is a function of the current board state). </br> In
Non-deterministic IJK , the new a or A is added to a random position on the board. The rest of the rules
are the same for the two variants. </br> </br>
Your goal is to write AI code that plays these two variants of IJK well.  You can run the code like this: </br></br>
./ijk.py [uppercase-player] [lowercase-player] [mode]  </br></br>
where uppercase-player and lowercase-player are each either ai or human, and mode is either det for deterministic IJK or nondet for nondeterministic IJK. These commands let you set up various types of games. </br>
For example, if you (a human) want to play a deterministic game against the ai, you could type: </br></br>
./ijk.py human ai det </br></br>
Similarly, you can set up games between AIs or between humans. Currently, the AI logic is very simple – it
just plays randomly. You’ll want to edit ai IJK.py to implement more advanced logic. You shouldn’t need
to edit the other files, although you’ll probably want to look at them to understand how the code works. </br>
Hints: You’ll probably want to start by implementing the deterministic version first, but it’s up to you.
Note that you don’t have to implement the game itself (or even to fully understand the rules) since our code
already does this for you. </br>
The tournament: To make things more interesting, we will hold a competition among all submitted solutions
to see whose solution can score the highest across several different games. While the majority of your grade
will be on correctness, programming style, quality of answers given in comments, etc., a small portion may
be based on how well your code performs in the tournaments, with particularly well-performing programs
eligible for prizes including extra credit points. </br>

## Solution 
##### 1. Set of States S: 
The set of states S, can be defined as all possible configurations of the 6 * 6 board partially populated with characters from the following set: {A,B,C,D,E,F,G,H,I,J,K} and {a,b,c,d,e,f,g,h,i,j,k}.

##### 2. Successor Function:
Successor function returns the game board after performing one movement from the following ['U','D','L','R'] and places an 'A' if it's uppercase's turn or an 'a' if it's lowercase's turn in a predictable position for Deterministic mode and in a random position for Non-Deterministic mode.

##### 3. Initial State:
Initial state is a 6 * 6 board with a tile labeled 'a' randomly placed somewhere if it's lowercase's turn and 'A' is added it's uppercase's turn.

##### 4. Goal State:
Game board with one of the 36 tiles having a 'K' or 'k' placed. 'K' implies uppercase wins and 'k' implies lowercase wins.

##### 5. Heuristic functions:

The program uses the following two heuristic functions to predict the next move:
1. Empty tiles:
It counts the number of empty tiles (tiles with no characters placed) on the 6 * 6 board.

2. Quantification of characters:
This function assigns weights to each of the characters of the set {A,B,C,D,E,F,G,H,I,J,K,a,b,c,d,e,f,g,h,i,j,k}. Characters have exponential weights assigned with 'A' and 'a' having the least value while 'K' and 'k' having the maximum value.

#### Approach:

We have implemented the minimax algorithm along with the alpha-beta implementation.
1. The game tree is expanded upto depth 4 taking into consideration 4 moves['U','D','L','R'] while expanding each node.
2. The leaf nodes are passed to the heuristic function which returns values by passing each of the nodes through the two heuristic functions used.
3. The leaf node with the most promising value of the heuristic function is traced back to the root node.
4. Hence, choice for further moves is made as per the path traced.

#### Alternative approaches considered:

1) For the Non-Deterministic mode of the game, as (A/a) is placed on a random tile;
    We tried taking care of the randomness by considering each of the 35 possible successor boards where each of the boards       would have an A/a placed on each of the empty tiles. (35 empty positions considering depth 1)

    This implementation was abandoned because of the constraints imposed by the available function definitions.
    
  2) Gradient Matrix:
     Gradient Matrix was another heuristic tried to reward the behavior of saving higher valued pieces towards the edges so        that lower valued pieces can be merged without any obstacles(higher valued pieces) in between.
    
     This heuristic was abandoned for the same reason as above, as we don't have any control over those pieces towards the          edges as the opposition player can change the position of the pieces.  
    
