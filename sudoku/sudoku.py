#! /usr/bin/python3

import sys
import copy

AllVals = set([1,2,3,4,5,6,7,8,9])
Cliques=[[0,1,2,3,4,5,6,7,8],\
[9,10,11,12,13,14,15,16,17],\
[18,19,20,21,22,23,24,25,26],\
[27,28,29,30,31,32,33,34,35],\
[36,37,38,39,40,41,42,43,44],\
[45,46,47,48,49,50,51,52,53],\
[54,55,56,57,58,59,60,61,62],\
[63,64,65,66,67,68,69,70,71],\
[72,73,74,75,76,77,78,79,80],\
[0,9,18,27,36,45,54,63,72],\
[1,10,19,28,37,46,55,64,73],\
[2,11,20,29,38,47,56,65,74],\
[3,12,21,30,39,48,57,66,75],\
[4,13,22,31,40,49,58,67,76],\
[5,14,23,32,41,50,59,68,77],\
[6,15,24,33,42,51,60,69,78],\
[7,16,25,34,43,52,61,70,79],\
[8,17,26,35,44,53,62,71,80],\
[0,1,2,9,10,11,18,19,20],\
[3,4,5,12,13,14,21,22,23],\
[6,7,8,15,16,17,24,25,26],\
[27,28,29,36,37,38,45,46,47],\
[30,31,32,39,40,41,48,49,50],\
[33,34,35,42,43,44,51,52,53],\
[54,55,56,63,64,65,72,73,74],\
[57,58,59,66,67,68,75,76,77],\
[60,61,62,69,70,71,78,79,80]\
]

class MyStack:
    def __init__(self, cells = [], list = []):
        self.cells = cells
        self.stack = list

    def __str__(self):
        return str(self.stack)

    def push(self, args):
        self.cells.append(args[0])
        #print(self.cells)
        self.stack.append(args[1])

    def pop(self):
        #print("cells: " + str(self.cells))
        return [self.cells.pop(len(self.cells)-1), self.stack.pop(len(self.stack)-1)]

# class Sudoku:
#     def __init__(self, fileName, boardName):
#         self.boards = Stack()
#         f = open(fileName, "r")
#         df = f.read()
#         lines = df.split('\n')
#         f.close()

def getBoard(argv):
    #print(argv[3])
    name = argv[3]
    f = open(argv[1], "r")
    df = f.read()
    lines = df.split('\n')
    f.close()
    board = []
    temp = ""
    for x in range(len(lines)):
        if lines[x]==name:
            for y in range(x+1, x+10):
                temp+=lines[y]
            temp = temp.replace(',', '')
            board = list(temp)
    return [name, board]

# def makeNeighbors():

def nextOpenCell(board, prev_cell):
    for x in range(len(board)):
        if board[x]=='_':
            return x
    return None

def nextValidGuess(board,cell,num):
    temp = [None, False]
    for guess in range(num, 10):
        #print(guess)
        valid = True
        for clique in Cliques:
            if valid and cell in clique:
                for index in range(len(clique)):
                    #print("board[clique[index]]: " + str(board[clique[index]]) + ", guess: " + str(guess))
                    #print(valid)
                    #print(len(board))
                    if valid and str(board[clique[index]])==str(guess):
                        valid = False
        if valid:
            if not temp[0]:
                temp = [guess, True]
            else:
                temp = [temp[0], False]
    return temp

def printBoard(board):
    result = ""
    for x in range(9):
        for y in range(8):
            result += str(board[x*9+y]) + ","
        result += str(board[x*9+8]) + "\n"
    print(result)

def writeBoard(argv,name,board):
    f = open(argv[2], "w")
    #f.write(name.replace("unsolved", "solved") + "\n")
    for x in range(9):
        for y in range(8):
            f.write(str(board[x*9+y]) + ",")
        f.write(str(board[x*9+8]) + "\n")
    f.close()

# States
NEW_CELL = 0
FIND_NEXT_CELL = 1
BACKTRACK = 2

def main(argv=None):
    if not argv:
        argv = sys.argv
    #print(argv)
    name,board = getBoard(argv)
    #print(name)
    printBoard(board)
    mystack = MyStack()
    #makeNeighbors()
    nback = 0
    ntrials = 0
    cell = nextOpenCell(board,-1)
    # print(cell)
    # print(Cliques)
    Count = 0
    state = NEW_CELL
    while True:
        ntrials += 1
        #if ntrials % 10000 == 0: print ('ntrials,nback',ntrials,nback)

        # we're on a new open cell
        if state == NEW_CELL:
            #printBoard(board)
            #print("-------")
            guess,forced = nextValidGuess(board,cell,1)
            #print ("NEW_CELL,cell,guess,forced",cell,guess,forced)
            if not guess:
                # failed to find a valid guess for this cell, backtrack
                state = BACKTRACK
            else:
                board[cell] = guess
                #print(cell)
                if not forced:
                    mystack.push([cell,board[:]])
                state = FIND_NEXT_CELL
            continue

        # find a new open cell
        if state == FIND_NEXT_CELL:
            cell = nextOpenCell(board,cell)
            if not cell:
                # Solution!
                break
            state = NEW_CELL
            continue

        # backtrack
        if state == BACKTRACK:
            nback += 1
            #print("cell: " + str(cell))
            cell,board = mystack.pop()
            old_guess = board[cell]
            guess,forced = nextValidGuess(board,cell,old_guess+1)  # note: state cannot be forced
            #print('BACKTRACK,cell,guess,forced',cell,guess,forced)
            if not guess:
                state = BACKTRACK
            else:
                board[cell] = guess
                mystack.push([cell,board[:]])
                state = FIND_NEXT_CELL
            continue

    print ('Solution!, with ntrials, backtracks: ', ntrials,nback)
    printBoard(board)
    writeBoard(argv,name,board)

main()
