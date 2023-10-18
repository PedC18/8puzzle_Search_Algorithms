import numpy as np
import copy
from Node import *
from SearchAlgorithms import *
import sys

Goal = [[1,2,3],[4,5,6],[7,8," "]]

Estado_Inicial = [[0,0,0],[0,0,0],[0,0,0]]

count_arg = 2 # pois os valores começam a partir de argv[2]

#PREENCHE MATRIZ Estado_Inicial
for i in range (3):
    for j in range(3):
        if sys.argv[count_arg] == '0':
            Estado_Inicial[i][j] = " "
            idx_i = i
            idx_j = j
        else:
            Estado_Inicial[i][j] = int(sys.argv[count_arg])
        
        count_arg += 1

node = Node(Estado_Inicial,idx_i,idx_j,0) #inicia node com valores passados

#Escolhe alg a ser usado

if sys.argv[1] == "B":
    node_final = BFS(node)
elif sys.argv[1] == "I":
    node_final = IDS(node)
elif sys.argv[1] == "U":
    node_final = UCS(node)
elif sys.argv[1] == "G":
    node_final = Greedy(node)
elif sys.argv[1] == "A":
    node_final = A_estrela(node)
elif sys.argv[1] == "H":
    node_final = hill_Climbing(node)

num = node_final.nivel
print(num) #Imprime passos na tela

if len(sys.argv) == 12 and sys.argv[11] == "PRINT":
    print() #APENAS PARA FORMATAR A SAÍDA 
    currNode = node_final
    pais = []
    while currNode != None:
        pais.insert(0,currNode)
        currNode = currNode.parent

    for node in pais:
        node.PrintState()
