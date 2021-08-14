from game.game import Game, Direction


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
            self.game.move(direction)
            new_state = self.game.get_state()
            if new_state not in self.expanded_nodes:
                return self._process_rec(new_state)

        return None


class BFS:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
        self.has_won = False
        self.expanded_nodes = {}
        self.queue_dictionary = {}
        self.queue = []
        self.queue.append(self.game.get_state())  # pongo el estado inicial en la cola

    def process(self):
        if self.game.has_won():
            print('Solution:', None)
            return self.game.get_state()
        prev_moves = 0
        while True:
            state = self.queue.pop(0)
            self.expanded_nodes[state] = True

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
                if next_state not in self.expanded_nodes and next_state not in self.queue_dictionary:
                    self.queue.append(next_state)
                    self.queue_dictionary[next_state] = True
