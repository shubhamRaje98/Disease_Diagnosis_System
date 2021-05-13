from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as tkFont
import covidpython1Gui as cov
import Risk_analysis as stk
#from python_tkinter4create_calculator import abc

class Diagnosis:
	def __init__(self, res):
		root = Tk()
		root.title('Digital Doctor')
		#root.iconbitmap('images/d3.ico')
		root.geometry('1300x700')

		app_width = 1300
		app_height = 700
		screen_width = root.winfo_screenwidth()
		screen_height = root.winfo_screenheight()
		x = (screen_width / 2) - (app_width / 2)
		y = (screen_height / 2) - (app_height / 2)
		root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

		# root.wm_attributes('-transparentcolor', root['bg'])

		bg = PhotoImage(file="background.png")

		my_label = Label(root,image=bg)
		my_label.place(x=0,y=0,relwidth=1,relheight=1)

		fontStyle = tkFont.Font(family="helvetica",size=44)
		fontStyle2 = tkFont.Font(family="helvetica",size=20)
			
		label2 = Label(root,text = 'WELCOME TO DIAGNOSIS',padx=160,pady=20,fg='white',bg='#de3b4e',font = fontStyle)
		label2.grid(row=0,columnspan=2,pady=50)

		image=Image.open("covid.jpg")
		image = image.resize((700,300),Image.ANTIALIAS)
		my_img1 = ImageTk.PhotoImage(image)

		label1 = Label(root,image=my_img1,bg='#003355')
		label1.grid(row=1,column=0)

		image=Image.open("heart.jpg")
		image = image.resize((700,300),Image.ANTIALIAS)
		my_img2 = ImageTk.PhotoImage(image)


		label2 = Label(root,image=my_img2,bg='#003355')
		label2.grid(row=1,column=1)

		# Methods 

		def open_covid():
			root.destroy()
			cov.GUI_Prog(res)

		def open_heart():
			root.destroy()
			stk.GUI_Prog(res)

		#button 1
		myButton1 = Button(root,text='COVID DIAGNOSIS',fg='#f29e43',bg='white',padx=170,font = fontStyle2, command=open_covid)
		myButton1.grid(row=2,column=0,pady=20)

		#button 2
		myButton2 = Button(root,text='HEART DIAGNOSIS',fg='#f29e43',bg='white',padx=170,font = fontStyle2, command=open_heart)
		myButton2.grid(row=2,column=1,pady=20)


		root.mainloop()