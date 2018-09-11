import sys

from tictactoe import TicTacToe

MIN_BOARD_SIZE = 3
MAX_BOARD_SIZE = 10

if __name__ == "__main__":
    try:
        assert sys.version_info >= (3, 0)
    except AssertionError:
        print('Please run this script using Python 3.0 or later\n')
    else:
        invalid_input_N = True
        while invalid_input_N:
            try:
                print('Enter board size, N: ')
                N = int(input())
                if N < MIN_BOARD_SIZE or N > MAX_BOARD_SIZE:
                    print('Pick a board size between {} and {}\n'
                          .format(MIN_BOARD_SIZE, MAX_BOARD_SIZE))
                else:
                    invalid_input_N = False
            except ValueError:
                print('N must be an integer\n')
        game = TicTacToe(dimension=N)
        while True:
            invalid_input_move = True
            while invalid_input_move:
                try:
                    print('Enter move position as m<space>n: ')
                    m, n = map(int, input().split())
                    invalid_input_move = False
                except ValueError:
                    print('Invalid input - need two '
                          'space separated integers\n')
                except Exception as e:
                    print('Invalid input: {}\n'.format(e))
            game.playMove(m, n)
            if game.game_over:
                print('Start new game? [Y/n]')
                start_new_game = input()
                if start_new_game.lower() == 'y':
                    print('\nStarting new game...\n')
                    game.newGame()
                else:
                    print('\nThank you for playing!')
                    break
