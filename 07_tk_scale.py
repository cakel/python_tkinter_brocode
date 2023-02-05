from tkinter import *
from PIL import Image, ImageTk
from enum import Enum, auto

class TEMPERATURE(Enum):
    CELSIUS = auto()
    FAHRENHEIT = auto()
method = TEMPERATURE.CELSIUS

def on_object_press(event):
    global hotLabel_x, hotLabel_y
    hotLabel_x = event.x
    hotLabel_y = event.y

def on_object_release(event):
    global hotLabel_x, hotLabel_y
    hotLabel_x = None
    hotLabel_y = None

def on_object_motion(event):
    global hotLabel_x, hotLabel_y
    deltax = event.x - hotLabel_x
    deltay = event.y - hotLabel_y
    x = window.winfo_x() + deltax
    y = window.winfo_y() + deltay
    window.geometry("+%s+%s" % (x, y))

def update_convert_temperature_label(event):
    global method
    if method==TEMPERATURE.CELSIUS:
        celsius = scale.get()
        fahrenheit = (celsius * 9/5) + 32
        convert_temperature_label.config(text=f"{fahrenheit:.1f}° F")
    else:
        fahrenheit = scale.get()
        celsius = (fahrenheit - 32)/(9/5)
        convert_temperature_label.config(text=f"{celsius:.1f}° C")

def submit():
    global method
    if method==TEMPERATURE.CELSIUS:
        print("Change Celsius to Fahrenheit")
        method=TEMPERATURE.FAHRENHEIT
        scale.configure(from_=212, to_=-148)
        button.config(text="° F")
    else:
        print("Change Fahrenheit to Celsius")
        scale.configure(from_=100, to_=-100)
        method=TEMPERATURE.CELSIUS
        button.config(text="° C")
    scale.set(((scale['from']-scale['to'])/2)+scale['to']) # not from_ or to_


window = Tk()
window.configure(bg='#111111')

hotOrg = Image.open('Hot.png')
hotResize = hotOrg.resize((100,100))
hotImageTk = ImageTk.PhotoImage(hotResize)
hotLabel = Label(image=hotImageTk, bg="#111111")
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to_=-100,
              length=600,
              orient=VERTICAL, # orientation of scale
              font = ("Consolas", 20),
              tickinterval=10, # Adds numeric indicators for value
              # showvalue = 0 # Hide current value
              troughcolor="#69eaff",
              highlightthickness=0,
              fg = "#FF1C00",
              bg = "#111111")
scale.set(((scale['from']-scale['to'])/2)+scale['to']) # not from_ or to_
scale.pack()

coldOrg = Image.open('Cold.png')
coldResize = coldOrg.resize((100,100))
coldImageTk = ImageTk.PhotoImage(coldResize)
coldLabel = Label(image=coldImageTk, bg="#111111")
coldLabel.pack()

button = Button(window, text='° C', font=("Consolas", 20), command=submit, fg="#FF1C00", bg="#111111")
button.pack()

convert_temperature_label = Label(window,
                         font=("Consolas", 20),
                         fg="#FF1C00",
                         bg="#111111")
convert_temperature_label.pack()


for _obj  in [hotLabel, coldLabel, convert_temperature_label]:
    _obj.bind("<ButtonPress-1>", on_object_press)
    _obj.bind("<ButtonRelease-1>", on_object_release)
    _obj.bind("<B1-Motion>", on_object_motion)

scale.bind("<ButtonRelease-1>", update_convert_temperature_label)

update_convert_temperature_label(None)
window.mainloop()