import time

''' Layout positions:
0 1 2
3 4 5
6 7 8
'''
# layouts look like "_x_ox__o_"

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode

class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None
        self.parents = [] # all layouts that can lead to this one, by one move
        self.children = [] # all layouts that can be reached with a single move

    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        print ('parents:',self.parents)
        print ('children:',self.children)

def CreateAllBoards(layout,parent):
    # recursive function to manufacture all BoardNode nodes and place them into the AllBoards dictionary
    AllBoards[layout] = BoardNode(layout)
    # print(layout)

    if not '_' in layout:
        AllBoards[layout].endState = 'd'

    if not parent==None and layout.count('x')>parent.count('x'):
        mark = 'o'
    else:
        mark = 'x'

    for clique in Wins:
        num_filled=0
        if not layout[clique[0]]=='_':
            temp = layout[clique[0]]
            for spot in clique:
                if layout[spot]==temp:
                    num_filled+=1
            if num_filled>2:
                if mark=='x':
                    AllBoards[layout].endState = 'o'
                else:
                    AllBoards[layout].endState = 'x'
                for i in range(9):
                    if not layout[i]=='_':
                        AllBoards[layout].parents.append(''.join([layout[:i],'_',layout[i+1:]]))
                return

    for i in range(9):
        if layout[i]=='_':
            AllBoards[layout].children.append(''.join([layout[:i],mark,layout[i+1:]]))
            CreateAllBoards(AllBoards[layout].children[-1],layout)
        else:
            AllBoards[layout].parents.append(''.join([layout[:i],'_',layout[i+1:]]))

    return

def main():
    start = time.time()
    CreateAllBoards('_________', None)
    end = time.time()-start
    print("Runtime: ", round(end,2))
    print("Len of AllBoards: ", len(AllBoards))
    num_children = 0
    num_xs = 0
    num_os = 0
    num_ds = 0
    num_nones = 0
    for board in AllBoards:
        num_children+=len(AllBoards[board].children)
        if AllBoards[board].endState=='x':
            num_xs+=1
        elif AllBoards[board].endState=='o':
            num_os+=1
        elif AllBoards[board].endState=='d':
            num_ds+=1
        else:
            num_nones+=1
    print("num_children: ", num_children)
    print("num_xs: ", num_xs)
    print("num_os: ", num_os)
    print("num_ds: ", num_ds)
    print("num_nones: ", num_nones)

main()
