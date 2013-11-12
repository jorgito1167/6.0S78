from planner import *
class GrabFromTable(Action):
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
class PutOnTable(Action):
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

class SprayPaint(Action):
    actionName = 'spray paint'
    def resultStateAndCost(self, state, noDel = False):
        (block, sprayer, color, arm) = self.args
        if state.check([('has-color', color, sprayer),('on', sprayer, arm),
                                    ('on-table', block), ('clear', block)]):

            return (state.addDelete([('is-color', color, block)],
                                    # Deletes
                                    [],
                                    noDel),1)

class LoadBrush(Action):
    actionName = 'load brush'
    def resultStateAndCost(self, state, noDel = False):
        (brush, can, color, arm) = self.args
        if state.check([('clean', brush), ('has-color', color, can),('on', brush, arm), 
                        ('clear', can)]):

            return (state.addDelete([('has-color', color, brush)],
                                    # Deletes
                                    [('clean',brush)],
                                    noDel),1)

class BrushPaint(Action):
    actionName = 'brush paint'
    def resultStateAndCost(self, state, noDel = False):
        (block, color, brush, arm) = self.args
        if state.check([('has-color', color, brush),('on', brush, arm), ('on-table', block), ('clear', block)]): 
            return (state.addDelete([('is-color', color, block)],
                                    # Deletes
                                    [],
                                    noDel),1)

class WashBrush(Action):
    actionName = 'wash brush'
    def resultStateAndCost(self, state, noDel = False):
        (brush, color, bucket, arm) = self.args
        if state.check([('has-color', color, brush),('on', brush, arm),('clear', bucket)]):

            return (state.addDelete([('clean',brush)],
                                    # Deletes
                                    [('has-color', color, brush)],
                                    noDel),1)







BLOCKS = ['blockA', 'blockB', 'blockC', 'blockD', 'blockE']
ARMS = ['arm1']
COLOR = ['red','blue','green', 'yellow']
CANS = ['can1', 'can2', 'can3']
BRUSHES = ['brush1', 'brush2']
SPRAYERS = ['sprayer1', 'sprayer2', 'sprayer3']
BUCKET = ['bucket1']

INITIAL0 = State([('clear', block) for block in BLOCKS] +\
                [('on-table', block) for block in BLOCKS] +\
                [('free', arm) for arm in ARMS])

GOAL0 = [('on-table', 'blockA'),('on', 'blockC', 'blockB'), ('on', 'blockB', 'blockA'), \
         ('on-table', 'blockE'), ('on', 'blockD', 'blockE')]

ACTS0 = [GrabFromTable(args) for args in combinations([ARMS,BLOCKS])] +\
        [GrabBlockFromBlock(args) for args in combinations([ARMS,BLOCKS,BLOCKS])] + \
        [PutOnTable(args) for args in combinations([ARMS,BLOCKS])]+\
        [PutBlockOnBlock(args) for args in combinations([ARMS, BLOCKS,BLOCKS])]

INITIAL1 = State([(

block_world = PlanProblem(INITIAL, GOAL0, ACTS0)
block_world.findPlan(1000)

