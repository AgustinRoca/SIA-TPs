from typing import Callable

from game.game import Game, GameState
from utils.direction import Direction
from sortedcontainers import SortedList


# Global Greedy Search
class GGS:
    def __init__(self, heuristic: Callable[[GameState], int]):
        self.game = Game()
        self.game.parse_board()
        self.visited_nodes = set()
        self.frontier = SortedList(key=heuristic)

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
                if next_state not in self.visited_nodes:
                    self.frontier.add(next_state)
                    self.visited_nodes.add(next_state)