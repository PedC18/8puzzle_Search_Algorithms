import copy

class Node:
    def __init__(self, State, empty_tile_x, empty_tile_y, nivel, parent = None):
        self.State = State
        self.empty_tile_x = empty_tile_x
        self.empty_tile_y = empty_tile_y
        self.nivel = nivel
        self.parent = parent

    def PrintState(self):
        temp = self.State
        result = ""
        for i in range (3):
            for j in range(3):
                result += f"{temp[i][j]} "

            result += "\n"
        
        print(result)

def Right(node):
    temp = 0
    x = node.empty_tile_x
    y = node.empty_tile_y
    nivel = node.nivel
    
    aux = copy.deepcopy(node.State)
    
    temp = aux[x][y+1]
    aux[x][y+1] = aux[x][y]
    aux[x][y] = temp

    newNode = Node(aux,x,y+1,nivel+1)
    return newNode

def Left(node):
    temp = 0
    x = node.empty_tile_x
    y = node.empty_tile_y
    nivel = node.nivel
    
    aux = copy.deepcopy(node.State)
    
    temp = aux[x][y-1]
    aux[x][y-1] = aux[x][y]
    aux[x][y] = temp

    newNode = Node(aux,x,y-1,nivel+1)
    return newNode

def Up(node):
    temp = 0
    x = node.empty_tile_x
    y = node.empty_tile_y
    nivel = node.nivel
    
    aux = copy.deepcopy(node.State)
    
    temp = aux[x-1][y]
    aux[x-1][y] = aux[x][y]
    aux[x][y] = temp

    newNode = Node(aux,x-1,y,nivel+1)
    return newNode

def Down(node):
    temp = 0
    x = node.empty_tile_x
    y = node.empty_tile_y
    nivel = node.nivel
    
    aux = copy.deepcopy(node.State)
    
    temp = aux[x+1][y]
    aux[x+1][y] = aux[x][y]
    aux[x][y] = temp

    newNode = Node(aux,x+1,y,nivel+1)
    return newNode
