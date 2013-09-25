import math

class Segment:
    
    def __init__(self, window, p1, p2):
        self.window = window
        self.p1 = p1
        self.p2 = p2

    def draw(self, color = "black"):
        self.window.drawLineSeg(self.p1.x, self.p1.y, self.p2.x, self.p2.y, color)

    def copy(self):
        return Segment(self.window, self.p1.copy(), self.p2.copy())

    def moveDelta(self, delta_x, delta_y):
        self.p1.move(delta_x, delta_y)
        self.p2.move(delta_x, delta_y)

    def move(self, p):
        delta_x = p.x - self.p1.x
        delta_y = p.y - self.p1.y
        self.p1.move(p.x,p.y)
        self.p2.moveDelta(delta_x, delta_y)
    def reverse(self):
        p1 = self.p1
        p2 = self.p2
        self.p1 = p2
        self.p2 = p1

    def intersect(self, segment):
        sign = [0,0,0,0]
        sign[0]  = math.copysign(1.0, self.crossProduct(segment.p1))
        sign[1]  = math.copysign(1.0, self.crossProduct(segment.p2))
        sign[2]  = math.copysign(1.0, segment.crossProduct(self.p1))
        sign[3]  = math.copysign(1.0, segment.crossProduct(self.p2))

        if (sign[0] == sign[1]) or (sign[2] == sign[3]):
            return False

        return True

    def crossProduct(self,p):
        u1 = p.x - self.p1.x
        u2 = p.y - self.p1.y
        v1 = self.p2.x - self.p1.x
        v2 = self.p2.y - self.p1.y

        return (u1*v2 - u2*v1)

    def normalAngle(self, side):
        if side == "right":
            x = (self.p2.y - self.p1.y)
            y = -(self.p2.x - self.p1.x)
        else:
            x = -(self.p2.y - self.p1.y)
            y = (self.p2.x - self.p1.x)
        if y<0:
          sign = -1
        else:
          sign = 1

        return sign*math.degrees(math.acos(x/math.sqrt(math.pow(x,2) + math.pow(y,2))))

    def __str__(self):
        return "P1: " + str(self.p1) + " P2: " + str(self.p2)

