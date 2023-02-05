from tkinter import *
from PIL import ImageTk, Image

food = ["pizza", "hamburger", "hotdog"]

window = Tk()

# pizzaOrgImage=Image.open('pizza.png')
# pizzaImage=pizzaOrgImage.resize((50,50))
# pizzaImage = ImageTk.PhotoImage(pizzaImage)
# # pizzaImage = PhotoImage(file='pizza.png')
# hamburgerImage = PhotoImage(file='hamburger.png')
# hotdogImage = PhotoImage(file='hotdog.png')

# foodImages = [pizzaImage, hamburgerImage, hotdogImage]
x = IntVar()
imageOrg= [None] * len(food)
imageResize= [None] * len(food)
imageImageTk= [None] * len(food)

def order():
    print(f"You ordered a {food[x.get()]}")

for index in range(len(food)):
    imageOrg[index]=Image.open(f'{food[index]}.png')
    imageResize[index]=imageOrg[index].resize((50,50))
    imageImageTk[index]=ImageTk.PhotoImage(imageResize[index])

    radiobutton = Radiobutton(window,
                    text=food[index], # adds text to radio buttons
                    variable=x, # groups radiobuttons, if they share same variable
                    value=index, # assigns each radiobutton a different value
                    padx=25, # adds padding on x-axis
                    font=('Impact', 50),
                    image = imageImageTk[index],
                    compound='left',
                    indicatoron=0,  # eliminate circle indicators
                    width=500,
                    command=order # Set command of radtiobutton to funtion
                    )

    radiobutton.pack(anchor='w')


window.mainloop()


