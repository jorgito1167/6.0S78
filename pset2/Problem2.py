from DrawingWindowStandalone import *
import copy
import math
from geometry import *
from utils import *
from Map import *
from VisibilityGraph import *
from Node import *
      

class GraphNode():
      def __init__(self, parent, node):
          self.state = node.state
          self.parent = parent
          self.node = node
          self.window = self.node.window
          if parent != None:
              self.cost = parent.cost + euclideanDistance(parent.state[0], node.state[0])
              self.length = parent.length + 1
              self.priority = self.cost
          else:
              self.cost = 0
              self.priority = 0
              self.length = 0
          self.children = node.children
      def draw(self, color= "black"):
          n = self.node
          p = self.parent
          while p != None:
              s = Segment(self.window,n.state[0], p.state[0])
              s.draw(color)
              n = p
              p = p.parent
      

def search(graph, priorityQueue, firstGoal = False):
    pq = priorityQueue
    start = GraphNode(None, graph.start)
    pq.push(start)
    visited = set([])
    counter = 0
    while not (pq.isEmpty()):
        node = pq.pop()
        if graph.goal.state[0].equal(node.state[0]) and firstGoal:
            return (node, counter)
        
        if not (node.state in visited):
            counter += 1
            visited.update([node.state])
            
            for n in node.children:
                pq.push(GraphNode(node,n))
    return (node, counter)

def breadthFirstSearch(graph):
    q = Queue()
    return search(graph, q, True)

def depthFirstSearch(graph):
    s = Stack()
    return search(graph, s, True)

def uniformCostSearch(graph):
    pq = PriorityQueue()
    return search(graph, pq, True)

def aStar(graph, heuristic, alpha):

    def priority_function(node):
        return alpha*heuristic(node.state[0],graph.start.state[0]) + node.cost

    q = PriorityQueueWithFunction(priority_function)
    return search(graph, q, True)

if __name__ == "__main__":
    (window,bounds) = makeRoom(0,100,0,100)
    head_points = ([0,0], [0,3], [2,1])
    head = Polygon(window, head_points)
    head.move(Point(17,8))

    s = Segment(window, Point(20,10), Point(20,40))
    torso_points = ((0,0), (0,1),(7,1), (7,0))
    torso = Polygon(window,torso_points)
    torso.move(Point(10,10))
    '''
    s = Segment(window, Point (50, 50), Point(70, 50))
    s.draw()
    for n in [30, 60, 90]:
        s.rotate(n)
        print s.p2
        s.draw()
        s.rotate(-n)
    pol = torso.copy()
    pol.draw()
    pol.rotate(60)
    pol.draw()
    '''
    robot = Robot([torso, head])

    #robot.draw()
    
    robot.setPosition(Point(3,3))
    robot.draw()
    robot.rotate(-60)
    #robot.draw()
    #robot.extendedX.move(Point(5,15))
    #robot.extendedX.draw()
    #robot.extendedY.move(Point(15,5))
    #robot.extendedY.draw()
    '''
    vertices1 = ([0,0], [0,15], [30,7])
    poly1 = Polygon(window, vertices1)
    poly1.move(Point(10, 20))
    obs1 = Obstacle(poly1)
    #obs1.draw('blue')
    obs1.getCSpace(robot)
    obs1.drawCSpace('red')

    vertices2 = ((0,0), (0,10),(30,10), (30,0))
    poly2 = Polygon(window, vertices2)
    poly2.move(Point(10, 75))
    obs2 = Obstacle(poly2)
    #obs2.draw('blue')
    obs2.getCSpace(robot)
    obs2.drawCSpace('red')

    poly3 = poly2.copy()
    poly3.move(Point(30, 46))
    obs3 = Obstacle(poly3)
    #obs3.draw('blue')
    obs3.getCSpace(robot)
    obs3.drawCSpace('red')

    poly4 = poly3.copy()
    poly4.move(Point(60, 15))
    obs4 = Obstacle(poly4)
    #obs4.draw('blue')
    obs4.getCSpace(robot)
    obs4.drawCSpace('red')

    vertices5 = ((0,0), (10,10),(20,10), (30,0), (20,-10), (10, -10))
    poly5 = Polygon(window, vertices5)
    poly5.move(Point(70, 70))
    obs5 = Obstacle(poly5)
    #obs5.draw('blue')
    obs5.getCSpace(robot)
    obs5.drawCSpace('red')
    '''
    vertices1 = ([0,0], [0,15], [40,15], [40,0])
    poly1 = Polygon(window, vertices1)
    poly1.move(Point(15, 50))
    obs1 = Obstacle(poly1)
    obs1.draw('blue')
    obs1.getCSpace(robot)
    obs1.drawCSpace('red')
    
    poly2 = poly1.copy()
    poly2.move(Point(60, 50))
    obs2 = Obstacle(poly2)
    obs2.draw('blue')
    obs2.getCSpace(robot)
    obs2.drawCSpace('red')
    '''
    visi = VisibilityGraph(window,Point(80,80), Point(50,5), [obs1,obs2], robot)
    #window.drawPoint(3,3,'black')
    #window.drawPoint(65,55, 'orange')
    #visi.nodes[2].drawChildren()
    (b, bcount) = breadthFirstSearch(visi)
    print "Done with BFS"
    (d, dcount) = depthFirstSearch(visi)
    print "Done with DFS"
    (u, ucount) = uniformCostSearch(visi)
    print "Done with UCS"
    (a, acount) = aStar(visi, euclideanDistance, 1)
    print "Done with ASTAR"
    (ap,apcount) = aStar(visi, euclideanDistance, 10000)



    b.draw("blue")
    d.draw("black")
    u.draw("orange")
    a.draw("yellow")
    print "BFS: "
    print b.cost
    print b.length
    print bcount
    
    print "DFS: "
    print d.cost
    print d.length
    print dcount

    print "UCS: "
    print u.cost
    print u.length
    print ucount

    print "A STAR: "
    print a.cost
    print a.length
    print acount
  
    print "A STAR(non admissible): "
    print ap.cost
    print ap.length
    print apcount
    '''
    window.tk.mainloop()
    
