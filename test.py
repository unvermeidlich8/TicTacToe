import unittest

from main import TicTacToe


class TicTacToeTest(unittest.TestCase):
    def test_create_empty_board(self):
        game = TicTacToe()
        expected_board = [' '] * 9
        self.assertEqual(game.board, expected_board)




if __name__ == '__main__':
    unittest.main()
