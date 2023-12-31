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

    def make_a_move(self):
        pos = int(input(f"Player {self.current_player}, please choose position (0-8): "))
        if self.check_move(pos):
            self.board[pos] = self.current_player
        else:
            self.make_a_move()

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == self.current_player:
                return True
        return False

    def play_game(self):
        self.draw_board()

        while True:
            self.make_a_move()
            self.draw_board()

            if self.check_winner():
                print(f"Player {self.current_player} won!")
                break

            if ' ' not in self.board:
                print("Draw!")
                break

            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'



