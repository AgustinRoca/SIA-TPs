from game.game import Game
from utils.direction import Direction


class IDDFS:
    def __init__(self, init_max_depth):
        self.game = Game()
        self.game.parse_board()
        self.init_max_depth = init_max_depth
        self.visited_nodes = {}
        self.frontier = [self.game.get_state()]
        self.last_frontier = []
        self.ancestors_stack = []

    def process(self):
        max_depth = self.init_max_depth
        while True:
            ans = self._process_with_depth(max_depth)
            if ans is not None:
                return ans
            max_depth += 10
            self.frontier = [*self.last_frontier]
            self.last_frontier = []
            print('Trying with', max_depth)

    def _process_with_depth(self, max_depth):
        found_state = None
        while len(self.frontier) > 0:
            self.ancestors_stack = [self.frontier.pop(0)]  # Limpiamos los ancestros, empezamos desde este nodo

            while len(self.ancestors_stack) > 0:
                state = self.ancestors_stack[-1]  # Peek last element (LIFO)
                self.game.set_state(state)
                if self.game.has_won():
                    if found_state is None or found_state.moves > state.moves:
                        found_state = state
                        self.ancestors_stack.pop()
                        break

                delete_ancestor = True
                for direction in Direction:
                    self.game.set_state(state)
                    if self._process_direction(direction, max_depth):
                        delete_ancestor = False
                        break
                    elif self.game.get_state().moves == max_depth and self.game.has_won():
                        # Chequeamos en el caso limite que la solucion este a max_depth
                        if found_state is None or found_state.moves > self.game.get_state():
                            found_state = self.game.get_state()

                if delete_ancestor:
                    self.ancestors_stack.pop()  # Si todas las direcciones dan estados ya visitados, no tengo nada mas para hacer

        if found_state is not None:
            return found_state
        # if self.game.has_won():
        #     return self.game.get_state()
        # while len(self.frontier) > 0:
        #     state = self.frontier.pop()
        #
        #     for direction in Direction:
        #         self.game.set_state(state)
        #         self.game.move(direction)
        #         if self.game.has_won():
        #             return self.game.get_state()
        #
        #         new_state = self.game.get_state()
        #         if (new_state not in self.visited_nodes) or (self.visited_nodes[new_state] > new_state.moves):
        #             self.visited_nodes[new_state] = new_state.moves
        #             if new_state.moves == max_depth:
        #                 self.last_frontier.add(new_state)
        #             else:
        #                 self.frontier.append(new_state)

    def _process_direction(self, direction: Direction, max_depth: int) -> bool:
        self.game.move(direction)  # Lo muevo en una direccion
        new_state = self.game.get_state()

        not_visited = new_state not in self.visited_nodes
        different_state = False if not_visited else self.visited_nodes[new_state] > new_state.moves
        if not_visited or different_state:
            self.visited_nodes[new_state] = new_state.moves
            if new_state.moves == max_depth:
                self.last_frontier.append(new_state)
                return False  # No podemos seguir expandiendo este nodo
            elif not_visited or different_state:
                # Si no fue visitado, lo pongo como ancestro y vuelvo al loop
                self.ancestors_stack.append(new_state)
                return True
        return False
