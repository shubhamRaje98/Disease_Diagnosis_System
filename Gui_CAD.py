from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox
import prog_heart_dia as ph
import Result_dia as Result
import Gui_HeartAttack as HeartAtt

# Taken from: https://stackoverflow.com/a/17985217/11106801
def _create_circle(self, x, y, r, **kwargs):
	return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)


Canvas.create_circle = _create_circle


class Radiobutton:
	def __init__(self, canvas, text="", variable=None, value=0, radius=10,
				 fill="black"):
		self.canvas = canvas
		self.variable = variable
		self.fill = fill
		self.text = text
		self.value = value
		self.radius = radius

		self.variable.trace("w", self.redraw)

		self.circle = None

	def put(self, x, y):
		self.x = x
		self.y = y
		self.canvas.create_circle(x, y, self.radius, outline=self.fill)
		self.canvas.create_text(x + 2*self.radius, y, text=self.text,
								fill=self.fill, anchor="w")
		self.redraw()
		self.canvas.bind("<Button-1>", self.select, add=True)

	def select(self, event):
		if (self.x - event.x)**2 + (self.y - event.y)**2 <= self.radius**2:
			self.variable.set(self.value)
			self.redraw()

	def create_circle(self):
		self.circle = self.canvas.create_circle(self.x, self.y, self.radius-4,
												outline=self.fill,
												fill=self.fill)

	def redraw(self, *args):
		if self.value == self.variable.get():
			if self.circle is None:
				self.create_circle()
		else:
			if self.circle is not None:
				self.canvas.delete(self.circle)
				self.circle = None

class GUI_CAD:
	def __init__(self, risk_factor, res):
		root_CAD = Tk()
		root_CAD.title("Diagnosing CAD")
		cent = "1000x660+160+40"
		root_CAD.geometry(cent)
		print("Here")

		CAD_r_1 = StringVar()
		CAD_r_2 = StringVar()
		CAD_r_3 = StringVar()
		CAD_r_4 = StringVar()
		CAD_r_5 = StringVar()
		CAD_r_6 = StringVar()
		CAD_r_7 = StringVar()

		CAD_my_canvas = Canvas(root_CAD)
		CAD_my_canvas.pack(side=LEFT, fill=BOTH,expand=1)

		# Background:

		CAD_img = Image.open("background.png")
		CAD_img = CAD_img.resize((1800,1280), Image.ANTIALIAS)
		CAD_bg = ImageTk.PhotoImage(CAD_img)
		CAD_my_canvas.create_image(0,0, image=CAD_bg, anchor="nw")

		# Creating title text:
		CAD_my_canvas.create_text(520, 40, text="Answer some question", font=("Times", 20), fill="white")
		
		# quetion 1:
		CAD_my_canvas.create_text(220, 100, text="1) Do you have chest pain/angina ?",
							  font=("helvetica", 15), fill="black")

		CAD_but_1 = Radiobutton(CAD_my_canvas, text="yes", variable=CAD_r_1, value="yes",
							fill="white", radius=8)
		CAD_but_1.put(120, 150)

		CAD_but_2 = Radiobutton(CAD_my_canvas, text="no", variable=CAD_r_1, value="no",
							fill="white", radius=8)
		CAD_but_2.put(220, 150)

		# CAD_r_1.set("yes")

		# question 2:
		CAD_my_canvas.create_text(230, 200, text="2) Do you have pain in legs or arms ?",
							  font=("helvetica", 15), fill="black")

		CAD_but_3 = Radiobutton(CAD_my_canvas, text="yes", variable=CAD_r_2, value="yes",
							fill="white", radius=8)
		CAD_but_3.put(120, 250)

		CAD_but_4 = Radiobutton(CAD_my_canvas, text="no", variable=CAD_r_2, value="no",
							fill="white", radius=8)
		CAD_but_4.put(220, 250)

		# CAD_r_2.set("yes")

		# question 3:
		CAD_my_canvas.create_text(260, 300, text="3) Have you experienced mental confusion ?",
							  font=("helvetica", 15), fill="black")

		CAD_but_5 = Radiobutton(CAD_my_canvas, text="yes", variable=CAD_r_3, value="yes",
							fill="white", radius=8)
		CAD_but_5.put(120, 350)

		CAD_but_6 = Radiobutton(CAD_my_canvas, text="no", variable=CAD_r_3, value="no",
							fill="white", radius=8)
		CAD_but_6.put(220, 350)

		# CAD_r_3.set("yes")

		# question 4:
		CAD_my_canvas.create_text(170, 400, text="4) Do you feel fatigue ?",
							  font=("helvetica", 15), fill="black")

		CAD_but_7 = Radiobutton(CAD_my_canvas, text="yes", variable=CAD_r_4, value="yes",
							fill="white", radius=8)
		CAD_but_7.put(120, 450)

		CAD_but_8 = Radiobutton(CAD_my_canvas, text="no", variable=CAD_r_4, value="no",
							fill="white", radius=8)
		CAD_but_8.put(220, 450)

		# CAD_r_4.set("yes")

		# question 5:
		CAD_my_canvas.create_text(230, 500, text="5) Do you feel shortness of breath ?",
							  font=("helvetica", 15), fill="black")

		CAD_but_9 = Radiobutton(CAD_my_canvas, text="yes", variable=CAD_r_5, value="yes",
							fill="white", radius=8)
		CAD_but_9.put(120, 550)

		CAD_but_10 = Radiobutton(CAD_my_canvas, text="no", variable=CAD_r_5, value="no",
							 fill="white", radius=8)
		CAD_but_10.put(220, 550)

		# CAD_r_5.set("yes")
		CAD_obj = ph.Prog()

		def calculate_fatality_risk():
			global fatality_r
			
			CAD_que_1 = CAD_r_1.get()
			CAD_que_2 = CAD_r_2.get()
			CAD_que_3 = CAD_r_3.get()
			CAD_que_4 = CAD_r_4.get()
			CAD_que_5 = CAD_r_5.get()

			print(CAD_que_1)
			print(CAD_que_2)
			print(CAD_que_3)
			print(CAD_que_4)
			print(CAD_que_5)
			
			fatality_r = CAD_obj.diagnose_coronary_artery_disease(CAD_que_1,CAD_que_2, CAD_que_3, CAD_que_4, CAD_que_5, risk_factor)


			print("Returned value is : " + str(fatality_r))

			print("Your fatality risk is : " + str(fatality_r) + "%")

			message_CAD_res = messagebox.showinfo("Risk factor ", "Your fatality risk is : " + str(fatality_r) + "%")
			if message_CAD_res == 'ok':
				if fatality_r > 0 :
					root_CAD.destroy()
					Result.GUI_result("Coronary Artery Disease", fatality_r, risk_factor, res)
				else:
					root_CAD.destroy()
					HeartAtt.GUI_Heart_Attack(risk_factor, res)
					#Result.GUI_result("Unkown", fatality_r, risk_factor)
				print("Back here in GUI_CHD")

		but_To_result = ttk.Button(CAD_my_canvas, text="submit", width=18, command=calculate_fatality_risk)
		CAD_my_canvas.create_window(770, 580, window=but_To_result)



		root_CAD.mainloop()

#CAD_obj = GUI_CAD(30)
