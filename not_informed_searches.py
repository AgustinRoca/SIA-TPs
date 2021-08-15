from game.game import Game, Direction


class DFS:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
        self.expanded_nodes = {}
        self.queues = [[] for _ in list(Direction)] # Array of queues of direction
        self.queue_dict = {}

    def process(self):
        least_moves_state = None
        directions = list(Direction)

        starting_state = self.game.get_state()
        while self._has_next_queue() or starting_state is not None:
            if starting_state is None:
                queue = self._next_queue()
                state = queue.pop(0)
            else:
                state = starting_state
                starting_state = None

            if (least_moves_state is not None and state.moves >= least_moves_state.moves) or state in self.expanded_nodes:
                continue

            self.expanded_nodes[state] = True

            self.game.set_state(state)
            if self.game.has_won():
                least_moves_state = state
                print(state)
                continue

            for i in range(len(directions)):
                self.game.set_state(state)
                self.game.move(directions[i])
                new_state = self.game.get_state()
                if new_state not in self.expanded_nodes and new_state not in self.queue_dict:
                    self.queues[i].insert(0, new_state)

        return least_moves_state

    def _has_next_queue(self):
        return any(len(queue) > 0 for queue in self.queues)

    def _next_queue(self):
        for i in range(len(list(Direction))):
            if len(self.queues[i]) > 0:
                return self.queues[i]
        return None


class BFS:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
        self.expanded_nodes = {}
        self.queue_dictionary = {}
        self.queue = [self.game.get_state()] # pongo el estado inicial en la cola

    def process(self):
        if self.game.has_won():
            print('Solution:', None)
            return self.game.get_state()
        prev_moves = 0
        while True:
            state = self.queue.pop(0)
            if state in self.queue_dictionary:
                self.queue_dictionary.pop(state)

            self.expanded_nodes[state] = True

            if prev_moves != state.moves:
                # print(state.moves)
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
