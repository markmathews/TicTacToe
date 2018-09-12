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
        while True:  # size input loop
            try:
                N = int(input('Enter board size, N: '))
                if N < MIN_BOARD_SIZE or N > MAX_BOARD_SIZE:
                    raise ValueError()
                break
            except ValueError:
                print('N must be an integer between {} and {}\n'
                      .format(MIN_BOARD_SIZE, MAX_BOARD_SIZE))
        game = TicTacToe(board_size=N)
        while True:  # game loop
            while True:  # input move loop
                try:
                    m, n = map(int,
                               input('Enter move position as m<space>n: ')
                               .split())
                    break
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
