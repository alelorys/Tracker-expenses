# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:29:34 2020

@author: Ola
"""

from tkinter import *
from datetime import datetime
import pickle
win = Tk()

win.title("Tracker wydatków")
win.geometry("600x450")

class Window:
    
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()
        self.total = 0
        self.history = {}

        self.tracker = Label(master, text="Podaj nazwę:")
        self.tracker.pack()
        self.tracker.place(x=20, y=20)
        self.nameEntry = Entry(master)
        self.nameEntry.pack()
        self.nameEntry.place(x=100, y=20)
        self.prizeLbl = Label(master, text="Podaj kwotę:")
        self.prizeLbl.pack()
        self.prizeLbl.place(x=20,y=50)
        self.prizeEntry = Entry(master)
        self.prizeEntry.pack()
        self.prizeEntry.place(x=100, y=50)

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
        self.history = pickle.load(open("payment.dat", "rb"))
        self.historyPay = Text(master)
        self.historyPay.pack()
        self.historyPay.place(x=20,y=200, height=200, width=500)
        self.historyPay.delete(1.0,"end")
        for key, value in self.history.items():
                string = key + " : "+str(value)+"\n"
                self.historyPay.insert(1.0, string)

    def payment(self):
        cashInName = self.nameEntry.get()
        cashInPrize = float(self.prizeEntry.get())
        self.total = self.total+cashInPrize
        self.history[cashInName] = cashInPrize
        pickle.dump(self.history,open("payment.dat","wb"))
        self.totalTxt.delete(1.0,"end")
        self.totalTxt.insert(1.0,self.total)
        # self.historyPay.delete(1.0, "end")
        # for i in self.history:
        #   self.historyPay.insert(1.0, "Wypłata "+str(i)+"\n")
        self.historyPay.delete(1.0, "end")

        for key, value in self.history.items():
            string = key + " : "+str(value)+"\n"
            self.historyPay.insert(1.0, string)

    def cashout(self):
        cashOutName = self.nameEntry.get()
        cashOutPrize = float(self.prizeEntry.get())
        self.history[cashOutName] = cashOutPrize
        pickle.dump(self.history,open("payment.dat","wb"))
        self.total = self.total - cashOutPrize
        self.totalTxt.delete(1.0,"end")
        self.totalTxt.insert(1.0, self.total)
        self.historyPay.delete(1.0, "end")
        for key, value in self.history.items():
            cashout = key + " : " + str(value) + "\n"
            self.historyPay.insert(1.0, cashout)



mainWindow = Window(win)       
win.mainloop()