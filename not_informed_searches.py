from game.game import Game, Direction
from copy import deepcopy


class Dfs:
    def __init__(self):
        pass

    def process(self):
        pass


class Bfs:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
        self.state_root = self.game.get_state()
        self.has_won = False
        self.bfs_queue = []
        self.bfs_queue.append(self.state_root)

    def process(self):
        for i in range(0, 5):
            state = self.bfs_queue.pop(0)

            self.game.set_state(state)
            print('Checking state:')
            print(state)

            if self.game.has_won():
                return state

            self.game.move(Direction.UP)
            aux_state = deepcopy(self.game.get_state())
            if aux_state not in self.bfs_queue:
                self.bfs_queue.append(aux_state)

            self.game.set_state(state)
            self.game.move(Direction.DOWN)
            aux_state = deepcopy(self.game.get_state())
            if aux_state not in self.bfs_queue:
                self.bfs_queue.append(aux_state)

            self.game.set_state(state)
            self.game.move(Direction.LEFT)
            aux_state = deepcopy(self.game.get_state())
            if aux_state not in self.bfs_queue:
                self.bfs_queue.append(aux_state)

            self.game.set_state(state)
            self.game.move(Direction.RIGHT)
            aux_state = deepcopy(self.game.get_state())
            if aux_state not in self.bfs_queue:
                self.bfs_queue.append(aux_state)

            for e in self.bfs_queue:
                print(e, end=' | ')
            print()
