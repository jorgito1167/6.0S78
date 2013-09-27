from Robot import *
from Map import *
from Obstacle import *
from Node import *

class VisibilityGraph():

    def __init__(self, window, start, goal, obstacles, robot):
        self.Map = Map(obstacles, robot)
        self.window = window
        self.segments = []
        self.nodes =[]

        self.start = Node(window, start)
        self.goal = Node(window, goal)
        self.getNodes()
        for i in xrange(len(self.nodes)):
            node1 = self.nodes[i]
            for j in xrange(len(self.nodes)):
                node2 = self.nodes[j]
                if not node1.state.equal(node2.state):
                    s = Segment(self.window, node1.state.copy(), node2.state.copy())
                    if self.Map.isSegLegal(s):
                        self.segments.append(s)
                        node1.addChild(node2)
                        s.draw("green")
    
    def getNodes(self):
        vertices = self.Map.vertices()
        self.nodes = []

        for v in vertices:
            self.nodes.append(Node(self.window, v))
            
        self.nodes.append(self.start)
        self.nodes.append(self.goal)
        
         



