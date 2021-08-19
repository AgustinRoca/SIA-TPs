from enum import Enum
from TP1.utils.direction import Direction


class GameState:
    def __init__(self, moves=0):
        self.static_board = []
        self.goals = set()
        self.boxes = set()
        self.player = None
        self.moves = moves
        self.last_moves = []

    def __str__(self):
        s = ''
        for move in self.last_moves:
            s += str(move)
        return s

    def __eq__(self, other):
        return self.boxes == other.boxes and self.player == other.player

    def __hash__(self):
        return hash((tuple(self.boxes), self.player))

    def get_boxes_left(self):
        boxes_left = len(self.boxes)
        for goal in self.goals:
            for box in self.boxes:
                if goal == box:
                    boxes_left -= 1

        return boxes_left

    def copy(self):
        new_state = GameState()
        new_state.static_board = self.static_board
        new_state.boxes = set(self.boxes)
        new_state.goals = self.goals
        new_state.player = self.player  # Tuples are immutable
        new_state.moves = self.moves
        new_state.last_moves = [*self.last_moves]
        return new_state


class BoardCell(Enum):
    FREE_SPACE = ' '
    WALL = '#'
    GOAL = '.'
    BOX = '$'
    BOX_OVER_GOAL = '*'
    PLAYER = '@'

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, s: str):
        self.string = s

    def __str__(self):
        return self.string

    def __eq__(self, other):
        return self.string == other


class Game:
    GOALS_AND_BOXES_DONT_MATCH = -1
    NO_GOALS_AND_BOXES = -2

    def __init__(self):
        self.state = GameState()

    def parse_board(self, filename='TP1/boards/board.txt'):
        b = open(filename, 'r')
        x = 0
        y = 0
        longest_line = 0

        for line in b.readlines():
            self.state.static_board.append([])
            for c in line:
                if c == BoardCell.FREE_SPACE:
                    self.state.static_board[y].append(BoardCell.FREE_SPACE)
                elif c == BoardCell.WALL:
                    self.state.static_board[y].append(BoardCell.WALL)
                elif c == BoardCell.GOAL:
                    self.state.goals.add((x, y))
                    self.state.static_board[y].append(BoardCell.FREE_SPACE)
                elif c == BoardCell.BOX:
                    self.state.boxes.add((x, y))
                    self.state.static_board[y].append(BoardCell.FREE_SPACE)
                elif c == BoardCell.BOX_OVER_GOAL:
                    self.state.boxes.add((x, y))
                    self.state.goals.add((x, y))
                    self.state.static_board[y].append(BoardCell.FREE_SPACE)
                elif c == BoardCell.PLAYER:
                    self.state.player = (x, y)
                    self.state.static_board[y].append(BoardCell.FREE_SPACE)
                x += 1
            x = 0
            y += 1

        if len(self.state.goals) != len(self.state.boxes):
            return self.GOALS_AND_BOXES_DONT_MATCH

        if len(self.state.goals) == 0:
            return self.NO_GOALS_AND_BOXES

        for line in self.state.static_board:
            if len(line) > longest_line:
                longest_line = len(line)

        for line in self.state.static_board:
            while len(line) < longest_line:
                line.append(BoardCell.FREE_SPACE)

    def show_board(self):
        for y in range(0, len(self.state.static_board)):
            for x in range(0, len(self.state.static_board[0])):
                if (x, y) == self.state.player:
                    print(BoardCell.PLAYER.string, end='')
                elif (x, y) in self.state.boxes:
                    if (x, y) in self.state.goals:
                        print(BoardCell.BOX_OVER_GOAL.string, end='')
                    else:
                        print(BoardCell.BOX.string, end='')
                elif (x, y) in self.state.goals:
                    print(BoardCell.GOAL.string, end='')
                else:
                    print(self.state.static_board[y][x], end='')
            print()
        print()
        print('Goals: ', end='')
        for goal in self.state.goals:
            print(goal, end='')
        print()
        print('Player position:', self.state.player)
        print('Boxes left:', self.get_boxes_left())
        print('Moves:', self.state.moves)

    def move(self, direction: Direction):
        player_move_position = (self.state.player[0] + direction.direction.x, self.state.player[1] + direction.direction.y)
        push_box_position = (self.state.player[0] + 2*direction.direction.x, self.state.player[1] + 2*direction.direction.y)

        can_move = False
        if self.valid_position(player_move_position) and self.is_free_place(player_move_position):
            can_move = True

        elif (player_move_position in self.state.boxes) and self.valid_position(push_box_position) and self.is_free_place(push_box_position):
            self.state.boxes.remove(player_move_position)
            self.state.boxes.add(push_box_position)
            can_move = True
        # move player
        if can_move:
            self.state.player = player_move_position
            self.state.moves += 1
            self.state.last_moves.append(direction)

    def get_boxes_left(self):
        return self.state.get_boxes_left()

    def has_won(self):
        return self.get_boxes_left() == 0

    def is_free_place(self, position):
        return (self.state.static_board[position[1]][position[0]] == BoardCell.FREE_SPACE) and \
               (position not in self.state.boxes)

    def valid_position(self, position):
        return 0 <= position[0] < len(self.state.static_board[0]) - 1 and \
               0 <= position[1] < len(self.state.static_board) - 1

    def set_state(self, state: GameState):
        self.state = state.copy()

    def get_state(self):
        return self.state

    def deadlock(self):
        for box in self.state.boxes:
            if box in self.state.goals:
                continue
            y_block = False
            x_block = False
            if (self.state.static_board[box[1] - 1][box[0]] == BoardCell.WALL) or (self.state.static_board[box[1] + 1][box[0]] == BoardCell.WALL):
                y_block = True
            if (self.state.static_board[box[1]][box[0] - 1] == BoardCell.WALL) or (self.state.static_board[box[1]][box[0] + 1] == BoardCell.WALL):
                x_block = True
            if y_block and x_block:
                return True
        return False
