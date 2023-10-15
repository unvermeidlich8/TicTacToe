class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def draw_board(self):
        print('-------------')
        for i in range(3):
            print('|', self.board[i * 3], '|', self.board[i * 3 + 1], '|', self.board[i * 3 + 2], '|')
            print('-------------')

    def check_move(self, position):


