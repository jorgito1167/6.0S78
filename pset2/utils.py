import copy
import math
from DrawingWindowStandalone import *
from geometry import *

class Stack():

    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        if len(self.stack)==0:
            return True
        return False


class Queue():
    def __init__(self):
        self.queue = []
    
    def push(self, item):
        self.queue.insert(0, item)

    def pop(self):
        return self.queue.pop()

    def isEmpty(self):
        if len(self.queue)==0:
            return True
        return False

class PriorityQueue:

    def  __init__(self):
        self.queue = []
        self.priority = []

    def push(self, item):
        self.queue.append(item)
        self.priority.append(item.cost)

    def pop(self):
        mini = self.findMin(self.priority)
        item = self.queue.pop(mini)
        self.priority.pop(mini)
        return item

    def findMin(self,l):
        current = []
        index = None
        for i in xrange(len(l)):
            if l[i] < current:
                current = l[i]
                index = i
        return index
          

    def isEmpty(self):
        return len(self.queue) == 0

class PriorityQueueWithFunction(PriorityQueue):

    def  __init__(self, priorityFunction):
        self.priorityFunction = priorityFunction
        PriorityQueue.__init__(self)     

    def push(self, item):
        PriorityQueue.push(self, item, self.priorityFunction(item))


def manhattanDistance(state, goal_state):
    p1 = state.robot_position
    p2 = goal_state.robot_position
    return abs( p1.x - p2.x ) + abs( p1.y - p2.y )

def euclideanDistance(p1, p2):
    return math.sqrt(math.pow(p2.x-p1.x, 2) + math.pow(p2.y - p1.y, 2))

def drawPath(window, plan, robot):
    for p in plan:
        window.drawPoint(p.robot_position.x, p.robot_position.y)
        robot.setPosition(p.robot_position)
        robot.draw()


def makeRoom(min_x, max_x, min_y, max_y):
    window = DrawingWindow(1200, 700, min_x,max_x, min_y, max_y, 'test')
    outer_points = ((min_x+1,min_y+1), (min_x+1,max_y-1),(max_x-1,max_y-1), (max_x-1,min_y+1))
    
    b = Polygon(window, outer_points)
    bounds = Obstacle(b)
    return (window,bounds)
