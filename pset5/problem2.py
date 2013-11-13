
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


