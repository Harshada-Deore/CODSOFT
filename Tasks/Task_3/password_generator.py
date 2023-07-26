from tkinter import *
from tkinter import ttk
import random,string

root=Tk()
root.geometry('400x280')
root.title("Password Generator")

style = ttk.Style()
style.theme_use('clam')

title = StringVar()
lable = ttk.Label(root,textvariable=title, font=('Arial',14,'bold')).pack(pady=10)
title.set("The Strength of Password: ")

def selection():
    selection=choice.get()

frame=ttk.Frame(root).pack(pady=10)

choice=IntVar()
R1=ttk.Radiobutton(frame,text="POOR",variable=choice,value=1,command=selection).pack(side=LEFT, padx=5)
R1=ttk.Radiobutton(frame,text="AVERAGE",variable=choice,value=2,command=selection).pack(side=LEFT, padx=5)
R1=ttk.Radiobutton(frame,text="STRONG",variable=choice,value=3,command=selection).pack(side=LEFT, padx=5)

lablechoice=Label(root)
lablechoice.pack()

lenlabel=StringVar()
lenlabel.set("Password Length")
lentitle=ttk.Label(root,textvariable=lenlabel).pack()

val=IntVar()
spinlength=Spinbox(root,from_=8,to_=24,textvariable=val,width=13).pack()

def callback():
    lsum.config(text=passgen())

passgenButton=ttk.Button(root,text="Generate password",command=callback)
passgenButton.pack(pady=10)
password=str(callback)

lsum=Label(root,text="")
lsum.pack(side=TOP)

#logic for password generation

poor=string.ascii_uppercase + string.ascii_lowercase
average=string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols="""'~!@#$%^&*()_-+={}[]\|:;'"<>,.?/"""
advance=poor+average+symbols

def passgen():
    if choice.get()==1:
        return "".join(random.sample(poor,val.get()))
    elif choice.get==2:
        return "".join(random.sample(average,val.get()))
    elif choice.get()==3:
        return "".join(random.sample(advance,val.get()))
    
root.mainloop()