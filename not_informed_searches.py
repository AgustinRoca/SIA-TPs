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
        self.expanded_nodes = {}
        self.queues = [[] for _ in list(Direction)]  # Array of queues of direction
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
                # print(state.moves)
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
