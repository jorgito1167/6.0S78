from planner import *

class RelaxGraphPlan:

    def __init__(self, inital, goal, acts):
        self.initalState = initial
        self.goal = goal
        self.actions = actions
        self.action_layers = []
        self.state_layers = []

   
    def buildGraph(self):
        state = initialState
        while not self.goalTest(state):
            (actions,state) = self.buildLayer(state)
            self.action_layers.append(actions)
            self.state_layers.append(state)
            
        
    def buildLayer(self, state):
        new_assertions = set()
        actions = []
        for a in self.actions:
            result = a.resultStateAndCost(state,noDel=True)
            if result!=None:
                actions.append(a)
                for r in result[0].assertions:
                    new_assertions.update([r])
        new_state = State(list(new_assertions))
        return (actions,new_state)

    def goalTest(self, state):
        return state.check(self.goal)

    def buildPlan(self):
        

