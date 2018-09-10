from tictactoe import TicTacToe

if __name__ == "__main__":
    game = TicTacToe()
    while True:
        invalid_input = True
        while invalid_input:
            try:
                print('Enter move position as m n: ')
                m, n = map(int, input().split())
                invalid_input = False
            except Exception as e:
                print('Invalid input: {}\n'.format(e))
        game.playMove(m, n)
        if game.game_over:
            print('Starting new game...\n')
            game.newGame()
