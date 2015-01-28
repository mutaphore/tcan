#!/usr/bin/python2

import sys
from space import Space, Vec

class Can(object):

    def __init__(self, frame_width, frame_height, lim_x=1000, lim_y=1000):
        self._space = Space(frame_width, frame_height, lim_x, lim_y)


    def printv(self, val, vec):
        if type(vec) is not Vec:
            return
        for c in str(val):
            self._space.putc(vec.x, vec.y, c) 
            vec.x += 1
            if not self._space.range_x(vec.x):
                vec.x = 0
                vec.y += 1
    

    def move_frame(self, vec):
        if type(vec) is not Vec:
            return
        self._space.shift_x(vec.x)
        self._space.shift_y(vec.y)


    def draw(self):
        self._space.draw_frame()
        

if __name__ == "__main__":
    
    canvas = Can(80, 30, 800, 300)
    canvas.printv(1234, Vec(0, 0))
    canvas.printv("hello world my name is Dewei", Vec(75, 4))
    canvas.printv(5.52e10, Vec(6, 10))
    canvas.move_frame(Vec(10, 0))
    canvas.draw()

