import tkinter
from tkinter import *

root=Tk()
root.title("To-Do-List")
root.geometry('400x650+400+100')
root.resizable(False,False)
 
task_list=[]

def Addtask():
    task=task_entry.get()
    task_entry.delete(0,END)
    
    if task:
        with open("tsk.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
        
        
def deletetsk():
    
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tsk.txt","w") as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        
        listbox.delete(ANCHOR)   

def openTaskFile():
    try:
        global task_list
        with open("tsk.txt","r") as taskfile:
            tasks=taskfile.readlines()
            
        for task in tasks:
            if tasks !='\n':
                task_list.append(task)
                listbox.insert(END,task)
                
    except:
        file=open("tsk.txt","w")
        file.close()


Top_image=PhotoImage(file="topbar.png")
Label(root,image=Top_image).pack()

dockimage=PhotoImage(file="icons8-menu-48.png")
Label(root,image=dockimage,bg='cyan').place(x=30,y=25)

noteImage=PhotoImage(file="icons8-menu-48.png")
Label(root,image=noteImage,bg="yellow").place(x=30,y=25)

heading=Label(root,text="To-Do-List",font="arial 20 bold",fg="black",bg="white")
heading.place(x=130,y=20)

#main
frame= Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

tast=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)


button=Button(frame,text="ADD",width=6,font="arial 20",bg="black",fg="white",bd=0,command=Addtask)
button.place(x=300,y=0)

#list
frame1=Frame(root,bd=3,width=700,height=280,bg="pink")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=("arial",12),width=40,height=16,bg="black",fg="white",cursor="hand2",selectbackground="#5a95ff")

listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrbar=Scrollbar(frame1)
scrbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrbar.set)
scrbar.config(command=listbox.yview)

openTaskFile()

dticon=PhotoImage(file="icons8-delete-30.png")
Button(root,image=dticon,bd=0,command=deletetsk).pack(side=BOTTOM,pady=30)


 
root.mainloop()