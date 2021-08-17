import copy
from typing import Callable
from game.game import Game, GameState
from utils.direction import Direction
from sortedcontainers import SortedList


def fn(state: GameState, heuristic: Callable[[GameState], int]) -> (int, int):
    h = heuristic(state)
    return state.moves + h, h


class IDAStar:
    def __init__(self, heuristic: Callable[[GameState], int]):
        self.game = Game()
        self.game.parse_board()
        f = fn(self.game.get_state(), heuristic)[0]
        self.init_max_f = f
        self.visited_nodes = {self.game.get_state(): 0}
        self.frontier = [self.game.get_state()]
        self.last_frontier = {}
        self.heuristic = heuristic

    def process(self):
        max_f = self.init_max_f
        while True:
            ans, min_f_in_frontier = self._process_with_f(max_f)
            if ans is not None:
                return ans
            else:
                max_f = min_f_in_frontier
                self.frontier = copy.copy(self.last_frontier[max_f])
                self.last_frontier[max_f] = []

    def _process_with_f(self, f):
        min_f = None
        while len(self.frontier) > 0:
            state = self.frontier.pop()
            self.game.set_state(state)
            if self.game.has_won():
                return self.game.get_state(), min_f

            for direction in Direction:
                self.game.set_state(state)
                self.game.move(direction)
                new_state = self.game.get_state()
                if (new_state not in self.visited_nodes.keys()) or (self.visited_nodes[new_state] > new_state.moves):
                    self.visited_nodes[new_state] = new_state.moves
                    new_f = fn(new_state, self.heuristic)[0]

                    if new_f > f:
                        if min_f is None or new_f < min_f:
                            min_f = new_f
                        if new_f not in self.last_frontier.keys():
                            self.last_frontier[new_f] = []
                        self.last_frontier[new_f].append(new_state)
                    else:
                        self.frontier.append(new_state)
        return None, min_f

    def expanded_nodes(self):
        return len(self.visited_nodes)

    def frontier_size(self):
        return len(self.frontier)
