from collections import deque
from copy import deepcopy
import heapq
from common import Node as Node, Matrix as Matrix

class dfs(Matrix):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = "dfs"

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
    dfs = dfs()
    dfs.writeOutput()