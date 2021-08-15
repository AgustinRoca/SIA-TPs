from not_informed_searches import BFS, DFS
from time import time
from output_tester import OutputTester
from game.game import Game, Direction


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

    print('BFS')
    bfs = BFS()
    t0 = time()
    final_state = bfs.process()
    t1 = time()
    print(t1 - t0)
    print(final_state.moves)
    # ot = OutputTester('lrrluulldlddruuuudddlllluurururrrlddrruuudddrrdrddluuuudddrrrruulululllrddlluu')
    # ot.test()

    # dfs = DFS()
    # t0 = time()
    # final_state = dfs.process()
    # t1 = time()
    # print(t1 - t0)
    # print(final_state.moves)
    # print(final_state)
    # ot = OutputTester('lluuuulldldlddrrruruuurrddddrluuuulldddlddruuuuddddlullluurururrddddrruuuullddddrruuuurrdddrddluuuuddddrurrruululullddddlluuuulldddddlullluurururldldlddrrrururruurlddddlluldllluurururrddddrruuuullddddrruuuurrddddlluuuulldddddlullluurururldldlddrrrururruurrdddddrurrruulululllrddddlluuuuudddddlluldllluurururrrlddddrruuuu')
    # ot.test()

    # iddfs = IDDFS(320)
    # t0 = time()
    # final_state = iddfs.process()
    # t1 = time()
    # print(t1 - t0)
    # print(final_state.moves)
    # print(final_state)
    # # ot = OutputTester('lluuuulldldlddrrruruuurrddddrluuuulldddlddruuuuddddlullluurururrddddrruuuullddddrruuuurrdddrddluuuudddrrrruulululllrddlluuudddddlllllluurururrrlddrruu')
    # # ot.test()


if __name__ == '__main__':
    run()
