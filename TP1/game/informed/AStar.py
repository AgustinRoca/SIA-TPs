from typing import Callable
from game.game import Game, GameState
from utils.direction import Direction
from sortedcontainers import SortedList


def fn(state: GameState, heuristic: Callable[[GameState], int]) -> (int, int):
    h = heuristic(state)
    return state.moves + h, h


# A*
class AStar:
    def __init__(self, game, check_deadlock, heuristic: Callable[[GameState], int]):
        self.game = game
        self.visited_nodes = {self.game.get_state()}
        self.frontier = SortedList(key=lambda state: fn(state, heuristic))
        self.heuristic = heuristic
        self.frontier.add(self.game.get_state())
        self.check_deadlock = check_deadlock

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
                if self.check_deadlock and self.game.deadlock():
                    continue
                if next_state not in self.visited_nodes:
                    self.frontier.add(next_state)
                    self.visited_nodes.add(next_state)

    def expanded_nodes(self):
        return len(self.visited_nodes)

    def frontier_size(self):
        return len(self.frontier)
