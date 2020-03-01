from collections import deque
from copy import deepcopy
from functools import cmp_to_key
from common import Node
from bfs import BFS
import heapq
import sys

class A(BFS):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = "astar"

    def getG(self, node):
        return node.parentNode.g + 1

if __name__ == "__main__":
    A = A()
    if len(sys.argv) > 1:
        bfs.maxExploratoryDepth = int(sys.argv[1])

    A.writeOutput()