import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox as tm
#from mainpage import *
import libpagea
FONT= ("Verdana",12)

class Adminpage(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Library System", font=("Verdana", 30), fg="blue").place(x=450,y=30)
        label2 = tk.Label(self, text="Admin Login", font=("Verdana", 16)).place(x=550, y=100)
        self.user = tk.StringVar()
        self.pass1= tk.StringVar()

        self.lab1 = tk.Label(self, text="Username :").place(x=500,y=150)
        self.entry1 = tk.Entry(self, textvariable = self.user,font=FONT)
        self.entry1.place(x=570,y=150)

        self.lab2 = tk.Label(self, text="Password :").place(x=500,y=200)
        self.entry2 = tk.Entry(self, textvariable= self.pass1, show= "*",font=FONT)
        self.entry2.place(x=570,y=200)
        self.loginbutton=ttk.Button(self, text="Login", command= lambda: self.data_entry())
        self.loginbutton.place(x=550,y=250)
        import login
        self.registerbutton = ttk.Button(self, text="User mode", command=lambda:  self.controller.show_frame(login.Loginpage))
        self.registerbutton.place(x=670, y=250)

    def data_entry(self):
        conn = sqlite3.connect('database/login.db')
        c = conn.cursor()
        self.user1 = self.user.get()
        self.pass2 = self.pass1.get()
        if (self.user1 == ""):
            tm.showwarning("Error", "Enter Username")
        elif (self.pass2 == ""):
            tm.showwarning("Error", "Enter Password")
        else:
            c.execute('CREATE TABLE IF NOT EXISTS admintable(username TEXT,password TEXT)')
            d = c.execute('SELECT username,password FROM admintable WHERE username= "%s" AND password="%s"' % (self.user1, self.pass2))
            conn.commit()
            if (d.fetchone()):
                self.controller.show_frame(libpagea.Mainmenu1)
            else:
                tm.showerror("Error","Data unmatch")
            self.entry1.delete(0, 'end')
            self.entry2.delete(0, 'end')
