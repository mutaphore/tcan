import sys

class Vec(object):

    def __init__(self, x, y):
        self.x = int(x) 
        self.y = int(y)


class Space(object):

    def __init__(self, frame_width, frame_height, lim_x, lim_y):
        self._lim_x = lim_x
        self._lim_y = lim_y
        self._wd = frame_width
        self._ht = frame_height
        self._x = 0
        self._y = 0
        self._mat = [[None] * self._lim_x for i in range(self._lim_y)]


    def range_x(self, x):
        return x >= 0 and x < self._lim_x


    def range_y(self, y):
        return y >= 0 and y < self._lim_y


    def shift_x(self, s):
        if s > 0 and self._x + self._wd + s > self._lim_x:
            self._x = self._lim_x - self._wd
        elif s < 0 and self._x + s < 0:
            self._x = 0
        else:
            self._x += s


    def shift_y(self, s):
        if s > 0 and self._y + self._ht + s > self._lim_y:
            self._y = self._lim_y - self._ht
        elif s < 0 and self._y + s < 0:
            self._y = 0
        else:
            self._y += s


    def putc(self, x, y, c):
        if type(c) is not str or len(c) > 1:
            return
        if x > self._lim_x:
            x = self._lim_x
        elif x < 0:
            x = 0
        elif y > self._lim_y:
            y = self._lim_y
        elif y < 0:
            y = 0
        self._mat[y][x] = str(c)


    def draw_frame(self): 
        sys.stdout.write("".join(["-"] * (self._wd + 2 )) + "\n")
        for row in self._mat[self._y:(self._y+self._ht)]: 
            line = map(lambda x : " " if x == None else x, row[self._x:(self._x+self._wd)])
            sys.stdout.write("|" + "".join(line) + "|\n")
        sys.stdout.write("".join(["-"] * (self._wd + 2 )) + "\n")