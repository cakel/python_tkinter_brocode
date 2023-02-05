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

    canvas.move(myimage, 0, -(10+acceleration))

    if canvas.coords(myimage)[1] < -50:
        canvas.moveto(myimage, canvas.coords(myimage)[0], 550)

    pass
def move_down(event):
    global beforeDirection, acceleration

    if beforeDirection == DOWN:
        acceleration += 1
    else:
        beforeDirection = DOWN
        acceleration = 0

    canvas.move(myimage, 0, 10+acceleration)

    if canvas.coords(myimage)[1] > 550:
        canvas.moveto(myimage, canvas.coords(myimage)[0], -50)

    pass

def move_left(event):
    global beforeDirection, acceleration
    if beforeDirection == LEFT:
        acceleration += 1
    else:
        beforeDirection = LEFT
        acceleration = 0

    canvas.move(myimage, -(10+acceleration), 0)

    if canvas.coords(myimage)[0] < -50:
        canvas.moveto(myimage, 550, canvas.coords(myimage)[1])

    pass

def move_right(event):
    global beforeDirection, acceleration
    if beforeDirection == RIGHT:
        acceleration += 1
    else:
        beforeDirection = RIGHT
        acceleration = 0

    canvas.move(myimage, 10+acceleration, 0)

    if canvas.coords(myimage)[0] > 550:
        canvas.moveto(myimage, -50, canvas.coords(myimage)[1])

    pass

window = Tk()

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

photoimage = PhotoImage(file='racing-car.png')
myimage = canvas.create_image(0,0,image=photoimage, anchor=NW)

window.mainloop()