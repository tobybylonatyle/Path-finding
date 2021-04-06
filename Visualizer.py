'''
Helper Class which deals with pygame in visualizing 
and animating the pathfinding Algorithm.

@author Rafal Muszalski 
'''

import pygame
import math

color_visited = (102,255,102)
color_path = (30,150,30)

def Animate_Algorithm(visited,current_node, start_node, all_nodes):
    current_path = []
    while current_node != start_node:
        current_path.append(current_node)
        try:
            current_node = all_nodes[current_node.origin]
        except:
            print("had an origin error")
            return
    for vertex in visited:
        vertex.color = color_visited
        
    for vertex in current_path:
        vertex.color = color_path

def AddBlockade(xpos,ypos,obstacle,all_nodes,graph_size, adj_matrix): 
    '''adjusts the adjecency matrix to adds obstacles and walls'''
   
    for t in range(len(all_nodes)):
        if all_nodes[t].xpos == xpos and all_nodes[t].ypos == ypos:
            adj_mat_row = all_nodes[t].row
    if obstacle == 11:    #FUTURE PROOF THAT FOR WALLS AND SAND AND GRASS ETC
        obstacle_color = (255,255,153)   #sand yellow
    elif obstacle == math.inf:
        obstacle_color = (0,0,0)
  
    for i in range(graph_size): #updating adj_matrix with new edges 
        if adj_matrix[i][adj_mat_row].distance != 0:
            adj_matrix[i][adj_mat_row].distance = obstacle
        
        if adj_matrix[adj_mat_row][i].distance != 0:
            adj_matrix[adj_mat_row][i].distance = obstacle
             
    for i in range(len(all_nodes)): #just coloring the box
        if all_nodes[i].xpos == xpos and all_nodes[i].ypos == ypos: #ypos
            all_nodes[i].color = obstacle_color
            all_nodes[i].distance = obstacle
    
def DrawScreen(start_node, end_node, all_nodes, screen, square_size):
    '''draws (refreshes) the animation after each iteration of the algorithm'''
    start_node.color = (50,50,255)
    end_node.color = (255,0,0)
    for t in range(len(all_nodes)):
        xpos = all_nodes[t].xpos
        ypos= all_nodes[t].ypos
        pygame.draw.rect(screen,all_nodes[t].color,(square_size*xpos +1,square_size*ypos + 1,square_size-2,square_size-2))     
    pygame.display.update()
      
def Path(all_nodes, end_node_row, start_node_row):
    '''prints the optimal path to console'''
    path=[]
    via = end_node_row
    print(via)
    while via != start_node_row:
        path.append(via)
        try:
            via = all_nodes[via].origin
        except:
            TypeError
            print("cant get a path")
            return
        
    path.append(via)
    for i in range(len(path)):
        print('node: ',path[len(path) -1 - i],'current distance: ',all_nodes[path[len(path) -1 - i]].total)