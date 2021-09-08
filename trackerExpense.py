import tkinter as tk
from tkinter import *
from datetime import datetime
import os
import pickle
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
        self.totalTxt.delete(1.0,"end")
        self.totalTxt.insert(1.0,self.total)

        today = datetime.now().date()
        dateTxt = Label(self, font='Helvetica 10 bold')
        dateTxt.pack()
        dateTxt.place(x=500, y=10)
        #dateTxt.insert(1.0, dateCur)
        dateTxt.config(bg="#a5a6f6", text= today)

        totalLbl = Label(self, text="Saldo:")
        totalLbl.pack()
        totalLbl.place(x=20,y=140)
        totalLbl.config(bg="#a5a6f6")

        summary_month = []
        if os.path.exists("total.dat")==True:
            self.total = pickle.load(open("total.dat","rb"))
            self.totalTxt.delete(1.0,"end")
            self.totalTxt.insert(1.0, self.total)
            
        if today.day == 1 or os.path.exists("summaryMonth.dat") == False:
            summary_month.append((str(today)[0:10]+":",self.total))
            pickle.dump(summary_month,open("summaryMonth.dat","wb"))
        
        
        
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
        self.historyPay.delete(1.0,"end")

        if os.path.exists("payment.dat")==True:
            self.history = pickle.load(open("payment.dat", "rb"))
            for i in self.history:
                self.historyPay.insert(1.0, i)
                
        summaryBtn = tk.Button(self, text="Podsumowanie",
                               command = lambda:controller.show_frame(Summary))        
        summaryBtn.pack()
        summaryBtn.place(x = 20, y = 415)
        
        piggybankBtn = tk.Button(self,text="Skarbonka",
                                 command = lambda: controller.show_frame(Piggy))
        
        piggybankBtn.pack()
        piggybankBtn.place(x = 120, y= 415)
        
    def payment(self):
        cashName = self.nameEntry.get()
        cashInPrize = float(self.prizeEntry.get())
        self.total = self.total+cashInPrize
        cash = cashName + ": "+ str(cashInPrize)
        self.history.append(cash + " zł\n")
        pickle.dump(round(self.total,2),open("total.dat","wb"))
        pickle.dump(self.history,open("payment.dat","wb"))
        self.totalTxt.delete(1.0,"end")
        self.totalTxt.insert(1.0, self.total)
        
        self.historyPay.delete(1.0, "end")
        for i in self.history:
            self.historyPay.insert(1.0, i)
    
    def cashOut(self):
        cashName = self.nameEntry.get()
        cashOutPrize = float(self.prizeEntry.get())
        self.total = self.total-cashOutPrize
        cash = cashName + ": "+ str(cashOutPrize)
        self.history.append(cash + " zł\n")
        pickle.dump(round(self.total,2),open("total.dat","wb"))
        pickle.dump(self.history,open("payment.dat","wb"))
        self.totalTxt.delete(1.0,"end")
        self.totalTxt.insert(1.0,str(self.total,"zł"))
        
        self.historyPay.delete(1.0, "end")
        for i in self.history:
            self.historyPay.insert(1.0, i)
  
class Summary(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text ="Podsumowanie", font = ('Helvetica', 10, 'bold'))
        label.pack()
        label.place(x=10, y=0)
        summary_payment_txt = tk.Text(self)
        summary_payment_txt.pack()
        summary_payment_txt.place(x=20,y=30, height=350, width=500)

        if os.path.getsize("summaryMonth.dat")> 0:
            summary_payment = pickle.load(open("summaryMonth.dat", "rb"))
            for i in summary_payment:
                summary_payment_txt.delete(1.0, "end")
                summary_payment_txt.insert(1.0, i)
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
    
