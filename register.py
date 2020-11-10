#from mainpage import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as tm
import sqlite3
import smtplib

class Registerpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        self.user= tk.StringVar()
        self.fname=tk.StringVar()
        self.lname=tk.StringVar()
        self.pwd= tk.StringVar()
        self.email= tk.StringVar()
        #self.dob= tk.StringVar()
        self.cpwd=tk.StringVar()
        self.enroll=tk.IntVar()
        self.mob=tk.IntVar()
        self.lid=tk.StringVar()
        self.firstname= tk.Label(self, text="Firstname :").place(x=400,y=50)
        self.firstname_entry=tk.Entry(self, textvariable=self.fname,width=25)
        self.firstname_entry.place(x=470,y=50)
        self.lastname = tk.Label(self, text="Lastname :").place(x=650, y=50)
        self.lastname_entry = tk.Entry(self, textvariable=self.lname,width=25)
        self.lastname_entry.place(x=720, y=50)
        self.username = tk.Label(self, text="Username :").place(x=400, y=100)
        self.username_entry= tk.Entry(self, textvariable=self.user,width=67)
        self.username_entry.place(x=470, y=100)
        #self.libid = tk.Label(self, text="Library_ID :").place(x=650, y=100)
        #self.libid_entry= tk.Entry(self, textvariable=self.lid,width=25)
        #self.libid_entry.place(x=720, y=100)
        self.password = tk.Label(self, text="Password :").place(x=400, y=150)
        self.password_entry = tk.Entry(self, textvariable=self.pwd,width=25,show="*")
        self.password_entry.place(x=470, y=150)
        self.cpassword = tk.Label(self, text="Confirm\n Password :").place(x=650, y=140)
        self.cpassword_entry = tk.Entry(self, textvariable=self.cpwd,width=25,show="*")
        self.cpassword_entry.place(x=720, y=150)
        self.emailid = tk.Label(self, text="Email :").place(x=400, y=200)
        self.emailid_entry = tk.Entry(self, textvariable=self.email,width=67)
        self.emailid_entry.place(x=470, y=200)
        self.enrno = tk.Label(self, text="Enrollment\n number :").place(x=400, y=240)
        self.enrno_entry = tk.Entry(self, textvariable=self.enroll,width=25)
        self.enrno_entry.place(x=470, y=250)
        self.mobile = tk.Label(self, text="Contact no :").place(x=650, y=250)
        self.mobile_entry = tk.Entry(self, textvariable=self.mob, width=25)
        self.mobile_entry.place(x=720, y=250)
        #date = tk.Label(self, text="Date of Birth :").place(x=650, y=300)
        #date_entry = tk.Entry(self, textvariable=user, width=25)
        #self.date_entry.place(x=720, y=300)
        self.registerbutton = ttk.Button(self, text="Submit", command= lambda: self.check_detail())
        self.registerbutton.place(x=450, y=350)
        #.send_email()
        import login
        self.back = ttk.Button(self, text="Back", command=lambda: self.controller.show_frame(login.Loginpage))
        self.back.place(x=550, y=350)

    def send_email(self):
        self.host=""
        self.port= 0
        self.username1 = ""
        self.password1 = ""
        self.server=smtplib.SMTP(self.host,self.port)
        self.server.starttls()
        self.server.login(self.username1,self.password1)


    def check_detail(self):
        f1= self.firstname_entry.get()
        l1=self.lastname_entry.get()
        usr = self.username_entry.get()
        pass1 = self.password_entry.get()
        pass2 = self.cpassword_entry.get()
        email1 = self.emailid_entry.get()
        enr = self.enrno_entry.get()
        con = self.mobile_entry.get()
        #libd=self.libid_entry.get()
        if (f1 != '' and l1 != '' and usr != '' and pass1 != '' and pass2 != '' and email1 != '' and con != '' and enr != ''):
            if (pass1 != pass2):
                tm.showerror("Error", "Wrong passwords")
            else:
                conn = sqlite3.connect('database/login.db')
                s = conn.cursor()
                s.execute('CREATE TABLE IF NOT EXISTS signup_table (firstname TEXT, lastname TEXT,username TEXT,password TEXT,email TEXT, enrollment_no INTEGER,contact_no INTEGER,library_id INTEGER PRIMARY KEY AUTOINCREMENT)')
                d = s.execute(
                    'SELECT username FROM signup_table WHERE username="%s"' % (usr))
                conn.commit()
                #print (d)
                if d.fetchone():
                    tm.showerror("error", "User already Exist")
                else:
                    s.execute(
                        'INSERT INTO signup_table (firstname,lastname,username,password,email,enrollment_no,contact_no) VALUES (?,?,?,?,?,?,?) ',
                        (f1, l1, usr, pass1, email1, enr, con))
                    conn.\
                        commit()

                    """sendmail=self.username1
                    tomail=[email1]
                    self.server.sendmail(sendmail,tomail,"you Are now Part oF DEDSec Limited")"""
                    tm.showinfo("Done", "Submitted")

                    import login
                    self.controller.show_frame(login.Loginpage)
        else:
            tm.showerror("Error", "Fill all details")
        self.firstname_entry.delete(0,'end')
        self.lastname_entry.delete(0,'end')
        self.username_entry.delete(0,'end')
        self.password_entry.delete(0,'end')
        self.cpassword_entry.delete(0,'end')
        self.emailid_entry.delete(0,'end')
        self.enrno_entry.delete(0,'end')
        self.mobile_entry.delete(0,'end')




