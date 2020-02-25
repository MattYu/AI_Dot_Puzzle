from collections import deque
from copy import deepcopy
from functools import cmp_to_key
from common import Matrix, Node
import heapq
import sys 

class BFS(Matrix):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maxExploratoryDepth = kwargs.pop('maxExploratoryDepth', 0)

    def getMinHWithExploratorySearch(self, currentMatrix, maxDepth):
        stack = deque()
        stack.append(currentMatrix)
        res = self.getHScoreFromString(str(currentMatrix.matrix))
        while stack:
            current = stack.pop()
            if (current.exporatoryDepth <= maxDepth):
                res = min(res, self.getHScoreFromString(str(current.matrix)))

                for i in range (0, self.size):
                    for j in range (0, self.size):
                        newMatrix = self.newBoard(i, j, current.matrix)
                        exploratoryDepth = current.exporatoryDepth + 1
                        serialMatrix = str(newMatrix)
                        n = Node(parent=None, matrix=newMatrix, exploratoryDepth = exploratoryDepth)
                        stack.append(n)
        return res

    def run(self, path):
        h = []

        self.startNode.f = self.getHScoreFromString(str(self.startNode.matrix))
        self.startNode.h = self.startNode.f
        self.startNode.g = 0

        heapq.heappush(h, self.startNode)

        while h:
            current = heapq.heappop(h)

            if (current.depth <= self.maxDepth):

                path.write(str(current.f) + "\t" + str(current.h) + "\t" + str(current.g) + "\t")
                path.write(self.matrixToString(current.matrix)+"\n")
                
                if str(current.matrix) == self.expectedResult:
                    return current
                
                for i in range (0, self.size):
                    for j in range (0, self.size):
                        newMatrix = self.newBoard(i, j, current.matrix)
                        depth = current.depth + 1

                        serialMatrix = str(newMatrix)
                        n = Node(parent=current, matrix=newMatrix, move= chr(i + 65) + str(j), depth = depth)
                        n.maxExploratoryDepth = 0

                        n.h = self.getMinHWithExploratorySearch(n, self.maxExploratoryDepth)
                        n.g = self.getG(n)
                        n.f = self.getF(n)
                        
                        if serialMatrix in self.seen:
                            if self.seen[serialMatrix].f > n.f:
                                self.seen[serialMatrix].parent = n.parent
                                self.seen[serialMatrix].f = n.f
                                self.seen[serialMatrix].g = n.g
                                self.seen[serialMatrix].h = n.h
                                self.seen[serialMatrix].depth = depth
                        else:
                            heapq.heappush(h,n)
                            self.seen[serialMatrix] = n

    def getHScoreFromString(self, s):
        res = 0
        for i in s:
            if i == '1':
                res += 1
        return res

    def getF(self, node):
        return node.h

    def getG(self, node):
        return 0

if __name__ == "__main__":
    n = Node()
    bfs = BFS()
    if len(sys.argv) > 1:
        bfs.maxExploratoryDepth = int(sys.argv[1])

    input_file = open("input.txt", "r")
    line_nbr = 0

    for line in input_file:
        solution = open(str(line_nbr)+"_bfs_solution.txt", "w")
        search = open(str(line_nbr)+"_bfs_search.txt", "w")
        bfs.seen = {}
        
        data = line.split()
        size = int(data[0])
        max_d = int(data[1])
        max_l = int(data[2])
        puzzle = data[3]

        graph = n.createGraph(puzzle, size)

        bfs.size = size
        bfs.maxDepth = max_d
        bfs.solution = str(graph)

        node = Node()
        node.depth = 1
        node.move = '0 '
        node.matrix = graph
        
        bfs.startNode = node
        bfs.expectedResult = str(n.createGraph("0"*(size*size), size))
        ans = bfs.run(search)

        res = ans
        path = []
        if ans == None:
            solution.write("No solution")
        while ans != None:
            path.append(ans)
            ans = ans.parentNode
            
        for sol in reversed(path):
            solution.write(sol.move + ' ')
            solution.write(''.join([''.join(element) for element in sol.matrix])+'\n')
            
        line_nbr += 1
            
    input_file.close()
    solution.close()
    search.close()
