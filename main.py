from game.game import Game


def run():
    game = Game()
    game.parseBoard()
    game.showBoard()
    while True:
        i = input()
        if i == 'w':
            game.moveUp()
        elif i == 's':
            game.moveDown()
        elif i == 'd':
            game.moveRight()
        elif i == 'a':
            game.moveLeft()
        game.showBoard()
        if game.hasWon():
            print('Congratulations, you won!')
            return


if __name__ == '__main__':
    run()
