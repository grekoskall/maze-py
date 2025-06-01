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
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

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

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            cells_to_visit = []
            #print(f"My choice {i}, {j}")
            if i+1 < self.__num_cols and self.__cells[i+1][j].visited == False:
                cells_to_visit.append("right")
            if j+1 < self.__num_rows and self.__cells[i][j+1].visited == False:
                cells_to_visit.append("bottom")
            if i-1 > 0 and self.__cells[i-1][j].visited == False:
                cells_to_visit.append("left")
            if j-1 > 0 and self.__cells[i][j-1].visited == False:
                cells_to_visit.append("top")
            #print(f"My options: {cells_to_visit}")
            if len(cells_to_visit) == 0:
                self.__draw_cell(i, j)
                return 0
            direction = random.choice(cells_to_visit)
            #print(f"I chose: {direction}")
            cells_to_visit.remove(direction)
            if direction == "right":
                cell = self.__cells[i][j]
                self.__cells[i][j].has_right_wall = False
                self.__draw_cell(i, j)
                self.__cells[i+1][j].has_left_wall = False
                self.__draw_cell(i+1, j)
                rec = self.__break_walls_r(i+1, j)
            elif direction == "left":
                cell = self.__cells[i][j]
                self.__cells[i][j].has_left_wall = False
                self.__draw_cell(i, j)
                self.__cells[i-1][j].has_right_wall = False
                self.__draw_cell(i-1, j)
                rec = self.__break_walls_r(i-1, j)
            elif direction == "top":
                cell = self.__cells[i][j]
                self.__cells[i][j].has_top_wall = False
                self.__draw_cell(i, j)
                self.__cells[i][j-1].has_bottom_wall = False
                self.__draw_cell(i, j-1)
                rec = self.__break_walls_r(i, j-1)
            elif direction == "bottom":
                cell = self.__cells[i][j]
                self.__cells[i][j].has_bottom_wall = False
                self.__draw_cell(i, j)
                self.__cells[i][j+1].has_top_wall = False
                self.__draw_cell(i, j+1)
                rec = self.__break_walls_r(i, j+1)

    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False
