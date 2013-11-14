from planner import *
BLOCKS = ['blockA', 'blockB', 'blockC']
ARMS = ['arm1']
COLORS = ['red','blue','yellow', 'green']
CANS = ['can1','can2','can3']
BRUSHES = ['brush1']
SPRAYERS = ['sprayer1','sprayer2','sprayer3']
BUCKETS = ['bucket1']

INITIAL = State([('on-table', block) for block in BLOCKS]+\
                 [('clear',block) for block in BLOCKS]+\
                 [('free','arm1')]+\
                 [('clear',sprayer) for sprayer in SPRAYERS]+\
                 [('on-table',sprayer) for sprayer in SPRAYERS]+\
                 [('has-color', 'red', 'sprayer1'), ('has-color', 'green','sprayer2'),('has-color','blue','sprayer3')]+\
                 [('clear',can) for can in CANS]+\
                 [('on-table',can) for can in CANS]+\
                 [('has-color', 'red', 'can1'), ('has-color', 'green','can2'),('has-color','blue','can3')]+\
                 [('clear','brush1'),('clean', 'brush1'), ('on-table', 'brush1')]+\
                 [('clear','bucket1')])

GOAL = [('free','arm1'),('is-color','green','blockC'),('is-color','blue', 'blockB'),('is-color','red','blockA'),('clean','brush1')]


