#Anton Danylenko
#05/15/19

# A): Number of Games=255168
# B1): X Wins=131184
# B2): O Wins=77904
# B3): Draws=46080
# # Intermediate boards (C): 5478
# # Board Families (D): 765

cliques = [
[0,1,2], [3,4,5], [6,7,8],
[0,3,6], [1,4,7], [2,5,8],
[0,4,8], [2,4,6]
]

def printBoard(board):
    for i in range(3):
        row = ""
        for ii in range(3):
            if board[i*3+ii]==1:
                row+='x '
            elif board[i*3+ii]==0:
                row+='o '
            else:
                row+='_ '
        print(row)
    # print("--------------------")

class TicTacToe:
    def __init__(self):
        self.win_x = 0
        self.win_o = 0
        self.draw = 0
        self.boards = set([])

    def __str__(self):
        return "Win_x: " + str(self.win_x) + ", win_o: " + str(self.win_o) + ", draw: " + str(self.draw) + \
               ", Num Boards: " + str(len(self.boards))

    def count_games_total(self, board, mark):
        count = 0
        for i in range(9):
            if board[i]=='_':
                board[i] = mark
                not_win=True
                for clique in cliques:
                    if i in clique and not_win:
                        num_filled=0
                        for spot in clique:
                            if board[spot]==mark:
                                num_filled+=1
                        if num_filled>2:
                            if mark==1:
                                self.win_x+=1
                            else:
                                self.win_o+=1
                            count+=1
                            not_win=False
                if not_win:
                    count+=self.count_games_total(board[:],1-mark)
                board[i]='_'
        if not '_' in board:
            self.draw+=1
            count+=1
        return count

    def count_orientations(self, board, mark):
        count = 0
        for i in range(9):
            if board[i]=='_':
                board[i] = mark
                if not str(board) in self.boards:
                    self.boards.add(str(board))
                not_win=True
                for clique in cliques:
                    if i in clique and not_win:
                        num_filled=0
                        for spot in clique:
                            if board[spot]==mark:
                                num_filled+=1
                        if num_filled>2:
                            if mark==1:
                                self.win_x+=1
                            else:
                                self.win_o+=1
                            count+=1
                            not_win=False
                if not_win:
                    count+=self.count_games_total(board[:],1-mark)
                board[i]='_'
        if not '_' in board:
            self.draw+=1
            count+=1
        return count

def main():
    game = TicTacToe()
    board = ['_' for x in range(9)]
    # print("Total number of games: ", game.count_games_total(board, 1))
    # print(game)
    game.count_orientations(board,1)
    print(game)


main()
