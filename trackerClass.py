# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:29:34 2020

@author: Ola
"""

from tkinter import *
from datetime import datetime

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
        self.currentDate = datetime.now()
        self.dateCur = self.currentDate.month,".",self.currentDate.year
        self.dateTxt = Text(master)
        self.dateTxt.pack()
        self.dateTxt.place(x=510, y=10, height=20, width=80)
        self.dateTxt.delete(1.0, "end")
        self.dateTxt.insert(1.0, self.dateCur)
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



        self.historyLbl = Label(master, text="Historia:")
        self.historyLbl.pack()
        self.historyLbl.place(x=20,y=180)
        self.historyPay = Text(master)
        self.historyPay.pack()
        self.historyPay.place(x=20,y=200, height=200, width=500)


    def payment(self):
        self.paymentVar = float(self.prize.get())
        self.total = self.total + self.paymentVar
        #t.insert(tk.END, "Coś tu\npiszę\nSobie")
        self.totalTxt.delete(1.0,"end")
        self.totalTxt.insert(1.0, self.total)
        self.historyPay.insert(END, "Wpłata "+ str(self.paymentVar)+"\n")

    def cashout(self):
        self.cashoutVar = float(self.prize.get())
        self.total = self.total - self.cashoutVar
        self.totalTxt.delete(1.0,"end")
        self.totalTxt.insert(1.0, self.total)
        self.historyPay.insert(END, "Wypłata "+str(self.cashoutVar)+"\n")

mainWindow = Window(win)       
win.mainloop()