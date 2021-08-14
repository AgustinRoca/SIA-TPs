from not_informed_searches import BFS, DFS
from time import time


def run():
    # game = Game()
    # game.parse_board()
    # game.show_board()
    # while True:
    #     i = input()
    #     if i == 'w':
    #         game.move(Direction.UP)
    #     elif i == 's':
    #         game.move(Direction.DOWN)
    #     elif i == 'd':
    #         game.move(Direction.RIGHT)
    #     elif i == 'a':
    #         game.move(Direction.LEFT)
    #     game.show_board()
    #     if game.has_won():
    #         print('Congratulations, you won!')
    #         return

    # bfs = BFS()
    # t0 = time()
    # final_state = bfs.process()
    # t1 = time()
    # print(t1 - t0)
    # print(final_state.moves)

    dfs = DFS()
    t0 = time()
    final_state = dfs.process()
    t1 = time()
    print(t1 - t0)
    print(final_state.moves)
    print(final_state)


if __name__ == '__main__':
    run()
