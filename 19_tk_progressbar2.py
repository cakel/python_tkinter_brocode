from tkinter import *
from tkinter.ttk import *
import time

def update_download():
    global download, speed

    if download >= GB:
        return

    download += speed
    bar['value'] = (download / GB) * 100
    percent.set(f"{int(download / GB * 100)}%")
    text.set(f"{download}/{GB} GB completed")

    window.after(50, update_download)

def start():
    global download, GB, speed

    download = 0
    GB = 100
    speed = 1
    update_download()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()
