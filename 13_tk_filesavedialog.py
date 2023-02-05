from tkinter import filedialog, Tk, Button, Text, END

def saveFile():
    file=filedialog.asksaveasfile(defaultextension=".txt",
                                  initialdir="D:\Work\Python_Image_Board_Downloader",
                                    filetypes=(("Text file", ".txt"),
                                    ("HTML", ".html"),
                                    ("All files", ".*")))
    if file is None:
        return

    # filetext = str(text.get(1.0, END))
    filetext=input("Enter some text I guess:")
    file.write(filetext)
    file.close()

window=Tk()
button=Button(text='save', command=saveFile)
button.pack()
text=Text(window)
text.pack()
window.mainloop()