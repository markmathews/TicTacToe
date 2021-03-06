"""Tic Tac Toe game implementation in Python 3"""

import numpy as np
import itertools


class TicTacToe:
    """
    Represents game state and score for 2 players using:
        ' ' for empty square,
        'X' for player 1,
        'O' for player 2
    """
    def __init__(self, board_size=3):
        self.default_cell_value = ' '  # single char as placeholder
        self.markers = ('X', 'O')
        self.board_size = board_size
        self.dash_length = 4 * self.board_size - 1
        self.max_moves = self.board_size ** 2
        self.showGameTitle()
        self.showHelp()
        self.newGame(reset_scores=True)

    def showGameTitle(self):
        print(
            ' _____ _     _____         _____          \n'
            '|_   _(_) __|_   _|_ _  __|_   _|__   ___\n'
            '  | | | |/ __|| |/ _` |/ __|| |/ _ \\ / _ \\\n'
            '  | | | | (__ | | (_| | (__ | | (_) |  __/\n'
            '  |_| |_|\\___||_|\\__,_|\\___||_|\\___/ \\___|\n')

    def showHelp(self):
        help_msg = '\n'.join(['Methods',
                              '-' * self.dash_length,
                              'playMove(m, n)\n'
                              '    '
                              'Place next player\'s move on this square',
                              'newGame(reset_scores=False)\n'
                              '    '
                              'Start a new game, optionally reset both'
                              ' player scores',
                              'showScores()\n'
                              '    '
                              'Show player scores\n'])
        print(help_msg)

    def newGame(self, reset_scores=False):
        if reset_scores:
            self.player_scores = np.array([0, 0], dtype=float)
        self.board_state = np.full((self.board_size, self.board_size),
                                   self.default_cell_value)
        self.num_moves = 0
        self.game_over = False
        self.displayBoard()

    def playMove(self, m, n, show_board_after=True):
        """Execute move if possible"""
        if not self.game_over:
            if m in range(self.board_size) and n in range(self.board_size):
                if self.board_state[m, n] != self.default_cell_value:
                    print('That square has already been marked\n')
                    # return False
                else:
                    marker = self.markers[self.num_moves % 2]
                    self.board_state[m, n] = marker
                    self.num_moves += 1
                    if show_board_after:
                        self.displayBoard()
                    self._updateGameStatus()  # check if either player won
                    # return True
            else:
                print('Invalid position\n')
        else:
            print('Game over, start a new one\n')
            # return False

    def showScores(self):
        score_msg = '\n'.join(['Scores', '-' * self.dash_length,
                               'Player 1: {}'.format(self.player_scores[0]),
                               'Player 2: {}\n'.format(self.player_scores[1])
                               ])
        print(score_msg)

    def _updateGameStatus(self):
        """Check whether either player has won"""
        def _checkLine(arr):
            """Check whether all values in arr are the same"""
            if self.default_cell_value not in arr:
                all_same = arr == arr[0]
                return False not in all_same
            return False

        def _linesToCheck():
            """Get a list of lists (lines) to check"""
            lines_to_check = []
            # Add rows and columns
            for line in itertools.chain(*[self.board_state,
                                          self.board_state.T]):
                lines_to_check.append(line)
            # Add diagonals
            for diagonal in [np.diagonal(self.board_state),
                             np.diagonal(np.flip(self.board_state, axis=1))]:
                lines_to_check.append(diagonal)
            return lines_to_check

        def _detectGameOver(lines_to_check):
            for line in lines_to_check:
                if _checkLine(line):  # someone has won
                    player_num = self.markers.index(line[0]) + 1
                    print('Player {} wins!\n'.format(player_num))
                    self.player_scores[player_num - 1] += 1
                    self.showScores()
                    self.game_over = True

        _detectGameOver(_linesToCheck())

        if not self.game_over:
            if self.num_moves == self.max_moves - 1:
                empty_square = np.where(
                    self.board_state == self.default_cell_value
                )
                m, n = empty_square
                # play obvious last move
                self.playMove(m, n, show_board_after=False)
            # Check if game drawn
            elif self.num_moves == self.max_moves:
                    print('Draw!\n')
                    self.player_scores += 0.5
                    self.showScores()
                    self.game_over = True
            else:
                print('Next turn: {}\n'
                      .format(self.markers[self.num_moves % 2]))

    def displayBoard(self):
        """Print out board state with formatting"""
        vertical_row = '+' + self.dash_length * '-' + '+\n'
        marker_rows = ['| ' + ' | '.join(row) + ' |\n'
                       for row in self.board_state]
        board = vertical_row + ''.join(marker_rows) + vertical_row
        print(board)
