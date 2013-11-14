from planner import *

class RelaxGraphPlan:

    def __init__(self, initial, goal, acts):
        self.initialState = initial
        self.goal = goal
        self.actions = acts
        self.action_layers = []
        self.state_layers = [initial]
        self.buildGraph()

   
    def buildGraph(self):
        state = self.initialState
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
        plan = []
        goals_not_achieved = self.goal
        for i in xrange(len(self.state_layers)-1,0,-1):
            (yes_g, not_g) = self.goalsInLayer(i-1, goals_not_achieved)
            (acts,pres) = self.selectActions(not_g,i)
            plan.append(acts)
            goals_not_achieved = yes_g + pres
        plan.reverse()
        print len(plan)

    def goalsInLayer(self,i, goals):
        yes_goals = []
        not_goals = []
        state = self.state_layers[i]
        for g in goals:
            if g in state.assertions:
                yes_goals.append(g)
            else:
                not_goals.append(g)
        return (yes_goals, not_goals)

    def selectActions(self, goals,i):
        achieved_goals =[]
        actions = []
        preconditions = []
        for g in goals:
            if not (g in achieved_goals):
                action = self.getAction(g,i)
                achieved_goals += action.posEffects()
                actions.append(action)
                preconditions += action.preconditions()
        return (actions, preconditions)


                
    def getAction(self, g, i):
        actions = self.action_layers[i-1]
        for a in actions:
            if g in a.posEffects():
                return a
        
          
        


    def __str__(self):
        s = ''
        for i in xrange(len(self.state_layers)-1):
            s += "State Layer " + str(i) + ": \n"
            s += str(self.state_layers[i]) +"\n"
            s += "Action Layer " + str(i) + ": \n"
            s += str(self.action_layers[i]) + "\n"
        s += "State Layer " + str(len(self.state_layers)-1) + ": \n"
        s += str(self.state_layers[-1]) +"\n"
        return s
        

