import os
import sys
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import MySQLdb


class Db:
    def __init__(self, tup, uname):
        flag = 2
        c = MySQLdb.connect('localhost', 'root', 'Pass@123', 'dds')
        s = c.cursor()
        print('Connected To The Server....')
        s.execute("select * from login ")
        rows = s.fetchall()
        print('Total number of rows = ', s.rowcount)
        print(rows)
        if rows == ():
            flag = 1;
        else:
            for a in rows:
                if a[0] != uname:
                    flag = 1
                else:
                    flag = 0
        if flag == 1:
            s.execute("insert into login values (%s, %s)", tup)
            print('Records Inserted Successfully....')
            messagebox.showinfo("Welcome", "Registered! You will be redirected to the login page")
            c.commit()
            s.close()
            c.close()
            print('Disconnected From Server....')
            self.root.destroy()
            os.system('login.py')
        if flag == 0:
            messagebox.showerror("Alert!", "Username is not available")


class User(Db):
    def __init__(self):
        self.root = Tk()
        self.root.title('WELCOME | Creating User')
        self.root.iconbitmap("temp\\add-user.ico")

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

        self.my1 = Image.open("temp\\user1.jpg")
        self.new1 = self.my1.resize((1200, 700), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(self.new1)

        self.my2 = Image.open("temp\\user2.png")
        self.new2 = self.my2.resize((1060, 560), Image.ANTIALIAS)
        self.bg2 = ImageTk.PhotoImage(self.new2)

        self.my3 = Image.open("temp\\user3.png")
        self.new3 = self.my3.resize((550, 520), Image.ANTIALIAS)
        self.bg3 = ImageTk.PhotoImage(self.new3)

        self.my4 = Image.open("temp\\user4.png")
        self.new4 = self.my4.resize((470, 520), Image.ANTIALIAS)
        self.bg4 = ImageTk.PhotoImage(self.new4)

        self.my5 = Image.open("temp\\user2.png")
        self.new5 = self.my5.resize((720, 460), Image.ANTIALIAS)
        self.bg5 = ImageTk.PhotoImage(self.new5)

        self.my6 = Image.open("temp\\add-user.png")
        self.new6 = self.my6.resize((200, 200), Image.ANTIALIAS)
        self.bg6 = ImageTk.PhotoImage(self.new6)

        self.can.create_image(0, 0, image=self.bg1, anchor='nw')
        self.can.create_image(70, 70, image=self.bg2, anchor='nw')
        self.can.create_image(90, 90, image=self.bg3, anchor='nw')
        self.can.create_image(640, 90, image=self.bg4, anchor='nw')
        self.can.create_image(360, 120, image=self.bg5, anchor='nw')
        self.can.create_image(130, 215, image=self.bg6, anchor='nw')

        app_width = 1200
        app_height = 700
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.x = (screen_width / 2) - (app_width / 2)
        self.y = (screen_height / 2) - (app_height / 2)
        self.cent = f'{app_width}x{app_height}+{int(self.x)}+{int(self.y)}'
        self.root.geometry(self.cent)

    def widget(self):
        self.can.create_text(525, 190, text='Create Username', font=('Helvetica', 25, 'bold'))

        self.can.create_text(525, 303, text='Create Password', font=('Helvetica', 25, 'bold'))

        self.can.create_text(525, 416, text='Re-enter Password', font=('Helvetica', 25, 'bold'))

        self.can.create_text(225, 430, text='Create User', font=('Helvetica', 30, 'bold'))

        self.e1 = Entry(self.root, font=('Helvetica', 25, ), bg='#dbdbdb', width=20, bd=0.5, highlightthickness=0)
        self.e2 = Entry(self.root, font=('Helvetica', 25), show='•', bg='#dbdbdb', width=20, bd=0.5,
                        highlightthickness=0)
        self.e3 = Entry(self.root, font=('Helvetica', 25), show='•', bg='#dbdbdb', width=20, bd=0.5,
                        highlightthickness=0)

        self.e1_window = self.can.create_window(700, 170, anchor='nw', window=self.e1)
        self.e2_window = self.can.create_window(700, 282, anchor='nw', window=self.e2)
        self.e3_window = self.can.create_window(700, 395, anchor='nw', window=self.e3)

        self.b = Button(self.root, text='Proceed', width=10, bd=1, bg='#f57114', font=('Helvetica', 20, 'bold'),
                        activebackground='#dbdbdb', cursor='hand2', command=self.inputs)
        self.b_window = self.can.create_window(630, 500, anchor='nw', window=self.b)

        self.root.mainloop()

    def inputs(self):
        if self.e1.get() == "" or self.e2.get() == "" or self.e3.get() == "":
            messagebox.showerror("Alert!", "All fields are required")
        elif self.e2.get() != self.e3.get():
            messagebox.showerror("Alert!", "The password you entered do not match")
        else:
            data = (self.e1.get(), self.e3.get())
            uname = self.e1.get()
        super().__init__(data, uname)


ob = User()
ob.widget()
