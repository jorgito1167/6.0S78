


class CollisionBox():
    
    def __init__(self, obstacles, robot):
        self.obstacles = obstacles
        self.robot = robot
        self.checks = 0

    def collides(self, config):
        self.checks +=1
        self.robot.setConfig(config)
        for o in self.obstacles:
            if self.robot.intersect(o):
                #self.robot.draw('red')
                return True

        return False
