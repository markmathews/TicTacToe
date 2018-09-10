from tictactoe import TicTacToe

if __name__ == "__main__":
    game = TicTacToe()
    while True:
        invalid_input = True
        while invalid_input:
            try:
                ip = map(int, input('Enter move position \'m n\': ').split())
                invalid_input = False
            except Exception as e:
                print('Invalid input: {}'.format(e))
        game.playMove(ip[0], ip[1])
        if game.game_over:
            print('Starting new game...\n')
            game.newGame()
