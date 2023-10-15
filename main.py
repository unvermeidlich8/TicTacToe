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
        if not (0 <= position < 9):
            print("Invalid position, please choose number between 0 and 8")
            return False
        if self.board[position] != ' ':
            print("This position is already taken. Please choose another position")
            return False
        return True
