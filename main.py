from game.informed.AStar import AStar
from game.informed.GGS import GGS
from game.informed.heuristics import heuristic_completed_boxes
from game.not_informed.BFS import BFS
from game.not_informed.DFS import DFS
from game.not_informed.IDDFS import IDDFS
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

    print('BFS')
    bfs = BFS()
    t0 = time()
    final_state = bfs.process()
    t1 = time()
    print("{:.2f}s".format(t1 - t0))
    print(final_state)
    # ot = OutputTester('lrrluulldlddruuuudddlllluurururrrlddrruuudddrrdrddluuuudddrrrruulululllrddlluu')
    # ot.test()
    print()

    print('DFS')
    dfs = DFS()
    t0 = time()
    final_state = dfs.process()
    t1 = time()
    print("{:.2f}s".format(t1 - t0))
    print(final_state)
    # ot = OutputTester('rrrrlllllrrruulllldldrrrrllllllluurururrrrrrrrdrdrddlruulululllllllldldlddrrrrrruurrdrdrlllruulllldldllluurururrrrrrrrdrdrddlruulululllllllldldlddrrrrrrrllllllluurururrrrrrdddrddlurrlllllllllluurururrrrrrrrdrdrddllrruulululllllllldldlddrrrrrrrrudrrlllllllllluurururrrrrrrrdrdrddlllrrruululullddlllldldllluurururrrrrrrrdrdrddlllllrurdrrruulululllllllldldlddrrrrrrlllllluurururrrrrrrrdrdrddlllululllldldllluurururrrrrrrrdrdrddlllllrrrrruulululllllllldldlddrrrrrrrrrrlllllllllluurururrrrrrrrdrdrddlllrrruulululllllllldldlddrrrruurrrrudlllldldllluurururrrrrrlllllldldlddrrrrrruurrdrdrrruulululrdrdrddllllrrrruululullrrdrdrddlllllrrrrruulululllrrrdrdrddllllllrrrrrruululullllrrrrdrdrddlllllllrrrrrrruulululllllrrrrrdrdrddlllllluulldldrrrrrrrlllllllllluurururrrrlllldldlddrrrrrrrruuuurrdrdrddlruulululllrrrdrdrddllrruululullllrrrrdrdrddlllrrruulululllllrrrrrdrdrddllllrrrruululullllllrrrrrrdrdrddlllllrrrrruulululllllldddldllluurururrrrrrlllllldldlddrrrrrrrllllllluurururrrrrrdddrddlurrrruulululrdrdrddllllurdrrruululullrrdrdrddlllllllllllluurururrrrrrlllllldldlddrrrrrrrruullllddrrrrrrrruulululllrrrdrdrddlllllllllllluurururrddrrrrudllllddrrrrrrrruululullrrdrdrddlllllllllllluurururrddrruurrlllllldldlddrrrrrrrrrrrruulululllllrudrrrrdrdrddlllllllllllluurururrrrrrlllllldldlddrrrrrrrrrrrruulululllrrrdrdrddlllllllluurruu')
    # ot.test()
    print()

    print('IDDFS')
    iddfs = IDDFS(50)
    t0 = time()
    final_state = iddfs.process()
    t1 = time()
    print("{:.2f}s".format(t1 - t0))
    print(final_state.moves)
    print(final_state)
    # ot = OutputTester('rllruurrdrddluuuuddrdrrruulululllrddlluuudlldddlddruuuuddldllluurururrrlddrruu')
    # ot.test()
    print()

    print('GGS')
    ggs = GGS(heuristic=heuristic_completed_boxes)
    t0 = time()
    final_state = ggs.process()
    t1 = time()
    print("{:.2f}s".format(t1 - t0))
    print(final_state.moves)
    print(final_state)
    # ot = OutputTester('rllruurrdrddluuuuddrdrrruulululllrddlluuudlldddlddruuuuddldllluurururrrlddrruu')
    # ot.test()
    print()

    print('A*')
    a_star = AStar(heuristic=heuristic_completed_boxes)
    t0 = time()
    final_state = a_star.process()
    t1 = time()
    print("{:.2f}s".format(t1 - t0))
    print(final_state.moves)
    print(final_state)
    # ot = OutputTester('rllruurrdrddluuuuddrdrrruulululllrddlluuudlldddlddruuuuddldllluurururrrlddrruu')
    # ot.test()
    print()


if __name__ == '__main__':
    run()
