
# defining cells, their actions/events (nature), numbers, height width,
# basically the file cell.py contain all the information about cells being used in the game
# and all the function which are going to be performed within the game using each cell


from tkinter import Button, Label
import random
import settings
import ctypes       # for generating warning msgs
import sys


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # append the object to the cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        # btn = Button ( location,  width=12, height=4, text=f"{self.x},{self.y}")

        btn = Button( location, width=12, height=4,)
        # defining the events/actions for the button
        btn.bind('<Button-1>', self.left_click_actions)    # <Button-1> is for left click and <Button-3> is for the right click
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    # creating method, which will display how many cells are remaining
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(location, bg='black', fg='white', text=f"Cells Left:{Cell.cell_count}", font=("", 30))
        Cell.cell_count_label_object = lbl

    # methods for events
    def left_click_actions(self, event):
        # print(event)
        # print("Left clicked")
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations, You Won!', 'Game Over', 0)
        # cancel the left & right event if the button is already opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    # function for return the cell object based on the value of x, y
    def get_cell_by_axis(self, x,y):
        for cell in Cell.all:
           if cell.x == x and cell.y == y:
               return cell
    # Read only attribute
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),

        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    # Defining a method that will count the mines surrounded the cell
    # whenever the cell is clicked
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter +=1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1  # Decreasing the cell count on each click, when number is detected not mine
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            if Cell.cell_count_label_object:    # Replace the number of cell count with new count
                 Cell.cell_count_label_object.configure(text=f"Cells Left:{Cell.cell_count}")
        self.cell_btn_object.configure(bg='SystemButtonFace')   # if there Mine detected, then Bg configure color = SystemButtonFace
        self.is_opened = True   # marking the cell as opened


    # function/method for game interruption and display a message
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'Mine Detected', 'Game Over', 0)
        sys.exit()



    def right_click_actions(self, event):
        # print(event)
        # print("Right clicked")
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg='blue')
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg='SystemButtonFace')
            self.is_mine_candidate = False


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cells in picked_cells:
            picked_cells.is_mine = True

    # function will display the cells with their coordinates
    def __repr__(self):
        return f"Cell({self.x},{self.y})"
