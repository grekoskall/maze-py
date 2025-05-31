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

    cell1 = Cell(win)
    cell2 = Cell(win)
    cell3 = Cell(win)

    cell1.draw(50, 100, 100, 150)
    cell2.draw(150, 100, 200, 150)
    cell3.draw(50, 200, 100, 250)


    cell1.draw_move(cell2)

    cell1.draw_move(cell3, True)

    win.wait_for_close()


main()
