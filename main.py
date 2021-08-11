from not_informed_searches import Bfs
from game.game import Game, Direction


def run():
    bfs = Bfs()
    final_state = bfs.process()
    print(final_state.moves)
    # l = []
    # for i in range(0, 100):
    #     l.append(i)
    #
    # print(l)
    #
    # while len(l) > 0:
    #     print(l.pop(0))


if __name__ == '__main__':
    run()
