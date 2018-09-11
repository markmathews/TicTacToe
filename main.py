import sys

from tictactoe import TicTacToe

if __name__ == "__main__":
    try:
        assert sys.version_info >= (3, 0)
    except AssertionError:
        print('Please run this script using Python 3.0 or later')
    else:
        game = TicTacToe()
        while True:
            invalid_input = True
            while invalid_input:
                try:
                    print('Enter move position as m<space>n: ')
                    m, n = map(int, input().split())
                    invalid_input = False
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
