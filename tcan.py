#!/usr/bin/python2

import sys
import space

class Can(object):

    def __init__(self, frame_width, frame_height):
        self.space = space.Space(frame_width, frame_height)


    def print_int(self, x, y, val):
        if type(val) is not int:
            return 
        for c in str(val):
            self.space._putc(x, y, c)
            x += 1


    def print_str(self, x, y, val):
        if type(val) is not str:
            return
        for c in val:
            self.space._putc(x, y, c) 
            x += 1

    
    def move_x(self, s):
        if type(s) is not int:
            return
        self.space._shift_x(s)


    def move_y(self, s):
        self.space._shift_y(s)


    def draw(self):
        self.space._draw_frame()
        

if __name__ == "__main__":
    
    canvas = Canvas(80, 30)
    canvas.print_int(0, 0, 1234)
    canvas.print_str(4, 4, "hello")
    canvas.move_x(2)
    canvas.move_y(3)
    canvas.draw()

