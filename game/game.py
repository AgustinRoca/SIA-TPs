from enum import Enum


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
    board = []
    goals = []
    player = Player()
    moves = 0

    def __init__(self):
        pass

    def parse_board(self):
        b = open('board.txt', 'r')
        x = 0
        y = 0
        goals = 0
        boxes = 0
        longest_line = 0

        for line in b.readlines():
            self.board.append([])
            for c in line:
                if c == self.GOAL:
                    self.goals.append(Point(x, y))
                    goals += 1
                if c == self.BOX:
                    boxes += 1
                if c == self.PLAYER:
                    self.player.set_pos(Point(x, y))
                if c != '\n':
                    self.board[y].append(c)
                x += 1
            x = 0
            y += 1

        if goals != boxes:
            return self.GOALS_AND_BOXES_DONT_MATCH

        for line in self.board:
            if len(line) > longest_line:
                longest_line = len(line)

        for line in self.board:
            while len(line) < longest_line:
                line.append(self.FREE_SPACE)

    def show_board(self):
        for line in self.board:
            for c in line:
                print(c, end='')
            print()
        print()
        print('Goals: ', end='')
        for goal in self.goals:
            print(goal, end='')
        print()
        print('Player position: (' + str(self.player.x) + ', ' + str(self.player.y) + ')')
        print('Boxes left: ' + str(self.get_boxes_left()))
        print('Moves: ' + str(self.moves))

    def move(self, direction: Direction):
        player_move_position = Point(self.player.x + direction.direction.x, self.player.y + direction.direction.y)
        push_box_position = Point(self.player.x + 2*direction.direction.x, self.player.y + 2*direction.direction.y)

        can_move = False
        if self.valid_position(player_move_position) and self.is_free_place(player_move_position):
            can_move = True

        elif self.board[player_move_position.y][player_move_position.x] == self.BOX and \
                self.valid_position(push_box_position) and self.is_free_place(push_box_position):
            self.board[push_box_position.y][push_box_position.x] = self.BOX  # push box
            can_move = True

        # move player
        if can_move:
            if self.__exists_goal(Point(self.player.x, self.player.y)):
                self.board[self.player.y][self.player.x] = self.GOAL
            else:
                self.board[self.player.y][self.player.x] = self.FREE_SPACE
            self.player.set_pos(player_move_position)
            self.board[self.player.y][self.player.x] = self.PLAYER
            self.moves += 1

    def get_boxes_left(self):
        boxes_left = len(self.goals)
        for goal in self.goals:
            if self.board[goal.y][goal.x] == self.BOX:
                boxes_left -= 1

        return boxes_left

    def has_won(self):
        return self.get_boxes_left() == 0

    def is_free_place(self, position: Point):
        return (self.board[position.y][position.x] == self.GOAL) or \
               (self.board[position.y][position.x] == self.FREE_SPACE)

    def valid_position(self, position: Point):
        return 0 <= position.x < len(self.board[0]) - 1 and \
               0 <= position.y < len(self.board) - 1

    def __exists_goal(self, position: Point):
        for goal in self.goals:
            if goal == position:
                return True
        return False
