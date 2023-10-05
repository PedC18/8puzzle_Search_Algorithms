import numpy as np
import copy
from Node import *
from SearchAlgorithms import *

a = [[8,0,2],[5,7,3],[1,4,6]]

node = Node(a,0,1,0)

# node_final = BFS(node)
node_final = IDS(node)
print(node_final.State)
print(node_final.nivel)
