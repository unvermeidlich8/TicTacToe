import sys

from behave import given, when, then
from io import StringIO
from unittest.mock import patch

from main import TicTacToe


@given('an empty board')
def step_given_empty_board(context):
    context.game = TicTacToe()
    context.game.board = [' '] * 9


@when('we draw the board')
def step_when_draw_board(context):
    capture_output = StringIO()
    context.orig_stdout = sys.stdout
    sys.stdout = capture_output
    context.game.draw_board()
    sys.stdout = context.orig_stdout
    context.output = capture_output.getvalue().strip()


@then('we expect the following output')
def step_then_expect_output(context):
    expected_output = context.text
    assert context.output == expected_output


@given('a TicTacToe game')
def step_given_TicTacToe_game(context):
    context.game = TicTacToe()


@when('player makes a valid move')
@patch('builtins.input', side_effect=['1'])
def step_when_make_valid_move(context, mock_input):
    context.game.make_a_move()


@then('we expect the board to be updated correctly')
def step_then_expect_updated_board(context):
    expected_board = list(context.table.headings[0])
    assert context.game.board == expected_board


@when('player makes invalid moves')
@patch('builtins.input', side_effect=['9', '9', '9', '1'])
def step_when_make_invalid_moves(context, mock_input):
    context.game.make_a_move()


@given('a TicTacToe game with a winning state')
def step_given_TicTacToe_game_winning_state(context):
    context.game = TicTacToe()
    context.game.board = ['O', 'X', 'O',
                          'O', 'X', 'O',
                          ' ', 'X', ' ']


@then('we expect the game to have a winner')
def step_then_expect_winner(context):
    assert context.game.check_winner()


@given('a TicTacToe game with a draw state')
def step_given_TicTacToe_game_draw_state(context):
    context.game = TicTacToe()
    context.game.board = ['X', 'O', 'X',
                          'O', 'X', 'X',
                          'O', 'X', 'O']


@then('we expect the game to end in a draw')
def step_then_expect_draw(context):
    capture_output = StringIO()
    context.orig_stdout = sys.stdout
    sys.stdout = capture_output
    context.game.play_game()
    sys.stdout = context.orig_stdout
    output = capture_output.getvalue().split('\n')
    expected_output = context.text.strip()

    assert output[len(output) - 2] == expected_output