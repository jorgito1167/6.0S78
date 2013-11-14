from planner import *

BLOCKS = ['blockA', 'blockB']
ARMS = ['arm1']
COLORS = ['red','blue']
CANS = ['can1']
BRUSHES = ['brush1']
SPRAYERS = ['sprayer1']
BUCKETS = ['bucket1']

INITIAL = State([('on-table', 'blockA'), ('on','blockB','blockA'), ('clear', 'blockB')]+\
                 [('free','arm1')]+\
                 [('clear','sprayer1'), ('on-table','sprayer1'),('has-color','blue','sprayer1')]+\
                 [('clear','can1'),('has-color', 'red', 'can1')]+\
                 [('clear','brush1'),('clean', 'brush1'), ('on-table', 'brush1')]+\
                 [('clear','bucket1')])

GOAL = [('free','arm1'),('is-color','blue', 'blockB'),('is-color','red','blockA'),('clean','brush1')]


