from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        if seed != None:
            random.seed(seed)

    def __create_cells(self):
        self.__cells = [[0 for j in range(self.__num_rows)] for i in range(self.__num_cols)]
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j] = Cell(self.__win)
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        cell_x1 = self.__x1 + i * self.__cell_size_x
        cell_y1 = self.__y1 + j * self.__cell_size_y
        cell_x2 = cell_x1 + self.__cell_size_x
        cell_y2 = cell_y1 + self.__cell_size_y
        self.__cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        if self.__win != None:
            self._animate()

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols-1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols-1, self.__num_rows - 1)

