import tkinter as tk
from login import *
from tkinter import ttk
class Startpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.begin= tk.Label(self,text= "Library System",font=("Verdana",30),fg="blue")
        self.begin.place(x=450,y=50)
        self.loginbutton = tk.Button(self,command= lambda: controller.show_frame(Loginpage),border=0)
        self.login_image=tk.PhotoImage(file="images/begin2.png")
        self.loginbutton.config(image=self.login_image,)
        self.loginbutton.place(x=500,y=150)
        self.label=tk.Label(self,text="Let's begin",font=("Verdana",14)).place(x=550,y=370)


