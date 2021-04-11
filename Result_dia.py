from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox

class GUI_result:

	def __init__(self, disease_name="", fatality_risk=0, risk_fac=0):
		Result_root = Tk()
		Result_root.title("Diagnosis Result")
		Result_root.geometry("1200x750")

		#Setting up canvas:
		Result_my_canvas = Canvas(Result_root)
		Result_my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

		#Background:
		Result_img = Image.open("background.png")
		Result_img = Result_img.resize((1500, 1280), Image.ANTIALIAS)
		Result_bg = ImageTk.PhotoImage(Result_img)
		Result_my_canvas.create_image(0, 0, image=Result_bg, anchor="nw")

		# Creating title text:
		Result_my_canvas.create_text(650, 40, text="Diasgnosis result : ", font=("Times", 20), fill="white")
		

		# line 1:
		Result_my_canvas.create_text(140, 100, text="Diagnosed disease : " , font=("helvetica", 15), fill="black")
		Result_my_canvas.create_text(350, 100, text=disease_name , font=("helvetica", 15), fill="black")

		# line 2:
		Result_my_canvas.create_text(110, 200, text="Risk factor : ", font=("helvetica", 15), fill="black")
		Result_my_canvas.create_text(240, 200, text=str(risk_fac) , font=("helvetica", 15), fill="black")

		# line 3:
		Result_my_canvas.create_text(120, 300, text="Risk of fatality : ", font=("helvetica", 15), fill="black")
		Result_my_canvas.create_text(240, 300, text=str(fatality_risk) , font=("helvetica", 15), fill="black")



		Result_root.mainloop()

#Result_obj = GUI_result()