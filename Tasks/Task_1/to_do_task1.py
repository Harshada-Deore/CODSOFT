
from tkinter import messagebox
import customtkinter
from tkinter import *


application = customtkinter.CTk()
application.title('TO-DO LIST')
application.geometry('400x500')
application.config(bg='#70dbdb')


font_title = ('Arial', 30, 'bold')
font_text1 = ('Arial', 18, 'bold')
font_text2 = ('Arial', 10, 'bold')


def addt():
    task = entry_box.get()
    if task:
        list_box.insert(0,task)
        entry_box.delete(0, END)
        savet()
    else:
        messagebox.showerror('ERROR OCCURED','Enter Task!')

def removet():
    selected = list_box.curselection()
    if selected:
        list_box.delete(selected[0])
        savet()
    else:
        messagebox.showerror('ERROR OCCURED','Choose a task to delete!')


def savet():
    with open("tasks.txt", "w") as f:
        tasks = list_box.get(0,END)
        for task in tasks:
            f.write(task + "\n")


def loadt():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                list_box.insert(0,task.strip())
    except FileNotFoundError:
        messagebox.showerror('ERROR OCCURED','Cannot load tasks!')


title = customtkinter.CTkLabel(application,font=font_title,text='TO-DO LIST',text_color='#000',bg_color='#70dbdb')
title.place(x=100,y=20)


button1 = customtkinter.CTkButton(application,command=addt,font=font_text1,text='ADD TASK',text_color='#fff',fg_color='#009933',hover_color='#a6a6a6',bg_color='#70dbdb',cursor='hand2',corner_radius=8,width=120)
button1.place(x=40,y=450)


button2 = customtkinter.CTkButton(application,command=removet,font=font_text1,text='DELETE TASK',text_color='#fff',fg_color='#ff0000',hover_color='#a6a6a6',bg_color='#70dbdb',cursor='hand2',corner_radius=8,width=120)
button2.place(x=220,y=450)


entry_box = customtkinter.CTkEntry(application,font=font_text2,text_color='#000000',fg_color='#c2f0f0',border_color='#c2f0f0',width=300,corner_radius=10)
entry_box.place(x=50,y=100)


list_box = Listbox(application,width=40,height=20,font=font_text2,bg='#c2f0f0')
list_box.place(x=100,y=180)


loadt()
application.mainloop()