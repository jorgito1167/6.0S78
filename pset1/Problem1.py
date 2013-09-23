from DrawingWindowStandalone import *
import copy
import math
from geometry import *
from utils import *

       
class ProblemState():
    
    def __init__(self, robot_position, time_step):
        self.robot_position = robot_position
        self.time_step = time_step

    def getPossibleNextStates(self):
        position = [0,0,0,0]
        position[0] = Point(self.robot_position.x + 1, self.robot_position.y)
        position[1] = Point(self.robot_position.x - 1, self.robot_position.y)
        position[2] = Point(self.robot_position.x, self.robot_position.y + 1)
        position[3] = Point(self.robot_position.x, self.robot_position.y - 1)
        possible_next_states = []
        for pos in position:
            possible_next_states.append(ProblemState(pos,self.time_step+1))

        return possible_next_states

class Node():
      
      def __init__(self, state, parent=None):
          self.parent = parent
          self.state = state

      def getPossibleNextStates(self):
          return self.state.getPossibleNextStates()

      
class SearchProblem:
    # The State includes the position of the robot, and the time step
    def __init__(self, obstacles, robot, start_state, goal_state):
        self.obstacles = obstacles
        self.robot = robot
        self.robot.setPosition(start_state)
        self.robot.draw()
        self.start_state = ProblemState(start_state,0)
        self.goal_state = ProblemState(goal_state,0)
        window.drawPoint(start_state.x, start_state.y)
        window.drawPoint(goal_state.x, goal_state.y)
        self.nodes_exp = 0
    
    def getStartState(self):
        return self.start_state

    def getSuccessors(self, state):
        self.nodes_exp +=1
        possible_states = state.getPossibleNextStates()
        succesors = []
        for s in possible_states:
            if self.noCollisions(s):
                succesors.append(s)
        return succesors

    def noCollisions(self, state):
        self.robot.setPosition(state.robot_position)
        for obs in self.obstacles:
            obs.setPosition(state.time_step)

        for obs in self.obstacles:
            if robot.intersect(obs.polygon):
                return False
        return True
                
    def isGoalState(self, state):
        return self.goal_state.robot_position.equal(state.robot_position)


def search(problem, priorityQueue, firstGoal = False):
    pq = priorityQueue
    if isinstance(pq,PriorityQueueWithFunction):
        pq.push([problem.getStartState(),0])
        visited = set([])
        while not (pq.isEmpty()):
            plan = pq.pop()
            node = plan[-2]
            #print "Node: " + str(node.robot_position)
            #print "Cost: " + str(plan[-1])
            if problem.isGoalState(node) and firstGoal:
                print "Length of Path: " + str(len(plan[:-1]))
                print "Nodes Expanded: " + str(problem.nodes_exp)
                return plan[:-1]
            
            if not (node.robot_position.toTuple() in visited):
                visited.update([node.robot_position.toTuple()])
                
                for n in problem.getSuccessors(node):
                    
                    tempPlan = plan[:-1]
                    tempPlan.append(n)
                    tempPlan.append(plan[-1]+1)
                    pq.push(tempPlan)
        print "Length of Path: " + str(len(plan[:-1]))
        print "Nodes Expanded: " + str(problem.nodes_exp)
        return plan[:-1]

    else:
        pq.push([problem.getStartState()])
        visited = set([])
        while not (pq.isEmpty()):
            plan = pq.pop()
            node = plan[-1]
            if problem.isGoalState(node) and firstGoal:
                print "Length of Path: " + str(len(plan))
                print "Nodes Expanded: " + str(problem.nodes_exp)
                return plan
            
            if not (node.robot_position.toTuple() in visited):
                visited.update([node.robot_position.toTuple()])
                
                for n in problem.getSuccessors(node):
                    tempPlan = plan[:]
                    tempPlan.append(n)
                    pq.push(tempPlan)
        print "Length of Path: " + str(len(plan))
        print "Nodes Expanded: " + str(problem.nodes_exp)
        return plan

def breadthFirstSearch(problem):
    q = Queue()
    return search(problem, q, True)

def depthFirstSearch(problem):
    s = Stack()
    return search(problem, s, True)

def aStar(problem, heuristic, alpha):

    def priority_function(plan):
        return alpha*heuristic(plan[-2],problem.goal_state) + plan[-1]

    q = PriorityQueueWithFunction(priority_function)
    return search(problem, q, True)

    
if __name__ == "__main__":
    (window,bounds) = makeRoom(0,100,0,100)

    head_points = ([0,0], [3,7], [5,0])
    head = Polygon(window, head_points)
    head.move(Point(10,10))
    '''
    torso_points = ((0,0), (0,7),(5,7), (5,0))
    torso = Polygon(window,torso_points)
    torso.move(Point(1,1))
    '''
    robot = Robot([head])

    robot.extendedX.move(Point(5,15))
    #robot.extendedX.draw()
    robot.extendedY.move(Point(15,5))
    #robot.extendedY.draw()


    vertices1 = ([0,0], [0,30], [60,15])
    poly1 = Polygon(window, vertices1)
    poly1.move(Point(3,20))
    obs1 = Obstacle(poly1)
    obs1.draw()
    obs1.getCSpace(robot)
    obs1.CSpace.draw()

    vertices2 = ((0,0), (0,20),(60,20), (60,0))
    poly2 = Polygon(window, vertices2)
    poly2.move(Point(40, 60))
    obs2 = Obstacle(poly2)
    obs2.draw()

    q = PriorityQueueWithFunction(manhattanDistance)

    problem = SearchProblem([obs1,obs2,bounds], robot, Point(5,5), Point(90,90))

    #drawPath(window, breadthFirstSearch(problem),robot)
    #drawPath(window, depthFirstSearch(problem),robot)
    #drawPath(window, aStar(problem, manhattanDistance,1),robot)
    
    window.tk.mainloop()
