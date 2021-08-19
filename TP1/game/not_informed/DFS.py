from collections import deque

from TP1.game.game import Game
from TP1.utils.direction import Direction


class DFS:
    def __init__(self, game, check_deadlock):
        self.game = game
        self.visited_nodes = {self.game.get_state()}
        self.frontier = deque()
        self.frontier.append(self.game.get_state())
        self.check_deadlock = check_deadlock

    def process(self):
        while len(self.frontier) > 0:
            state = self.frontier.pop()
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
                    self.frontier.append(next_state)
                    self.visited_nodes.add(next_state)

    def expanded_nodes(self):
        return len(self.visited_nodes)

    def frontier_size(self):
        return len(self.frontier)
