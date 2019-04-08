import * from stack

class Sudoku:
    def __init__(self, fileName):
        self.boards = Stack()
        f = open(fileName, "r")
        df = f.read()
        
