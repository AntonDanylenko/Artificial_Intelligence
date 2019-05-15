#Anton Danylenko
#05/15/19

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
            elif board[i*3+ii]==-1:
                row+='o '
            else:
                row+='_ '
        print(row)
    print("--------------------")

class TicTacToe:
    def __init__(self):
        self.win_x = 0
        self.win_o = 0
        self.draw = 0

    def __str__(self):
        return "Win_x: " + str(self.win_x) + ", win_o: " + str(self.win_o) + ", draw: " + str(self.draw)

    def count_games_total(self, board, mark):
        # printBoard(board)
        count = 0
        for i in range(9):
            # printBoard(board)
            if board[i]=='_':
                board[i] = mark
                for clique in cliques:
                    if i in clique:
                        num_filled=0
                        # print("clique: ", clique)
                        for spot in clique:
                            # print(i, spot, board[spot], mark)
                            if board[spot]==mark:
                                num_filled+=1
                        # print("num_filled: ", num_filled)
                        if num_filled>2:
                            if mark>0:
                                self.win_x+=1
                            else:
                                self.win_o+=1
                            # print("Mark: ", mark)
                            # printBoard(board)
                            return count+1
                count+=self.count_games_total(board[:],0-mark)
                board[i]='_'
        self.draw+=1
        # print("Mark: ", mark)
        # printBoard(board)
        return count+1

def count_games(board, mark):
    # printBoard(board)
    count = 0
    i=0
    while i<9:
        # printBoard(board)
        if board[i]=='_':
            board[i] = mark
            for clique in cliques:
                if i in clique:
                    num_filled=0
                    # print("clique: ", clique)
                    for spot in clique:
                        # print(i, spot, board[spot], mark)
                        if board[spot]==mark:
                            num_filled+=1
                    # print("num_filled: ", num_filled)
                    if num_filled>2:
                        # if mark>0:
                        #     self.win_x+=1
                        # else:
                        #     self.win_o+=1
                        # print("Mark: ", mark)
                        # printBoard(board)
                        return count+1
            count+=count_games(board[:],0-mark)
            # if not i==8:
            # print("i: ", i)
            board[i]='_'
            i+=1
    # for i in range(9):
    #     if board[i]
    # self.draw+=1
    # print("Mark: ", mark)
    # printBoard(board)
    return count+1

def main():
    # game = TicTacToe()
    # board = ['_' for x in range(9)]
    # print(game)
    # print("Total number of games: ", game.count_games_total(board, 1))
    # print(game)
    #printBoard(board)
    board = ['_' for x in range(9)]
    print("Total number of games 2: ", count_games(board,1))

main()
