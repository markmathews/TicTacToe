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
    def __init__(self):
        self.default_cell_value = ' '  # single char as placeholder
        self.markers = ('X', 'O')
        self.dash_length = 11
        self.newGame(reset_scores=True)
        self.showHelp()

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
                              'Show player scores'])
        print(help_msg)

    def newGame(self, reset_scores=False):
        if reset_scores:
            self.player_scores = [0, 0]
        self.board_state = np.full((3, 3), self.default_cell_value)
        self.num_moves = 0
        self.game_over = False
        self.displayBoard()

    def playMove(self, m, n):
        """Execute move if possible"""
        if not self.game_over:
            if m in range(3) and n in range(3):
                if self.board_state[m, n] != self.default_cell_value:
                    print('That square has already been marked')
                    # return False
                else:
                    marker = self.markers[self.num_moves % 2]
                    self.board_state[m, n] = marker
                    self.num_moves += 1
                    self.displayBoard()
                    self._updateGameStatus()  # check if either player won
                    # return True
            else:
                print('Invalid position')
        else:
            print('Game over, start a new one')
            # return False

    def showScores(self):
        score_msg = '\n'.join(['Scores', '-' * self.dash_length,
                               'Player 1: {}'.format(self.player_scores[0]),
                               'Player 2: {}'.format(self.player_scores[1])
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

        # Get lines to check
        lines_to_check = _linesToCheck()

        # Check lines
        for line in lines_to_check:
            if _checkLine(line):  # someone has won
                player_num = self.markers.index(line[0]) + 1
                print('Player {} wins!\n'.format(player_num))
                self.player_scores[player_num - 1] += 1
                self.showScores()
                self.game_over = True

    def displayBoard(self):
        """Print out board state with formatting"""
        vertical_row = '+' + self.dash_length * '-' + '+\n'
        marker_rows = ['| ' + ' | '.join(row) + ' |\n'
                       for row in self.board_state]
        board = vertical_row + ''.join(marker_rows) + vertical_row
        print(board)
