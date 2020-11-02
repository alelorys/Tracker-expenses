# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:29:25 2020

@author: Ola
"""

from tkinter import *


total = 0

def incost():
    wplata = int(cost.get())
    label_in = Label(root,text=f"Wpłata {wplata}")
    label_in.grid(row=2,column=0)
    global total
    total = total + wplata
    label_total = Label(root,text=f"Dostępne środki {total}")
    label_total.grid(row=3,column=0)
    


    #label_bmi = tk.Label(win,text=f"Twoje BMI wynosi:{bmi_user}",
                         #font=("calibri",10,"italic"))
    #label_bmi.grid(row=6,column=0)
def outcost():
    wyplata = int(cost.get())
    label_out = Label(root,text=f"Wypłata {wyplata}")
    label_out. grid(row=2,column=1)  
    global total
    total = total - wyplata
    label_total = Label(root,text=f"Dostępne środki {total}")
    label_total.grid(row=3,column=0)


    

root = Tk()
root.title("Śledzenie wydatków")
root.geometry("600x450")


tracker = Label(root, text="Podaj kwotę")
tracker.grid(row=0,column=0)

cost = Entry(root)
cost.grid(row=0,column=1)


add = Button(root,text="Wpłata",command=incost)
add.grid(row=1,column=0)
odd = Button(root,text="Wypłata",command=outcost)
odd.grid(row=1,column=1)



root.mainloop()