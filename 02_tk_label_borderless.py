from tkinter import *
from PIL import ImageTk, Image

# open image and get dimensions
img = Image.open("free.png")
width, height = img.size

window = Tk()
window.overrideredirect(True)  # remove window border
window.geometry(f"{width}x{height}")  # set window size to match image

# create image object and label
photo = ImageTk.PhotoImage(img)
label = Label(window,
    image=photo,
    borderwidth=0,
    highlightthickness=0,
    padx=0,
    pady=0,
    )
label.pack()

# create canvas and draw X icon
canvas = Canvas(window, width=20, height=20, highlightthickness=0)
canvas.create_line(2, 2, 18, 18, width=2)
canvas.create_line(2, 18, 18, 2, width=2)
canvas.place(x=width-20, y=0)

# bind canvas to close window
def close_window(event):
    window.destroy()

canvas.bind("<Button-1>", close_window)

# bind label to dragging events
def start_drag(event):
    global x, y
    x = event.x
    y = event.y

def drag(event):
    global x, y
    deltax = event.x - x
    deltay = event.y - y
    window.geometry(f"+{window.winfo_x()+deltax}+{window.winfo_y()+deltay}")

label.bind("<ButtonPress-1>", start_drag)
label.bind("<B1-Motion>", drag)

window.mainloop()