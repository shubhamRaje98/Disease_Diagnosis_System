from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox
import smtplib

class GUI_result:

	def __init__(self, disease_name="", fatality_risk=0, risk_fac=0, res=""):
		Result_root = Tk()
		Result_root.title("Diagnosis Result")
		cent = "800x660+300+40"
		Result_root.geometry(cent)

		#Setting up canvas:
		Result_my_canvas = Canvas(Result_root)
		Result_my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

		#Background:
		Result_img = Image.open("background.png")
		Result_img = Result_img.resize((1500, 1280), Image.ANTIALIAS)
		Result_bg = ImageTk.PhotoImage(Result_img)
		Result_my_canvas.create_image(0, 0, image=Result_bg, anchor="nw")

		# Creating title text:
		Result_my_canvas.create_text(410, 40, text="Diasgnosis result : ", font=("Times", 20), fill="white")
		

		# line 1:
		Result_my_canvas.create_text(140, 100, text="Diagnosed disease : " , font=("helvetica", 15), fill="black")
		Result_my_canvas.create_text(350, 100, text=disease_name , font=("helvetica", 15), fill="black")

		# line 2:
		Result_my_canvas.create_text(110, 200, text="Risk factor : ", font=("helvetica", 15), fill="black")
		Result_my_canvas.create_text(240, 200, text=str(risk_fac) + "%", font=("helvetica", 15), fill="black")

		# line 3:
		Result_my_canvas.create_text(120, 300, text="Risk of fatality : ", font=("helvetica", 15), fill="black")
		Result_my_canvas.create_text(240, 300, text=str(fatality_risk) + "%", font=("helvetica", 15), fill="black")

		server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
		server.login("diseasediagnosissystem@gmail.com", "*Shubh@m9820632974")
		mailContent = f'\nHello sir, your dianosis result is : \n\n Diagnosed Disease : {disease_name} \n Risk Factor : {risk_fac}% \n fatality_risk : {fatality_risk}% \n\n We advice you to consult a doctor' # Here add \n in start of string to make it work
		print(mailContent)
		print(res)
		server.sendmail("diseasediagnosissystem@gmail.com", res, mailContent)

		server.quit()

		Result_root.mainloop()

#Result_obj = GUI_result()
