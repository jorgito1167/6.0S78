from DrawingWindowStandalone import *
import copy
import math
from geometry import *

if __name__ == "__main__":
    window = DrawingWindow(700, 700, 0,100, 0, 100, 'test')

    vertices = ((5,5), (5, 9), (20,9), (20,5))
    link1 = Link(window,vertices,(8,7), (18,7))
    robot = NLinkRobot(link1, 4,True)
    robot.moveBase(Point(50,50))
    robot.draw()
    robot.setPosition((130,30,-60,20))
    robot.draw()
    robot.setPosition((10,10,-10,-20))
    robot.draw()
    robot.setPosition((-90,30,60,30))
    robot.draw()
    robot.setPosition((210,-30,20,90))
    robot.draw()



    window.tk.mainloop()

  
