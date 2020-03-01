from collections import deque
from copy import deepcopy
from functools import cmp_to_key
from common import Matrix, Node
import heapq
import sys 
import math

class BFS(Matrix):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maxExploratoryDepth = kwargs.pop('maxExploratoryDepth', 0)
        self.type = "bfs"

    def getMinHWithExploratorySearch(self, currentMatrix, maxDepth):
        stack = deque()
        stack.append(currentMatrix)
        res = self.getHScoreFromString(str(currentMatrix.matrix))
        while stack:
            current = stack.pop()
            if (current.exploratoryDepth <= maxDepth):
                currentH = self.getHScoreFromString(str(current.matrix)) + current.exploratoryDepth
                res = min(res, currentH)

                for i in range (0, self.size):
                    for j in range (0, self.size):
                        newMatrix = self.newBoard(i, j, current.matrix)
                        exploratoryDepth = current.exploratoryDepth + 1
                        serialMatrix = str(newMatrix)
                        n = Node(parent=None, matrix=newMatrix, exploratoryDepth = exploratoryDepth)
                        stack.append(n)
        return res

    def run(self, path):
        h = []
        count = 0

        self.startNode.h = self.getHScoreFromString(str(self.startNode.matrix))
        self.startNode.g = 0
        self.startNode.f = self.startNode.h

        heapq.heappush(h, self.startNode)

        while h:
            current = heapq.heappop(h)
            count = count + 1

            if (count <= self.maxLength):

                path.write(str(current.f) + " " + str(current.g) + " " + str(current.h) + " ")
                path.write(self.matrixToString(current.matrix)+"\n")
                
                if str(current.matrix) == self.expectedResult:
                    return current
                
                for i in range (0, self.size):
                    for j in range (0, self.size):
                        newMatrix = self.newBoard(i, j, current.matrix)
                        depth = current.depth + 1

                        serialMatrix = str(newMatrix)
                        n = Node(parent=current, matrix=newMatrix, move= chr(i + 65) + str(j), depth = depth)
                        n.exploratoryDepth = 0

                        n.h = self.getMinHWithExploratorySearch(n, self.maxExploratoryDepth)
                        n.g = self.getG(n)
                        n.f = self.getF(n)
                        
                        if serialMatrix in self.seen:
                            if self.seen[serialMatrix].f > n.f:
                                self.seen[serialMatrix].parentNode = n.parentNode
                                self.seen[serialMatrix].f = n.f
                                self.seen[serialMatrix].g = n.g
                                self.seen[serialMatrix].h = n.h
                                self.seen[serialMatrix].depth = depth
                        else:
                            heapq.heappush(h,n)
                            self.seen[serialMatrix] = n

    def getHScoreFromString(self, s):
        nbrOnes = 0
        for i in s:
            if i == '1':
                nbrOnes += 1
        if nbrOnes == 1:
            return 3
        if nbrOnes == 2:
            return 2
        else :
            return math.ceil(nbrOnes/5)

    def getF(self, node):
        return node.h + node.g

    def getG(self, node):
        return 0

if __name__ == "__main__":
    bfs = BFS()
    if len(sys.argv) > 1:
        bfs.maxExploratoryDepth = int(sys.argv[1])

    bfs.writeOutput()
