import tkinter as tk
from tkinter import ttk

class Productdata(tk.Frame):
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