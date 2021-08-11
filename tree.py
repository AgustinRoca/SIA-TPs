class GameState:
    def __init__(self, board=None, goals=None, player=None, moves=0):
        self.children = None
        self.board = board
        self.goals = goals
        self.player = player
        self.moves = moves

    def __eq__(self, other):
        for i in range(0, len(self.board)):
            if self.board[i] != other.board[i]:
                return False
        return self.player == other.player

    def __str__(self):
        return 'Moves: ' + str(self.moves) + '. Player pos.: ' + str(self.player)

    def get_heuristic_1(self):
        return
