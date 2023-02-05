from tkinter import *
from PIL import ImageTk, Image

window = Tk()

def display():
    if(x.get() == "Yes"):
        print("You agree!")
    else:
        print("You don't agree :(")

x = StringVar()
x.set("No")
like_photo = Image.open('like.png')
img = like_photo.resize((50,50))
my_img = ImageTk.PhotoImage(img)


check_button = Checkbutton(window,
                            text="I agree to something",
                            variable=x,
                            onvalue="Yes",
                            offvalue="No",
                            command=display,
                            font=('Arial', 20),
                            foreground='#00FF00',
                            bg='black',
                            activeforeground='#00FF00',
                            activebackground='black',
                            padx=25,
                            pady=10,
                            image=my_img,
                            compound='bottom',
                            indicatoron=1
                            )

check_button.pack()

window.mainloop()