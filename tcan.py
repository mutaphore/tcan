#!/usr/bin/python2

import sys
import space

class Can(object):

    def __init__(self, frame_width, frame_height, lim_x=1000, lim_y=1000):
        self.space = space.Space(frame_width, frame_height, lim_x, lim_y)


    def print_int(self, coord, int_):
        if type(int_) is not int:
            return 
        for c in str(int_):
            self.space._putc(coord[0], coord[1], c)
            x += 1


    def print_str(self, coord, str_):
        if type(str_) is not str:
            return
        for c in str_:
            self.space._putc(coord[0], coord[1], c) 
            x += 1

    
    def move_frame_x(self, s):
        if type(s) is not int:
            return
        self.space._shift_x(s)


    def move_frame_y(self, s):
        self.space._shift_y(s)


    def draw(self):
        self.space._draw_frame()
        

if __name__ == "__main__":
    
    canvas = Can(80, 30, 80, 30)
    canvas.print_int((0, 0), 1234)
    canvas.print_str((4, 4), "hello")
    canvas.move_frame_x(2)
    canvas.move_frame_y(3)
    canvas.draw()

