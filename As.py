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

    def getF(self, node):
        return node.h + node.g

    def getG(self, node):
        return node.parentNode.f

if __name__ == "__main__":
    n = Node()
    bfs = A()
    if len(sys.argv) > 1:
        bfs.maxExploratoryDepth = int(sys.argv[1])

    input_file = open("input.txt", "r")
    line_nbr = 0

    for line in input_file:
        solution = open(str(line_nbr)+"_A_solution.txt", "w")
        search = open(str(line_nbr)+"_A_search.txt", "w")
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