import tkinter as tk
from tkinter import ttk
import login,Admin,register
from users import *
from tkinter import messagebox
class Mainmenu1(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
        self.begin = tk.Label(self, text="Library System", font=("Verdana", 30), fg="blue")
        self.begin.place(x=450, y=50)

        self.search_image = tk.PhotoImage(file="images/eye.png")
        self.search = tk.Button(self,image=self.search_image, text="Search Book",font=('Verdana',16),compound='left',height=50,width=250,fg='blue')
        self.search.place(x=300, y=150)

        self.renew_image = tk.PhotoImage(file="images/bookshelf.png")
        self.renew_book = tk.Button(self, image=self.renew_image, text="Renew Book", font=('Verdana', 16), compound='left',height=50, width=250,fg='red')
        self.renew_book.place(x=600, y=150)

        self.user_image = tk.PhotoImage(file="images/bookshelf.png")
        self.user = tk.Button(self, image=self.user_image, text="User Accounts", font=('Verdana', 16), compound='left',height=50, width=250,fg='green',command= lambda: self.controller.show_frame(Userdata))
        self.user.place(x=300, y=250)

        self.return_image = tk.PhotoImage(file="images/bookshelf.png")
        self.return_books = tk.Button(self, image=self.return_image, text="Return Book", font=('Verdana', 16),
                                      compound='left', height=50, width=250, fg='grey')
        self.return_books.place(x=600, y=250)

        self.stocks_image = tk.PhotoImage(file="images/bookshelf.png")
        self.stocks = tk.Button(self, image=self.stocks_image, text="Book Stock", font=('Verdana', 16), compound='left',height=50, width=250,fg='purple')
        self.stocks.place(x=300, y=350)

        self.issue_image = tk.PhotoImage(file="images/bookshelf.png")
        self.issue_book = tk.Button(self, image=self.issue_image, text="Issue Book", font=('Verdana', 16),compound='left',height=50, width=250,fg='skyblue')
        self.issue_book.place(x=600, y=350)

        self.logout_image = tk.PhotoImage(file="images/bookshelf.png")
        self.logout = tk.Button(self, image=self.logout_image, text="Logout", font=('Verdana', 16), compound='left',
                                height=50, width=250, command=lambda: self.logout_button(), fg='black')
        self.logout.place(x=300, y=450)

        self.exit_image = tk.PhotoImage(file="images/bookshelf.png")
        self.exit = tk.Button(self, image=self.exit_image, text="Exit account", font=('Verdana', 16),compound='left',height=50, width=250,command= lambda :quit(),fg='black')
        self.exit.place(x=600, y=450)

    def logout_button(self):
        import login
        """try:
            conn = sqlite3.connect('database/login.db')
            s = conn.cursor()
        except:
            messagebox.showerror("Can not connect to Database")
        s.execute('DROP TABLE IF EXISTS TEMP_LoginDB')"""
        self.controller.show_frame(login.Loginpage)


