"""
Main class for pathfinding algorithm.
User can select an appropriate pathfinding algorithm, graph size and randomize the edge weights.

@author: Rafal Muszalski
"""
import Setup as Setup
import Visualizer as Visualizer
import math
adj_matrix = []
visited = []
distances =[]
graph_size = 900
starting_node_number = 0
ending_node_number = 100
edge_weight_options = [1,1,2,3,5] #choose random edge weights for the graph

def PathfindingAlgorithm(start_node, end_node, all_nodes, unvisited):
    '''Common Pathfinding Core, Adapts its method to the heuristic and algorithm'''
    current_node = start_node
    while len(unvisited) != 0:
        current_node = Sort(unvisited)

        if current_node == end_node:
            break
            
        for horizontal in adj_matrix[current_node.row]:
            if horizontal.connected == 1:
                section_distance = adj_matrix[horizontal.row][horizontal.column].distance
                new_total = current_node.total + section_distance
                
                
                if new_total < all_nodes[horizontal.column].total:
                    all_nodes[horizontal.column].total = new_total
                    all_nodes[horizontal.column].Manhattan(end_node)           #Select Heuristic Here
                    all_nodes[horizontal.column].origin = current_node.row
    Visualizer.Path(all_nodes, end_node.row, start_node.row)     #prints optimal path in console
                         
def Sort(unvisited): 
    '''Sorts the PQ in order of least distance'''
    unvisited.sort(key=lambda AVertex: AVertex.composite)  
    current_node = unvisited[0]     
    unvisited.remove(current_node)
    visited.append(current_node)
    return current_node
 
square = int(math.sqrt(graph_size))  #for matricies and such  
if __name__ == "__main__":
    start_node, end_node, all_nodes, unvisited = Setup.CreateNodes(square,starting_node_number, ending_node_number)
    Setup.CreateDistances4D(graph_size, distances, square, edge_weight_options)  #Select Diagonal movement here
    Setup.CreateMatrix(graph_size, adj_matrix, distances)
    PathfindingAlgorithm(start_node,end_node,all_nodes,unvisited)          