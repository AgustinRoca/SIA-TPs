from collections import deque

from game.game import Game
from utils.direction import Direction


class BFS:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
        self.visited_nodes = set()
        self.frontier = deque()

    def process(self):
        if self.game.has_won():
            return self.game.get_state()

        self.frontier.append(self.game.get_state())
        while len(self.frontier) > 0:
            state = self.frontier.popleft()

            for direction in Direction:
                self.game.set_state(state)
                self.game.move(direction)
                if self.game.has_won():
                    return self.game.get_state()

                next_state = self.game.get_state()
                if next_state not in self.visited_nodes:
                    self.frontier.append(next_state)
                    self.visited_nodes.add(next_state)