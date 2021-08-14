from game.game import Game, Direction, GameState


class DFS:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
        self.expanded_nodes = {}

    # def process(self):
    #     return self._process_rec(self.game.get_state())
    # 
    # def _process_rec(self, state):
    #     self.game.set_state(state)
    # 
    #     if self.game.has_won():
    #         return self.game.get_state()
    # 
    #     self.expanded_nodes[state] = True
    # 
    #     for direction in Direction:
    #         self.game.set_state(state)
    #         self.game.move(direction)
    #         new_state = self.game.get_state()
    #         if new_state not in self.expanded_nodes:
    #             ans = self._process_rec(new_state)
    #             if ans is not None:
    #                 return ans
    # 
    #     return None

    def process_rec_direction(self, direction: Direction, moves: int, state: GameState) -> (int, GameState):
        self.expanded_nodes[state] = True
        self.game.set_state(state)
        self.game.move(direction)
        new_state = self.game.get_state()

        # If both states are equal or the game has won, that means that we cannot longer traverse that path
        if new_state == state or self.game.has_won():
            return moves, state
        return moves + 1, new_state

    def process_rec(self, moves: int, state: GameState) -> (int, GameState):
        if state in self.expanded_nodes:
            return moves, state

        won_moves = []

        self.game.set_state(state)
        left = self.process_rec_direction(Direction.LEFT, moves, state)
        # New state has not already been processed
        if left[1] not in self.expanded_nodes:
            left = self.process_rec(left[0], left[1])
        if not self.game.has_won():
            left = None
        else:
            won_moves.append(left)

        self.game.set_state(state)
        down = self.process_rec_direction(Direction.DOWN, moves, state)
        # New state has not already been processed
        if down[1] not in self.expanded_nodes:
            down = self.process_rec(down[0], down[1])
        if not self.game.has_won():
            down = None
        else:
            won_moves.append(down)

        self.game.set_state(state)
        up = self.process_rec_direction(Direction.UP, moves, state)
        # New state has not already been processed
        if up[1] not in self.expanded_nodes:
            up = self.process_rec(up[0], up[1])
        if not self.game.has_won():
            up = None
        else:
            won_moves.append(up)

        self.game.set_state(state)
        right = self.process_rec_direction(Direction.RIGHT, moves, state)
        # New state has not already been processed
        if right[1] not in self.expanded_nodes:
            right = self.process_rec(right[0], right[1])
        if not self.game.has_won():
            right = None
        else:
            won_moves.append(right)

        # Sort by smallest moves
        won_moves = sorted(won_moves, key=lambda move: move[0])
        if len(won_moves) > 0:
            return won_moves[0]
        return None


    def process(self):
        if self.game.has_won():
            return self.game.get_state()

        result = self.process_rec(0, self.game.get_state())
        print(result)
        return result[1]


class BFS:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
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
