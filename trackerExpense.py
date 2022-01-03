import tkinter as tk
from tkinter import *
from datetime import datetime
import os
import csv

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Tk()
app.title("Śledzenie wydatków")
app.geometry("600x450")
LARGEFONT =("Verdana", 35)
class Window:
    # __init__ function for class tkinterApp
    def __init__(self, master):
        
        # creating a container
        container = tk.Frame(master) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Summary, Piggy):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #container.config(bg="#a5a6f6")
        tk.Frame.config(self, bg="#a5a6f6")
        label = tk.Label(self, text ="Strona Główna", font=('Helvetica', 10, 'bold'))
        label.pack()
        label.place(x=10, y=0)
        label.config(bg="#a5a6f6")

        tracker = tk.Label(self, text="Podaj nazwę:")
        tracker.pack()
        tracker.place(x=20, y=30)
        tracker.config(bg="#a5a6f6")

        self.nameEntry = tk.Entry(self)
        self.nameEntry.pack()
        self.nameEntry.place(x=100, y=30)
        self.nameEntry.config(bg="#fcddec", highlightthickness = 0, borderwidth=0)

        prizeLbl = tk.Label(self, text="Podaj kwotę:")
        prizeLbl.pack()
        prizeLbl.place(x=20,y=60)
        prizeLbl.config(bg="#a5a6f6")

        self.prizeEntry = tk.Entry(self)
        self.prizeEntry.pack()
        self.prizeEntry.place(x=100, y=60)
        self.prizeEntry.config(bg="#fcddec", highlightthickness = 0, borderwidth=0)

        self.totalTxt = tk.Text(self)
        self.total = 0.00
        self.totalTxt.pack()
        self.totalTxt.place(x=60, y=140, height=20, width=100)
        self.totalTxt.config(bg="#fcddec", highlightthickness = 0, borderwidth=0)
        self.totalTxt.insert(1.0,self.total)
        
        #print(self.predict_total())
        self.predictTotalTxt = tk.Text(self)
        self.predictTotalTxt.pack()
        self.predictTotalTxt.place(x=180, y=140, height=20, width=100)
        self.predictTotalTxt.config(bg="#fcddec", highlightthickness = 0, borderwidth=0)
        
        
        
        
        self.today = datetime.now().date()
        dateTxt = Label(self, font='Helvetica 10 bold')
        dateTxt.pack()
        dateTxt.place(x=500, y=10)
        #dateTxt.insert(1.0, dateCur)
        dateTxt.config(bg="#a5a6f6", text= self.today)

        totalLbl = Label(self, text="Saldo:")
        totalLbl.pack()
        totalLbl.place(x=20,y=140)
        totalLbl.config(bg="#a5a6f6")

        summary_month = []
        
        
            
            
            
        paymentBtn = tk.Button(self, text="Wpłata", command= self.payment)
        paymentBtn.pack()
        paymentBtn.place(x=60, y=95)
        paymentBtn.config(bg="#fcddec", highlightthickness = 0, borderwidth=0)
        cashoutBtn = tk.Button(self, text="Wypłata", command=self.cashOut)#, 
        cashoutBtn.pack()
        cashoutBtn.place(x=120, y=95)
        cashoutBtn.config(bg="#fcddec", highlightthickness = 0, borderwidth=0)
        self.history = []
        
        historyLbl = Label(self, text="Historia:")
        historyLbl.pack()
        historyLbl.place(x=20,y=180)
        historyLbl.config(bg="#a5a6f6", highlightthickness = 0, borderwidth=0)

        self.historyPay = Text(self)
        self.historyPay.pack()
        self.historyPay.place(x=20,y=200, height=200, width=500)
        self.historyPay.config(bg="#fcddec", highlightthickness = 0, borderwidth=0)
        self.historyPay.delete(1.0, "end")

        

        if os.path.exists("payment.csv")==True:
            with open('payment.csv', newline='', encoding='utf-8') as csvfile:
                payment = csv.reader(csvfile, delimiter=' ', quotechar='|')
                
                for row in payment:

                    i = row[0] + ": " + row[1] + " " + row[2]
                    self.history.append(i)
                    self.historyPay.insert(1.0, i + "\n")
                    self.total += float(row[1])
                    self.totalTxt.delete(1.0,"end")
                    self.totalTxt.insert(1.0, self.total)            

        
        if self.today.day == 3:
            self.predict = self.predict_total()
            self.predictTotalTxt.delete(1.0, 'end')
            self.predictTotalTxt.insert(1.0, self.predict)
            
            with open('saves.csv', 'a', newline='', encoding='utf-8') as csvfile:
                saves = csv.writer(csvfile, delimiter=' ', quotechar='|',
                quoting=csv.QUOTE_MINIMAL)
                saves.writerow([self.total])
                
            self.total = 0.00
            self.totalTxt.delete(1.0, 'end')
            self.totalTxt.insert(1.0, self.total)
            
        summaryBtn = tk.Button(self, text="Podsumowanie",
                               command = lambda:controller.show_frame(Summary))        
        summaryBtn.pack()
        summaryBtn.place(x = 20, y = 415)
        summaryBtn.config(bg="#fcddec", highlightthickness = 0, borderwidth=0)

        piggybankBtn = tk.Button(self,text="Skarbonka",
                                 command = lambda: controller.show_frame(Piggy))
        
        piggybankBtn.pack()
        piggybankBtn.place(x = 120, y= 415)
        piggybankBtn.config(bg="#fcddec", highlightthickness = 0, borderwidth=0)

    def payment(self):
        name = self.nameEntry.get()
        amount = float(self.prizeEntry.get())
        date = self.today
        cash = name + ": "+ str(amount)+' '+str(date)
        self.total = self.total + amount
        self.totalTxt.delete(1.0,"end")
        self.totalTxt.insert(1.0, self.total)
        self.history.append(cash)
        
        with open('payment.csv', 'a', newline='', encoding='utf-8') as csvfile:
            payment = csv.writer(csvfile, delimiter=' ', quotechar='|',
            quoting=csv.QUOTE_MINIMAL)
            payment.writerow([name, amount, date])
            

            csvfile.close()
        
        self.historyPay.delete(1.0, "end")
        for i in self.history:
            self.historyPay.insert(1.0, i + "\n")
    
    def cashOut(self):
        name = self.nameEntry.get()
        amount = float(self.prizeEntry.get())
        date = self.today
        self.total = self.total + (-amount)
        self.totalTxt.delete(1.0,"end")
        self.totalTxt.insert(1.0, self.total)
        cash = name + ": "+ str(-amount) + ' ' + str(date)

        self.history.append(cash)
        with open('payment.csv', 'a', newline='', encoding='utf-8') as csvfile:
            payment = csv.writer(csvfile, delimiter=' ', quotechar='|',
            quoting=csv.QUOTE_MINIMAL)
            payment.writerow([name, (-amount), date])

            csvfile.close()
        
        self.historyPay.delete(1.0, "end")
        for i in self.history:
            self.historyPay.insert(1.0, i + "\n")
            
    def predict_total(self):
        df = pd.read_csv('summary.csv')
        
        date = np.array(df['date'],
                dtype='datetime64[ns]')

        amount = np.array(df['amount'])
        df = pd.DataFrame({'date': date, 'amount': amount})
        
        
        df['date'] = pd.to_datetime(df['date'])
        df['date'] = df['date'].map(datetime.toordinal)
        
        
        reg = LinearRegression()
        reg.fit(df[['date']], df.amount)
        #np.asarray(['2022-01-10'])
        next_month = pd.to_datetime(['2022-01-10'])
        next_month = next_month.map(datetime.toordinal)
        
        #next_month = 
        
        #print(next_month_pd)
        saldoPredict = reg.predict([[next_month[0]]])
        
        return round(saldoPredict[0], 2)
        
        
  
class Summary(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent, bg="#a5a6f6")
        label = tk.Label(self, text ="Podsumowanie", font = ('Helvetica', 10, 'bold'))
        label.pack()
        label.place(x=10, y=0)
        Summary_payment = []
        summary_payment_txt = tk.Text(self)
        summary_payment_txt.pack()
        summary_payment_txt.place(x=20,y=30, height=350, width=500)
        self.today = datetime.now().date()
        
        if self.today.day == 3:
            if os.path.exists("payment.csv")==True:
                with open('payment.csv', newline='', encoding='utf-8') as csvfile:
                    payment = csv.reader(csvfile, delimiter=' ', quotechar='|')
                    
                    i = 0
                    for row in payment:
                        i += float(row[1])
                        
                
            
            with open('summary.csv', 'a', newline='', encoding='utf-8') as csvfile:
                summary = csv.writer(csvfile, delimiter=',', quotechar='|',
                    quoting=csv.QUOTE_MINIMAL)
                
                summary.writerow([self.today, i])
                         
        if os.path.exists('summary.csv') == True:
            with open('summary.csv', newline='', encoding='utf-8') as csvfile:
                 summary = csv.reader(csvfile, delimiter=',', quotechar='|')
                 
                 for row in summary:
                     i = row[0] + ": " + row[1]
                     
                     if i not in Summary_payment:
                         Summary_payment.append(i)
        
        
        for i in Summary_payment:
            summary_payment_txt.insert(1.0, i + "\n")
                     
          
        mainBtn = tk.Button(self, text="Główna",
                               command = lambda:controller.show_frame(StartPage))        
        mainBtn.pack()
        mainBtn.place(x = 20, y = 415)
        
        piggybankBtn = tk.Button(self,text="Skarbonka",
                                 command = lambda: controller.show_frame(Piggy))
        
        piggybankBtn.pack()
        piggybankBtn.place(x = 120, y= 415)
  
  
  
# third window frame page2
class Piggy(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text ="W budowie", font = ('Helvetica', 10, 'bold'))
        label.pack()
        label.place(x=10, y=0)
  
        # button to show frame 2 with text
        # layout2
        mainBtn = tk.Button(self, text="Główna",
                               command = lambda:controller.show_frame(StartPage))        
        mainBtn.pack()
        mainBtn.place(x = 20, y = 415)
        
        piggybankBtn = tk.Button(self,text="Podsumowanie",
                                 command = lambda: controller.show_frame(Summary))
        
        piggybankBtn.pack()
        piggybankBtn.place(x = 75, y= 415)
  
        
appRun = Window(app)
app.mainloop()
    
