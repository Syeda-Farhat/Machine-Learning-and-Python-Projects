from tkinter import *
import settings
import utils
from cell import Cell
root = Tk()

root.geometry('1440x750')       # adjusting the size of the window
root.title("The Mines Game")
root.configure(bg="grey")

# divide the window according to the requirements into three sections, Top, Left and the center one for the game
top_frame = Frame(root, bg='grey', width=settings.WIDTH, height=utils.height_prct(25))
top_frame.place(x=0, y=0)

game_title = Label(top_frame, bg='black', fg='white', text='The Mines Game', font=('', 40))
game_title.place(x=utils.width_prct(25), y=0)

left_frame = Frame(root, bg='grey', width=utils.width_prct(25), height=utils.height_prct(75))
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(root, bg='grey', width=utils.width_prct(75), height=utils.height_prct(75))
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

# creating the cells using class Cell
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)

# View the list of all cells
# print(Cell.all)
# print(len(Cell.all))
# Call the label from Cell.py

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()

# checking if the cells are randomized or not
#for c in Cell.all:
   # print(c.is_mine)

root.mainloop()  # Run window

