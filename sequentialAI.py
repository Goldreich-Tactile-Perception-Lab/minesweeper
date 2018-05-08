import minesweeper as ms
import random


class SeqAI(ms.GameAI):
    def __init__(self):
        self.width = 0
        self.height = 0
        self.exposed_squares = set()

    def init(self, config):
        self.width = config.width
        self.height = config.height
        self.x = self.width
        self.y = self.height - 1
        self.exposed_squares.clear()

    def next(self):
        while True:
            if self.x is 0:
                self.x = self.width - 1
                self.y = self.y - 1
            else:
                self.x = self.x - 1
            x = self.x
            y = self.y
            if (x, y) not in self.exposed_squares:
                break
        print('selecting point ({0},{1})'.format(x, y))
        return x, y

    def update(self, result):
        for position in result.new_squares:
            self.exposed_squares.add((position.x, position.y))


num_games = 1
config = ms.GameConfig() # Sets 3 variables: height, width, and # of mines. This is then used throughout rest of program.
ai = SeqAI()
viz = ms.GameVisualizer('key')
results = ms.run_games(config, 1, ai, viz)
if results[0].success:
    print('Success!')
else:
    print('Boom!')
print('Game lasted {0} moves'.format(results[0].num_moves))