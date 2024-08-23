from tkinter import *
import random
import string

root=Tk()
root.geometry("400x650+400+100")
root.title("password generator")


pwdstr=StringVar()
pwdlen=IntVar()

def getpass():
    pwd1=string.ascii_letters + string.digits +string.punctuation
    password=""
    
    for i in range(pwdlen.get()):
        password=password+random.choice(pwd1)
        pwdstr.set(password)
        
        
Label(root,text="PASSWORD GENERATOR",font="calibri 18 bold").pack()
Label(root,text="Enter the length of password",font="calibri 8 bold").pack(pady=9)
Entry(root,textvariable=pwdlen).pack(pady=2)
Button(root,text="GENERATE PASSWORD",command=getpass).pack(pady=15)
Entry(root,textvariable=pwdstr).pack(pady=2)


root.mainloop()