import sys
import unittest
from unittest.mock import patch
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

    def test_check_move(self):
        game = TicTacToe()

        # Проверка допустимого хода
        self.assertTrue(game.check_move(0))
        self.assertTrue(game.check_move(4))

        # Проверка недопустимого хода из-за некорректной позиции
        self.assertFalse(game.check_move(-1))
        self.assertFalse(game.check_move(9))

    def setUp(self):
        self.game = TicTacToe()
        self.game.current_player = 'X'
        self.game.board = [' '] * 9

    @patch('builtins.input', side_effect=['1'])
    def test_make_a_move_valid(self, mock_input):
        self.game.make_a_move()
        expected_board = [' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(self.game.board, expected_board)

    @patch('builtins.input', side_effect=['9', '9', '9', '1'])
    def test_make_a_move_with_invalid_positions(self, mock_input):
        self.game.make_a_move()
        expected_board = [' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(self.game.board, expected_board)


    def test_check_winner(self):


if __name__ == '__main__':
    unittest.main()
