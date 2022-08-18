from tkinter import *
window = Tk()

photo = PhotoImage(file = "image/GIF/dog.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()
