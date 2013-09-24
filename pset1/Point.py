class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveDelta(self,delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def move(self, x, y):
        self.x = x
        self.y = y

    def toTuple(self):
        return (self.x,self.y)

    def equal(self, otherPoint):
        if (self.x == otherPoint.x) and (self.y == otherPoint.y):
            return True
        return False

    def copy(self):
        return Point(self.x,self.y)
    
    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x, self.y + otherPoint.y)
    
    def __sub__(self, otherPoint):
        return Point(self.x - otherPoint.x, self.y - otherPoint.y)

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

