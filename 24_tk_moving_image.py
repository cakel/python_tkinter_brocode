from tkinter import *

beforeDirection = 0
acceleration = 0
UP = 1
DOWN = -1
LEFT = -2
RIGHT = 2

def move_up(event):
    global beforeDirection, acceleration
    if beforeDirection == UP:
        acceleration += 1
    else:
        beforeDirection = UP
        acceleration = 0

    label.place(x=label.winfo_x(), y=label.winfo_y()-(10+acceleration))

    if label.winfo_y() < -50:
        label.place(x=label.winfo_x(), y=550)

    pass

def move_down(event):
    global beforeDirection, acceleration

    if beforeDirection == DOWN:
        acceleration += 1
    else:
        beforeDirection = DOWN
        acceleration = 0

    label.place(x=label.winfo_x(), y=label.winfo_y()+(10+acceleration))

    if label.winfo_y() > 550:
        label.place(x=label.winfo_x(), y=-50)

    pass

def move_left(event):
    global beforeDirection, acceleration
    if beforeDirection == LEFT:
        acceleration += 1
    else:
        beforeDirection = LEFT
        acceleration = 0

    label.place(x=label.winfo_x()-(10+acceleration), y=label.winfo_y())

    if label.winfo_x() < -50:
        label.place(x=550, y=label.winfo_y())

    pass

def move_right(event):
    global beforeDirection, acceleration
    if beforeDirection == RIGHT:
        acceleration += 1
    else:
        beforeDirection = RIGHT
        acceleration = 0

    label.place(x=label.winfo_x()+(10+acceleration), y=label.winfo_y())

    if label.winfo_x() > 550:
        label.place(x=-50, y=label.winfo_y())

    pass

window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

myimage = PhotoImage(file="racing-car.png")
label = Label(window, image=myimage)

label.place(x=0, y = 0)

window.mainloop()