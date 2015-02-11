#!/usr/bin/python2

import sys
import os
from threading import Thread, Event

from space import Space, Vec
from getch import Getch

class TextFrame(object):

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
        """Print horizontally"""
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
        """Print vertically"""
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


    def move(self, vec):
        if type(vec) is not Vec:
            return
        self._space.shift_x(vec.x)
        self._space.shift_y(vec.y)

    # TODO: ruler
    # 0----+----1----+----2
    def draw(self, ruler=False):
        self._space.draw_frame()


class KeyListener(Thread):
    
    def __init__(self, frame, key_event, *args, **kwargs):
        kwargs["name"] = "KeyListenerThread"
        super(KeyListener, self).__init__(*args, **kwargs)
        self.frame = frame
        self.key_event = key_event
            
    
    def run(self):
        getc = Getch()
        keys = ['h', 'l', 'j', 'k']
        dirs = [Vec(-1, 0), Vec(1, 0), Vec(0, -1), Vec(0, 1)]
        while True:
            c = getc()
            if c == '\x04':
                print "Exiting"
                break
            self.key_event.clear()
            try:
                index = keys.index(c)
                print index
                vec = dirs[index]
                self.frame.move(vec)
                self.key_event.set()
            except ValueError:
                print "Invalid key"


class Drawer(Thread):
    
    def __init__(self, frame, key_event, *args, **kwargs):
        kwargs["name"] = "DrawerThread"
        super(Drawer, self).__init__(*args, **kwargs)
        self.frame = frame
        self.key_event = key_event


    def run(self):
        while True:
            self.key_event.wait() 
        #    os.system('cls' if os.name == 'nt' else 'clear')    
            self.frame.draw() 


if __name__ == "__main__":
    
    frame = TextFrame(80, 30, lim_x=80, lim_y=30)
    frame.printh(1234, Vec(0, 0))
    frame.printh("hello world my name is Dewei", Vec(75, 4))
    frame.printh(5.52e10, Vec(6, 10))

    frame.draw()

    key_event = Event()
    key_listener = KeyListener(frame, key_event)
    drawer = Drawer(frame, key_event)
    drawer.start()
    key_listener.start()
    key_listener.join()
#        frame.draw()

