import copy

from game.game import Game
from utils.direction import Direction


class IDDFS:
    def __init__(self, init_max_depth):
        self.game = Game()
        self.game.parse_board()
        self.init_max_depth = init_max_depth
        self.starting_visited_nodes = {0: {}, init_max_depth: {}}
        self.frontier = [self.game.get_state()]
        self.last_frontier = {0: {self.game.get_state()}, init_max_depth: set()}
        self.max_depth_not_found = 0
        self.min_depth_found = None
        self.expanded = 0

    def process(self, verbose=False):
        max_depth = self.init_max_depth
        partial_ans = None
        while True:
            ans = self._process_with_depth(max_depth)
            if ans is not None:
                partial_ans = ans
                if verbose:
                    print('Found with', max_depth)
                self.min_depth_found = max_depth
                if self.min_depth_found - 1 == self.max_depth_not_found:
                    return ans
                else:
                    max_depth = (self.max_depth_not_found + self.min_depth_found) // 2
            else:
                if verbose:
                    print('Not found with', max_depth)
                self.max_depth_not_found = max_depth
                if self.min_depth_found is not None and (self.min_depth_found - 1 == self.max_depth_not_found):
                    return partial_ans
                if self.min_depth_found is None:
                    max_depth *= 2
                else:
                    max_depth = (self.max_depth_not_found + self.min_depth_found) // 2

            self.frontier = list(self.last_frontier[self.max_depth_not_found])
            if verbose:
                print('Trying with', max_depth, '. Starting from:', self.max_depth_not_found)
            self.last_frontier[max_depth] = set()

    def _process_with_depth(self, max_depth):
        visited_nodes = copy.copy(self.starting_visited_nodes[self.max_depth_not_found])

        while len(self.frontier) > 0:
            state = self.frontier.pop()
            self.game.set_state(state)
            self.expanded += 1
            if self.game.has_won():
                return self.game.get_state()

            for direction in Direction:
                self.game.set_state(state)
                self.game.move(direction)
                new_state = self.game.get_state()
                if (new_state not in visited_nodes) or (visited_nodes[new_state] > new_state.moves):
                    visited_nodes[new_state] = new_state.moves
                    if new_state.moves == max_depth:
                        self.last_frontier[max_depth].add(new_state)
                    else:
                        self.frontier.append(new_state)

        for state in self.last_frontier[max_depth]:
            self.game.set_state(state)
            if self.game.has_won():
                return state
        self.starting_visited_nodes[max_depth] = visited_nodes

    def expanded_nodes(self):
        return self.expanded

    def frontier_size(self, depth):
        return len(self.last_frontier[depth])
