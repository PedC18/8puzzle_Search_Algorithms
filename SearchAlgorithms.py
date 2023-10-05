from Node import *

def BFS(node_inicial):
    goal_state = [[1,2,3],[4,5,6],[7,8,0]]
    frontier = []
    visitados = []
    
    if goal_state == node_inicial.State:            
        return node_inicial
    frontier.append(node_inicial)
    
    while len(frontier) > 0:

        curr_node = frontier.pop(0)
        if curr_node in visitados:
            continue

        if curr_node.empty_tile_y > 0:
            newNode = Left(curr_node)
            if goal_state == newNode.State:
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

        visitados.append(curr_node)
    
    return "Deu ruim"


def IDS(node_inicial):
    goal_state = [[1,2,3],[4,5,6],[7,8,0]]
    frontier = []
    visitados = []
    
    limit = 0

    if goal_state == node_inicial.State:            
        return node_inicial
    
    while 1:
        frontier.append(node_inicial)
        
        while len(frontier) > 0:

            curr_node = frontier.pop(len(frontier)-1)
            
            if (curr_node in visitados) or (curr_node.nivel > limit):
                continue
            

            if curr_node.empty_tile_y > 0:
                newNode = Left(curr_node)
                if goal_state == newNode.State:
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

            visitados.append(curr_node)
        
        frontier.clear()
        visitados.clear()
        limit +=1
