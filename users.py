import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import libpagea
import sqlite3
class Userdata(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
        #tk.Label(self,text="User Accounts").place(x=400,y=50)
        self.conn=sqlite3.connect('database/login.db')
        self.c=self.conn.cursor()
        self.conn.commit()
        self.b1=ttk.Button(self,text="Click me for details",command= lambda : self.readdata())
        self.b1.place(x=500,y=100)

    def readdata(self):
        self.b1.destroy()
        self.firstname = tk.Label(self, text="Firstname", bd=3)
        self.firstname.grid(row=0, column=0)
        self.lastname = tk.Label(self, text="Lastname", bd=3)
        self.lastname.grid(row=0, column=1)
        self.username = tk.Label(self, text="Username", bd=3)
        self.username.grid(row=0, column=2)
        self.password = tk.Label(self, text="Password", bd=3)
        self.password.grid(row=0, column=3)
        self.email = tk.Label(self, text="Email", bd=3)
        self.email.grid(row=0, column=4)
        self.enrollment = tk.Label(self, text="Enrollment_no", bd=3)
        self.enrollment.grid(row=0, column=5)
        self.contact = tk.Label(self, text="Contact_no", bd=3)
        self.contact.grid(row=0, column=6)
        self.library = tk.Label(self, text="Library_ID", bd=3)
        self.library.grid(row=0, column=7)
        self.c.execute("SELECT * FROM signup_table")
        for i, dat in enumerate(self.c.fetchall()):
            tk.Label(self, text=dat[0],bd=3).grid(row=i + 1, column=0)
            tk.Label(self, text=dat[1],bd=3).grid(row=i + 1, column=1)
            tk.Label(self, text=dat[2],bd=3).grid(row=i + 1, column=2)
            tk.Label(self, text=dat[3],bd=3).grid(row=i + 1, column=3)
            tk.Label(self, text=dat[4],bd=3).grid(row=i + 1, column=4)
            tk.Label(self, text=dat[5],bd=3).grid(row=i + 1, column=5)
            tk.Label(self, text=dat[6],bd=3).grid(row=i + 1, column=6)
            tk.Label(self, text=dat[7],bd=3).grid(row=i + 1, column=7)
        import libpagea
        self.back=ttk.Button(self,text="Back",command= lambda: self.controller.show_frame(libpagea.Mainmenu1))
        self.back.place(x=500,y=400)