from Node import *
import math

def BFS(node_inicial):
    goal_state = [[1,2,3],[4,5,6],[7,8," "]]

    frontier = []
    visitados = []
    
    if goal_state == node_inicial.State:            
        return node_inicial
    
    frontier.append(node_inicial) 
    
    while len(frontier) > 0:

        curr_node = frontier.pop(0) # Fila FIFO

        if curr_node.State in visitados:
            continue

        if curr_node.empty_tile_y > 0:
            newNode = Left(curr_node)
            if goal_state == newNode.State: # EARLY GOAL TEST
                return newNode
            frontier.append(newNode)

        if curr_node.empty_tile_y < 2:
            newNode = Right(curr_node)
            if goal_state == newNode.State:
                return newNode
            frontier.append(newNode)

        if curr_node.empty_tile_x > 0:
            newNode = Up(curr_node)
            if goal_state == newNode.State:
                return newNode
            frontier.append(newNode)

        if curr_node.empty_tile_x < 2:
            newNode = Down(curr_node)
            if goal_state == newNode.State:
                return newNode
            frontier.append(newNode)

        visitados.append(curr_node.State)
    
    return None

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------

def IDS(node_inicial):
    goal_state = [[1,2,3],[4,5,6],[7,8," "]]
    
    frontier = []
    visitados = []
    limit = 0

    if goal_state == node_inicial.State:            
        return node_inicial
    
    while 1: # Outer loop para incrementar o limit
        frontier.append(node_inicial)
        
        while len(frontier) > 0: #inner loop to run a limited DFS

            curr_node = frontier.pop()
            
            if goal_state == curr_node.State:
                    return curr_node
            
            if (curr_node.State in visitados) or (curr_node.nivel > limit):
                continue
            
            if curr_node.empty_tile_y > 0:
                newNode = Left(curr_node)
                frontier.append(newNode)

            if curr_node.empty_tile_y < 2:
                newNode = Right(curr_node)
                frontier.append(newNode)

            if curr_node.empty_tile_x > 0:
                newNode = Up(curr_node)
                frontier.append(newNode)

            if curr_node.empty_tile_x < 2:
                newNode = Down(curr_node)
                frontier.append(newNode)

            visitados.append(curr_node.State)
        
        #Resetting for next iteration
        frontier.clear()
        visitados.clear()
        limit +=1

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------


def UCS(node_inicial):
    goal_state = [[1,2,3],[4,5,6],[7,8," "]]
    frontier = []
    visitados = []
    Path_cost = [0]
    
    if goal_state == node_inicial.State:            
        return node_inicial
    
    frontier.append(node_inicial)
    
    while len(frontier) > 0:
        idx = 0
        min_path = math.inf
        
        #Finding min_path and index
        for i in range (len(Path_cost)):
            if min_path > Path_cost[i]:
                min_path = Path_cost[i]
                idx = i

        curr_node = frontier.pop(idx)
        Path_cost.pop(idx)
        
        if goal_state == curr_node.State:            
            return curr_node
        
        if curr_node.State in visitados:
            continue

        if curr_node.empty_tile_y > 0:
            newNode = Left(curr_node)
            frontier.append(newNode)
            Path_cost.append(newNode.nivel)

        if curr_node.empty_tile_y < 2:
            newNode = Right(curr_node)
            frontier.append(newNode)
            Path_cost.append(newNode.nivel)

        if curr_node.empty_tile_x > 0:
            newNode = Up(curr_node)
            frontier.append(newNode)
            Path_cost.append(newNode.nivel)

        if curr_node.empty_tile_x < 2:
            newNode = Down(curr_node)
            frontier.append(newNode)
            Path_cost.append(newNode.nivel)

        visitados.append(curr_node.State)
    
    return None

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------

def Greedy(node):
    goal_state = [[1,2,3],[4,5,6],[7,8," "]]
    
    if node == goal_state:
        return node
    
    frontier = []
    heuristic_val = [0]

    frontier.append(node)

    visitados = []
    idx = 0

    while len(frontier) > 0:

        min_value = math.inf

        # finding minimal value of heuristic
        for i in range(len(frontier)):
            if min_value > heuristic_val[i]:
                min_value = heuristic_val[i]
                idx = i

        currNode = frontier.pop(idx)
        heuristic_val.pop(idx)

        if currNode == goal_state:
            return currNode
        
        if currNode.State in visitados:
            continue

        if currNode.empty_tile_y > 0:
            newNode = Left(currNode)
            if goal_state == newNode.State:
                return newNode
            frontier.append(newNode)
            heuristic_val.append(Tiles_Miss(newNode)) # calculating f(n) = h(n)
       
        if currNode.empty_tile_y < 2:
            newNode = Right(currNode)
            if goal_state == newNode.State:
                return newNode
            frontier.append(newNode)
            heuristic_val.append(Tiles_Miss(newNode))
        
        if currNode.empty_tile_x > 0:
            newNode = Up(currNode)
            if goal_state == newNode.State:
                return newNode
            frontier.append(newNode)
            heuristic_val.append(Tiles_Miss(newNode))
        
        if currNode.empty_tile_x <2:
            newNode = Down(currNode)
            if goal_state == newNode.State:
                return newNode
            frontier.append(newNode)
            heuristic_val.append(Tiles_Miss(newNode))


        visitados.append(currNode.State)
        

    return None

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------

def A_estrela(node):
    goal_state = [[1,2,3],[4,5,6],[7,8," "]]
    
    if node == goal_state:
        return node
    
    node_inicial = node
    
    frontier = []
    heuristic_val = [0]

    frontier.append(node)

    visitados = []
    idx = 0

    while len(frontier) > 0:

        min_value = math.inf

        for i in range(len(frontier)):
            if min_value > heuristic_val[i]:
                min_value = heuristic_val[i]
                idx = i

        currNode = frontier.pop(idx)
        heuristic_val.pop(idx)

        if currNode == goal_state:
            return currNode
        
        if currNode.State in visitados:
            continue

        if currNode.empty_tile_y > 0:
            newNode = Left(currNode)
            if goal_state == newNode.State:
                return newNode
            frontier.append(newNode)
            heuristic_val.append(newNode.nivel + Manhattan(newNode)) # calculating f(n) = g(n) + h(n)
       
        if currNode.empty_tile_y < 2:
            newNode = Right(currNode)
            if goal_state == newNode.State:
                return newNode
            frontier.append(newNode)
            heuristic_val.append(newNode.nivel + Manhattan(newNode))
        
        if currNode.empty_tile_x > 0:
            newNode = Up(currNode)
            if goal_state == newNode.State:
                return newNode
            frontier.append(newNode)
            heuristic_val.append(newNode.nivel + Manhattan(newNode))
        
        if currNode.empty_tile_x <2:
            newNode = Down(currNode)
            if goal_state == newNode.State:
                return newNode
            frontier.append(newNode)
            heuristic_val.append(newNode.nivel + Manhattan(newNode))


        visitados.append(currNode.State)

    return None

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------

def hill_Climbing(node_inicial):
    goal_state = [[1,2,3],[4,5,6],[7,8," "]]
    
    if node_inicial.State == goal_state:
        return node_inicial
    
    curr_node = node_inicial
    count = 0
    visitados = []

    while True:
        
        if curr_node.State == goal_state:
                return curr_node
        best_node = None

        neighbors = []
        n_values = []
        
        if curr_node.empty_tile_y > 0:
            newNode = Left(curr_node)
            neighbors.append(newNode)
            n_values.append(Manhattan(newNode))

        if curr_node.empty_tile_y < 2:
            newNode = Right(curr_node)
            neighbors.append(newNode)
            n_values.append(Manhattan(newNode))

        if curr_node.empty_tile_x > 0:
            newNode = Up(curr_node)
            neighbors.append(newNode)
            n_values.append(Manhattan(newNode))

        if curr_node.empty_tile_x < 2:
            newNode = Down(curr_node)
            neighbors.append(newNode)
            n_values.append(Manhattan(newNode))
        
        idx = 0

        best_cost = Manhattan(curr_node)
        
        min = math.inf
        for i in range (len(n_values)):
            if min > n_values[i]:
                idx = i
                min = n_values[i]
        
        best_neighbor = n_values[idx]
            
        if(best_neighbor < best_cost):
            curr_node = neighbors[idx]
        else:
            return curr_node
