from random import choice
import math
class PathTrim():

    window = None

    def __init__(self, collision_box,dimensions, node1, node2=None):
        self.collision_box = collision_box
        self.collision_box.checks = 0
        self.dimensions = dimensions
        self.nodes = [node1,node2]
        self.path = self.totalPath() 

    def extractPath(self, node):
        path = []
        while node!=None:
            path.append(node.state)
            node = node.parent
        return path

    def totalPath(self):
        path1 = self.extractPath(self.nodes[0])
        path1.reverse()
        path2 = self.extractPath(self.nodes[1]) 
        if path2!=[]:
            path2.pop(0)
        #path2.reverse()
        path1.extend(path2)
        return path1

    def draw(self, color= 'blue'):
        for i in xrange(len(self.path)-1):
            s = self.path[i]
            p = self.path[i+1]
            self.window.drawOval((s[0]-1,s[1]+1),(s[0]+1,s[1]-1), color)
            self.window.drawLineSeg(s[0],s[1],p[0],p[1], color)
        s = self.path[-1]
        self.window.drawOval((s[0]-1,s[1]+1),(s[0]+1,s[1]-1), color)

    def shortcutPath(self):
        c1 = choice(self.path)
        c2 = choice(self.path)
        i1 = self.path.index(c1)
        i2 = self.path.index(c2)

        connected = self.connected(c1,c2)
        
        if connected and i1 != i2:
            chunck1 = self.path[0:min(i1,i2)+1]
            chunck2 = self.path[max(i1,i2):]
            self.path = chunck1 + chunck2

    def shortcut(self,iterations):
        for i in xrange(iterations):
            self.shortcutPath()
        print self.collision_box.checks
    '''
    Takes one step from the old configuration towards the a new configuration
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
    def connected(self, q_old, q_new):
        next_step = q_old    
        collision = False
      
        while next_step!= q_new and (not collision):
            next_step = self.step(next_step, q_new) 
            collision = self.collision_box.collides(next_step)

        if next_step== q_new and (not collision):
            return True

        else:
            return False


