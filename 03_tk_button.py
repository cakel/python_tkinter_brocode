from tkinter import *
from PIL import Image, ImageTk

count = 0

def click():
    global count
    count +=1
    print(count)
    button.config(text="Click me! "+str(count))


window = Tk()

photo= PhotoImage(file="like.png")
image=Image.open('like.png')
img=image.resize((450,350))
my_img=ImageTk.PhotoImage(img)


button = Button(window,
        text="Click me!",
        command=click,
        font=("Comic Sans", 30),
        fg="#00FF00",
        bg="black",
        activeforeground="#00FF00",
        activebackground="black",
        state=ACTIVE,
        image=my_img,
        compound='bottom')

button.pack()

window.mainloop()