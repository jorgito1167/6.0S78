from planner import *
class GrabFromTable(Action):
    actionName = 'grab from table'
    def resultStateAndCost(self, state, noDel = False):
        (arm,block) = self.args
        if state.check([('free', arm), ('clear', block), ('on-table', block)]):
            return (state.addDelete([('on', block, arm)],
                                    # Deletes
                                    [('free', arm), ('clear', block), ('on-table', block)],
                                    noDel),1)

class GrabBlockFromBlock(Action):
    actionName = 'grab from block'
    def resultStateAndCost(self, state, noDel = False):
        (arm, block1, block2) = self.args
        if state.check([('free', arm), ('clear', block1), ('on', block1, block2)]):
            return (state.addDelete([('on', block, arm), ('clear', block2)],
                                    # Deletes
                                    [('free', arm), ('clear', block1), ('on', block1, block2)],
                                    noDel),1)
class PutOnTable(Action):
    actionName = 'put on table'
    def resultStateAndCost(self, state, noDel = False):
        (arm,block) = self.args
        if state.check([('on', block, arm)]):
            return (state.addDelete([('free', arm), ('on-table', block), ('clear', block)],
                                    # Deletes
                                    [('on', block,arm)],
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


BLOCKS = ['blockA', 'blockB']
ARMS = ['arm1']
COLORS = ['red','blue']
CANS = ['can1']
BRUSHES = ['brush1']
SPRAYERS = ['sprayer1']
BUCKETS = ['bucket1']

INITIAL0 = State([('clear', block) for block in BLOCKS] +\
                [('on-table', block) for block in BLOCKS] +\
                [('free', arm) for arm in ARMS])

GOAL0 = [('on-table', 'blockA'),('on', 'blockC', 'blockB'), ('on', 'blockB', 'blockA'), \
         ('on-table', 'blockE'), ('on', 'blockD', 'blockE')]

ACTS1 = [GrabFromTable(args) for args in combinations([ARMS,BLOCKS])] +\
        [GrabFromTable(args) for args in combinations([ARMS,BRUSHES])] +\
        [GrabFromTable(args) for args in combinations([ARMS,SPRAYERS])] +\
        [GrabBlockFromBlock(args) for args in combinations([ARMS,BLOCKS,BLOCKS])] + \
        [PutOnTable(args) for args in combinations([ARMS,BLOCKS])]+\
        [PutOnTable(args) for args in combinations([ARMS,BRUSHES])]+\
        [PutOnTable(args) for args in combinations([ARMS,SPRAYERS])]+\
        [SprayPaint(args) for args in combinations([BLOCKS, SPRAYERS, COLORS, ARMS])] +\
        [LoadBrush(args) for args in combinations([BRUSHES, CANS, COLORS, ARMS])] +\
        [BrushPaint(args) for args in combinations([BLOCKS, COLORS, BRUSHES, ARMS])] +\
        [WashBrush(args) for args in combinations([BRUSHES,COLORS,BUCKETS,ARMS])]+\
        [PutBlockOnBlock(args) for args in combinations([ARMS, BLOCKS,BLOCKS])]

INITIAL1 = State([('on-table', 'blockA'), ('on','blockB','blockA'), ('clear', 'blockB')]+\
                 [('free','arm1')]+\
                 [('clear','sprayer1'), ('on-table','sprayer1'),('has-color','blue','sprayer1')]+\
                 [('clear','can1'),('has-color', 'red', 'can1')]+\
                 [('clear','brush1'),('clean', 'brush1'), ('on-table', 'brush1')]+\
                 [('clear','bucket1')])

GOAL1 = [('free','arm1'),('is-color','blue', 'blockB'),('is-color','red','blockA'),('clean','brush1')]

block_world = PlanProblem(INITIAL1, GOAL1, ACTS1)
block_world.findPlan(100000)

