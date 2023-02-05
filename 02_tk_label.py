from tkinter import *

window = Tk()

photo = PhotoImage(file='free.png')

window.config(background="#00FF00")
label = Label(window,
    text="Hello World",
    font=('Arial',40,'bold'),
    relief=RAISED,
    bd=10,
    padx=20,
    pady=20,
    image=photo,
    compound="bottom"
    )
label.pack()
# label.place(x=100, y=100)

window.mainloop()