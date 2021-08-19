from typing import Callable

from sortedcontainers import SortedDict

from game.game import Game, GameState
from utils.direction import Direction


def fn(state: GameState, heuristic: Callable[[GameState], int]) -> (int, int):
    h = heuristic(state)
    return state.moves + h, h


class IDAStar:
    def __init__(self, game, check_deadlock, heuristic: Callable[[GameState], int]):
        self.game = game
        f = fn(self.game.get_state(), heuristic)[0]
        self.init_max_f = f
        self.visited_nodes = {self.game.get_state(): 0}
        self.frontier = [self.game.get_state()]
        self.last_frontier = SortedDict()
        self.heuristic = heuristic
        self.changed = 0
        self.check_deadlock = check_deadlock

    def process(self):
        max_f = self.init_max_f
        while True:
            ans = self._process_with_f(max_f)
            if ans is not None:
                return ans
            else:
                if len(self.last_frontier) == 0:
                    return None
                entry = self.last_frontier.popitem(0)
                max_f = entry[0]
                self.frontier = entry[1]

    def _process_with_f(self, f):
        while len(self.frontier) > 0:
            state = self.frontier.pop()
            self.game.set_state(state)
            if self.game.has_won():
                return self.game.get_state()

            for direction in Direction:
                self.game.set_state(state)
                self.game.move(direction)
                new_state = self.game.get_state()
                if self.check_deadlock and self.game.deadlock():
                    continue
                if (new_state not in self.visited_nodes) or (self.visited_nodes[new_state] > new_state.moves):
                    if new_state in self.visited_nodes:
                        self.changed += 1
                    self.visited_nodes[new_state] = new_state.moves
                    new_f = fn(new_state, self.heuristic)[0]

                    if new_f > f:
                        if new_f not in self.last_frontier:
                            self.last_frontier[new_f] = []
                        self.last_frontier[new_f].append(new_state)
                    else:
                        self.frontier.append(new_state)
        return None

    def expanded_nodes(self):
        return len(self.visited_nodes) + self.changed

    def frontier_size(self):
        return len(self.frontier) + len(self.last_frontier)
