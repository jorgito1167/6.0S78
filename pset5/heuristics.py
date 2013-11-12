from utils import *
      

class GraphNode():
      def __init__(self, parent, state, cost, action):
          self.state = state
          self.parent = parent
          self.action = action
          if parent != None:
              self.cost = parent.cost + cost
              self.length = parent.length + 1
          else:
              self.cost = 0
              self.length = 0


def search(initialState, goalTest, stateActions, succesors, priorityQueue, maxNodes):
    pq = priorityQueue
    start = GraphNode(None, initialState, 0, None)
    pq.push(start)
    visited = set([])
    counter = 0
    while (not pq.isEmpty()) and counter < maxNodes:
        node = pq.pop()
        if goalTest(node.state):

            return (extractPlan(node), node.cost)
        
        if not (node.state in visited):
            counter += 1
            visited.update([node.state])
            
            for a in stateActions(node.state):
                newStateCost =  succesors(node.state,a)
                if not (newStateCost[0] in visited):
                    pq.push(GraphNode(node,newStateCost[0],newStateCost[1],a))

def aStar(initialState, goalTest, stateActions, succesors, heuristic = None, maxNodes =1000):
    alpha = 1
    def priority_function(node):
        return alpha*heuristic(node.state) + node.cost

    q = PriorityQueueWithFunction(priority_function)
    return search(initialState, goalTest, stateActions, succesors, q, maxNodes)

def extractPlan(node):
    plan = []
    while node!=None:
        plan.append((node.action,node.state))
        node = node.parent
    plan.reverse()
    return plan

def literalsNotInGoal(state, goal):
    count = 0
    for a in goal:
        if a not in state.assertions:
            count +=1
    return count
