from graphics import Window 
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)

    #point_a = Point(0, 0)
    #point_b = Point(10, 10)
    #line_a = Line(point_a, point_b)

    #win.draw_line(line_a, "black")

    cell = Cell(win)

    cell.draw(0, 0, 10, 10)
    cell.draw(10, 10, 20, 20)

    cell.draw(50, 100, 100, 200)

    win.wait_for_close()


main()
