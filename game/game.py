class Player:
    def __init__(self):
        self.x = None
        self.y = None

    def setPos(self, x, y):
        self.x = x
        self.y = y


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


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

    def __init__(self):
        pass


    def parseBoard(self):
        b = open('board.txt', 'r')
        x = 0
        y = 0
        goals = 0
        boxes = 0
        longest_line = 0

        for line in b.readlines():
            self.board.append([])
            for c in line:
                if c == self.GOAL[0]:
                    self.goals.append(Point(x, y))
                    goals += 1
                if c == self.BOX[0]:
                    boxes += 1
                if c == self.PLAYER[0]:
                    self.player.setPos(x, y)
                if c != '\n'[0]:
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


    def showBoard(self):
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


    def moveUp(self):
        if self.player.y == 0:
            return

        if self.board[self.player.y - 1] == self.FREE_SPACE:
            self.board[self.player.x][self.player.y] = self.FREE_SPACE
            self.player.setPos(self.player.x, self.player.y - 1)
            self.board[self.player.x][self.player.y] = self.PLAYER

        if self.board[self.player.y - 1] == self.BOX and self.player.y > 1 and self.board[self.player.y - 2] == self.FREE_SPACE:
            self.board[self.player.x][self.player.y] = self.FREE_SPACE
            self.player.setPos(self.player.x, self.player.y - 1)
            self.board[self.player.x][self.player.y] = self.PLAYER
            self.board[self.player.x][self.player.y - 1] = self.BOX