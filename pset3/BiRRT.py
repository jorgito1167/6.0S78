import random
from utils import *
from TreeNode import *
from CollisionBox import *

class BiRRT():
    window = None
    def __init__(self,start, goal, collision_box, dimensions,metric, node_step = 3, max_count= 10000):
        self.goal = TreeNode(goal,None)
        self.start = TreeNode(start,None)
        self.collision_box = collision_box
        self.dimensions = dimensions
        self.startTreeNodes = [self.start]
        self.goalTreeNodes = [self.goal]
        self.node_step = node_step
        self.max_count = max_count
        self.metric = metric
    
  
    '''
    Produces a random configuration using the dimensions provided
    '''
    def randConfig(self):
        config = []
        for i in xrange(len(self.dimensions)):
            config.append(random.uniform(self.dimensions[i][0],self.dimensions[i][1]))
        return config
    '''
    find the nearest node
    '''
    def findNearNodeBiDir(self, config, root):
        q = Queue()
        q.push(root)
        current_min = self.metric(root.state ,config) 
        min_node = root
        while not q.isEmpty():
            node = q.pop()
            d = self.metric(node.state ,config)
            for c in node.children:
                q.push(c)
            if d < current_min:
                current_min = d
                min_node = node
        return min_node

    '''
    steps the a given configuration towards the a new configuration
    '''
    def step(self, oldConfig, newConfig):
        step = []
        limits = 0
        for i in xrange(len(oldConfig)):
            diff = newConfig[i] - oldConfig[i]
            newDimension = oldConfig[i] + math.copysign(self.dimensions[i][2], diff)
            new_diff = newConfig[i] - newDimension
            if math.copysign(1.0, diff)== math.copysign(1.0,new_diff):
            #if abs(newDimension) < abs(newConfig[i]):
                step.append(newDimension)
            else:
                step.append(oldConfig[i])
                limits += 1
        if limits == len(self.dimensions):
            return newConfig
        else:
            return step
        

    '''
    Once you have the nearest node, step to the new node and check for collisions.
    Then, expand the tree by adding nodes along the path.
    '''
    def stepAndExpand(self, q_near, q_rand, tree):
        next_step = q_near.state    #configuration
        node = q_near     #node
        node_step = self.node_step
        collision = False
      
        while next_step!= q_rand and (not collision):
            next_step = self.step(next_step, q_rand) #configuration
            collision = self.collision_box.collides(next_step)

            if (node_step == 0 or next_step == q_rand) and (not collision):
                node_step = self.node_step

                new = TreeNode(next_step,node)
                tree.append(new)
                node.addChild(new)
                #print node
                #print new
                node = new

            else:
                node_step -= 1 

        if next_step== q_rand and (not collision):
            return (True,node)

        else:
            return (False,node)

    def draw(self):
        for n in self.startTreeNodes:
            n.draw()
        for g in self.goalTreeNodes:
            g.draw()

    def run(self):
        max_count = self.max_count
        tree1 = self.startTreeNodes
        tree2 = self.goalTreeNodes

        while max_count > 0:
            max_count -=1
            #print max_count
            q_rand = self.randConfig()
            q_near_node = self.findNearNodeBiDir(q_rand,tree1[0])
            (connected, q_stop) = self.stepAndExpand(q_near_node, q_rand,tree1)
            if q_stop.state != q_near_node.state:
                q_near_node2 = self.findNearNodeBiDir(q_stop.state, tree2[0])
                (connected2, q_stop2) = self.stepAndExpand(q_near_node2, q_stop.state, tree2)
                if connected2:
                    print self.max_count - max_count
                    print "done!"
                    print self.collision_box.checks
                    return (q_stop,q_stop2)               
            if len(tree1) > len(tree2):
                temptree = tree1
                tree1 = tree2
                tree2 = temptree
