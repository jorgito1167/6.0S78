


class CollisionBox():
    
    def __init__(self, obstacles, robot):
        self.obstacles = obstacles
        self.robot = robot.copy()

    def collides(self, config):
        self.robot.setConfig(config)
        for o in self.obstacles:
            if self.robot.intersect(o):
                self.robot.draw('red')
                return True

        return False
