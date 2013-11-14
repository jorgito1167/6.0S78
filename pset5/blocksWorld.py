from planner import *
from graphplan import *
from problem5 import *
class GrabFromTable(Action):
    actionName = 'grab from table'
    def resultStateAndCost(self, state, noDel = False):
        (arm,block) = self.args
        if state.check([('free', arm), ('clear', block), ('on-table', block)]):
            return (state.addDelete([('on', block, arm)],
                                    # Deletes
                                    [('free', arm), ('clear', block), ('on-table', block)],
                                    noDel),1)
    def preconditions(self):
        (arm,block) = self.args
        return [('free', arm), ('clear', block), ('on-table', block)]

    def posEffects(self):
        (arm,block) = self.args
        return [('on', block, arm)]


class GrabFromObj(Action):
    actionName = 'grab from object'
    def resultStateAndCost(self, state, noDel = False):
        (arm, block1, block2) = self.args
        if state.check([('free', arm), ('clear', block1), ('on', block1, block2)]):
            return (state.addDelete([('on', block1, arm), ('clear', block2)],
                                    # Deletes
                                    [('free', arm), ('clear', block1), ('on', block1, block2)],
                                    noDel),1)
    def preconditions(self):
        (arm,block1,block2) = self.args
        return [('free', arm), ('clear', block1), ('on', block1, block2)]

    def posEffects(self):
        (arm,block1,block2) = self.args
        return [('on', block1, arm), ('clear', block2)]
        
class PutOnTable(Action):
    actionName = 'put on table'
    def resultStateAndCost(self, state, noDel = False):
        (arm,block) = self.args
        if state.check([('on', block, arm)]):
            return (state.addDelete([('free', arm), ('on-table', block), ('clear', block)],
                                    # Deletes
                                    [('on', block,arm)],
                                    noDel),1)
    def preconditions(self):
        (arm,block) = self.args
        return [('on', block, arm)]
    def posEffects(self):
        (arm,block) = self.args
        return [('free', arm), ('on-table', block), ('clear', block)]

class Stack(Action):
    actionName = 'stack'
    def resultStateAndCost(self, state, noDel = False):
        (arm, block1, block2) = self.args
        if state.check([('on', block1, arm), ('clear', block2)]):
            return (state.addDelete([('on', block1, block2), ('clear', block1), ('free', arm)],
                                    # Deletes
                                    [('clear', block2), ('on', block1,arm)],
                                      noDel),1)
    def preconditions(self):
        (arm,block1,block2) = self.args
        return [('on', block1, arm), ('clear', block2)]
    def posEffects(self):
        (arm,block1,block2) = self.args
        return [('on', block1, block2), ('clear', block1), ('free', arm)]

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
    def preconditions(self):
        (block, sprayer, color, arm) = self.args
        return [('has-color', color, sprayer),('on', sprayer, arm),('on-table', block), ('clear', block)]   
    def posEffects(self):
        (block, sprayer, color, arm) = self.args
        return [('is-color', color, block)]

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
    def preconditions(self):
        (brush, can, color, arm) = self.args
        return [('clean', brush), ('has-color', color, can),('on', brush, arm), ('clear', can)]

    def posEffects(self):
        (brush, can, color, arm) = self.args
        return [('has-color', color, brush)] 

class BrushPaint(Action):
    actionName = 'brush paint'
    def resultStateAndCost(self, state, noDel = False):
        (block, color, brush, arm) = self.args
        if state.check([('has-color', color, brush),('on', brush, arm), ('on-table', block), ('clear', block)]): 
            return (state.addDelete([('is-color', color, block)],
                                    # Deletes
                                    [],
                                    noDel),1)
    def preconditions(self):
        (block, color, brush, arm) = self.args
        return [('has-color', color, brush),('on', brush, arm), ('on-table', block), ('clear', block)]
    def posEffects(self):
        (block, color, brush, arm) = self.args
        return [('is-color', color, block)]


class WashBrush(Action):
    actionName = 'wash brush'
    def resultStateAndCost(self, state, noDel = False):
        (brush, color, bucket, arm) = self.args
        if state.check([('has-color', color, brush),('on', brush, arm),('clear', bucket)]):

            return (state.addDelete([('clean',brush)],
                                    # Deletes
                                    [('has-color', color, brush)],
                                    noDel),1)

    def preconditions(self):
        (brush, color, bucket, arm) = self.args
        return [('has-color', color, brush),('on', brush, arm),('clear', bucket)]
    def posEffects(self):
        (brush, color, bucket, arm) = self.args
        return [('clean',brush)]



ACTS = [GrabFromTable(args) for args in combinations([ARMS,BLOCKS])] +\
        [GrabFromTable(args) for args in combinations([ARMS,BRUSHES])] +\
        [GrabFromTable(args) for args in combinations([ARMS,SPRAYERS])] +\
        [GrabFromTable(args) for args in combinations([ARMS,CANS])] +\
        [GrabFromTable(args) for args in combinations([ARMS,BUCKETS])] +\
        [GrabFromObj(args) for args in combinations([ARMS,BLOCKS,BLOCKS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,CANS,BLOCKS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BLOCKS,CANS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BRUSHES,BLOCKS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BLOCKS,BRUSHES])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BLOCKS,SPRAYERS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,SPRAYERS,BLOCKS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BUCKETS,BLOCKS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BLOCKS,BUCKETS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,CANS,CANS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,CANS,BRUSHES])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BRUSHES,CANS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,CANS,SPRAYERS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,SPRAYERS,CANS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,CANS,BUCKETS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BUCKETS,CANS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BRUSHES,BRUSHES])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BRUSHES,SPRAYERS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,SPRAYERS,BRUSHES])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BRUSHES,BUCKETS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BUCKETS,BRUSHES])] + \
        [GrabFromObj(args) for args in combinations([ARMS,SPRAYERS,SPRAYERS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,SPRAYERS,BUCKETS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BUCKETS,SPRAYERS])] + \
        [GrabFromObj(args) for args in combinations([ARMS,BUCKETS,BUCKETS])] + \
        [PutOnTable(args) for args in combinations([ARMS,BLOCKS])]+\
        [PutOnTable(args) for args in combinations([ARMS,BRUSHES])]+\
        [PutOnTable(args) for args in combinations([ARMS,SPRAYERS])]+\
        [PutOnTable(args) for args in combinations([ARMS,CANS])]+\
        [PutOnTable(args) for args in combinations([ARMS,BUCKETS])]+\
        [SprayPaint(args) for args in combinations([BLOCKS, SPRAYERS, COLORS, ARMS])] +\
        [LoadBrush(args) for args in combinations([BRUSHES, CANS, COLORS, ARMS])] +\
        [BrushPaint(args) for args in combinations([BLOCKS, COLORS, BRUSHES, ARMS])] +\
        [WashBrush(args) for args in combinations([BRUSHES,COLORS,BUCKETS,ARMS])]+\
        [Stack(args) for args in combinations([ARMS, BLOCKS,BLOCKS])]+\
        [Stack(args) for args in combinations([ARMS, BRUSHES,CANS])]



block_world = PlanProblem(INITIAL, GOAL, ACTS)
block_world.findPlan(10000000)
g = RelaxGraphPlan(INITIAL, GOAL, ACTS)
print g
g.buildPlan()

