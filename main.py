from graphics import Window 
from point import Point
from line import Line

def main():
    win = Window(800, 600)

    point_a = Point(0, 0)
    point_b = Point(10, 10)
    line_a = Line(point_a, point_b)

    win.draw_line(line_a, "black")
    win.wait_for_close()

main()
