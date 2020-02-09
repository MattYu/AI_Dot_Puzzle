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

    def run(self, path):

        stack = deque()

        stack.append(self.origin)

        while stack:
            current = stack.pop()
            #print(len(stack))
            #if (True):
            if (current.depth <= self.maxDepth):
                path.write("0\t0\t0\t")
                path.write(self.matrixToString(current.matrix)+"\n")
                
                priority = []
                for i in range (0, self.size):
                    for j in range (0, self.size):
                        newMatrix = self.newBoard(i, j, current.matrix)
                        depth = current.depth + 1

                        serialMatrix = str(newMatrix)

                        n = Node(parent=current, matrix=newMatrix, move= chr(i + 65) + str(j), depth = depth)
                                               
                        if serialMatrix == self.expectedResult:
                            return n
                        
                        if serialMatrix in self.seen:
                            if self.seen[serialMatrix].depth > depth:
                                self.seen[serialMatrix] = n
                        else:
                            priority.append(n)
                            self.seen[serialMatrix] = n
                            
                priority.sort(key=lambda x: x.matrix, reverse=True)
                stack.extend(priority)

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

    
n = Node()
dfs = dfs()
input_file = open("input.txt", "r")
line_nbr = 0

for line in input_file:
    solution = open(str(line_nbr)+"_dfs_solution.txt", "w")
    search = open(str(line_nbr)+"_dfs_search.txt", "w")
    
    data = line.split()
    size = int(data[0])
    max_d = int(data[1])
    max_l = int(data[2])
    puzzle = data[3]

    graph = n.createGraph(puzzle, size)

    dfs.size = size
    dfs.maxDepth = max_d
    dfs.solution = str(graph)

    node = Node()
    node.depth = 1
    node.move = '0 '
    node.matrix = graph
    
    dfs.origin = node
    dfs.expectedResult = str(n.createGraph("0"*(size*size), size))
    ans = dfs.run(search)

    res = ans
    if ans == None:
        solution.write("No solution")
    while ans != None:
        #content = solution.read()
        #solution.seek(0,0)
        #solution.write('\n'+ ans.move.rstrip('\r\n') + ' ')
        solution.write(ans.move + ' ')
        solution.write(''.join([''.join(element) for element in ans.matrix])+'\n')
        #solution.write(content)

        ans = ans.parentNode
        
    line_nbr += 1
        
input_file.close()
solution.close()
search.close()

'''
ans = dfs.newBoard(0, 2, graph)
print()
for l in ans:
    print(l)

print(str(ans))
'''