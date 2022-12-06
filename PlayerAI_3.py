from BaseAI_3 import BaseAI
from math import *
import sys
import time
import random

sys.setrecursionlimit(100000)

class PlayerAI(BaseAI):

    def getMove(self, grid):
        return random.choice(grid.getAvailableMoves())

