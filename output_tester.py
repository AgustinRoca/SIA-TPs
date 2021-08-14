from game.game import Game, Direction


class OutputTester:
    def __init__(self, sequence=None):
        self.sequence = sequence
        self.game = Game()
        self.game.parse_board()

    def test(self):
        if self.sequence is None:
            print('Sequence can\'t be None')
            return

        print('Starting board:')
        self.game.show_board()
        i = 0

        for c in self.sequence:
            print('Move ' + str(i) + ' - ' + c + ':')

            if c == 'u':
                self.game.move(Direction.UP)
            elif c == 'd':
                self.game.move(Direction.DOWN)
            elif c == 'l':
                self.game.move(Direction.LEFT)
            elif c == 'r':
                self.game.move(Direction.RIGHT)

            i += 1

            self.game.show_board()
