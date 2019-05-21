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
        self.test_index = 0

    def __str__(self):
        return "Win_x: " + str(self.win_x) + ", win_o: " + str(self.win_o) + ", draw: " + str(self.draw)

    def count_games_total(self, board, mark):
        # printBoard(board)
        # if self.test_index==0:
        #     print("start count_games_total")
        #     printBoard(board)
        #     print("----------------------------")
        #     self.test_index+=1
        count = 0
        for i in range(9):
            # if self.test_index==1:
            #     print("for i in range(9)")
            #     printBoard(board)
            #     print("----------------------------")
            # printBoard(board)
            if board[i]=='_':
                # if self.test_index==1:
                #     print("board[i]=='_'")
                #     printBoard(board)
                #     print("----------------------------")
                #     self.test_index+=1
                board[i] = mark
                # if self.test_index==2:
                #     print("board[i]=mark")
                #     printBoard(board)
                #     print("----------------------------")
                #     self.test_index+=1
                not_win=True
                for clique in cliques:
                    if i in clique and not_win:
                        num_filled=0
                        # print("clique: ", clique)
                        for spot in clique:
                            # if self.test_index==3:
                            #     print("for spot in clique")
                            #     printBoard(board)
                            #     print("i: ", i)
                            #     print("spot: ", spot)
                            #     print("board[spot]: ", board[spot])
                            #     print("mark: ", mark)
                            #     print("----------------------------")
                            #     self.test_index+=1
                            # print(i, spot, board[spot], mark)
                            if board[spot]==mark:
                                num_filled+=1
                        # print("num_filled: ", num_filled)
                        if num_filled>2:
                            if mark==1:
                                self.win_x+=1
                                # print("Win X")
                                # printBoard(board)
                                # print("----------------------------")
                            else:
                                self.win_o+=1
                                # print("Win O")
                                # printBoard(board)
                                # print("----------------------------")
                            # print("Mark: ", mark)
                            # printBoard(board)
                            count+=1
                            not_win=False
                count+=self.count_games_total(board[:],1-mark)
                board[i]='_'
        if not '_' in board:
            self.draw+=1
            # if self.test_index==4:
            # print("Draw")
            # printBoard(board)
            # print("Mark: ", mark)
            # print("----------------------------")
                # self.test_index=0
            return 1
        else:
            return count

def count_games(board, mark):
    # printBoard(board)
    count = 0
    while '_' in board:
        printBoard(board)
        i=0
        while i<9:
            # printBoard(board)
            if board[i]=='_':
                # print("Mark: ", mark)
                # print("Before")
                # printBoard(board)
                board = board[:i] + str(mark) + board[i+1:]
                # print("After")
                # printBoard(board)
                for clique in cliques:
                    # print("Clique: ", clique)
                    if i in clique:
                        num_filled=0
                        # print("clique: ", clique)
                        for spot in clique:
                            # print(i, spot, board[spot], mark)
                            if board[spot]==str(mark):
                                num_filled+=1
                        # print("num_filled: ", num_filled)
                        if num_filled>2:
                            # if mark>0:
                            #     self.win_x+=1
                            # else:
                            #     self.win_o+=1
                            # print("Mark: ", mark)
                            # print("Win")
                            # printBoard(board)
                            return count+1
                count+=count_games(board,1-mark)
                # if not i==8:
                # print("i: ", i)
                board = board[:i] + '_' + board[i+1:]
                # printBoard(board)
            i+=1
        board = board[:i-1] + str(mark) + board[i:]
    # for i in range(9):
    #     if board[i]
    # self.draw+=1
    # print("Mark: ", mark)
    # print("Draw")
    # printBoard(board)
    return count+1

def main():
    game = TicTacToe()
    board = ['_' for x in range(9)]
    # print(game)
    print("Total number of games: ", game.count_games_total(board, 1))
    print(game)
    #printBoard(board)
    # board = "_________"
    # print("Total number of games 2: ", count_games(board,1))

main()
