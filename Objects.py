'''
Class contains all the Object Oriented Features.
Stores the vertex objects as well as edge objects.
In hindisight edge objects were unnecessry and slow down the search.

@author Rafal Muszalski
'''

import math
class Edge:
    def __init__(self,row,column,connected,distance,total,origin):
        self.row = row
        self.column = column
        self.connected = connected
        self.distance = distance #not necessary
        self.total = total #not necessary
        self.origin = origin #not necessary
        
        
class AVertex:
    def __init__(self,row,total,origin,xpos,ypos,color,heuristic,composite):  #row refers to row in adjecency matrix/distance matrix
        self.row = row
        self.total = total
        self.origin = origin
        self.xpos = xpos
        self.ypos = ypos
        self.color = color 
        self.heuristic = heuristic
        self.composite = composite
        
    def Dijkstra(self, end_node):
        self.heuristic = 0
        self.composite = self.total + self.heuristic
        
    def Manhattan(self, end_node):
        dx = abs(self.xpos - end_node.xpos)
        dy = abs(self.ypos - end_node.ypos) 
        self.heuristic = dx +dy 
        self.composite =  self.heuristic + self.total
        
    def Chebyshev(self, end_node):
        dx = abs(self.xpos - end_node.xpos)
        dy = abs(self.ypos - end_node.ypos)
        self.heuristic = max(dx, dy)
        self.composite = self.total + self.heuristic
        
    def Euclidean(self, end_node):
        dx = abs(self.xpos - end_node.xpos)
        dy = abs(self.ypos - end_node.ypos)
        #D = 1
        modifier = int(math.sqrt(dx*dx +dy*dy))
        self.heuristic = modifier
        self.composite = self.heuristic + self.total
         
    def Diagonal(self,end_node):
        D = 1
        D1 = 1.414
        dx = abs(self.xpos - end_node.xpos)
        dy = abs(self.ypos - end_node.ypos)
        self.heuristic =  D*max(dx,dy) + (D1 -D)*min(dx,dy)
        self.composite = self.heuristic + self.total
        