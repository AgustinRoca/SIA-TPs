from typing import Callable

from game.game import Game, GameState
from utils.direction import Direction
from sortedcontainers import SortedList


def fn(state: GameState, heuristic: Callable[[GameState], int]) -> int:
    return state.moves + heuristic(state)


# A*
class AStar:
    def __init__(self, heuristic: Callable[[GameState], int]):
        self.game = Game()
        self.game.parse_board()
        self.visited_nodes = set()
        self.frontier = SortedList(key=lambda state: fn(state, heuristic))
        self.heuristic = heuristic

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

    def _get_next_frontier_node(self):
        if len(self.frontier) == 1:
            return self.frontier.pop(0)
        elif len(self.frontier) > 1:
            i = 0
            while fn(self.frontier[i], self.heuristic) == fn(self.frontier[i + 1], self.heuristic):
                h1 = self.heuristic(self.frontier[i])
                h2 = self.heuristic(self.frontier[i + 1])
                if h1 < h2:
                    return h1
                elif h2 < h1:
                    return h2

                i += 1
            return self.frontier.pop(i)
        else:
            return None
