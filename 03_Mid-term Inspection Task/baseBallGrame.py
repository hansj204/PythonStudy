from random import randint
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def newGrame() :
    rightNumbers = []
    rightNumbers = selectThreeNumber() 
    
    listbox.delete(0, END)

    firstNumber.delete(0, END)
    secondNumber.delete(0, END)
    thirdNumber.delete(0, END)

def exit() :
    window.quit()
    window.destroy()
 
def selectThreeNumber():
    numbers = []
    
    while len(numbers) < 3:
        number = randint(1, 9)
        
        if number not in numbers: 
            numbers.append(str(number))
            
    return numbers

def findIndex(list, findValue):
    findIndex = -1;
    
    for i in range(0, len(rightNumbers)):
        if rightNumbers[i] == findValue:
            findIndex = i
            
    return findIndex

def checkCondition(checkNumberList):
    overlapList = []
    
    for number in checkNumberList:        
        if number == '':
            messagebox.showinfo("경고", "숫자가 비어있습니다.")
            return False
        if not number.isdigit():
            messagebox.showinfo("경고", "입력한 값이 숫자가 아닙니다")
            return False        
        if int(number) < 1 or int(number) > 9:
            messagebox.showinfo("경고", "입력한 숫자의 범위는 1 ~ 9 입니다.")
            return False
        
        if number in overlapList:
            messagebox.showinfo("경고", "중복됩니다.")
            return False
        else:
            overlapList.append(number)
        
def checkAnswer():
    answerNumbers = [firstNumber.get(), secondNumber.get(), thirdNumber.get()]
    
    if(checkCondition(answerNumbers) == False) : 
        firstNumber.delete(0, END)
        secondNumber.delete(0, END)
        thirdNumber.delete(0, END)
        return
    
    ballCnt = 0
    strikeCnt = 0
    
    for i in range(0, len(answerNumbers)):
        
        if i == findIndex(rightNumbers, answerNumbers[i]):
            strikeCnt += 1
        elif answerNumbers[i] in rightNumbers:
            ballCnt += 1
    
    resultLine = firstNumber.get() + secondNumber.get() + thirdNumber.get() + ' → ' + str(ballCnt) + 'B' + str(strikeCnt) + 'S';
    listbox.insert(END, resultLine)
    
    if strikeCnt == 3:
        messagebox.showinfo("성공", "WINNER!")
        
    firstNumber.delete(0, END)
    secondNumber.delete(0, END)
    thirdNumber.delete(0, END)
    
## 메인 코드 부분 ##    
window = Tk()
window.geometry("300x300")
window.title('야구게임')

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)

fileMenu.add_command(label = "새게임", command = newGrame)
fileMenu.add_separator()
fileMenu.add_command(label = "종료", command = exit)

rightNumbers = selectThreeNumber() 

noticeLabel = Label(window, text = "1 ~ 9 사이의 숫자 3개를 예측해보세요")
noticeLabel.pack()

frame= Frame(window)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill='y')

listbox = Listbox(frame, yscrollcommand=scrollbar.set, width=100, font = ("맑은 고딕", 12))
listbox.pack(side=LEFT, fill='both')

scrollbar["command"]=listbox.yview
frame.pack()

firstNumber = Entry(window, width=7)
firstNumber.pack(side=LEFT, padx=10)  

secondNumber = Entry(window, width=7)
secondNumber.pack(side=LEFT, padx=10)  

thirdNumber = Entry(window, width=7)
thirdNumber.pack(side=LEFT, padx=10)  

checkBtn = Button(window, text = "Go", width= 10, command=checkAnswer)
checkBtn.pack(side = LEFT, padx=10)

window.mainloop()
