#! /usr/bin/python3

import sudoku_smart
import random
import os

class MyStack2:
    def __init__(self, cells = [], list = [], available = []):
        self.cells = cells
        self.stack = list
        self.available = available

    def __str__(self):
        return str(self.stack)

    def push(self, args):
        self.cells.append(args[0])
        #print(self.cells)
        self.stack.append(args[1])
        self.available.append(args[2])

    def pop(self):
        #print("cells: " + str(self.cells))
        return [self.cells.pop(len(self.cells)-1), self.stack.pop(len(self.stack)-1), self.available.pop(len(self.available)-1)]

def checkBoard(board):
    for cell_index in range(len(board)):
        num = board[cell_index]
        board[cell_index] = '_'
        if not sudoku_smart.canPlace(board,cell_index,num):
            return False
    return True

def generateFilled():
    board = ['_' for x in range(81)]
    sudoku_smart.makeNeighbors()
    mystackcells = MyStack2()
    row = 0
    nums_list = [1,2,3,4,5,6,7,8,9]
    while row < 9:
        col = 0
        while col < 9:
            cell_index = col+row*9
            while str(board[cell_index]) == '_':
                if len(nums_list)==0:
                        cell_index, board, nums_list = mystackcells.pop()
                        board[cell_index] = '_'
                        col-=1
                else:
                    num = nums_list[random.randint(0,len(nums_list)-1)]
                    nums_list.remove(num)
                    if sudoku_smart.canPlace(board, cell_index, num):
                        board[cell_index] = num
                        mystackcells.push([cell_index,board[:],nums_list])
                        nums_list = [1,2,3,4,5,6,7,8,9]
                # os.system('cls' if os.name == 'nt' else 'clear')
                # printBoard(board)
                # time.sleep(.5)
            col+=1
        row+=1
    sudoku_smart.printBoard(board)
    return board

board = generateFilled()
print(checkBoard(board))
