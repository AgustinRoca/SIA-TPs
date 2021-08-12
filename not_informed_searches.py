from game.game import Game, Direction
from tree import Tree

class Dfs:
    def __init__(self):
        pass

    def process(self):
        pass


class Bfs:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
        self.has_won = False
        self.tree = Tree(self.game.get_state())
        self.bfs_queue = []
        self.bfs_queue.append(self.tree.root.elem)

    def process(self):
        if self.game.has_won():
            print('Solution:', None)
            return self.game.get_state()

        while True:
            state = self.bfs_queue.pop(0)
            current_node = self.tree.find(state)

            for direction in Direction:
                self.game.set_state(state)
                self.game.move(direction)
                aux_state = self.game.get_state()
                if self.game.has_won():
                    print('Solution:', aux_state)
                    return aux_state
                if aux_state not in self.tree:
                    self.bfs_queue.append(aux_state)
                    current_node.add_child(aux_state)
