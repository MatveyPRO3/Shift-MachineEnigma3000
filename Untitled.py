import tkinter as tk
from tkinter import ttk
import webbrowser as web
import pyperclip as copy
import Backend as func
import sys
import os
import keyboard
import datetime 
import string
import csv
import logging
import json
import time
logging.basicConfig(filename="logs.log",level=logging.DEBUG)
logger = logging.getLogger()
logger.info(str(datetime.datetime.now())[:-7])
logger.info("Programm is running")
LARGEFONT = ("Verdana",20)
FONT = ("Verdana",13)
FYNOT = ("Verdana",13)
global jsonsettings
jsonsettings = "settings.json"
try:
    open(jsonsettings,"r")
except:
    defaultsettings = {"Language":"eng"}
    with open(jsonsettings,"w") as file:
        json.dump(defaultsettings,file)
global filename
filename = "history.csv"
try:
    open(filename,"r")
except:
    a = open(filename,"w")
    a.close()
keyboard.add_hotkey("ctrl+q", lambda: exit())#Message: spAzI KEY: {14 14 18 17 23}
keyboard.add_hotkey("ctrl+s",lambda:app.showframe(code))
keyboard.add_hotkey("ctrl+s+shift",lambda:app.showframe(decode))
keyboard.add_hotkey("ctrl+s+alt",lambda:app.showframe(StartPage))
keyboard.add_hotkey("ctrl+i",lambda:app.showframe(InfoPage))
keyboard.add_hotkey("ctrl+a+u",lambda:app.showframe(AuthorsPage))
keyboard.add_hotkey("ctrl+h",lambda:app.showframe(HistoryPage))
keyboard.add_hotkey("ctrl+u",lambda:app.showframe(Settings))
class app(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        app.iconbitmap(self,os.path.abspath("logov2.ico"))
        app.geometry(self,"1000x600")
        app.title(self,"Shift machine")
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand="true")
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames = {}
        for Frame in (StartPage,code,decode,SecretPage,InfoPage,AuthorsPage,XOR,Cesar,OTP,deXOR,deCesar,deOTP,HistoryPage,Settings):
            frame = Frame(container,self)
            self.frames[Frame] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.showframe(StartPage)
    def showframe(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("{} window oppened".format(frame))
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="start page",font=LARGEFONT)
        label.pack()
        button1 = ttk.Button(self,text="Make a code (or ctrl+s)",command=lambda:controller.showframe(code),cursor="hand2")
        button1.pack()
        button5 = ttk.Button(self,text="Decode the message (or ctrl+s+shift)",command=lambda:controller.showframe(decode),cursor="hand2")
        button5.pack()
        button2 = ttk.Button(self,text="Secret",command=lambda:controller.showframe(SecretPage),cursor="hand2")
        button2.place(x=1000,y=500)
        button3 = ttk.Button(self,text="Info (or ctrl+i)",command=lambda:controller.showframe(InfoPage),cursor="hand2")
        button3.pack()
        button4 = ttk.Button(self,text="Author (or ctrl+a+u)",command=lambda:controller.showframe(AuthorsPage),cursor="hand2")
        button4.pack()
        button5 = ttk.Button(self,text="History (or ctrl+h)",command=lambda:controller.showframe(HistoryPage),cursor="hand2")
        button5.pack()
        button6 = ttk.Button(self,text="Settings (or ctrl+u)",command=lambda:controller.showframe(Settings),cursor="hand2")
        button6.pack()
        exitbutton = ttk.Button(self,text="Quit (Or press ctrl+Q)",command=exit,cursor="hand2")
        exitbutton.pack()
        exitbutton1 = ttk.Button(self,text="Close All (I don't recomend you touch this)",command=exitt,cursor="hand2")
        exitbutton1.pack()
class HistoryPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="History",font=LARGEFONT)
        label.pack()
        button1 = ttk.Button(self,text="Back to start page",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self,text="Clear history",command=lambda:clearH(),cursor="hand2")
        button2.pack()
        button3 = ttk.Button(self,text="Refresh",command=lambda:self.refresh(controller),cursor="hand2")
        button3.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
        self.refresh(controller)
    def refresh(self,controller):
        count = 0
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("History refreshed")
        for i in HistoryPage.pack_slaves(self):
            i.pack_forget()
            time.sleep(0.001)
        label = tk.Label(self,text="History",font=LARGEFONT)
        label.pack()
        button1 = ttk.Button(self,text="Back to start page",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self,text="Clear history",command=lambda:clearH(),cursor="hand2")
        button2.pack()
        button3 = ttk.Button(self,text="Refresh",command=lambda:self.refresh(controller),cursor="hand2")
        button3.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
        with open(filename,"r") as file:
            global history
            history = list(csv.reader(file))
        if history != []:
            vars()["my_tree{}".format(count)] = ttk.Treeview(self)
            vars()["my_tree{}".format(count)]["columns"]  = ("Date","Cypher","Recived message","Returned message")
            vars()["my_tree{}".format(count)].column("#0",anchor="center",width=0,minwidth=0)
            vars()["my_tree{}".format(count)].column("Date",anchor="w",width=120,minwidth=100)
            vars()["my_tree{}".format(count)].column("Cypher",anchor="w",width=120,minwidth=100)
            vars()["my_tree{}".format(count)].column("Recived message",anchor="center",width=350,minwidth=100)
            vars()["my_tree{}".format(count)].column("Returned message",anchor="e",width=350,minwidth=100)
            vars()["my_tree{}".format(count)].heading("Date",anchor="w",text="Date & time")
            vars()["my_tree{}".format(count)].heading("Cypher",anchor="w",text="Type of Cypher")
            vars()["my_tree{}".format(count)].heading("Recived message",anchor="center",text="Recived message")
            vars()["my_tree{}".format(count)].heading("Returned message",anchor="e",text="Returned message")
            iid = 0 
            for i in history:
                if i != []:
                    vars()["my_tree{}".format(count)].insert(parent="",index="end",iid=iid,text="",values=(i[0],i[1],(i[2] if i[2] != "" else "None"),(i[3] if i[3] != "" else "None")))
                    iid+=1
            vars()["my_tree{}".format(count)].pack()
            count+=1
        else:
            label1 = tk.Label(self,text="Empty history",font=LARGEFONT)
            label1.pack()
class code(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Choose type of cypher",font=LARGEFONT)
        label.pack()
        button2 = ttk.Button(self,text="XOR",command=lambda:controller.showframe(XOR),cursor="hand2")
        button2.pack()
        button3 = ttk.Button(self,text="Cesar's",command=lambda:controller.showframe(Cesar),cursor="hand2")
        button3.pack()
        button4 = ttk.Button(self,text="One-time-pad",command=lambda:controller.showframe(OTP),cursor="hand2")
        button4.pack()
        button1 = ttk.Button(self,text="back to Start page (or ctrl+s+alt)",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
class Settings(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Settings",font=LARGEFONT)
        label.pack()
        label1 = tk.Label(self,text="Set color mode",font=LARGEFONT)
        label1.pack()
        button = ttk.Button(self,text="Red mode",command=lambda:setcolormode(self,"red"),cursor="hand2")
        button.pack()
        button2 = ttk.Button(self,text="Green mode",command=lambda:setcolormode(self,"green"),cursor="hand2")
        button2.pack()
        button3 = ttk.Button(self,text="Classic mode",command=lambda:setcolormode(self,"grey"),cursor="hand2")
        button3.pack()
        button4 = ttk.Button(self,text="Yellow mode",command=lambda:setcolormode(self,"yellow"),cursor="hand2")
        button4.pack()
        button5 = ttk.Button(self,text="Black(night) mode",command=lambda:setcolormode(self,"black"),cursor="hand2")
        button5.pack()
        button1 = ttk.Button(self,text="Blue mode",command=lambda:setcolormode(self,"blue"),cursor="hand2")
        button1.pack()
        button6 = ttk.Button(self,text="back to Start page (or ctrl+s+alt)",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button6.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
class decode(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Choose type of cypher",font=LARGEFONT)
        label.pack()
        button2 = ttk.Button(self,text="XOR",command=lambda:controller.showframe(deXOR),cursor="hand2")
        button2.pack()
        button3 = ttk.Button(self,text="Cesar's",command=lambda:controller.showframe(deCesar),cursor="hand2")
        button3.pack()
        button4 = ttk.Button(self,text="One-time-pad",command=lambda:controller.showframe(deOTP),cursor="hand2")
        button4.pack()
        button1 = ttk.Button(self,text="back to Start page (or ctrl+s+alt)",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
class SecretPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Top Secret",font=LARGEFONT)
        label.pack()
        label1 = tk.Label(self,text="My congratulations! You find it!",font=LARGEFONT)
        label1.pack()
        button1 = ttk.Button(self,text="Back to start page",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
        
            
class InfoPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="About Cyphers",font=LARGEFONT)
        label.pack()
        label1 = tk.Label(self,text="In my programm I use three types of cyphers.",font=LARGEFONT)
        label1.pack()
        label2 = tk.Label(self,text="Using my programm, you can code and decode different messages in three different ways",font=FONT)
        label2.pack()
        label3 = tk.Label(self,text="You can read about cyphers here:",font=LARGEFONT)
        label3.pack()
        label4 = tk.Label(self,text="XOR cypher",font=LARGEFONT, fg="blue", cursor="hand2")
        label4.pack()
        label4.bind("<Button-1>",lambda e: callback("https://en.wikipedia.org/wiki/Xor%E2%80%93encrypt%E2%80%93xor"))
        label5 = tk.Label(self,text="Cesar's cypher",font=LARGEFONT, fg="blue", cursor="hand2")
        label5.pack()
        label5.bind("<Button-1>",lambda e: callback("https://en.wikipedia.org/wiki/Caesar_cipher"))
        label6 = tk.Label(self,text="One-time-pad cypher",font=LARGEFONT,fg="blue", cursor="hand2")
        label6.pack()
        label6.bind("<Button-1>",lambda e: callback("https://en.wikipedia.org/wiki/One-time_pad"))
        button1 = ttk.Button(self,text="Back to start page",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
class AuthorsPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="About me",font=LARGEFONT)
        label.pack()
        label1 = tk.Label(self,text="Made in Russia by MatveyPRO3.",font=LARGEFONT)
        label1.pack()
        label2 = tk.Label(self,text="On python, using tkinter.",font=LARGEFONT)
        label2.pack()
        label3 = tk.Label(self,text="Timur Zukhba helped me only with cyphers.",font=LARGEFONT)
        label3.pack()
        button1 = ttk.Button(self,text="Back to start page",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
class XOR(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Enter your message",font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self,width=200)
        self.entrybox.pack()
        button = ttk.Button(self,text="Get coded message",command=self.a,cursor="hand2")
        button.pack()
        button1 = ttk.Button(self,text="Back to start page",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self,text="Clear",command=self.cl,cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
    def a(self):
        self.label = tk.Text(self)
        ins = func.XOR_cypher(str(self.entrybox.get()))
        self.label.insert(5.0,ins)
        self.label.pack()
        self.m = tk.Label(self,text="message was coping into your clipboard")
        self.m.pack()
        copy.copy(ins[3])
        data = [str(datetime.datetime.now())[:-10],"XOR",self.entrybox.get(),ins[3]]
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("all data:")
        logger.info(data)
        with open(filename,"r") as file:
            reader = list(csv.reader(file))
            reader.append(data)
            write = csv.writer(open(filename,"w"))
            write.writerows(reader)
            file.close()
    def cl(self):
        self.label.pack_forget()
        self.m.pack_forget()
class Cesar(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Enter your message",font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self,width=200)
        self.entrybox.pack()
        label1 = tk.Label(self,text="Enter num",font=LARGEFONT)
        label1.pack()
        self.entrybox1 = tk.Entry(self,width=200)
        self.entrybox1.pack()
        button = ttk.Button(self,text="Get coded message",command=self.a,cursor="hand2")
        button.pack()
        button1 = ttk.Button(self,text="Back to start page",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self,text="Clear",command=self.cl,cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
    def a(self):
        self.label = tk.Text(self)
        ins = func.cesars_cypher(str(self.entrybox.get()),str(self.entrybox1.get()))
        self.label.insert(5.0,ins)
        self.label.pack()
        self.m = tk.Label(self,text="message was coping into your clipboard")
        self.m.pack()
        copy.copy(ins[1])
        data = [str(datetime.datetime.now())[:-10],"Cesar",self.entrybox.get(),ins[1]]
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("all data:")
        logger.info(data)
        with open(filename,"r") as file:
            reader = list(csv.reader(file))
            reader.append(data)
            write = csv.writer(open(filename,"w"))
            write.writerows(reader)
            file.close()
    def cl(self):
        self.label.pack_forget()
        self.m.pack_forget()
class OTP(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Enter your message",font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self,width=200)
        self.entrybox.pack()
        button = ttk.Button(self,text="Get coded message",command=self.a,cursor="hand2")
        button.pack()
        button1 = ttk.Button(self,text="Back to start page",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self,text="Clear",command=self.cl,cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
    def a(self):
        self.label = tk.Text(self)
        ins = func.one_time_pad_cypher(str(self.entrybox.get()))
        self.label.insert(5.0,ins)
        self.label.pack()
        self.m = tk.Label(self,text="message was coping into your clipboard")
        self.m.pack()
        copy.copy(ins[1])
        data = [str(datetime.datetime.now())[:-10],"One-time-Pad",self.entrybox.get(),ins[1]]
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("all data:")
        logger.info(data)
        with open(filename,"r") as file:
            reader = list(csv.reader(file))
            reader.append(data)
            write = csv.writer(open(filename,"w"))
            write.writerows(reader)
            file.close()
    def cl(self):
        self.label.pack_forget()
        self.m.pack_forget()
        
class deOTP(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Enter your message",font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self,width=200)
        self.entrybox.pack()
        label1 = tk.Label(self,text="Enteк your key",font=LARGEFONT)
        label1.pack()
        self.entrybox1 = tk.Entry(self,width=200)
        self.entrybox1.pack()
        button = ttk.Button(self,text="Get decoded message",command=self.a,cursor="hand2")
        button.pack()
        button1 = ttk.Button(self,text="Back to start page",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self,text="Clear",command=self.cl,cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
    def a(self):
        self.label = tk.Text(self)
        ins = func.decoding_for_one_time_pad_cypher(str(self.entrybox.get()),str(self.entrybox1.get()))#key = list(map(int,key))
        self.label.insert(5.0,ins)
        self.label.pack()
        self.m = tk.Label(self,text="message was coping into your clipboard")
        self.m.pack()
        copy.copy(ins[1])
        data = [str(datetime.datetime.now())[:-10],"One-time-Pad",self.entrybox.get(),ins[1]]
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("all data:")
        logger.info(data)
        with open(filename,"r") as file:
            reader = list(csv.reader(file))
            reader.append(data)
            write = csv.writer(open(filename,"w"))
            write.writerows(reader)
            file.close()
    def cl(self):
        self.label.pack_forget()
        self.m.pack_forget()
class deCesar(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Enter your message",font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self,width=200)
        self.entrybox.pack()
        label1 = tk.Label(self,text="Enteк your num",font=LARGEFONT)
        label1.pack()
        self.entrybox1 = tk.Entry(self,width=200)
        self.entrybox1.pack()
        button = ttk.Button(self,text="Get decoded message",command=self.a,cursor="hand2")
        button.pack()
        button1 = ttk.Button(self,text="Back to start page",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self,text="Clear",command=self.cl,cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
    def a(self):
        self.label = tk.Text(self)
        ins = func.decoding_for_cesars_cypher()
        self.label.insert(5.0,ins)
        self.label.pack()
        self.m = tk.Label(self,text="message was coping into your clipboard")
        self.m.pack()
        copy.copy("(。_。) Are you stuped? Why you try to paste this, if I said that this doesn't work? So, well done. We need people like you. Goggle")
        data = [str(datetime.datetime.now())[:-10],"Cesar",self.entrybox.get(),"None"]
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("all data:")
        logger.info(data)
        with open(filename,"r") as file:
            reader = list(csv.reader(file))
            reader.append(data)
            write = csv.writer(open(filename,"w"))
            write.writerows(reader)
            file.close()
    def cl(self):
        self.label.pack_forget()
        self.m.pack_forget()
class deXOR(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Enter your message",font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self,width=200)
        self.entrybox.pack()
        label1 = tk.Label(self,text="Enter your key",font=LARGEFONT)
        label1.pack()
        self.entrybox1 = tk.Entry(self,width=200)
        self.entrybox1.pack()
        button = ttk.Button(self,text="Get decoded message",command=self.a,cursor="hand2")
        button.pack()
        button1 = ttk.Button(self,text="Back to start page",command=lambda:controller.showframe(StartPage),cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self,text="Clear",command=self.cl,cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(self,text="Quit",command=exit,cursor="hand2")
        exitbutton.pack()
    def a(self):
        self.label = tk.Text(self)
        ins = func.XOR_cypher(str(self.entrybox.get()),"decode",str(self.entrybox1.get()))
        self.label.insert(5.0,ins)
        self.label.pack()
        self.m = tk.Label(self,text="message was coping into your clipboard")
        self.m.pack()
        copy.copy(ins[3])
        data = [str(datetime.datetime.now())[:-10],"XOR",self.entrybox.get(),ins[3]]
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("all data:")
        logger.info(data)
        with open(filename,"r") as file:
            reader = list(csv.reader(file))
            reader.append(data)
            write = csv.writer(open(filename,"w"))
            write.writerows(reader)
            file.close()
    def cl(self):
        self.label.pack_forget()
        self.m.pack_forget()
def exit():
    logger.info(str(datetime.datetime.now())[:-7])
    logger.info("Quit button pressed")
    app.destroy()
def exitt():
    logger.info(str(datetime.datetime.now())[:-7])
    logger.info("Close all button pressed")
    for i in range(50):
        keyboard.send("ctrl+Win+Right")
def callback(url):
    logger.info(str(datetime.datetime.now())[:-7])
    logger.info("Way to browser")
    web.open_new(url)
def clearH():
    logger.info(str(datetime.datetime.now())[:-7])
    logger.info("Clear history button pressed")
    try:
        os.remove(filename)
    except:
        pass
    else:
        a = open(filename,"w")
        a.close()
def setcolormode(frame,color):
    frame.configure(bg=color)  
app = app()
app.mainloop()