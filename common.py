from collections import deque
from copy import deepcopy
from functools import cmp_to_key
import heapq

class Node:

    def __init__(self, *args, **kwargs):
        self.depth = kwargs.pop('depth', 1)
        self.parentNode = kwargs.pop('parent', None)
        self.matrix = kwargs.pop('matrix', None)
        #self.serialMatrix = kwargs.pop('serialMatrix', str(matrix))
        self.move = kwargs.pop('move', '')
        self.f = kwargs.pop('f', 0)
        self.g = kwargs.pop('g', 0)
        self.h = kwargs.pop('h', 0)
        self.exporatoryDepth = kwargs.pop('exploratoryDepth', 0)

    def createGraph(self, string, size):
        return self._chunkIt(string, size)

    def __lt__(self, other):
        if self.f != other.f:
            return self.f < other.f
        else:
            return self.matrix < other.matrix

    
    def _chunkIt(self, seq, num):
        # from stackoverflow. Convert string into 2x2 matrix to facilitate flipping
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(list(seq[int(last):int(last + avg)]))
            last += avg

        return out

class Matrix:
    seen = {}

    def __init__(self, *args, **kwargs):
        self.size = kwargs.pop('size', None)
        self.solution = kwargs.pop('graph', None)
        self.maxDepth = kwargs.pop('depth', None)
        self.startNode = kwargs.pop('startNode', None)
        self.matrix = kwargs.pop('matrix', None)
        self.expectedResult = kwargs.pop('expected', None)
        self.solution = None

    def colorflip(self, color):
        if color == "1":
            return "0"
        return "1"

    def newBoard(self, x, y, m):
        matrix = deepcopy(m)
        left = x - 1
        right = x + 1
        bottom = y + 1
        top = y - 1

        matrix[x][y] = self.colorflip(matrix[x][y])

        if (left >= 0):
            matrix[left][y] = self.colorflip(matrix[left][y])

        if (right < self.size):
            matrix[right][y] = self.colorflip(matrix[right][y])

        if (top >= 0):
            matrix[x][top] = self.colorflip(matrix[x][top])

        if (bottom < self.size):
            matrix[x][bottom] = self.colorflip(matrix[x][bottom])

        return matrix
    
    def matrixToString(self, matrix):
        return ''.join([''.join(element) for element in matrix])
