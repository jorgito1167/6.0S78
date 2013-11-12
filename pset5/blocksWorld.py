from planner import *
class GrabBlockFromTable(Action):
    actionName = 'grab block from table'
    def resultStateAndCost(self, state, noDel = False):
        (arm,block) = self.args
        if state.check([('free', arm), ('clear', block), ('on-table', block)]):
            return (state.addDelete([('on', block, arm)],
                                    # Deletes
                                    [('free', arm), ('clear', block), ('on-table', block)],
                                    noDel),1)

class GrabBlockFromBlock(Action):
    actionName = 'grab block from block'
    def resultStateAndCost(self, state, noDel = False):
        (arm, block1, block2) = self.args
        if state.check([('free', arm), ('clear', block1), ('on', block1, block2)]):
            return (state.addDelete([('on', block, arm), ('free', block2)],
                                    # Deletes
                                    [('free', arm), ('clear', block), ('on', block1, block2)],
                                    noDel),1)
class PutBlockOnTable(Action):
    actionName = 'put on table'
    def resultStateAndCost(self, state, noDel = False):
        (arm,block) = self.args
        if state.check([('on', block, arm)]):
            return (state.addDelete([('free', arm), ('on-table', block), ('clear', block)],
                                    # Deletes
                                    [('on', block,'arm')],
                                    noDel),1)

class PutBlockOnBlock(Action):
    actionName = 'put on block'
    def resultStateAndCost(self, state, noDel = False):
        (arm, block1, block2) = self.args
        if state.check([('on', block1, arm), ('clear', block2)]):
            return (state.addDelete([('on', block1, block2), ('clear', block1), ('free', arm)],
                                    # Deletes
                                    [('clear', block2), ('on', block1,arm)],
                                    noDel),1)

BLOCKS = ['blockA', 'blockB', 'blockC', 'blockD', 'blockE']
ARMS = ['arm1', 'arm2', 'arm3']

INITIAL = State([('clear', block) for block in BLOCKS] +\
                [('on-table', block) for block in BLOCKS] +\
                [('free', arm) for arm in ARMS])

GOAL0 = [('on-table', 'blockA'),('on', 'blockC', 'blockB'), ('on', 'blockB', 'blockA'), \
         ('on-table', 'blockE'), ('on', 'blockD', 'blockE')]

ACTS0 = [GrabBlockFromTable(args) for args in combinations([ARMS,BLOCKS])] +\
        [GrabBlockFromBlock(args) for args in combinations([ARMS,BLOCKS,BLOCKS])] + \
        [PutBlockOnTable(args) for args in combinations([ARMS,BLOCKS])]+\
        [PutBlockOnBlock(args) for args in combinations([ARMS, BLOCKS,BLOCKS])]

block_world = PlanProblem(INITIAL, GOAL0, ACTS0)
block_world.findPlan(1000)

