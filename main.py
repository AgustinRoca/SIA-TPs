from not_informed_searches import BFS, DFS
from game.game import Game, Direction
from time import time
from output_tester import OutputTester


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

    # print('BFS')
    # bfs = BFS()
    # t0 = time()
    # final_state = bfs.process()
    # t1 = time()
    # print(t1 - t0)
    # print(final_state.moves)

    print('DFS')
    dfs = DFS()
    t0 = time()
    final_state = dfs.process()
    t1 = time()
    print(t1 - t0)
    print(final_state.moves)
    print(final_state)
    # ot = OutputTester('lluuuulldldlddrrruruuurrddddrluuuulldddlddruuuuddddlullluurururrddddrruuuullddddrruuuurrdddrddluuuuddddrurrruululullddddlluuuulldddddlullluurururldldlddrrrururruurlddddlluldllluurururrddddrruuuullddddrruuuurrddddlluuuulldddddlullluurururldldlddrrrururruurrdddddrurrruulululllrddddlluuuuudddddlluldllluurururrrlddddrruuuu')
    # ot.test()


if __name__ == '__main__':
    run()
