import numpy as np
import copy
from Node import *
from SearchAlgorithms import *

a = [[1,5,2],[" ",4,3],[7,8,6]]


node = Node(a,1,0,0)

node.PrintState()

# node_final = BFS(node)
# node_final = IDS(node)
# print(node_final.State)
# print(node_final.nivel)
