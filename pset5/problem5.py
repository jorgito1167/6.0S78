from planner import *

BLOCKS = ['blockA', 'blockB', 'blockC']
ARMS = ['arm1']
COLORS = ['red','blue','yellow', 'green']
CANS = ['can1','can2']
BRUSHES = ['brush1']
SPRAYERS = ['sprayer1']
BUCKETS = ['bucket1']

INITIAL5 = State([('on-table', 'blockA'), ('on','blockB','blockA'), ('on','blockC','blockB')]+\
                 [('clear', 'blockC')]+\
                 [('free','arm1')]+\
                 [('on-table','sprayer1'), ('has-color','red','sprayer1'),('on','can1','sprayer1')]+\
                 [('has-color', 'green', 'can1'), ('on','can2','can1')]+\
                 [('has-color', 'blue', 'can2'), ('on-table','can2'),('on', 'bucket1','can2')] +\
                 [('clear','brush1') , ('clean','brush1'), ('on','brush1', 'bucket1')])

GOAL5 = [('free','arm1'),('is-color','blue','blockC'),('is-color','green', 'blockB'),('is-color','red','blockA'),('clean','brush1'),('on', 'blockA','blockB'),('on','blockB','blockC'), ('on-table', 'blockC'), ('on', 'brush1','can1')]


