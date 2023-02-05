from tkinter import *
from tkinter.ttk import *

def start_download():
    global GB, download, speed, bar, percent, text
    if download >= GB:
        return
    download += speed
    percent.set(str(int(download/GB*100)) + "%")
    text.set(str(download) + "/" + str(GB) + " GB completed")
    bar['value'] = int((download/GB)*100)
    window.update_idletasks()
    window.after(50, start_download)

def download():
    global GB, download, speed
    GB = 100
    download = 0
    speed = 1
    start_download()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=download).pack()

window.mainloop()
