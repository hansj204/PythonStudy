from tkinter import *
from tkinter import font

# 함수 선언 부분 ##
def clear():
    global infixStr
    
    calcAreatext.set('')
    infixStr = ''

def changeCalcLabel(letter): 
    global infixStr

    calcAreatext.set(calcArea.get() + str(letter))  
    
    calcLabel = letter
    
    if (letter == '÷'): calcLabel = '/'
    elif (letter == '×'): calcLabel = '*'
    
    infixStr += str(calcLabel)

def getPostfixArr():
    postfixList = ''
    stack = [] 
    
    for element in infixStr:        
        if element == '+' or element == '-':
            while stack and stack[-1] != '(':
                postfixList += stack.pop()
            stack.append(element)
        elif element == '*' or element == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                postfixList += stack.pop()
            stack.append(element)
        elif element == '(':
            stack.append(element)
        elif element == ')':
            while stack and stack[-1] != '(':
                postfixList += stack.pop()
            stack.pop()
        else:
            postfixList += element

    while stack:
        postfixList += stack.pop()         

    return postfixList;      

def calcVal():
    stack = []
    try:
        for token in getPostfixArr():
            if token == '+':
                stack.append(stack.pop()+stack.pop())
            elif token == '-':
                stack.append(-(stack.pop()-stack.pop()))
            elif token == '*':
                stack.append(stack.pop()*stack.pop())
            elif token == '/':
                divisor = stack.pop()
                
                if(0 == divisor): 
                    calcAreatext.set('0으로 나눌 수 없습니다.')
                    return;
                
                stack.append(stack.pop()/divisor)
            else:
                stack.append(int(token))
            
        if 0 == len(stack):
            calcAreatext.set('')
        else :
            calcAreatext.set(str(stack.pop())) 
    except Exception as error:
        print(error)
        clear()
        calcAreatext.set('수식 오류') 

# 변수 선언 부분
window = Tk()
window.title('계산기')
window.geometry('280x400')
window.resizable(False, False)
window.configure(background='#58657a') 
 
functionBtnBg='#4a72b0'
functionBtnActiveBg='#38598c'
numberBtnBg='white'

infixStr = ''    
    
# 메인 함수 부분    
calcAreatext = StringVar()
calcArea = Entry(window, width=25, textvariable=calcAreatext, justify='right', font=font.Font(family="맑은 고딕", size=13, weight='bold'), state='readonly', background='white')
calcArea.grid(row=0, columnspan=4, ipadx=2, ipady=18, padx=10, pady=10)

leftHoriz = Button(window, text="(", command=lambda:changeCalcLabel('('), padx=15, pady=10, borderwidth=1, background=functionBtnBg, activebackground=functionBtnActiveBg)
leftHoriz.grid(row=1, column=0, padx=5, pady=5)
rightHoriz = Button(window, text=")", command=lambda:changeCalcLabel(')'), padx=15, pady=10, borderwidth=1, background=functionBtnBg, activebackground=functionBtnActiveBg)
rightHoriz.grid(row=1, column=1, padx=5, pady=5)
clearBtn = Button(window, text="C", command=clear, padx=15, pady=10, borderwidth=1, background=functionBtnBg, activebackground=functionBtnActiveBg)
clearBtn.grid(row=1, column=2, padx=5, pady=5)
divideBtn = Button(window, text="÷", command=lambda:changeCalcLabel('÷'), padx=15, pady=10, borderwidth=1, background=functionBtnBg, activebackground=functionBtnActiveBg)
divideBtn.grid(row=1, column=3, padx=5, pady=5)

btn7 = Button(window, text="7", command=lambda:changeCalcLabel('7'), padx=15, pady=10, borderwidth=1, background=numberBtnBg)
btn7.grid(row=2, column=0, padx=5, pady=5)
btn8 = Button(window, text="8", command=lambda:changeCalcLabel('8'), padx=15, pady=10, borderwidth=1, background=numberBtnBg)
btn8.grid(row=2, column=1, padx=5, pady=5)
btn9 = Button(window, text="9", command=lambda:changeCalcLabel('9'), padx=15, pady=10, borderwidth=1, background=numberBtnBg)
btn9.grid(row=2, column=2, padx=5, pady=5)
multiBtn = Button(window, text="×", command=lambda:changeCalcLabel('×'), padx=15, pady=10, borderwidth=1, background=functionBtnBg, activebackground=functionBtnActiveBg)
multiBtn.grid(row=2, column=3, padx=5, pady=5)

btn4 = Button(window, text="4", command=lambda:changeCalcLabel('4'), padx=15, pady=10, borderwidth=1, background=numberBtnBg)
btn4.grid(row=3, column=0, padx=5, pady=5)
btn5 = Button(window, text="5", command=lambda:changeCalcLabel('5'), padx=15, pady=10, borderwidth=1, background=numberBtnBg)
btn5.grid(row=3, column=1, padx=5, pady=5)
btn6 = Button(window, text="6", command=lambda:changeCalcLabel('6'), padx=15, pady=10, borderwidth=1, background=numberBtnBg)
btn6.grid(row=3, column=2, padx=5, pady=5)
minusiBtn = Button(window, text="−", command=lambda:changeCalcLabel('-'), padx=17, pady=10, borderwidth=1, background=functionBtnBg, activebackground=functionBtnActiveBg)
minusiBtn.grid(row=3, column=3, padx=5, pady=5)

btn1 = Button(window, text="1", command=lambda:changeCalcLabel('1'), padx=15, pady=10, borderwidth=1, background=numberBtnBg)
btn1.grid(row=4, column=0, padx=5, pady=5)
btn2 = Button(window, text="2", command=lambda:changeCalcLabel('2'), padx=15, pady=10, borderwidth=1, background=numberBtnBg)
btn2.grid(row=4, column=1, padx=5, pady=5)
btn3 = Button(window, text="3", command=lambda:changeCalcLabel('3'), padx=15, pady=10, borderwidth=1, background=numberBtnBg)
btn3.grid(row=4, column=2, padx=5, pady=5)
plsuBtn = Button(window, text="+", command=lambda:changeCalcLabel('+'), padx=15, pady=10, borderwidth=1, background=functionBtnBg, activebackground=functionBtnActiveBg)
plsuBtn.grid(row=4, column=3, padx=5, pady=5)

btn0 = Button(window, text="0", command=lambda:changeCalcLabel('0'), padx=15, pady=10, borderwidth=1, background=numberBtnBg)
btn0.grid(row=5, column=0, padx=5, pady=5)
resultBtn = Button(window, text="=",command=calcVal, width=20, padx=1, pady=10, borderwidth=1, background='#79a2bd', activebackground='#27648c')
resultBtn.grid(row=5, column=1, columnspan=3, padx=5, pady=5)

window.mainloop()