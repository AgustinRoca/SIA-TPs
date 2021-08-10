from game.game import Game, Direction


def run():
    game = Game()
    game.parse_board()
    game.show_board()
    while True:
        i = input()
        if i == 'w':
            game.move(Direction.UP)
        elif i == 's':
            game.move(Direction.DOWN)
        elif i == 'a':
            game.move(Direction.LEFT)
        elif i == 'd':
            game.move(Direction.RIGHT)
        game.show_board()
        if game.has_won():
            print('Congratulations, you won!')
            return


if __name__ == '__main__':
    run()
