from tkinter import Tk, Button, colorchooser # submodule

def click():
    # color = colorchooser.askcolor()
    # # print(color)
    # colorHex = color[1]
    # # print(colorHex)
    # window.config(bg=colorHex) # Change background color
    window.config(bg=colorchooser.askcolor()[1])

    pass

window = Tk()
window.geometry("420x420")
button = Button(text='click me', command=click)
button.pack()
window.mainloop()