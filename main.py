from collections import deque
from copy import deepcopy



class Node:

    def __init__(self, *args, **kwargs):
        self.depth = kwargs.pop('depth', 0)
        self.parentNode = kwargs.pop('parent', None)
        self.matrix = kwargs.pop('matrix', None)
        self.move = kwargs.pop('move', '')


    def createGraph(self, string, size):
        return self._chunkIt(string, size)


    # from stackoverflow
    def _chunkIt(self, seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(list(seq[int(last):int(last + avg)]))
            last += avg

        return out

class dfs:
    seen = {}

    def __init__(self, *args, **kwargs):
        self.size = kwargs.pop('size', None)
        self.solution = kwargs.pop('graph', None)
        self.maxDepth = kwargs.pop('depth', None)
        self.origin = kwargs.pop('origin', None)
        self.matrix = kwargs.pop('matrix', None)
        self.expectedResult = kwargs.pop('expected', None)
        self.solution = None

    def run(self):

        stack = deque()

        stack.append(self.origin)

        while stack:
            current = stack.pop()
            #print(len(stack))
            #if (True):
            if (current.depth <= self.maxDepth):
                for i in range (0, self.size):
                    for j in range (0, self.size):
                        newMatrix = self.newBoard(i, j, current.matrix)
                        depth = current.depth + 1

                        serialMatrix = str(newMatrix)

                        n = Node(parent=current, matrix=newMatrix, move= str(i) + "-" + str(j), depth = depth)


                        if serialMatrix in self.seen:
                            if self.seen[serialMatrix].depth > depth:
                                self.seen[serialMatrix] = n
                        else:
                            stack.append(n)
                            self.seen[serialMatrix] = n
                                               
                        if serialMatrix == self.expectedResult:
                            return n



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

    
n = Node()
graph = n.createGraph("111001011", 3)
#graph = n.createGraph("1001", 2)

dfs = dfs()
dfs.size = 3
dfs.maxDepth = 15
dfs.solution = str(graph)



node = Node()
node.depth = 0
node.matrix = graph
dfs.origin = node

dfs.expectedResult = str(n.createGraph("000000000", 3))
#dfs.expectedResult = str(n.createGraph("0000", 2))
ans = dfs.run()

print(dfs.expectedResult)

res = ans
step = 0
while ans != None:
    print("step:")
    step +=1
    print(ans.move)
    for l in ans.matrix:
        print(l)
    
    ans = ans.parentNode

'''
ans = dfs.newBoard(0, 2, graph)
print()
for l in ans:
    print(l)

print(str(ans))
'''