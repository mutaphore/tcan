#!/usr/bin/python2

import sys
from space import Space, Vec

class Can(object):

    def __init__(self, frame_width, frame_height, lim_x=1000, lim_y=1000,
                 wrap_x=True, wrap_y=False, inc_x=1, inc_y=1):
        if frame_width > lim_x or frame_height > lim_y:
            raise Exception("Frame size smaller than x or y limits")
        self._space = Space(frame_width, frame_height, lim_x, lim_y)
        self._wrap_x = wrap_x
        self._wrap_y = wrap_y
        self._inc_x = inc_x
        self._inc_y = inc_y


    def printh(self, val, vec):
        """Print val horizontally"""
        if type(vec) is not Vec:
            return
        for c in str(val):
            if not self._space.range_x(vec.x) and self._wrap_x:
                vec.x = 0
                vec.y += self._inc_y
            if not self._space.range_y(vec.y) and self._wrap_y:
                vec.y = 0
            self._space.putc(vec.x, vec.y, c) 
            vec.x += self._inc_x


    def printv(self, val, vec):
        """Print val vertically"""
        if type(vec) is not Vec:
            return
        for c in str(val):
            if not self._space.range_y(vec.y) and self._wrap_y:
                vec.y = 0
                vec.x += self._inc_x
            if not self._space.range_x(vec.x) and self._wrap_x:
                vec.x = 0
            self._space.putc(vec.x, vec.y, c)
            vec.y += self._inc_y
            

    def move_frame(self, vec):
        if type(vec) is not Vec:
            return
        self._space.shift_x(vec.x)
        self._space.shift_y(vec.y)

    # TODO: ruler
    def draw(self, ruler=False):
        self._space.draw_frame()
        

if __name__ == "__main__":
    
    canvas = Can(80, 30, 80, 30, inc_x=2)
    canvas.printh(1234, Vec(0, 0))
    canvas.printh("hello world my name is Dewei", Vec(75, 4))
    canvas.printh(5.52e10, Vec(6, 10))
    canvas.move_frame(Vec(10, 0))
    canvas.draw()

