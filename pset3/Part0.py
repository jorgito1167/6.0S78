from DrawingWindowStandalone import *
import copy
import math
from geometry import *

if __name__ == "__main__":
    window = DrawingWindow(700, 700, 0,100, 0, 100, 'test')

    vertices = ((5,5), (5, 11), (20,11), (20,5))
    link1 = Link(window,vertices,(8,8), (18,8))
    link2 = Link(window, vertices,(8,8), (18,8))

    link1.connect(link2)

    link1.draw()
    link2.draw()

    link1.move(Point(30,30))
    link1.draw()
    link2.draw()

    link1.rotate(45)
    link1.draw()
    link2.draw()



    window.tk.mainloop()

  
