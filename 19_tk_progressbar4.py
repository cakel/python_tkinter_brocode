import asyncio
from tkinter import *
from tkinter.ttk import *
import threading

async def start_download():
    global GB, download, speed, bar, percent, text
    while download < GB:
        download += speed
        percent.set(str(int(download/GB*100)) + "%")
        text.set(str(download) + "/" + str(GB) + " GB completed")
        bar['value'] = (download/GB)*100
        window.update_idletasks()
        await asyncio.sleep(0.05)

def download():
    global GB, download, speed
    GB = 100
    download = 0
    speed = 1
    thread = threading.Thread(target=asyncio.run, args=(start_download(),))
    thread.start()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=download).pack()

window.mainloop()
