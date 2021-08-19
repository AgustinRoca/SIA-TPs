from game.game import Game
from game.informed.AStar import AStar
from game.informed.GGS import GGS
from game.informed.IDAStar import IDAStar
from game.informed.heuristics import heuristic_min_distance_boxes, heuristic_distance_to_closest_goals, heuristic_distance_to_closest_goals_and_player_to_closest_box
from game.not_informed.BFS import BFS
from game.not_informed.DFS import DFS
from game.not_informed.IDDFS import IDDFS
from time import time


algorithms = [BFS, DFS, IDDFS, GGS, AStar, IDAStar]
heuristics = [heuristic_min_distance_boxes, heuristic_distance_to_closest_goals, heuristic_distance_to_closest_goals_and_player_to_closest_box]


def process(file, algorithm, limit=None, heuristic=None, consider_deadlock=True):
    game = Game()
    game.parse_board(file)
    print(algorithms[algorithm - 1].__name__, end='')
    if consider_deadlock is True:
        print(' considering deadlocks')
    else:
        print(' not considering deadlocks')
    if algorithm == 3:
        algo = algorithms[algorithm - 1](game, consider_deadlock, limit)
    elif algorithm > 3:
        algo = algorithms[algorithm - 1](game, consider_deadlock, heuristics[heuristic - 1])
    else:
        algo = algorithms[algorithm - 1](game, consider_deadlock)
    t0 = time()
    final_state = algo.process()
    t1 = time()
    if final_state is not None:
        print('Success!')
        print('Moves:', final_state.moves)
        print('Expanded nodes:', algo.expanded_nodes())
        if algorithm == 3:
            print('Nodes in frontier:', algo.frontier_size(final_state.moves))
        else:
            print('Nodes in frontier:', algo.frontier_size())
        print('Solution:', final_state)
    else:
        print('Failure!')
    print("{:.2f}s".format(t1 - t0))
    print()


def run():
    args = parse_config()
    if args is None:
        print('Invalid config.txt')
        return
    process(args['file'], args['algorithm'], args['limit'], args['heuristic'], args['consider_deadlock'])


def parse_config():
    f = open('TP1/config.txt')
    arguments = {}
    for line in f.readlines():
        arg = line.strip().split('=')
        if arg[0] == 'consider_deadlock':
            if arg[1] == 'True':
                arguments[arg[0]] = True
            elif arg[1] == 'False':
                arguments[arg[0]] = False
            else:
                return None
        else:
            arguments[arg[0]] = int(arg[1])

    if not 1 <= arguments['algorithm'] <= 6:
        return None

    if not 1 <= arguments['heuristic'] <= 3:
        return None

    if not arguments['limit'] > 0:
        return None

    return arguments


if __name__ == '__main__':
    run()
