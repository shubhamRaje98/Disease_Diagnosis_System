import os
from tkinter import *
from PIL import ImageTk, Image


class Start:
    def __init__(self):
        self.root = Tk()
        self.root.title('WELCOME | Disease Diagnosis System')
        self.root.iconbitmap("temp\\signup.ico")

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

        self.my = Image.open("temp\\welcome.jpg")
        self.new = self.my.resize((1300, 700), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(self.new)
        self.can.create_image(0, 0, image=self.bg, anchor='nw')

    def widget(self):
        self.b = Button(self.root, text='Diagnose Now', width=15, bd=1, bg='#f7932f', activebackground='#dbdbdb',
                        font=('Helvetica', 20, 'bold'), cursor='hand2', command=self.run)
        self.b_window = self.can.create_window(140, 450, anchor='nw', window=self.b)

        self.can.create_text(270, 520, text='Want to diagnose?Click!',
                             font=('Helvetica', 18), fill='white')

        self.root.mainloop()

    def run(self):
        self.root.destroy()
        os.system('login.py')


ob = Start()
ob.widget()
