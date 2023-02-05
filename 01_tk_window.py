from tkinter import *

window = Tk() # Instantiate an instance of a window
window.geometry("420x420")
window.title("Bro")

icon = PhotoImage(file="free.png")
window.iconphoto(True, icon)
window.config(background="#5cfcff")

window.mainloop() # place window on computer screen, listen for events
