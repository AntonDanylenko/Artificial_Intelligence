#! /usr/bin/python3

import sys
import copy

class MyStack:
    def __init__(self, list = []):
        self.stack = list

    def __str__(self):
        return str(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop(len(self.stack)-1)

# class Sudoku:
#     def __init__(self, fileName, boardName):
#         self.boards = Stack()
#         f = open(fileName, "r")
#         df = f.read()
#         lines = df.split('\n')
#         f.close()

def getBoard(argv):
    name = argv[3]
    f = open(argv[1], "r")
    df = f.read()
    lines = df.split('\n')
    f.close()
    for x in lines:
        if x==name:
            board = [lines[y] for y in range(x, x+9)]
    return [name, board]

# def makeNeighbors():

# States
NEW_CELL = 0
FIND_NEXT_CELL = 1
BACKTRACK = 2
AllVals = set([1,2,3,4,5,6,7,8,9])

def main(argv=None):
    if not argv:
        argv = sys.argv

    name,board = getBoard(argv)
    print(name)
    print(board)
    mystack = MyStack()
    # makeNeighbors()
    # nback = 0
    # ntrials = 0
    # cell = nextOpenCell(board,-1)
    # state = NEW_CELL
    # while True:
    #     ntrials += 1
    #     #if ntrials % 10000 == 0: print ('ntrials,nback',ntrials,nback)
    #
    #     # we're on a new open cell
    #     if state == NEW_CELL:
    #         guess,forced = nextValidGuess(board,cell,1)
    #         #print ("NEW_CELL,cell,guess,forced",cell,guess,forced)
    #         if not guess:
    #             # failed to find a valid guess for this cell, backtrack
    #             state = BACKTRACK
    #         else:
    #             board[cell] = guess
    #             if not forced:
    #                 mystack.push([cell,board[:]])
    #             state = FIND_NEXT_CELL
    #         continue
    #
    #     # find a new open cell
    #     if state == FIND_NEXT_CELL:
    #         cell = nextOpenCell(board,cell)
    #         if not cell:
    #             # Solution!
    #             break
    #         state = NEW_CELL
    #         continue
    #
    #     # backtrack
    #     if state == BACKTRACK:
    #         nback += 1
    #         cell,board = mystack.pop()
    #         old_guess = board[cell]
    #         guess,forced = nextValidGuess(board,cell,old_guess+1)  # note: state cannot be forced
    #         #print('BACKTRACK,cell,guess,forced',cell,guess,forced)
    #         if not guess:
    #             state = BACKTRACK
    #         else:
    #             board[cell] = guess
    #             mystack.push([cell,board[:]])
    #             state = FIND_NEXT_CELL
    #         continue
    #
    # print ('Solution!, with ntrials, backtracks: ', ntrials,nback)
    # printBoard(board)
    # writeBoard(argv,name,board)
