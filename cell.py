from point import Point
from line import Line

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        point1 = Point(x1, y1)
        point2 = Point(x1, y2)
        point3 = Point(x2, y1)
        point4 = Point(x2, y2)
        if self.__win != None:
            left_line = Line(point1, point2)
            bottom_line = Line(point2, point4)
            right_line = Line(point3, point4)
            top_line = Line(point1, point3)
            if self.has_left_wall == True:
                self.__win.draw_line(left_line)
            else:
                self.__win.draw_line(left_line, "white")
            if self.has_right_wall == True:
                self.__win.draw_line(right_line)
            else:
                self.__win.draw_line(right_line, "white")
            if self.has_top_wall == True:
                self.__win.draw_line(top_line)
            else:
                self.__win.draw_line(top_line, "white")
            if self.has_bottom_wall == True:
                self.__win.draw_line(bottom_line)
            else:
                self.__win.draw_line(bottom_line, "white")

    def draw_move(self, to_cell, undo=False):
        my_center_x = (self.__x1 + self.__x2) / 2
        my_center_y = (self.__y1 + self.__y2) / 2
        to_center_x = (to_cell.__x1 + to_cell.__x2) / 2
        to_center_y = (to_cell.__y1 + to_cell.__y2) / 2
        point_start = Point(my_center_x, my_center_y)
        point_end = Point(to_center_x, to_center_y)
        line = Line(point_start, point_end)
        if self.__win != None:
            if undo == False:
                self.__win.draw_line(line, "red")
            else:
                self.__win.draw_line(line, "gray")
