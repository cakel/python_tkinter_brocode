from tkinter import *
import time
import threading
from tkinter.ttk import *

def start_download():
    GB = 100
    download = 0
    speed = 1
    while download < GB:
        time.sleep(0.05)
        download += speed
        percent.set(str(int(download/GB*100)) + "%")
        text.set(str(download) + "/" + str(GB) + " GB completed")
        bar['value'] = (download/GB)*100
        window.update_idletasks()

def download():
    t = threading.Thread(target=start_download)
    t.start()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=download).pack()

window.mainloop()
