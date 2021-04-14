import os
import sys
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import MySQLdb


class User:
    def __init__(self, data1, data2):
        flag = 2
        c = MySQLdb.connect('localhost', 'root', 'Pass@123', 'dds') 
        s = c.cursor()
        print('Connected To The Server....')
        print('Validating inputs....')
        s.execute("select * from login")
        rows = s.fetchall()
        print('Total number of rows = ', s.rowcount)
        for a in rows:
            if a[0] == data1 and a[1] == data2:
                flag = 1
                break
            else:
                flag = 0
        if flag == 1:
            messagebox.showinfo("Welcome", "Successful Login")
            print(data1, data2)
            c.commit()
            s.close()
            c.close()
            print('Disconnected From Server....')
            self.root.destroy()
            os.system('next.py') #next file that should be opened when login successfully
        if flag == 0:
            messagebox.showerror("Alert!", "Incorrect Login Credentials")


class Login(User):
    def __init__(self):
        self.root = Tk()
        self.root.title('WELCOME | Log In')
        self.root.iconbitmap("temp\\user.ico")

        app_width = 1200
        app_height = 700
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.x = (screen_width / 2) - (app_width / 2)
        self.y = (screen_height / 2) - (app_height / 2)
        self.cent = f'{app_width}x{app_height}+{int(self.x)}+{int(self.y)}'
        self.root.geometry(self.cent)

        self.f = Frame(self.root)
        self.f.pack(side=TOP, fill=BOTH)
        self.can = Canvas(self.f, height=700, width=1200, bd=0, highlightthickness=0)
        self.can.pack(fill='both', expand=True)

        self.my1 = Image.open("temp\\login1.png")
        self.new1 = self.my1.resize((1200, 700), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(self.new1)

        self.my2 = Image.open("temp\\login2.png")
        self.new2 = self.my2.resize((1060, 560), Image.ANTIALIAS)
        self.bg2 = ImageTk.PhotoImage(self.new2)

        self.my3 = Image.open("temp\\login3.png")
        self.new3 = self.my3.resize((550, 520), Image.ANTIALIAS)
        self.bg3 = ImageTk.PhotoImage(self.new3)

        self.my4 = Image.open("temp\\login4.png")
        self.new4 = self.my4.resize((470, 520), Image.ANTIALIAS)
        self.bg4 = ImageTk.PhotoImage(self.new4)

        self.my5 = Image.open("temp\\login2.png")
        self.new5 = self.my5.resize((720, 460), Image.ANTIALIAS)
        self.bg5 = ImageTk.PhotoImage(self.new5)

        self.my6 = Image.open("temp\\user.png")
        self.new6 = self.my6.resize((200, 200), Image.ANTIALIAS)
        self.bg6 = ImageTk.PhotoImage(self.new6)

        self.can.create_image(0, 0, image=self.bg1, anchor='nw')
        self.can.create_image(70, 70, image=self.bg2, anchor='nw')
        self.can.create_image(90, 90, image=self.bg3, anchor='nw')
        self.can.create_image(640, 90, image=self.bg4, anchor='nw')
        self.can.create_image(360, 120, image=self.bg5, anchor='nw')
        self.can.create_image(125, 220, image=self.bg6, anchor='nw')

    def widget(self):
        self.can.create_text(525, 190, text='Username', font=('Helvetica', 30, 'bold'))

        self.can.create_text(525, 299, text='Password', font=('Helvetica', 30, 'bold'))

        self.can.create_text(720, 480, text="Don't have an account? Sign Up!", font=('Arial', 18, 'bold'))
        self.can.create_text(225, 450, text='Log In', font=('Helvetica', 35, 'bold'))

        self.e1 = Entry(self.root, font=('Helvetica', 25), bg='#dbdbdb', width=20, bd=0.5, highlightthickness=0)
        self.e2 = Entry(self.root, font=('Helvetica', 25), show='•', bg='#dbdbdb', width=20, bd=0.5, highlightthickness=0)

        self.e1_window = self.can.create_window(700, 170, anchor='nw', window=self.e1)
        self.e2_window = self.can.create_window(700, 278, anchor='nw', window=self.e2)

        self.b1 = Button(self.root, text='Log In', width=10, bd=1, bg='#5bc3f0', font=('Helvetica', 20, 'bold'),
                         activebackground='#dbdbdb', cursor='hand2', command=self.inputs)
        self.b1_window = self.can.create_window(630, 370, anchor='nw', window=self.b1)

        self.b2 = Button(self.root, text='Sign Up', width=10, bd=1, bg='#5bc3f0', font=('Helvetica', 20, 'bold'),
                         activebackground='#dbdbdb', cursor='hand2', command=self.signup)
        self.b2_window = self.can.create_window(630, 510, anchor='nw', window=self.b2)

        self.root.mainloop()

    def signup(self):
        self.root.destroy()
        os.system('signup.py')

    def inputs(self):
        if self.e1.get() == "" and self.e2.get() == "":
            messagebox.showerror("Alert!", "All fields are required")
        elif self.e1.get() == "":
            messagebox.showerror("Alert!", "Enter Username First")
        elif self.e2.get() == "":
            messagebox.showerror("Alert!", "Enter Password First")
        else:
            data1 = self.e1.get()
            data2 = self.e2.get()
            print(data1, data2)
        super().__init__(data1, data2)


ob = Login()
ob.widget()
