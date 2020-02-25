from collections import deque
from copy import deepcopy
import heapq
from common import Node as Node, Matrix as Matrix

class dfs(Matrix):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self, path):

        stack = deque()

        stack.append(self.startNode)

        while stack:
            current = stack.pop()
            
            if (current.depth <= self.maxDepth):
                path.write("0\t0\t0\t")
                path.write(self.matrixToString(current.matrix)+"\n")
                
                if str(current.matrix) == self.expectedResult:
                    return current
                
                priority = []
                for i in range (0, self.size):
                    for j in range (0, self.size):
                        newMatrix = self.newBoard(i, j, current.matrix)
                        depth = current.depth + 1

                        serialMatrix = str(newMatrix)

                        n = Node(parent=current, matrix=newMatrix, move= chr(i + 65) + str(j), depth = depth)
                        
                        if serialMatrix in self.seen:
                            if self.seen[serialMatrix].depth > depth:
                                self.seen[serialMatrix] = n
                        else:
                            priority.append(n)
                            self.seen[serialMatrix] = n
                            
                priority.sort(key=lambda x: x.matrix, reverse=True)
                stack.extend(priority)

class bfs(Matrix):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self, path):

        stack = deque()

        stack.append(self.startNode)

        while stack:
            current = stack.pop()
            
            if (current.depth <= self.maxDepth):
                path.write("0\t0\t0\t")
                path.write(self.matrixToString(current.matrix)+"\n")
                
                if str(current.matrix) == self.expectedResult:
                    return current
                
                priority = []
                for i in range (0, self.size):
                    for j in range (0, self.size):
                        newMatrix = self.newBoard(i, j, current.matrix)
                        depth = current.depth + 1

                        serialMatrix = str(newMatrix)

                        n = Node(parent=current, matrix=newMatrix, move= chr(i + 65) + str(j), depth = depth)
                        
                        if serialMatrix in self.seen:
                            if self.seen[serialMatrix].depth > depth:
                                self.seen[serialMatrix] = n
                        else:
                            priority.append(n)
                            self.seen[serialMatrix] = n
                            
                priority.sort(key=lambda x: x.matrix, reverse=True)
                stack.extend(priority)

if __name__ == "__main__":
    n = Node()
    dfs = dfs()
    input_file = open("input.txt", "r")
    line_nbr = 0

    for line in input_file:
        solution = open(str(line_nbr)+"_dfs_solution.txt", "w")
        search = open(str(line_nbr)+"_dfs_search.txt", "w")
        dfs.seen = {}
        
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
        
        dfs.startNode = node
        dfs.expectedResult = str(n.createGraph("0"*(size*size), size))
        ans = dfs.run(search)

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