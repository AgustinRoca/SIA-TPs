from typing import Callable
from TP1.game.game import Game, GameState
from TP1.utils.direction import Direction
from sortedcontainers import SortedList


def fn(state: GameState, heuristic: Callable[[GameState], int]) -> (int, int):
    h = heuristic(state)
    return state.moves + h, h


# A*
class AStar:
    def __init__(self, heuristic: Callable[[GameState], int]):
        self.game = Game()
        self.game.parse_board()
        self.visited_nodes = {self.game.get_state()}
        self.frontier = SortedList(key=lambda state: fn(state, heuristic))
        self.heuristic = heuristic
        self.frontier.add(self.game.get_state())

    def process(self):
        while len(self.frontier) > 0:
            state = self.frontier.pop(0)
            self.game.set_state(state)
            if self.game.has_won():
                return self.game.get_state()

            for direction in Direction:
                self.game.set_state(state)
                self.game.move(direction)
                next_state = self.game.get_state()
                if next_state not in self.visited_nodes:
                    self.frontier.add(next_state)
                    self.visited_nodes.add(next_state)

    def expanded_nodes(self):
        return len(self.visited_nodes)

    def frontier_size(self):
        return len(self.frontier)
