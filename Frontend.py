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
import random

import googletrans as gtrans
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

logging.basicConfig(filename="logs.log", level=logging.DEBUG)
logger = logging.getLogger()
logger.info(str(datetime.datetime.now())[:-7])
logger.info("Programm is running")
LARGEFONT = ("Italic", 20)
FONT = ("Verdana", 13)
FYNOT = ("Verdana", 13)


jsonsettings = "settings.json"

defaultsettings = {"Language": "en", "deftheme": None, "Animation": True}
try:
    open(jsonsettings, "r")
except:

    with open(jsonsettings, "w") as file:
        json.dump(defaultsettings, file)
filename = "history.csv"
try:
    open(filename, "r")
except:
    a = open(filename, "w")
    a.close()
with open(jsonsettings, "r") as file:
    data = json.load(file)
    global nowlang
    nowlang = data["Language"]

keyboard.add_hotkey("ctrl+q", lambda: exit())
keyboard.add_hotkey("ctrl+s", lambda: app.showframe(code, nowframe))
keyboard.add_hotkey("ctrl+s+shift", lambda: app.showframe(decode, nowframe))
keyboard.add_hotkey("ctrl+r", lambda: restart())
keyboard.add_hotkey("ctrl+i", lambda: app.showframe(InfoPage, nowframe))
keyboard.add_hotkey("ctrl+a+u", lambda: app.showframe(AuthorsPage, nowframe))
keyboard.add_hotkey("ctrl+h", lambda: app.showframe(HistoryPage, nowframe))
keyboard.add_hotkey("ctrl+u", lambda: app.showframe(Settings, nowframe))
keyboard.add_hotkey("ctrl+l", lambda: showlogs())



class app(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        app.iconbitmap(self, os.path.abspath("logov2.ico"))
        app.geometry(self, "1000x630")
        app.title(self, "Shift machine")
        global style
        style = ttk.Style(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand="true")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for Frame in (StartPage, code, decode, SecretPage, InfoPage, AuthorsPage, XOR, Cesar, OTP, deXOR, deCesar, deOTP, HistoryPage, Settings, CombineCypherCode):
            frame = Frame(container, self)
            self.frames[Frame] = frame
            frame.grid(row=0, column=0, sticky="nsew")
    
        self.showframe(StartPage)
    

    def change_theme(self, theme):
        style.theme_use(theme)
        clicksound()

    def showframe(self, cont, now_frame=None):
        if now_frame == None or now_frame == "StartPage":
            clicksound()
            frame = self.frames[cont]
            frame.tkraise()
            logger.info(str(datetime.datetime.now())[:-7])
            logger.info("{} window oppened".format(frame))
            global nowframe
            nowframe = str(cont)[17:-2]
        else:
            logger.info(str(datetime.datetime.now())[:-7])
            logger.info(
                "{} window tried to open with hotkey but access denied.".format(nowframe))




class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=translate("Menu", nowlang), font=LARGEFONT)
        label.pack()
        button1 = ttk.Button(self, text="Make a code (or ctrl+s)",
                             command=lambda: controller.showframe(code), cursor="hand2")
        button1.pack()
        button5 = ttk.Button(self, text="Decode the message (or ctrl+s+shift)",
                             command=lambda: controller.showframe(decode), cursor="hand2")
        button5.pack()
        button2 = ttk.Button(self, text="Secret", command=lambda: controller.showframe(
            SecretPage), cursor="hand2")
        button2.place(x=1000, y=500)
        button3 = ttk.Button(self, text="Info (or ctrl+i)",
                             command=lambda: controller.showframe(InfoPage), cursor="hand2")
        button3.pack()
        button4 = ttk.Button(self, text="Author (or ctrl+a+u)",
                             command=lambda: controller.showframe(AuthorsPage), cursor="hand2")
        button4.pack()
        button5 = ttk.Button(self, text="History (or ctrl+h)",
                             command=lambda: controller.showframe(HistoryPage), cursor="hand2")
        button5.pack()
        button6 = ttk.Button(self, text="Settings (or ctrl+u)",
                             command=lambda: controller.showframe(Settings), cursor="hand2")
        button6.pack()
        button7 = ttk.Button(self, text="Restart the progrramm (or ctrl+r)",
                             command=lambda: restart(), cursor="hand2")
        button7.pack()
        button8 = ttk.Button(self, text="View logs(or ctrl + l)",
                             command=lambda: showlogs(), cursor="hand2")
        button8.pack()
        exitbutton = ttk.Button(
            self, text="Quit (Or press ctrl+Q)", command=exit, cursor="hand2")
        exitbutton.pack()
        exitbutton1 = ttk.Button(
            self, text="Close All (I don't recomend you touch this)", command=exitt, cursor="hand2")
        exitbutton1.pack()



class HistoryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="History", font=LARGEFONT)
        label.pack()
        button1 = ttk.Button(self, text="Back to start page",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self, text="Clear history",
                             command=lambda: clearH(), cursor="hand2")
        button2.pack()

        button3 = ttk.Button(self, text="Refresh", command=lambda: self.refresh(
            controller), cursor="hand2")
        button3.pack()

        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()
     
        self.refresh(controller)
    

    def refresh(self, controller):
    
        clicksound()
        count = 0
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("History refreshed")
        for i in HistoryPage.pack_slaves(self):
            i.pack_forget()
            time.sleep(0.001)
        label = tk.Label(self, text="History", font=LARGEFONT)
        label.pack()
        button1 = ttk.Button(self, text="Back to start page",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self, text="Clear history",
                             command=lambda: clearH(), cursor="hand2")
        button2.pack()
        button3 = ttk.Button(self, text="Refresh", command=lambda: self.refresh(
            controller), cursor="hand2")
        button3.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()
        with open(filename, "r") as file:
            global history
            history = list(csv.reader(file))
        if history != []:
            vars()["my_tree{}".format(count)] = ttk.Treeview(self)
            vars()["my_tree{}".format(count)]["columns"] = (
                "Date", "Cypher", "Recived message", "Returned message", "KEY")
            vars()["my_tree{}".format(count)].column(
                "#0", anchor="center", width=0, minwidth=0)
            vars()["my_tree{}".format(count)].column(
                "Date", anchor="w", width=120, minwidth=100)
            vars()["my_tree{}".format(count)].column(
                "Cypher", anchor="w", width=100, minwidth=100)
            vars()["my_tree{}".format(count)].column(
                "Recived message", anchor="center", width=250, minwidth=100)
            vars()["my_tree{}".format(count)].column(
                "Returned message", anchor="center", width=250, minwidth=100)
            vars()["my_tree{}".format(count)].column(
                "KEY", anchor="center", width=200, minwidth=200)
            vars()["my_tree{}".format(count)].heading(
                "Date", anchor="w", text="Date & time")
            vars()["my_tree{}".format(count)].heading(
                "Cypher", anchor="w", text="Type of Cypher")
            vars()["my_tree{}".format(count)].heading(
                "Recived message", anchor="center", text="Recived message")
            vars()["my_tree{}".format(count)].heading(
                "Returned message", anchor="center", text="Returned message")
            vars()["my_tree{}".format(count)].heading(
                "KEY", anchor="center", text="KEY")
            iid = 0
            for i in history:
                if i != []:
                    vars()["my_tree{}".format(count)].insert(parent="", index="end", iid=iid, text="", values=(
                        i[0], i[1], (i[2] if i[2] != "" else "None"), (i[3] if i[3] != "" else "None"), i[4]))
                    iid += 1

            vars()["my_tree{}".format(count)].pack()
            count += 1
        else:
            label1 = tk.Label(self, text="Empty history", font=LARGEFONT)
            label1.pack()



class code(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Choose type of cypher", font=LARGEFONT)
        label.pack()
        button2 = ttk.Button(
            self, text="XOR", command=lambda: controller.showframe(XOR), cursor="hand2")
        button2.pack()
        button3 = ttk.Button(
            self, text="Cesar's", command=lambda: controller.showframe(Cesar), cursor="hand2")
        button3.pack()
        button4 = ttk.Button(self, text="One-time-pad",
                             command=lambda: controller.showframe(OTP), cursor="hand2")
        button4.pack()
        button5 = ttk.Button(self, text="Combine cypher", command=lambda: controller.showframe(
            CombineCypherCode), cursor="hand2")
        button5.pack()
        button1 = ttk.Button(self, text="back to Start page (or ctrl+s+alt)",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()



class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Settings", font=LARGEFONT)
        label.pack()
        label1 = tk.Label(self, text="Set theme mode", font=LARGEFONT)
        label1.pack()
        self.styles = ['winnative', 'clam', 'alt',
                       'default', 'classic', 'vista', 'xpnative']
        self.selected_theme = tk.StringVar()

        self.data = None

        with open(jsonsettings, "r") as file:
            self.data = json.load(file)

        if self.data["deftheme"] != None:
       
            controller.change_theme(self.data["deftheme"])

        theme_frame = ttk.LabelFrame(self, text='Themes')
        theme_frame.pack()
        for theme_name in self.styles:
            rb = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=lambda: controller.change_theme(self.selected_theme.get()))
            rb.pack(expand=True, fill='both')
        button1 = ttk.Button(self, text="Use selected theme as deafult", command=lambda: self.deafulttheme(
            self.selected_theme.get()), cursor="hand2")
        button1.place(x=700, y=200)
        button2 = ttk.Button(self, text="Don't use selected theme as deafult", command=lambda: self.deafulttheme(
            self.selected_theme.get(), False), cursor="hand2")
        button2.place(x=700, y=230)
        soundsL = ttk.Label(self, text='Sounds', font=LARGEFONT)
        soundsL.pack()
        button3 = ttk.Button(
            self, text="On", command=lambda: yessounds(), cursor="hand2")
        button3.pack()
        button4 = ttk.Button(
            self, text="Off", command=lambda: nosounds(), cursor="hand2")
        button4.pack()
        AnimationLabel = ttk.Label(
            self, text='Codding animation', font=LARGEFONT)
        AnimationLabel.place(x=150, y=200)
        button5 = ttk.Button(self, text="Enable",
                             command=lambda: Anim("True"), cursor="hand2")
        button5.place(x=200, y=250)
        button6 = ttk.Button(self, text="Disable",
                             command=lambda: Anim("False"), cursor="hand2")
        button6.place(x=200, y=300)
        button = ttk.Button(self, text="back to Start Page (or ctrl+s+alt)",
                            command=lambda: controller.showframe(StartPage), cursor="hand2")
        button.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()

    def deafulttheme(self, deftheme, a=True):
        clicksound()
        if a:
            self.use = True
            defaultsettings["deftheme"] = deftheme
            with open(jsonsettings, "w") as file:
                json.dump(defaultsettings, file)
        else:
            self.use = False
            self.deftheme = None
            defaultsettings["deftheme"] = None
            with open(jsonsettings, "w") as file:
                json.dump(defaultsettings, file)


class decode(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Choose type of cypher", font=LARGEFONT)
        label.pack()
        button2 = ttk.Button(
            self, text="XOR", command=lambda: controller.showframe(deXOR), cursor="hand2")
        button2.pack()
        button3 = ttk.Button(self, text="Cesar's", command=lambda: controller.showframe(
            deCesar), cursor="hand2")
        button3.pack()
        button4 = ttk.Button(self, text="One-time-pad",
                             command=lambda: controller.showframe(deOTP), cursor="hand2")
        button4.pack()
        button1 = ttk.Button(self, text="back to Start page (or ctrl+s+alt)",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()



class SecretPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Top Secret", font=LARGEFONT)
        label.pack()
        label1 = tk.Label(
            self, text="My congratulations! You find it!", font=LARGEFONT)
        label1.pack()
        button1 = ttk.Button(self, text="Back to start page",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()


class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="About Cyphers", font=LARGEFONT)
        label.pack()
        label1 = tk.Label(
            self, text="In my programm I use three types of cyphers.", font=LARGEFONT)
        label1.pack()
        label2 = tk.Label(
            self, text="Using my programm, you can code and decode different messages in three different ways", font=FONT)
        label2.pack()
        label3 = tk.Label(
            self, text="You can read about cyphers here:", font=LARGEFONT)
        label3.pack()
        label4 = tk.Label(self, text="XOR cypher",
                          font=LARGEFONT, fg="blue", cursor="hand2")
        label4.pack()
        label4.bind("<Button-1>", lambda e: callback(
            "https://en.wikipedia.org/wiki/Xor%E2%80%93encrypt%E2%80%93xor"))
        label5 = tk.Label(self, text="Cesar's cypher",
                          font=LARGEFONT, fg="blue", cursor="hand2")
        label5.pack()
        label5.bind(
            "<Button-1>", lambda e: callback("https://en.wikipedia.org/wiki/Caesar_cipher"))
        label6 = tk.Label(self, text="One-time-pad cypher",
                          font=LARGEFONT, fg="blue", cursor="hand2")
        label6.pack()
        label6.bind(
            "<Button-1>", lambda e: callback("https://en.wikipedia.org/wiki/One-time_pad"))
        button1 = ttk.Button(self, text="Back to start page",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()



class AuthorsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="About me", font=LARGEFONT)
        label.pack()
        label1 = tk.Label(
            self, text="Made in Russia by Matvey Rotte.", font=LARGEFONT)
        label1.pack()
        label2 = tk.Label(self, text="On python, using: \n-tkinter\n-tkinter.ttk\n-webbrowser\n-pyperclip\n-sys\n-os\n-keyboard\n-datetime\n-string\n-csv\n-logging\n-json\n-time\n-pygame\n-random\n-Google googletrans API for python", font=LARGEFONT)
        label2.pack()
        button1 = ttk.Button(self, text="Back to start page",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.place(x=250, y=300)
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.place(x=250, y=360)


class XOR(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter your message", font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self, width=200)
        self.entrybox.pack()
        button = ttk.Button(self, text="Get coded message",
                            command=self.a, cursor="hand2")
        button.pack()
        button1 = ttk.Button(self, text="Back to start page",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self, text="Clear",
                             command=self.cl, cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()

    def a(self):
        clicksound()
        with open(jsonsettings, "r") as file:
            self.data = json.load(file)

        if self.data["Animation"] != "False":

            self.progressbar = showprogress(self)
        self.button_copy_message = ttk.Button(
            self, text="Copy message", command=lambda: self.copy("mes"), cursor="hand2")
        self.button_copy_key = ttk.Button(
            self, text="Copy key", command=lambda: self.copy("key"), cursor="hand2")
        self.button_copy_key.place(x=50, y=150)
        self.button_copy_message.place(x=50, y=200)
        self.label = tk.Text(self)
        self.ins = func.XOR_cypher(str(self.entrybox.get()))
        self.label.insert(5.0, self.ins)
        self.label.pack()

        data = [str(datetime.datetime.now())[:-10], "XOR",
                self.entrybox.get(), self.ins[1], self.ins[3]]
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("all data:")
        logger.info(data)
        with open(filename, "r") as file:
            reader = list(csv.reader(file))
            reader.append(data)
            for i in reader:
                if i == []:
                    reader.remove(i)
            write = csv.writer(open(filename, "w"))
            write.writerows(reader)
            file.close()

    def cl(self):
        clicksound()
        try:
            self.button_copy_message.destroy()
            self.button_copy_key.destroy()
            self.label.pack_forget()

            for i in range(100):
                self.suclabel.destroy()
        except:
            pass
        self.entrybox.delete(0, "end")

    def copy(self, status):
        if status == "key":
            copy.copy(self.ins[3])
        elif status == "mes":
            copy.copy(self.ins[1])



class Cesar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter your message", font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self, width=200)
        self.entrybox.pack()
        label1 = tk.Label(self, text="Enter num", font=LARGEFONT)
        label1.pack()
        self.entrybox1 = tk.Entry(self, width=200)
        self.entrybox1.pack()
        button = ttk.Button(self, text="Get coded message",
                            command=self.a, cursor="hand2")
        button.pack()
        button1 = ttk.Button(self, text="Back to start page",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self, text="Clear",
                             command=self.cl, cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()

    def a(self):
        clicksound()
        self.label100 = tk.Label(
            self, text="*We use classic cesar!!!!!!!!!!!!!!!!!!!!!!!!!", font=("Verdana", 8))
        self.label100.pack()
        with open(jsonsettings, "r") as file:
            self.data = json.load(file)

        if self.data["Animation"] != "False":

            self.progressbar = showprogress(self)
        self.button_copy_message = ttk.Button(
            self, text="Copy message", command=lambda: self.copy("mes"), cursor="hand2")
        self.button_copy_key = ttk.Button(
            self, text="Copy key", command=lambda: self.copy("key"), cursor="hand2")
        self.button_copy_key.place(x=50, y=150)
        self.button_copy_message.place(x=50, y=200)
        self.label = tk.Text(self)
        self.ins = func.cesars_cypher(
            str(self.entrybox.get()), str(self.entrybox1.get()))
        self.label.insert(5.0, self.ins)
        self.label.pack()
        data = [str(datetime.datetime.now())[:-10], "Cesar",
                self.entrybox.get(), self.ins[1], self.entrybox1.get()]
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("all data:")
        logger.info(data)
        with open(filename, "r") as file:
            reader = list(csv.reader(file))
            reader.append(data)
            for i in reader:
                if i == []:
                    reader.remove(i)
            write = csv.writer(open(filename, "w"))
            write.writerows(reader)
            file.close()

    def cl(self):
        clicksound()
        try:
            self.button_copy_message.destroy()
            self.button_copy_key.destroy()
            self.label.pack_forget()
            self.label100.pack_forget()
            for i in range(100):
                self.suclabel.destroy()
        except:
            pass
        self.entrybox.delete(0, "end")
        self.entrybox1.delete(0, "end")

    def copy(self, status):
        if status == "key":
            copy.copy(self.entrybox1.get())
        elif status == "mes":
            copy.copy(self.ins[1])



class OTP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter your message", font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self, width=200)
        self.entrybox.pack()
        button = ttk.Button(self, text="Get coded message",
                            command=self.a, cursor="hand2")
        button.pack()
        button1 = ttk.Button(self, text="Back to start page",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self, text="Clear",
                             command=self.cl, cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()

    def a(self):
        clicksound()
        with open(jsonsettings, "r") as file:
            self.data = json.load(file)
 
        if self.data["Animation"] != "False":

            self.progressbar = showprogress(self)
        self.button_copy_message = ttk.Button(
            self, text="Copy message", command=lambda: self.copy("mes"), cursor="hand2")
        self.button_copy_key = ttk.Button(
            self, text="Copy key", command=lambda: self.copy("key"), cursor="hand2")
        self.button_copy_key.place(x=50, y=150)
        self.button_copy_message.place(x=50, y=200)
        self.label = tk.Text(self)
        self.ins = func.one_time_pad_cypher(str(self.entrybox.get()))
        self.label.insert(5.0, self.ins)
        self.label.pack()
        data = [str(datetime.datetime.now())[:-10], "One-time-Pad",
                self.entrybox.get(), self.ins[1], self.ins[3]]
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("all data:")
        logger.info(data)
        with open(filename, "r") as file:
            reader = list(csv.reader(file))
            reader.append(data)
            for i in reader:
                if i == []:
                    reader.remove(i)
            write = csv.writer(open(filename, "w"))
            write.writerows(reader)
            file.close()

    def cl(self):
        clicksound()
        try:
            self.button_copy_message.destroy()
            self.button_copy_key.destroy()
            self.label.pack_forget()
            for i in range(100):
                self.suclabel.destroy()
        except:
            pass
        self.entrybox.delete(0, "end")

    def copy(self, status):
        if status == "key":
            copy.copy(str(self.ins[3]))
        elif status == "mes":
            copy.copy(self.ins[1])



class deOTP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter your message", font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self, width=200)
        self.entrybox.pack()
        label1 = tk.Label(self, text="Enteк your key", font=LARGEFONT)
        label1.pack()
        self.entrybox1 = tk.Entry(self, width=200)
        self.entrybox1.pack()
        button = ttk.Button(self, text="Get decoded message",
                            command=self.a, cursor="hand2")
        button.pack()
        button1 = ttk.Button(self, text="Back to start page",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self, text="Clear",
                             command=self.cl, cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()

    def a(self):
        clicksound()
        with open(jsonsettings, "r") as file:
            self.data = json.load(file)

        if self.data["Animation"] != "False":

            self.progressbar = showprogress(self)
        self.button_copy_message = ttk.Button(
            self, text="Copy message", command=lambda: self.copy("mes"), cursor="hand2")
        self.button_copy_key = ttk.Button(
            self, text="Copy key", command=lambda: self.copy("key"), cursor="hand2")
        self.button_copy_key.place(x=50, y=150)
        self.button_copy_message.place(x=50, y=200)
        self.label = tk.Text(self)
        self.ins = func.decoding_for_one_time_pad_cypher(
            str(self.entrybox.get()), str(self.entrybox1.get()))  # key = list(map(int,key))
        self.label.insert(5.0, self.ins)
        self.label.pack()
        data = [str(datetime.datetime.now())[:-10], "One-time-Pad",
                self.entrybox.get(), self.ins[1], self.entrybox1.get()]
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("all data:")
        logger.info(data)
        with open(filename, "r") as file:
            reader = list(csv.reader(file))
            reader.append(data)
            for i in reader:
                if i == []:
                    reader.remove(i)
            write = csv.writer(open(filename, "w"))
            write.writerows(reader)
            file.close()

    def cl(self):
        clicksound()
        try:
            self.button_copy_message.destroy()
            self.button_copy_key.destroy()
            self.label.pack_forget()
            for i in range(100):
                self.suclabel.destroy()
        except:
            pass
        self.entrybox.delete(0, "end")
        self.entrybox1.delete(0, "end")

    def copy(self, status):
        if status == "key":
            copy.copy(self.entrybox1.get())
        elif status == "mes":
            copy.copy(self.ins[1])


class deCesar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter your message", font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self, width=200)
        self.entrybox.pack()
        label1 = tk.Label(self, text="Enteк your num", font=LARGEFONT)
        label1.pack()
        self.entrybox1 = tk.Entry(self, width=200)
        self.entrybox1.pack()
        button = ttk.Button(self, text="Get decoded message",
                            command=self.a, cursor="hand2")
        button.pack()
        button1 = ttk.Button(self, text="Back to start page",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self, text="Clear",
                             command=self.cl, cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()

    def a(self):
        clicksound()
        with open(jsonsettings, "r") as file:
            self.data = json.load(file)

        if self.data["Animation"] != "False":

            self.progressbar = showprogress(self)
        self.button_copy_message = ttk.Button(
            self, text="Copy message", command=lambda: self.copy("mes"), cursor="hand2")
        self.button_copy_key = ttk.Button(
            self, text="Copy key", command=lambda: self.copy("key"), cursor="hand2")
        self.button_copy_key.place(x=50, y=150)
        self.button_copy_message.place(x=50, y=200)
        self.label = tk.Text(self)
        self.ins = func.decoding_for_cesars_cypher()
        self.label.insert(5.0, self.ins)
        self.label.pack()
        data = [str(datetime.datetime.now())[:-10], "Cesar",
                self.entrybox.get(), "None", "None"]
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("all data:")
        logger.info(data)
        with open(filename, "r") as file:
            reader = list(csv.reader(file))
            reader.append(data)
            for i in reader:
                if i == []:
                    reader.remove(i)
            write = csv.writer(open(filename, "w"))
            write.writerows(reader)
            file.close()

    def cl(self):
        clicksound()
        try:
            self.button_copy_message.destroy()
            self.button_copy_key.destroy()
            self.label.pack_forget()
            for i in range(100):
                self.suclabel.destroy()
        except:
            pass
        self.entrybox.delete(0, "end")
        self.entrybox1.delete(0, "end")

    def copy(self, status):
        if status == "key":
            copy.copy(self.entrybox1.get())
        elif status == "mes":
            copy.copy("O my gud! LooooooooooL GOOGLE :D （*゜ー゜*）（*゜ー゜*）（*゜ー゜*）（*゜ー゜*）（*゜ー゜*）（*゜ー゜*）（*゜ー゜*）o((⊙﹏⊙))o....(*￣０￣)ノ（*゜ー゜*）（*゜ー゜*）（*゜ー゜*）(⊙o⊙)(⊙_⊙;)")



class deXOR(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter your message", font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self, width=200)
        self.entrybox.pack()
        label1 = tk.Label(self, text="Enter your key", font=LARGEFONT)
        label1.pack()
        self.entrybox1 = tk.Entry(self, width=200)
        self.entrybox1.pack()
        button = ttk.Button(self, text="Get decoded message",
                            command=self.a, cursor="hand2")
        button.pack()
        button1 = ttk.Button(self, text="Back to start page",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self, text="Clear",
                             command=self.cl, cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()

    def a(self):
        clicksound()
        with open(jsonsettings, "r") as file:
            self.data = json.load(file)

        if self.data["Animation"] != "False":

            self.progressbar = showprogress(self)
        self.button_copy_message = ttk.Button(
            self, text="Copy message", command=lambda: self.copy("mes"), cursor="hand2")
        self.button_copy_key = ttk.Button(
            self, text="Copy key", command=lambda: self.copy("key"), cursor="hand2")
        self.button_copy_key.place(x=50, y=150)
        self.button_copy_message.place(x=50, y=200)
        self.label = tk.Text(self)
        self.ins = func.XOR_cypher(
            str(self.entrybox.get()), "decode", str(self.entrybox1.get()))
        self.label.insert(5.0, self.ins)
        self.label.pack()
        data = [str(datetime.datetime.now())[:-10], "XOR",
                self.entrybox.get(), self.ins[1], self.entrybox1.get()]
        logger.info(str(datetime.datetime.now())[:-7])
        logger.info("all data:")
        logger.info(data)
        with open(filename, "r") as file:
            reader = list(csv.reader(file))
            reader.append(data)
            for i in reader:
                if i == []:
                    reader.remove(i)
            write = csv.writer(open(filename, "w"))
            write.writerows(reader)
            file.close()

    def cl(self):
        clicksound()
        try:
            self.button_copy_message.destroy()
            self.button_copy_key.destroy()
            self.label.pack_forget()
            for i in range(100):
                self.suclabel.destroy()
        except:
            pass
        self.entrybox.delete(0, "end")
        self.entrybox1.delete(0, "end")

    def copy(self, status):
        if status == "key":
            copy.copy(self.entrybox1.get())
        elif status == "mes":
            copy.copy(self.ins[1])



class CombineCypherCode(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.y = 60
        self.labels = []
        self.R = False
        self.packedcyphers = 0
        self.cypherssequence = []
        self.buttonshowexpl = ttk.Button(
            self, text="Show explanation", command=self.showhelp, cursor="hand2")
        self.buttonhideexpl = ttk.Button(
            self, text="Hide explanation", command=self.hidehelp, cursor="hand2")
        self.buttonhideexpl.pack()
        self.label10 = tk.Label(
            self, text="What is combine cypher?", font=LARGEFONT)  # ("Verdana",9)
        self.label10.pack()
        self.label11 = tk.Label(self, text="Using combine cypher, at first, you will choose sequence of cyphers(less than 11).\n Next,programm will code your message in first cypher you choosed, \nthen, resulting coded message, will be coded one more time in your second cypher,and  etc.\n Of course, to decode this cypher we should know all cyphers in correct sequence and all keys in correct sequence.\n*If you will choose Cesar, number will being automaticly generated by programm", font=("Verdana", 9))  # ("Verdana",9)
        self.label11.pack()
        label = tk.Label(self, text="Enter your message", font=LARGEFONT)
        label.pack()
        self.entrybox = tk.Entry(self, width=200)
        self.entrybox.pack()

        self.labell = tk.Label(self, text="10 is maximum!",
                               font=LARGEFONT)  # ("Verdana",9)
        self.labell.place(x=20, y=550)

        self.buttonXORplus = ttk.Button(
            self, text="XOR", command=lambda: self.addcypher("XOR"), cursor="hand2")
        self.buttonXORplus.pack()
        self.buttonCesarplus = ttk.Button(
            self, text="Cesar", command=lambda: self.addcypher("Cesar"), cursor="hand2")
        self.buttonCesarplus.pack()
        self.buttonOTPplus = ttk.Button(
            self, text="One-Time-Pad", command=lambda: self.addcypher("OTP"), cursor="hand2")
        self.buttonOTPplus.pack()
        self.minusbutton = ttk.Button(
            self, text="-1", command=lambda: self.deletelastcypher(), cursor="hand2")
        self.minusbutton.pack()
        self.minusbutton2 = ttk.Button(
            self, text="reset", command=lambda: self.deletelastcypher("all"), cursor="hand2")
        self.minusbutton2.pack()

        button1 = ttk.Button(self, text="Back to start page",
                             command=lambda: controller.showframe(StartPage), cursor="hand2")
        button1.pack()
        button2 = ttk.Button(self, text="Clear",
                             command=self.cl, cursor="hand2")
        button2.pack()
        exitbutton = ttk.Button(
            self, text="Quit", command=exit, cursor="hand2")
        exitbutton.pack()

    def a(self):
   
        with open(jsonsettings, "r") as file:
            self.data = json.load(file)
     
        if self.data["Animation"] != "False":

            self.progressbar = showprogress(self, 100, 250)
        clicksound()
        self.keys = []
        self.labell.destroy()
        self.buttonXORplus.pack_forget()
        self.buttonCesarplus.pack_forget()
        self.buttonOTPplus.pack_forget()
        self.minusbutton.pack_forget()
        self.minusbutton2.pack_forget()

        self.message = str(self.entrybox.get())


        for i in self.cypherssequence:
            print(i)

            if i == "XOR":
                self.ins = func.XOR_cypher(self.message)
                self.keys.append(str(self.ins[3]) + " ")
                data = [str(datetime.datetime.now())[:-10], i,
                        self.message, self.ins[1], self.ins[3]]

            elif i == "Cesar":
                num = random.randint(0, 90)
                self.keys.append(str(num) + " ")
                self.ins = func.cesars_cypher(self.message, num)
                data = [str(datetime.datetime.now())[:-10],
                        i, self.message, self.ins[1], num]
 
            elif i == "OTP":
                self.ins = func.one_time_pad_cypher(self.message)
                self.keys.append(str(self.ins[3]) + " ")
                data = [str(datetime.datetime.now())[:-10], i,
                        self.message, self.ins[1], self.ins[3]]


            self.message = self.ins[1]
            print(data)
            print(self.message)  # IT writes translates over one
            logger.info(str(datetime.datetime.now())[:-7])
            logger.info("all data:")
            logger.info(data)

            with open(filename, "r") as file:
                reader = list(csv.reader(file))
                reader.append(data)
                for i in reader:
                    if i == []:
                        reader.remove(i)
                write = csv.writer(open(filename, "w"))
                write.writerows(reader)
                file.close()

        self.deletelastcypher("all")
        self.button_copy_message = ttk.Button(
            self, text="Copy message", command=lambda: self.copy("mes"), cursor="hand2")
        self.button_copy_key = ttk.Button(
            self, text="Copy key", command=lambda: self.copy("key"), cursor="hand2")
        self.button_copy_key.place(x=50, y=150)
        self.button_copy_message.place(x=50, y=200)
        self.label = tk.Text(self)
        self.label.insert(5.0, self.ins)
        self.label.pack()
        self.buttonshowexpl.pack_forget()

    def cl(self):
        clicksound()
        try:
            self.button_copy_key.destroy()
            self.button_copy_message.destroy()
            self.CodeItButton.pack_forget()
            self.label.pack_forget()
            self.entrybox.delete(0, "end")  # 33

            for i in range(100):
                self.suclabel.destroy()
        except:
            pass

    def copy(self, status):
        if status == "key":
            copy.copy("".join(self.keys))
        elif status == "mes":
            copy.copy(self.message)


    def hidehelp(self):
        clicksound()
        self.label10.pack_forget()
        self.label11.pack_forget()
        self.buttonshowexpl.pack()
        self.buttonhideexpl.pack_forget()

    def showhelp(self):
        clicksound()
        self.label10.pack()
        self.label11.pack()
        self.buttonshowexpl.pack_forget()
        self.buttonhideexpl.pack()

    def addcypher(self, cypher):
        self.hidehelp()

        if len(self.cypherssequence) > 1 and not self.R:
            self.CodeItButton = ttk.Button(
                self, text="Code IT", command=self.a, cursor="hand2")
            self.CodeItButton.pack()
            self.R = True
        if self.packedcyphers < 10:
            vars()["clabel{}".format(self.packedcyphers)] = tk.Label(
                self, text=cypher, font=LARGEFONT)  # ("Verdana",9)
            vars()["clabel{}".format(self.packedcyphers)].place(
                x=30, y=self.y+50)
            self.labels.append(vars()["clabel{}".format(self.packedcyphers)])
            self.y += 30
            self.packedcyphers += 1
            self.cypherssequence.append(cypher)

    def deletelastcypher(self, status=None):
        clicksound()
        if len(self.cypherssequence) < 3 and self.R:
            self.CodeItButton.pack_forget()
            self.R = False
        if status == "all":
            for i in range(11):
                try:
                    del self.cypherssequence[-1]
                    self.labels[-1].destroy()
                    del self.labels[-1]
                    self.packedcyphers -= 1
                    self.y -= 30
                    self.CodeItButton.pack_forget()
                    self.R = False
                except:
                    pass
        else:
            try:
                del self.cypherssequence[-1]
                self.labels[-1].destroy()
                del self.labels[-1]
                self.packedcyphers -= 1
                self.y -= 30
            except:
                pass


def exit():
    clicksound()
    logger.info(str(datetime.datetime.now())[:-7])
    logger.info("Quit button pressed")
    app.destroy()


def exitt():
    clicksound()
    logger.info(str(datetime.datetime.now())[:-7])
    logger.info("Close all button pressed")
    for i in range(50):
        keyboard.send("ctrl+Win+Right")


def callback(url):
    clicksound()
    logger.info(str(datetime.datetime.now())[:-7])
    logger.info("Way to browser")
    web.open_new(url)


def clearH():
    clicksound()
    logger.info(str(datetime.datetime.now())[:-7])
    logger.info("Clear history button pressed")
    try:
        os.remove(filename)
    except:
        pass
    else:
        a = open(filename, "w")
        a.close()


def yessounds(a=0):
    pygame.mixer.init()
    if a == 0:
        pygame.mixer.music.load("clicksound.mp3")
        pygame.mixer.music.play(loops=0)


def clicksound():
    try:
        pygame.mixer.music.load("clicksound.mp3")
        pygame.mixer.music.play(loops=0)
    except:
        pass


def nosounds():
    pygame.mixer.quit()


def Anim(status):
    clicksound()
    defaultsettings["Animation"] = status
    with open(jsonsettings, "w") as file:
        json.dump(defaultsettings, file)


def showprogress(frame, x=None, y=None):
    progressbar = ttk.Progressbar(
        frame, orient="horizontal", length=300, mode="determinate")
    progressbar["value"] = 0
    progresslabel = tk.Label(frame, text="0%")
    try:
        progressbar.place(x=x, y=y)
        progresslabel.place(x=x+100, y=y+30)
    except:
        progressbar.pack()
        progresslabel.pack()
    for i in range(100):
        progressbar["value"] += 1
        progresslabel.config(text="{}%".format(progressbar["value"]))
        time.sleep(0.01)
        app.update_idletasks()
    progresslabel.destroy()
    progressbar.destroy()


def showlogs():
    clicksound()
    os.startfile("logs.log")


def restart():
    os.startfile(f"{__file__}")
    sys.exit()


def translate(mes, lang):
    try:
        translator = gtrans.Translator()
        translation = translator.translate(mes, dest=lang)
        return translation.text
    except:
        return mes

    app.mainloop()



app = app()

app.bell()
yessounds(1)

app.mainloop()
