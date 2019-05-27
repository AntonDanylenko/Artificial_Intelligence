#! /usr/bin/python3

import sys
import time

import re

from flask import (Flask, render_template, redirect, url_for,
                   session, request, flash, get_flashed_messages)

app = Flask(__name__)
app.secret_key = 'ttt3'

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
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None if this board is not final
        self.children = [] # all layouts that can be reached with a single move
        self.best_move = None  # cell position (0-8) of the best move from this layout, or -1 if this is a final layout
        self.moves_to_end = None # how many moves until the end of the game, if played perfectly.  0 if this is a final layout
        self.final_state = None  # expected final state ('x' if 'x' wins, 'o' if 'o' wins, else 'd' for a draw)

def CreateAllBoards(layout):
    # recursive function to manufacture all BoardNode nodes and place them into the AllBoards dictionary
    AllBoards[layout] = BoardNode(layout)
    # print(layout)

    if not '_' in layout:
        AllBoards[layout].endState = 'd'
        AllBoards[layout].best_move = -1
        AllBoards[layout].moves_to_end = 0
        AllBoards[layout].final_state = 'd'
        return

    for clique in Wins:
        num_filled=0
        if not layout[clique[0]]=='_':
            temp = layout[clique[0]]
            for spot in clique:
                if layout[spot]==temp:
                    num_filled+=1
            if num_filled>2:
                if temp=='x':
                    AllBoards[layout].endState = 'x'
                    AllBoards[layout].final_state = 'x'
                else:
                    AllBoards[layout].endState = 'o'
                    AllBoards[layout].final_state = 'o'
                AllBoards[layout].best_move = -1
                AllBoards[layout].moves_to_end = 0
                return

    if layout.count('x')>layout.count('o'):
        mark = 'o'
    else:
        mark = 'x'

    for i in range(9):
        if layout[i]=='_':
            AllBoards[layout].children.append(''.join([layout[:i],mark,layout[i+1:]]))
            CreateAllBoards(AllBoards[layout].children[-1])

    for child in AllBoards[layout].children:
        if AllBoards[child].final_state==mark:
            if AllBoards[layout].moves_to_end==None or AllBoards[child].moves_to_end<AllBoards[layout].moves_to_end-1:
                AllBoards[layout].moves_to_end = AllBoards[child].moves_to_end+1
                AllBoards[layout].final_state = AllBoards[child].final_state
                for i in range(len(layout)):
                    if not layout[i]==AllBoards[child].layout[i]:
                        AllBoards[layout].best_move = i

    if AllBoards[layout].final_state==None:
        for child in AllBoards[layout].children:
            if AllBoards[child].final_state=='d':
                AllBoards[layout].moves_to_end = AllBoards[child].moves_to_end+1
                AllBoards[layout].final_state = AllBoards[child].final_state
                for i in range(len(layout)):
                    if not layout[i]==AllBoards[child].layout[i]:
                        AllBoards[layout].best_move = i

    if AllBoards[layout].final_state==None:
        for child in AllBoards[layout].children:
            if AllBoards[layout].moves_to_end==None or AllBoards[child].moves_to_end>AllBoards[layout].moves_to_end-1:
                AllBoards[layout].moves_to_end = AllBoards[child].moves_to_end+1
                AllBoards[layout].final_state = AllBoards[child].final_state
                for i in range(len(layout)):
                    if not layout[i]==AllBoards[child].layout[i]:
                        AllBoards[layout].best_move = i
    return

def position(index):
    positions=["top-left","top-middle","top-right",
               "middle-left","center","middle-right",
               "bottom-left","bottom-middle","bottom-right"]
    return positions[index]

curr_layout = 'x________'

def getLayout():
    return curr_layout

def setLayout(layout):
    print("CUR: ", curr_layout)
    curr_layout = layout
    return

@app.route('/')
def home():
    '''
    tictactoe time!
    '''
    print("curr_layout: ", curr_layout)
    return render_template('ttt.html', layout=curr_layout)

@app.route('/send_board', methods=['POST'])
def send_board():
    play = int(request.form['play'])
    print("SEND BOARD")
    print("PLAY: ", play)
    curr_layout = getLayout()
    if play>0 and play<10 and curr_layout[play-1]=='_':
        new_board = ''.join([curr_layout[:play-1],'o',curr_layout[play:]])
    else:
        flash("Can't place o there!")
        return redirect(url_for('home'))
    print("curr_layout: ", curr_layout)
    CreateAllBoards(new_board)
    setLayout(''.join([AllBoards[new_board].layout[:AllBoards[new_board].best_move],'x',AllBoards[new_board].layout[AllBoards[new_board].best_move+1:]]))
    print("curr_layout: ", curr_layout)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.debug = True
    app.run()
