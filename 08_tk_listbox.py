from tkinter import *

def submit():
    # print(listbox.get(listbox.curselection()))
    if listbox.curselection() is None:
        return

    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("You have ordered:")
    for index in food:
        print(index)

def add():
    if len(entryBox.get()) == 0:
        return

    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    #  listbox.delete(listbox.curselection())
    if listbox.curselection() is None:
        return

    for index in reversed(listbox.curselection()): # Last to first not too lose focus
        listbox.delete(index)

    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                    bg="#f7ffde",
                    font=("Constantia", 35),
                    width=12,
                    selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())

entryBox=Entry(window)
entryBox.pack()

submitButton=Button(window,text="submit", command=submit)
submitButton.pack()

addButton=Button(window,text="add", command=add)
addButton.pack()

deleteButton=Button(window,text="delete", command=delete)
deleteButton.pack()

window.mainloop()