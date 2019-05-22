#Anton Danylenko
#05/15/19

# A): Number of Games=255168
# B1): X Wins=131184
# B2): O Wins=77904
# B3): Draws=46080
# C): Number of Intermediate+Final Boards=5478
# D): Number of Unique Boards=765

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
        self.all_boards = set([])
        self.unique_boards = set([])

    def __str__(self):
        return "Win_x: " + str(self.win_x) + ", win_o: " + str(self.win_o) + ", draw: " + str(self.draw) + \
               "\nNum All Boards: " + str(len(self.all_boards)) + ", Num Unique Boards: " + str(len(self.unique_boards))

    def addBoardToList(self, board):
        # print(board)
        possibilities = [board[:]]
        # print(list(reversed(board[:3]))+(list(reversed(board[3:6]))))
        possibilities.append(list(reversed(board[:3]))+(list(reversed(board[3:6])))+(list(reversed(board[6:]))))
        possibilities.append(list(reversed(board[6:]))+(list(reversed(board[3:6])))+(list(reversed(board[:3]))))
        possibilities.append(board[6:]+board[3:6]+board[:3])
        temp = [board[6]]+[board[3]]+[board[0]]+[board[7]]+[board[4]]+[board[1]]+[board[8]]+[board[5]]+[board[2]]
        possibilities.append(temp[:])
        possibilities.append(list(reversed(temp[:3]))+(list(reversed(temp[3:6])))+(list(reversed(temp[6:]))))
        possibilities.append(list(reversed(temp[6:]))+(list(reversed(temp[3:6])))+(list(reversed(temp[:3]))))
        possibilities.append(temp[6:]+temp[3:6]+temp[:3])
        for b in possibilities:
            if str(b) in self.unique_boards:
                return
        else:
            self.unique_boards.add(str(board))
        return

    def count_games_total(self, board, mark):
        count = 0
        self.all_boards.add(str(board))
        self.addBoardToList(board)
        for i in range(9):
            if board[i]=='_':
                board[i] = mark
                self.all_boards.add(str(board))
                self.addBoardToList(board)
                not_win=True
                for clique in cliques:
                    if not_win and i in clique:
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
    print("Total number of games: ", game.count_games_total(board, 1))
    print(game)
    # board = [0,1,2,3,4,5,6,7,8]
    # possibilities = [board[:]]
    # # print(list(reversed(board[:3]))+(list(reversed(board[3:6]))))
    # possibilities.append(list(reversed(board[:3]))+(list(reversed(board[3:6])))+(list(reversed(board[6:]))))
    # possibilities.append(list(reversed(board[6:]))+(list(reversed(board[3:6])))+(list(reversed(board[:3]))))
    # possibilities.append(board[6:]+board[3:6]+board[:3])
    # temp = [board[6]]+[board[3]]+[board[0]]+[board[7]]+[board[4]]+[board[1]]+[board[8]]+[board[5]]+[board[2]]
    # possibilities.append(temp[:])
    # possibilities.append(list(reversed(temp[:3]))+(list(reversed(temp[3:6])))+(list(reversed(temp[6:]))))
    # possibilities.append(list(reversed(temp[6:]))+(list(reversed(temp[3:6])))+(list(reversed(temp[:3]))))
    # possibilities.append(temp[6:]+temp[3:6]+temp[:3])
    # print(possibilities)


main()
