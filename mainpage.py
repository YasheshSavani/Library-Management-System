import tkinter as tk
from tkinter import ttk
from login import *
import register as reg
from start import *
from Admin import *
from libpage import *
from libpagea import *
from users import *
VERSION = "BETA-1.0"

#LARGE_FONT= font=("Verdana",16)

class mainpage(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        #Tk.iconbitmap(self,default=".ico")
        tk.Tk.wm_title(self,"Library system")
        self.title("Library System")
        self.geometry("1200x600+50+50")
        self.iconbitmap(self, default="images\library.ico")
        #logo=tk.PhotoImage(file='images/logo.ico')
        #w1=tk.Label(self,image=logo).pack(side="center")
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        menubar= tk.Menu(container)
        filemenu = tk.Menu(menubar,tearoff=0)
        filemenu.add_command(label="Save Settings",command= lambda: tm.showinfo("Command ","Not Working!!!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda: quit())
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = tk.Menu(menubar,tearoff=0)
        editmenu.add_command(label="Copy", command=lambda: tm.showinfo("Command ", "Not Working!!!"))
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=lambda: tm.showinfo("Command ", "Not Working!!!"))
        editmenu.add_separator()
        editmenu.add_command(label="Paste", command=lambda: tm.showinfo("Command ", "Not Working!!!"))
        editmenu.add_separator()
        menubar.add_cascade(label="Edit", menu=editmenu)


        # STATUSBAR
        """status1 = tk.Frame(self, bd=1, relief='sunken')
        status1.pack(side='bottom', fill=x)
        statusu = tk.Label(status1, text="User name")
        statusu.pack(side='left', fill=y)
        w = ttk.Separator(status1, orient=VERTICAL)
        w.pack(side='left', fill=y)
        status1u1 = tk.Label(status1, text="NONE", fg="blue")
        status1u1.pack(side='left')
        w = ttk.Separator(status1, orient=VERTICAL)
        w.pack(side='left', fill=y, padx=20)
        w = ttk.Separator(status1, orient=VERTICAL)
        w.pack(side='left', fill=y)
        statusv = tk.Label(status1, text="Version")
        statusv.pack(side='left')
        w = ttk.Separator(status1, orient=VERTICAL)
        w.pack(side='left', fill=y)
        statusv1 = tk.Label(status1, text=VERSION, fg="blue")
        statusv1.pack(side='left')
        w = ttk.Separator(status1, orient=VERTICAL)
        w.pack(side='left', fill=y)
        w = ttk.Separator(status1, orient=VERTICAL)
        w.pack(side='left', fill=y, padx=50)
        statusc = tk.Label(status1, text="Copyright©2017 Library System,Inc.")
        statusc.pack(side='left')"""

        tk.Tk.config(self,menu=menubar)
        self.frames= {}
        for F in (Startpage, Loginpage,Registerpage,Adminpage,Mainmenu,Mainmenu1,Userdata):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Startpage)
    def show_frame(self, cont):
        frame=self.frames[cont]
        frame.tkraise()

root= mainpage()
root.mainloop()
