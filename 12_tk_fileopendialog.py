from tkinter import filedialog, Tk, Button

def openFile():
    filepath=filedialog.askopenfilename(initialdir="D:\\Work\\Python_Image_Board_Downloader",
                                        title="Open file okay?",
                                        filetype=(("text file","*.txt"),("all files", "*.*")))
    # print(filepath)
    file=open(filepath,"r")
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open", command=openFile)
button.pack()
window.mainloop()