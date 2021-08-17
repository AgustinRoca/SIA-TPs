from game.informed.AStar import AStar
from game.informed.GGS import GGS
from game.informed.IDAStar import IDAStar
from game.informed.heuristics import heuristic_min_distance_boxes, heuristic_distance_to_closest_goals
from game.not_informed.BFS import BFS
from game.not_informed.DFS import DFS
from game.not_informed.IDDFS import IDDFS
from time import time


# TODO: promedio de varias corridas para tiempos
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
    if final_state is not None:
        print('Success!')
        print('Moves:', final_state.moves)
        print('Expanded nodes:', bfs.expanded_nodes())
        print('Nodes in frontier:', bfs.frontier_size())
        print('Solution:', final_state)
    else:
        print('Failure!')
    print("{:.2f}s".format(t1 - t0))
    # ot = OutputTester('lrrluulldlddruuuudddlllluurururrrlddrruuudddrrdrddluuuudddrrrruulululllrddlluu')
    # ot.test()
    print()

    print('DFS')
    dfs = DFS()
    t0 = time()
    final_state = dfs.process()
    t1 = time()
    if final_state is not None:
        print('Success!')
        print('Moves:', final_state.moves)
        print('Expanded nodes:', dfs.expanded_nodes())
        print('Nodes in frontier:', dfs.frontier_size())
        print('Solution:', final_state)
    else:
        print('Failure!')
    print("{:.2f}s".format(t1 - t0))
    # ot = OutputTester('rrrrlllllrrruulllldldrrrrllllllluurururrrrrrrrdrdrddlruulululllllllldldlddrrrrrruurrdrdrlllruulllldldllluurururrrrrrrrdrdrddlruulululllllllldldlddrrrrrrrllllllluurururrrrrrdddrddlurrlllllllllluurururrrrrrrrdrdrddllrruulululllllllldldlddrrrrrrrrudrrlllllllllluurururrrrrrrrdrdrddlllrrruululullddlllldldllluurururrrrrrrrdrdrddlllllrurdrrruulululllllllldldlddrrrrrrlllllluurururrrrrrrrdrdrddlllululllldldllluurururrrrrrrrdrdrddlllllrrrrruulululllllllldldlddrrrrrrrrrrlllllllllluurururrrrrrrrdrdrddlllrrruulululllllllldldlddrrrruurrrrudlllldldllluurururrrrrrlllllldldlddrrrrrruurrdrdrrruulululrdrdrddllllrrrruululullrrdrdrddlllllrrrrruulululllrrrdrdrddllllllrrrrrruululullllrrrrdrdrddlllllllrrrrrrruulululllllrrrrrdrdrddlllllluulldldrrrrrrrlllllllllluurururrrrlllldldlddrrrrrrrruuuurrdrdrddlruulululllrrrdrdrddllrruululullllrrrrdrdrddlllrrruulululllllrrrrrdrdrddllllrrrruululullllllrrrrrrdrdrddlllllrrrrruulululllllldddldllluurururrrrrrlllllldldlddrrrrrrrllllllluurururrrrrrdddrddlurrrruulululrdrdrddllllurdrrruululullrrdrdrddlllllllllllluurururrrrrrlllllldldlddrrrrrrrruullllddrrrrrrrruulululllrrrdrdrddlllllllllllluurururrddrrrrudllllddrrrrrrrruululullrrdrdrddlllllllllllluurururrddrruurrlllllldldlddrrrrrrrrrrrruulululllllrudrrrrdrdrddlllllllllllluurururrrrrrlllllldldlddrrrrrrrrrrrruulululllrrrdrdrddlllllllluurruu')
    # ot.test()
    print()

    print('IDDFS')
    iddfs = IDDFS(50)
    t0 = time()
    final_state = iddfs.process()
    t1 = time()
    if final_state is not None:
        print('Success!')
        print('Moves:', final_state.moves)
        # print('Expanded nodes:', iddfs.expanded_nodes())  # TODO
        # print('Nodes in frontier:', iddfs.frontier_size())  # TODO
        print('Solution:', final_state)
    else:
        print('Failure!')
    print("{:.2f}s".format(t1 - t0))
    # ot = OutputTester('rllruurrdrddluuuuddrdrrruulululllrddlluuudlldddlddruuuuddldllluurururrrlddrruu')
    # ot.test()
    print()

    heuristics = [heuristic_min_distance_boxes, heuristic_distance_to_closest_goals]
    for i, heuristic in enumerate(heuristics):
        print('GGS - Heuristic', i)
        ggs = GGS(heuristic)
        t0 = time()
        final_state = ggs.process()
        t1 = time()
        if final_state is not None:
            print('Success!')
            print('Moves:', final_state.moves)
            print('Expanded nodes:', ggs.expanded_nodes())
            print('Nodes in frontier:', ggs.frontier_size())
            print('Solution:', final_state)
        else:
            print('Failure!')
        print("{:.2f}s".format(t1 - t0))
        # ot = OutputTester('rllruurrdrddluuuuddrdrrruulululllrddlluuudlldddlddruuuuddldllluurururrrlddrruu')
        # ot.test()
        print()

        print('A* - Heuristic', i)
        a_star = AStar(heuristic)
        t0 = time()
        final_state = a_star.process()
        t1 = time()
        if final_state is not None:
            print('Success!')
            print('Moves:', final_state.moves)
            print('Expanded nodes:', a_star.expanded_nodes())
            print('Nodes in frontier:', a_star.frontier_size())
            print('Solution:', final_state)
        else:
            print('Failure!')
        print("{:.2f}s".format(t1 - t0))
        # ot = OutputTester('rllruurrdrddluuuuddrdrrruulululllrddlluuudlldddlddruuuuddldllluurururrrlddrruu')
        # ot.test()
        print()

        print('IDA* - Heuristic', i)
        ida_star = IDAStar(heuristic, 50)
        t0 = time()
        final_state = ida_star.process()
        t1 = time()
        if final_state is not None:
            print('Success!')
            print('Moves:', final_state.moves)
            # print('Expanded nodes:', ida_star.expanded_nodes())  # TODO
            # print('Nodes in frontier:', ida_star.frontier_size())  # TODO
            print('Solution:', final_state)
        else:
            print('Failure!')
        print("{:.2f}s".format(t1 - t0))
        # ot = OutputTester('rllruurrdrddluuuuddrdrrruulululllrddlluuudlldddlddruuuuddldllluurururrrlddrruu')
        # ot.test()
        print()


if __name__ == '__main__':
    run()
