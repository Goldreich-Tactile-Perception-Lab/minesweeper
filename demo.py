import minesweeper as ms
import random
import numpy as np


class RandomAI(ms.GameAI):
    def __init__(self):
        self.width = 0
        self.height = 0
        self.exposed_squares = set() # a Set is an unordered list with no duplicates
        self.num_moves = 1

    def init(self, config): # reading in config, we can get access to the width and height of the gameboard
        self.width = config.width
        self.height = config.height
        self.exposed_squares.clear() # clear() removes all items from the list/set

    def next(self,game): # By including 'game' we can pull information from the minesweeper game.
        '''
        game.exposed = which squares are revealed in the gamespace
        game.counts = The numbers associated with each square. This is static

        We can use a combination of these two variables to determine what information is known to the "player"

        we can use numpy.where() to figure out the indices of every exposed value in the list
        example output: (array([0, 2, 2], dtype=int32), array([1, 0, 1], dtype=int32))
        - which looks weird, but you can read these like indices. array1 holds the "x" index, and array 2 holds the "y" index
        - for instance, the first True in the example list occurred at (0,1). In other words, within the first (0) list, the second (1) item.

        I am also going to convert our unruly nested 'lists' into numpy Arrays for convenience. Although this may not be necessary...
        '''
        exposed = np.array(game.exposed)
        counts = np.array(game.counts)

        exposed_locations = np.where(exposed)

        #Next, we can use these indices to pull out our "counts"
        known = counts[exposed_locations]
        # Now we have locations, and the counts at each of those locations

        print(known)
        print(exposed_locations)

        # Note that what will be shown on the screen is the state of the screen AFTER a choice has been made. So information at this stage will be one move behind.

        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.exposed_squares:
                break
        print('selecting point ({0},{1}) | Move {2}'.format(x, y, self.num_moves)) # The {} and .format() are how you can enter variables into the string
        return x, y

    def update(self, result):
        self.num_moves += 1
        for position in result.new_squares:
            self.exposed_squares.add((position.x, position.y)) # Here is where the program adds a unique x,y pair into the set. So it is keeping track of this info itself...


num_games = 1
config = ms.GameConfig() # sets 3 variables: height, width, and number of mines. These are used throughout the program to define the game.
ai = RandomAI()
viz = ms.GameVisualizer('key') # 'key' if you want enter. Else, number is seconds (must be integer)
results = ms.run_games(config, 1, ai, viz)
if results[0].success:
    print('Success!')
else:
    print('Boom!')
print('Game lasted {0} moves'.format(results[0].num_moves))