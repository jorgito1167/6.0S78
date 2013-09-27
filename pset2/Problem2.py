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
              self.cost = parent.cost + euclideanDistance(parent.state, node.state)
              self.length = parent.length + 1
          else:
              self.cost = 0
              self.length = 0
          self.children = node.children
      def draw(self, color= "black"):
          n = self.node
          p = self.parent
          while p != None:
              s = Segment(self.window,n.state, p.state)
              s.draw(color)
              n = p
              p = p.parent
      

def search(graph, priorityQueue, firstGoal = False):
    pq = priorityQueue
    start = GraphNode(None, graph.start)
    pq.push(start)
    visited = set([])
    while not (pq.isEmpty()):
        node = pq.pop()
    
        if graph.goal.state.equal(node.state) and firstGoal:
            return node
        
        if not (node.state in visited):
            visited.update([node.state])
            
            for n in node.children:
                pq.push(GraphNode(node,n))
    return node

def breadthFirstSearch(graph):
    q = Queue()
    return search(graph, q, True)

def depthFirstSearch(graph):
    s = Stack()
    return search(graph, s, True)

def uniformCostSearch(graph):
    pq = PriorityQueue()
    return search(graph, pq, True)

def aStar(problem, heuristic, alpha):

    def priority_function(plan):
        return alpha*heuristic(plan[-2],problem.goal_state) + plan[-1]

    q = PriorityQueueWithFunction(priority_function)
    return search(problem, q, True)

if __name__ == "__main__":
    (window,bounds) = makeRoom(0,100,0,100)
    head_points = ([0,0], [3,7], [5,0])
    head = Polygon(window, head_points)
    head.move(Point(12,17))

    s = Segment(window, Point(20,10), Point(20,40))
    torso_points = ((0,0), (0,7),(7,7), (7,0))
    torso = Polygon(window,torso_points)
    torso.move(Point(10,10))

    robot = Robot([torso, head])
    #robot.draw()

    robot.setPosition(Point(30,30))
    #robot.draw()
    #robot.extendedX.move(Point(5,15))
    #robot.extendedX.draw()
    #robot.extendedY.move(Point(15,5))
    #robot.extendedY.draw()

    '''
    vertices1 = ([0,0], [0,20], [40,10])
    poly1 = Polygon(window, vertices1)
    poly1.move(Point(40,30))
    obs1 = Obstacle(poly1)
    #obs1.draw('blue')
    obs1.getCSpace(robot)
    obs1.drawCSpace('red')
    '''

    vertices2 = ((0,0), (0,10),(50,10), (50,0))
    poly2 = Polygon(window, vertices2)
    poly2.move(Point(10, 75))
    obs2 = Obstacle(poly2)
    #obs2.draw('blue')
    obs2.getCSpace(robot)
    obs2.drawCSpace('red')

    poly3 = poly2.copy()
    poly3.move(Point(50, 30))
    obs3 = Obstacle(poly3)
    #obs3.draw('blue')
    obs3.getCSpace(robot)
    obs3.drawCSpace('red')

    visi = VisibilityGraph(window,Point(50,3), Point(30,90), [obs3,obs2], robot)

    #visi.nodes[2].drawChildren()
    b = breadthFirstSearch(visi)
    d = depthFirstSearch(visi)
    u = uniformCostSearch(visi)

    b.draw("blue")
    d.draw("black")
    u.draw("yellow")
    print "BFS: "
    print b.cost
    print b.length
    
    print "DFS: "
    print d.cost
    print d.length

    print "UCS: "
    print u.cost
    print u.length
    '''
    #obs1.draw('blue')
    #obs1.getCSpace(robot)
    obs1.drawCSpace('red')
    #obs2.draw('blue')
    #obs2.getCSpace(robot)
    obs2.drawCSpace('red')
    '''
    window.tk.mainloop()
