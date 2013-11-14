from planner import *

BLOCKS = ['blockA', 'blockB']
ARMS = ['arm1']
COLORS = ['red','blue']
CANS = []
BRUSHES = []
SPRAYERS = ['sprayer1']
BUCKETS = []

INITIAL = State([('on-table', 'blockA'), ('on','blockB','blockA'), ('clear', 'blockB')]+\
                 [('free','arm1')]+\
                 [('clear','sprayer1'), ('on-table','sprayer1'),('has-color','blue','sprayer1')])

GOAL = [('free','arm1'),('is-color','blue', 'blockB')] 

