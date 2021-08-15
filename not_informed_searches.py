from game.game import Game, Direction


class IDDFS:
    def __init__(self, init_max_depth):
        self.game = Game()
        self.game.parse_board()
        self.has_won = False
        self.expanded_nodes = {}
        self.init_max_depth = init_max_depth
        self.frontier = set()

    def process(self):
        max_depth = self.init_max_depth
        self.frontier.add(self.game.state)
        while True:
            frontier_nodes = []
            for node in self.frontier:
                frontier_nodes.append(node)
            for node in frontier_nodes:
                self.frontier.remove(node)
                ans = self._process_rec(node, max_depth)
                if ans is not None:
                    return ans
            max_depth += 50
            print('Trying with', max_depth)

    def _process_rec(self, state, max_depth):
        self.game.set_state(state)

        if self.game.has_won():
            return self.game.get_state()

        self.expanded_nodes[state] = state

        if state.moves < max_depth:
            for direction in Direction:
                self.game.set_state(state)
                self.game.move(direction)
                new_state = self.game.get_state()
                if new_state not in self.expanded_nodes:
                    ans = self._process_rec(new_state, max_depth)
                    if ans is not None:
                        return ans
                elif new_state.moves < self.expanded_nodes[new_state].moves:
                    self.expanded_nodes.pop(new_state)
                    self.expanded_nodes[new_state] = new_state
                    ans = self._process_rec(new_state, max_depth)
                    if ans is not None:
                        return ans

        else:
            self.frontier.add(state)
        return None


class DFS:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
        self.has_won = False
        self.expanded_nodes = {}

    def process(self):
        return self._process_rec(self.game.get_state())

    def _process_rec(self, state):
        self.game.set_state(state)

        if self.game.has_won():
            return self.game.get_state()

        self.expanded_nodes[state] = True

        for direction in Direction:
            self.game.set_state(state)
            self.game.move(direction)
            new_state = self.game.get_state()
            if new_state not in self.expanded_nodes:
                ans = self._process_rec(new_state)
                if ans is not None:
                    return ans

        return None


class BFS:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
        self.expanded_nodes = set()
        self.queue_set = set()
        self.queue = []
        self.queue.append(self.game.get_state())  # pongo el estado inicial en la cola

    def process(self):
        if self.game.has_won():
            print('Solution:')
            return self.game.get_state()
        prev_moves = 0
        while True:
            state = self.queue.pop(0)
            self.expanded_nodes.add(state)

            if prev_moves != state.moves:
                print(state.moves)
                prev_moves = state.moves

            for direction in Direction:
                self.game.set_state(state)
                self.game.move(direction)
                next_state = self.game.get_state()
                if self.game.has_won():
                    print('Solution:', next_state)
                    return next_state
                if next_state not in self.expanded_nodes and next_state not in self.queue_set:
                    self.queue.append(next_state)
                    self.queue_set.add(next_state)
