import random


class Monster:
    def __init__(self, nRows, nCols, maxSpeed):
        self.nRows = nRows
        self.nCols = nCols
        self.myRow = random.randrange(self.nRows)  # save away
        self.myCol = random.randrange(self.nCols)  # save away
        self.mySpeedX = random.randrange(self.nRows)  # chooses a random row
        self.mySpeedY = random.randrange(self.nCols)  # chooses a random column
        # Set other instances variables like health, power, etc.

    def move(self):
        self.myRow = (self.myRow + self.mySpeedY) % self.nRows
        self.myCol = (self.myCol + self.mySpeedX) % self.nCols


# Main code

N_MONSTERS = 20
N_ROWS = 100
N_COLS = 200
MAX_SPEED = 4

monstersList = []
for i in range(N_MONSTERS):
    oMonster = Monster(N_ROWS, N_COLS, MAX_SPEED)
    monstersList.append(oMonster)

print(monstersList)
