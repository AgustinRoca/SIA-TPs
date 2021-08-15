from game.game import Game
from utils.direction import Direction


class DFS:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
        self.visited_nodes = set()
        self.frontier = [self.game.get_state()]

    def process(self):
        if self.game.has_won():
            return self.game.get_state()
        while len(self.frontier) > 0:
            state = self.frontier.pop()

            for direction in Direction:
                self.game.set_state(state)
                self.game.move(direction)
                if self.game.has_won():
                    return self.game.get_state()

                new_state = self.game.get_state()
                if new_state not in self.visited_nodes:
                    self.frontier.append(new_state)
                    self.visited_nodes.add(new_state)