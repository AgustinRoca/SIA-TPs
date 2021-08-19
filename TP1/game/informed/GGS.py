from typing import Callable

from TP1.game.game import Game, GameState
from TP1.utils.direction import Direction
from sortedcontainers import SortedList


# Global Greedy Search
class GGS:
    def __init__(self, game, check_deadlock, heuristic: Callable[[GameState], int]):
        self.game = game
        self.visited_nodes = set()
        self.frontier = SortedList(key=heuristic)
        self.check_deadlock = check_deadlock

    def process(self):
        if self.game.has_won():
            return self.game.get_state()

        self.frontier.add(self.game.get_state())
        while len(self.frontier) > 0:
            state = self.frontier.pop(0)

            for direction in Direction:
                self.game.set_state(state)
                self.game.move(direction)
                if self.game.has_won():
                    return self.game.get_state()

                next_state = self.game.get_state()
                if self.check_deadlock and self.game.deadlock():
                    continue
                if next_state not in self.visited_nodes:
                    self.frontier.add(next_state)
                    self.visited_nodes.add(next_state)

    def expanded_nodes(self):
        return len(self.visited_nodes)

    def frontier_size(self):
        return len(self.frontier)
