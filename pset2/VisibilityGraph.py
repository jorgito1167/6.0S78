from Robot import *
from Map import *
from Obstacle import *
from Node import *

class VisibilityGraph():

    def __init__(self, window, start, goal, obstacles, robot):
        self.Map = Map(obstacles, robot)
        self.window = window
        self.segments = []
        self.nodes ={}
        self.new_nodes = {}
        self.start = Node(window, start, 0)
        self.goal = Node(window, goal, 0)
        for h in xrange(-60,0):
            self.nodes[h] = self.getNodes(h)

        for a in xrange(-60, 0):
            nodes = self.nodes[a]
            for i in xrange(len(nodes)):
                node1 = nodes[i]
                for j in xrange(len(nodes)):
                    node2 = nodes[j]
                    if not node1.state[0].equal(node2.state[0]):
                        s = Segment(self.window, node1.state[0].copy(), node2.state[0].copy())
                        if self.Map.isSegLegal(s, a):
                            self.segments.append(s)
                            node1.addChild(node2)
                            #s.draw("green")
                #if can connect to different layer do connect
                for t in xrange(-60,0):
                    if self.Map.pointInCSpace(t,node1.state[0]):
                        new_node = Node(self.window,node1.state[0], t)
                        node1.addChild(new_node)
                        if not self.new_nodes.has_key(t):
                            self.new_nodes[t] = [new_node]
                        else:
                            self.new_nodes[t].append(new_node)
                    else:
                        break

            print "done: " + str(a)
        for b in self.new_nodes.keys():
            nodes = self.nodes[b]
            print len(self.new_nodes[b])
            for c in self.new_nodes[b]:
                for j in xrange(len(nodes)):
                    node2 = nodes[j]
                    if not c.state[0].equal(node2.state[0]):
                        s = Segment(self.window, c.state[0].copy(), node2.state[0].copy())
                        if self.Map.isSegLegal(s, b):
                            self.segments.append(s)
                            c.addChild(node2)   
            print "second round: " + str(b)
        print "Done with Visibility Graph"
    
    def getNodes(self,i):
        vertices = self.Map.vertices(i)
        nodes = []

        for v in vertices:
            nodes.append(Node(self.window, v, i))
            
        nodes.append(self.start)
        nodes.append(self.goal)
        return nodes
        
         



