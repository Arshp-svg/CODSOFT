from tkinter import *

def butoon_press(num):
    
    global equation_text
    
    equation_text= equation_text+str(num)
    equation_lable.set(equation_text)
    

def equals():
    try:
        global equation_text
        total= str(eval(equation_text))
        equation_lable.set(total)
        
        equation_text=total
    except SyntaxError:
        equation_lable.set("Syntax error")
        equation_text=""
        
    except ZeroDivisionError:
        equation_lable.set("Arithmetic error")
        equation_text=""
        

def clear():
    global equation_text
    equation_lable.set("")
    
    equation_text=""


window=Tk()
window.title("calculator")
window.geometry('400x650+400+100')
equation_text=""

equation_lable= StringVar()
lable= Label(window,textvariable=equation_lable, font=('consolas',20),bg='white',width=24,height=2)
lable.pack()

frmae=Frame(window)
frmae.pack()

button1=Button(frmae,text=1,height=4,width=9,font=35,
               command= lambda:butoon_press(1))
button1.grid(row=0,column=0)
button2=Button(frmae,text=2,height=4,width=9,font=35,
               command= lambda:butoon_press(2))
button2.grid(row=0,column=1)
button3=Button(frmae,text=3,height=4,width=9,font=35,
               command= lambda:butoon_press(3))
button3.grid(row=0,column=2)

button4=Button(frmae,text=4,height=4,width=9,font=35,
               command= lambda:butoon_press(4))
button4.grid(row=1,column=0)
button5=Button(frmae,text=5,height=4,width=9,font=35,
               command= lambda:butoon_press(5))
button5.grid(row=1,column=1)
button6=Button(frmae,text=6,height=4,width=9,font=35,
               command= lambda:butoon_press(6))
button6.grid(row=1,column=2)
button7=Button(frmae,text=7,height=4,width=9,font=35,
               command= lambda:butoon_press(7))
button7.grid(row=2,column=0)
button8=Button(frmae,text=8,height=4,width=9,font=35,
               command= lambda:butoon_press(8))
button8.grid(row=2,column=1)
button9=Button(frmae,text=9,height=4,width=9,font=35,
               command= lambda:butoon_press(9))
button9.grid(row=2,column=2)
button0=Button(frmae,text=0,height=4,width=9,font=35,
               command= lambda:butoon_press(0))
button0.grid(row=3,column=0)
plus=Button(frmae,text='+',height=4,width=9,font=35,
               command= lambda:butoon_press('+'))
plus.grid(row=0,column=3)
minus=Button(frmae,text='-',height=4,width=9,font=35,
               command= lambda:butoon_press('-'))
minus.grid(row=1,column=3)

mult=Button(frmae,text='*',height=4,width=9,font=35,
               command= lambda:butoon_press('*'))
mult.grid(row=2,column=3)

div=Button(frmae,text='/',height=4,width=9,font=35,
               command= lambda:butoon_press('/'))
div.grid(row=3,column=3)

equal=Button(frmae,text='=',height=4,width=9,font=35,
               command=equals)
equal.grid(row=3,column=2)

decimal=Button(frmae,text='.',height=4,width=9,font=35,
               command= lambda:butoon_press('.'))
decimal.grid(row=3,column=1)

clear=Button(window,text='AC',height=4,width=40,font=35,
               command=clear)
clear.pack()




window.mainloop()