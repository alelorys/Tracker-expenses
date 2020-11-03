# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:29:34 2020

@author: Ola
"""

from tkinter import *

win = Tk()

win.title("Tracker wydatków")
win.geometry("600x450")

class Window:
    
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()
        self.total = 0
        self.tracker = Label(master, text="Podaj kwotę")
        self.tracker.pack()
        self.tracker.place(x=20, y=50)
        self.prize = Entry(master)
        self.prize.pack()
        self.prize.place(x=90, y=50)

        self.totalLbl = Label(master, text="Saldo:")
        self.totalLbl.pack()
        self.totalLbl.place(x=20,y=140)

        self.totalTxt = Text(master)
        self.totalTxt.pack()
        self.totalTxt.place(x=60, y=140, height=20, width=100)
        self.paymentBtn = Button(master, text="Wpłata", command=self.payment)
        self.paymentBtn.pack()
        self.paymentBtn.place(x=20, y=75)
        self.cashoutBtn = Button(master, text="Wypłata", command=self.cashout)
        self.cashoutBtn.pack()
        self.cashoutBtn.place(x=80, y=75)

    def payment(self):
        self.paymentVar = float(self.prize.get())
        self.total = self.total + self.paymentVar
        #t.insert(tk.END, "Coś tu\npiszę\nSobie")
        self.totalTxt.delete(1.0,"end")
        self.totalTxt.insert(1.0, self.total)

    def cashout(self):
        self.cashoutVar = float(self.prize.get())
        self.total = self.total - self.cashoutVar
        self.totalTxt.delete(1.0,"end")
        self.totalTxt.insert(1.0, self.total)

mainWindow = Window(win)       
win.mainloop()