from game.game import Game


def run():
    game = Game()
    game.parseBoard()
    game.showBoard()
    game.moveUp()
    game.showBoard()


if __name__ == '__main__':
    run()
