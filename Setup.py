'''
Helper Class with methods for creating and managing data strctures
Handles Distance Matrix and Priority Queue.

@author Rafal Muszalski
'''
import Objects as Obj
import math
import random
all_nodes =[]
unvisited =[]

def Check_Visualize(graph_size, distances):
    '''determines whether we can use visualizer'''
    for row in distances:
        if row.count(0) < graph_size -4:
            print("Cannot be Visualized")
            return False
    return True  

def CreateNodes(square,starting_node_number, ending_node_number):
    '''Creates list of all_nodes which are objects that track attributes for dijkstra and for pygame to visualize each node as a square'''
    adj_matrix_row = 0
    for column in range(square):
        for row in range(square):
            vertex = Obj.AVertex(adj_matrix_row, math.inf, (), row,column, (152,152,152), 0, 0) 
            all_nodes.append(vertex)
            unvisited.append(vertex)
            adj_matrix_row += 1
            
    start_node = unvisited[starting_node_number]   
    start_node.total = 0
    end_node = all_nodes[ending_node_number]  
       
    for i in unvisited:
        i.Dijkstra(end_node) #initialises self.heuristics for nodes, otherwise they are null which causes error

    return start_node, end_node, all_nodes, unvisited
              
def CreateDistances4D(graph_size, distances, square, edge_weight_options):
    '''Creates a distance matrix for a grid graph no diagonal movement'''
    for row in range(graph_size):
        distances.append([])
        for column in range(graph_size): 
            distances[row].append(0)
                  
    for node in range(graph_size):     
        if node < graph_size - square:
            distances[node][node +square] = random.choice(edge_weight_options) #'down'              
        if node > square -1:
            distances[node][node - square] = random.choice(edge_weight_options) #'up'      
        if node%square != square -1:
            distances[node][node + 1] = random.choice(edge_weight_options) #'right'      
        if node%square != 0:
            distances[node][node -1] = random.choice(edge_weight_options) #'left'      
    return distances

def CreateDistances8D(graph_size, distances, square, edge_weight_options):
    '''Creates a distance matrix grid graph with diagonal movement'''
    for row in range(graph_size):
        distances.append([])
        for column in range(graph_size):
            distances[row].append(0)
                  
    for node in range(graph_size):       
        if node < graph_size - square:
            distances[node][node +square] = random.choice(edge_weight_options) #'down'  
            if node%square != square -1:
                distances[node][node + square + 1] = random.choice(edge_weight_options) #' down right'    
            if node%square != 0:
                distances[node][node + square - 1] = random.choice(edge_weight_options) #'down left'
            
        if node > square -1:
            distances[node][node - square] = random.choice(edge_weight_options) #'up'
            if node%square != square -1:
                distances[node][node-square + 1] = random.choice(edge_weight_options) #' up right'       
            if node%square != 0:
                distances[node][node-square -1] = random.choice(edge_weight_options) #'up left'                
        if node%square != square -1:
            distances[node][node + 1] = random.choice(edge_weight_options) #'right'     
        if node%square != 0:
            distances[node][node -1] = random.choice(edge_weight_options) #'left'
    return distances
               
def CreateMatrix(graph_size, adj_matrix, distances):
    '''creates the adjecency matrix for bidirectional planar lattice visualizer'''
    for row in range(graph_size):
        adj_matrix.append([])
    for row in range(graph_size):
        for column in range(graph_size):
            if column >= row:
                dist = distances[row][column]
                if dist == 0:
                    connected = 0
                else:
                    connected = 1
                    
                edge = Obj.Edge(row, column, connected , dist , math.inf, ())
                edgeT = Obj.Edge(column, row, connected, dist, math.inf, ())
                
                adj_matrix[row].append(edge)  
                if column != row:
                    adj_matrix[column].append(edgeT)