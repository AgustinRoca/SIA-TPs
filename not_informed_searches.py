from game.game import Game, Direction


# TODO: Capaz lo mejor va a ser tener un arbol y mover nodos cuando se encuentra que se puede llegar a otro lugar
class IDDFS:
    def __init__(self, init_max_depth):
        self.game = Game()
        self.game.parse_board()
        self.init_max_depth = init_max_depth
        self.visited_nodes = {}
        self.frontier = [self.game.get_state()]
        self.last_frontier = set()

    def process(self):
        max_depth = self.init_max_depth
        while True:
            ans = self._process_with_depth(max_depth)
            if ans is not None:
                return ans
            max_depth += 10
            self.frontier = list(self.last_frontier)
            self.last_frontier = set()
            print('Trying with', max_depth)

    def _process_with_depth(self, max_depth):
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
                if (new_state not in self.visited_nodes) or (self.visited_nodes[new_state] > new_state.moves):
                    self.visited_nodes[new_state] = new_state.moves
                    if new_state.moves == max_depth:
                        self.last_frontier.add(new_state)
                    else:
                        self.frontier.append(new_state)


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


class BFS:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
        self.visited_nodes = set()
        self.frontier = [self.game.get_state()]

    def process(self):
        if self.game.has_won():
            return self.game.get_state()
        while len(self.frontier) > 0:
            state = self.frontier.pop(0)

            for direction in Direction:
                self.game.set_state(state)
                self.game.move(direction)
                if self.game.has_won():
                    return self.game.get_state()

                next_state = self.game.get_state()
                if next_state not in self.visited_nodes:
                    self.frontier.append(next_state)
                    self.visited_nodes.add(next_state)
