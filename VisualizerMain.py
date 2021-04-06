'''
Main method for the visualizer. 
User can select an appropriate pathfinding algorithm and graph size.
The animation feature is useful in seeing how heuristics alter the search

@author Rafal Muszalski
'''

import Setup as Setup
import Visualizer as Vis
import math
import pygame

'''initializations'''
adj_matrix = []
visited = []
distances =[]
graph_size = 400
disp_size = 1000
starting_node_number = 0
ending_node_number = 335

edge_weight_options = [1] #chose random edge weights, this may cause strange visual paths.
'''end initializations'''


square_size = disp_size / math.sqrt(graph_size)   #the size of the box in visualizer recommended not to exceed 900
square = int(math.sqrt(graph_size))  #helper for matricies

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
                    all_nodes[horizontal.column].Dijkstra(end_node)  #Select Algorithm Here (Dijkstra, Manhattan, Octile, Euclodean)
                    all_nodes[horizontal.column].origin = current_node.row
        
       # pygame.time.wait(150) #Slow down the animation
        Vis.Animate_Algorithm(visited,current_node, start_node, all_nodes)
        Vis.DrawScreen(start_node, end_node, all_nodes, screen, square_size)    
        
    Vis.Animate_Algorithm(visited,current_node, start_node, all_nodes)
    Vis.DrawScreen(start_node, end_node, all_nodes, screen, square_size)
    Vis.Path(all_nodes, end_node.row, start_node.row)     #prints optimal path to console
  
      
def Sort(unvisited): 
    '''Sorts the PQ in order of least distance'''
    unvisited.sort(key=lambda AVertex: AVertex.composite)  
    current_node = unvisited[0]     
    unvisited.remove(current_node)
    visited.append(current_node)
    return current_node
   
pygame.init()
screen = pygame.display.set_mode((disp_size,disp_size))
screen.fill((0,0,0))
pygame.display.set_caption("Dijkstra Visualizer")
pygame.display.update()
                
once = 0 
drawing = False
while True:
    if once == 0:
        start_node, end_node, all_nodes, unvisited = Setup.CreateNodes(square,starting_node_number, ending_node_number)
        Vis.DrawScreen(start_node, end_node, all_nodes, screen, square_size)
        Setup.CreateDistances8D(graph_size, distances, square, edge_weight_options)  #Select Diagonal movement here
        Setup.CreateMatrix(graph_size, adj_matrix, distances)
        Setup.Check_Visualize(graph_size,distances)
        once = once +1
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYUP:
            PathfindingAlgorithm(start_node,end_node,all_nodes,unvisited)  
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False 
        if event.type == pygame.MOUSEMOTION:
            if drawing:
               mousex, mousey = pygame.mouse.get_pos()
               xcord = int(mousex//square_size)
               ycord = int(mousey//square_size)
               Vis.AddBlockade(xcord,ycord,math.inf,all_nodes, graph_size, adj_matrix) 
               Vis.DrawScreen(start_node, end_node, all_nodes, screen, square_size)