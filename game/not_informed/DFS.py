from game.game import Game
from utils.direction import Direction


class DFS:
    def __init__(self):
        self.game = Game()
        self.game.parse_board()
        self.visited_nodes = {self.game.get_state()}
        self.ancestors_stack = [self.game.get_state()]

    def process(self):
        while len(self.ancestors_stack) > 0:
            state = self.ancestors_stack[-1]  # Peek last element (LIFO)
            self.game.set_state(state)
            if self.game.has_won():
                return state

            delete_ancestor = True
            for direction in Direction:
                self.game.set_state(state)
                if self._process_direction(direction):
                    delete_ancestor = False
                    break

            if delete_ancestor:
                self.ancestors_stack.pop()  # Si todas las direcciones dan estados ya visitados, no tengo nada mas para hacer

    def _process_direction(self, direction: Direction) -> bool:
        self.game.move(direction)  # Lo muevo en una direccion
        new_state = self.game.get_state()
        if new_state not in self.visited_nodes:
            # Si no fue visitado, lo pongo como ancestro y vuelvo al loop
            self.ancestors_stack.append(new_state)
            self.visited_nodes.add(new_state)
            return True
        return False
