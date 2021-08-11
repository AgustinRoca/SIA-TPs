from enum import Enum
from tree import GameState
from copy import deepcopy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Player:
    def __init__(self):
        self.x = None
        self.y = None

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def set_pos(self, pos: Point):
        self.x = pos.x
        self.y = pos.y


class Direction(Enum):
    UP = 0, Point(0, -1)
    DOWN = 1, Point(0, 1)
    LEFT = 2, Point(-1, 0)
    RIGHT = 3, Point(1, 0)

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, direction: Point = None):
        self._direction = direction

    def __str__(self):
        return self.value

    # this makes sure that the description is read-only
    @property
    def direction(self):
        return self._direction


class Game:
    FREE_SPACE = ' '
    WALL = '#'
    GOAL = '.'
    BOX = '$'
    PLAYER = '@'
    GOALS_AND_BOXES_DONT_MATCH = -1
    state = None

    def __init__(self):
        self.state = GameState()
        self.state.board = []
        self.state.goals = []
        self.state.player = Player()
        self.state.moves = 0

    def parse_board(self):
        b = open('board.txt', 'r')
        x = 0
        y = 0
        goals = 0
        boxes = 0
        longest_line = 0

        for line in b.readlines():
            self.state.board.append([])
            for c in line:
                if c == self.GOAL:
                    self.state.goals.append(Point(x, y))
                    goals += 1
                if c == self.BOX:
                    boxes += 1
                if c == self.PLAYER:
                    self.state.player.set_pos(Point(x, y))
                if c != '\n':
                    self.state.board[y].append(c)
                x += 1
            x = 0
            y += 1

        if goals != boxes:
            return self.GOALS_AND_BOXES_DONT_MATCH

        for line in self.state.board:
            if len(line) > longest_line:
                longest_line = len(line)

        for line in self.state.board:
            while len(line) < longest_line:
                line.append(self.FREE_SPACE)

    def show_board(self):
        for line in self.state.board:
            for c in line:
                print(c, end='')
            print()
        print()
        print('Goals: ', end='')
        for goal in self.state.goals:
            print(goal, end='')
        print()
        print('Player position: (' + str(self.state.player.x) + ', ' + str(self.state.player.y) + ')')
        print('Boxes left: ' + str(self.get_boxes_left()))
        print('Moves: ' + str(self.state.moves))

    def move(self, direction: Direction):
        player_move_position = Point(self.state.player.x + direction.direction.x, self.state.player.y + direction.direction.y)
        push_box_position = Point(self.state.player.x + 2*direction.direction.x, self.state.player.y + 2*direction.direction.y)

        can_move = False
        if self.valid_position(player_move_position) and self.is_free_place(player_move_position):
            can_move = True

        elif self.state.board[player_move_position.y][player_move_position.x] == self.BOX and \
                self.valid_position(push_box_position) and self.is_free_place(push_box_position):
            self.state.board[push_box_position.y][push_box_position.x] = self.BOX  # push box
            can_move = True

        # move player
        if can_move:
            if self.__exists_goal(Point(self.state.player.x, self.state.player.y)):
                self.state.board[self.state.player.y][self.state.player.x] = self.GOAL
            else:
                self.state.board[self.state.player.y][self.state.player.x] = self.FREE_SPACE
            self.state.player.set_pos(player_move_position)
            self.state.board[self.state.player.y][self.state.player.x] = self.PLAYER
            self.state.moves += 1

    def get_boxes_left(self):
        boxes_left = len(self.state.goals)
        for goal in self.state.goals:
            if self.state.board[goal.y][goal.x] == self.BOX:
                boxes_left -= 1

        return boxes_left

    def has_won(self):
        return self.get_boxes_left() == 0

    def is_free_place(self, position: Point):
        return (self.state.board[position.y][position.x] == self.GOAL) or \
               (self.state.board[position.y][position.x] == self.FREE_SPACE)

    def valid_position(self, position: Point):
        return 0 <= position.x < len(self.state.board[0]) - 1 and \
               0 <= position.y < len(self.state.board) - 1

    def __exists_goal(self, position: Point):
        for goal in self.state.goals:
            if goal == position:
                return True
        return False

    def set_state(self, state):
        self.state = deepcopy(state)

    def get_state(self):
        return deepcopy(self.state)
