import sys
import unittest
from io import StringIO

from main import TicTacToe


class TicTacToeTest(unittest.TestCase):
    def test_create_empty_board(self):
        game = TicTacToe()
        expected_board = [' '] * 9
        self.assertEqual(game.board, expected_board)


    def test_draw_board(self):
        game = TicTacToe()
        game.board = ['X', 'O', 'X', 'O', ' ', ' ', ' ', ' ', ' ']
        expected_output = '''-------------
| X | O | X |
-------------
| O |   |   |
-------------
|   |   |   |
-------------'''

        capture_output = StringIO()
        sys.stdout = capture_output
        game.draw_board()
        sys.stdout = sys.__stdout__
        output = capture_output.getvalue().strip()
        print(output)
        self.assertEqual(output, expected_output)


    def test_check_move(self,position):




if __name__ == '__main__':
    unittest.main()
