from tkinter import *
from tkinter.filedialog import *
from io import io

def func_open() :
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), "모든 파일", "*.*")))
        
    photo = PhotoImage(file = filename)
    
    img = io.imread(filename)
    imgGray = color.rgb2gray(img)
    
    pLabel.configure(image = imgGray)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()

window = Tk()

window.geometry('500x500')
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()
