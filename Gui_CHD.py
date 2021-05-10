from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox
import prog_heart_dia as ph
import Gui_CAD as CAD
import Result_dia as Result

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

class GUI_CHD:

	def __init__(self, risk_factor, res):

		root_CHD = Tk()
		root_CHD.title("Diagnosing CHD")
		root_CHD.geometry("1400x750")
		print("Here")

		CHD_r_1 = StringVar()
		CHD_r_2 = StringVar()
		CHD_r_3 = StringVar()
		CHD_r_4 = StringVar()
		CHD_r_5 = StringVar()
		CHD_r_6 = StringVar()
		CHD_r_7 = StringVar()

		CHD_my_canvas = Canvas(root_CHD)
		CHD_my_canvas.pack(side=LEFT, fill=BOTH,expand=1)

		# Background:

		CHD_img = Image.open("background.png")
		CHD_img = CHD_img.resize((1800,1280), Image.ANTIALIAS)
		CHD_bg = ImageTk.PhotoImage(CHD_img)
		CHD_my_canvas.create_image(0,0, image=CHD_bg, anchor="nw")

		# Creating title text:
		CHD_my_canvas.create_text(650, 40, text="Answer some question", font=("Times", 20), fill="white")

		# quetion 1:
		CHD_my_canvas.create_text(240, 100, text="1) Do you observe blue tiny on skin ?",
							  font=("helvetica", 15), fill="black")

		CHD_but_1 = Radiobutton(CHD_my_canvas, text="yes", variable=CHD_r_1, value="yes",
							fill="white", radius=8)
		CHD_but_1.put(120, 150)

		CHD_but_2 = Radiobutton(CHD_my_canvas, text="no", variable=CHD_r_1, value="no",
							fill="white", radius=8)
		CHD_but_2.put(220, 150)

		# CHD_r_1.set("yes")

		# question 2:
		CHD_my_canvas.create_text(230, 200, text="2) Are breathing fast than usual ?",
							  font=("helvetica", 15), fill="black")

		CHD_but_3 = Radiobutton(CHD_my_canvas, text="yes", variable=CHD_r_2, value="yes",
							fill="white", radius=8)
		CHD_but_3.put(120, 250)

		CHD_but_4 = Radiobutton(CHD_my_canvas, text="no", variable=CHD_r_2, value="no",
							fill="white", radius=8)
		CHD_but_4.put(220, 250)

		# CHD_r_2.set("yes")

		# question 3:
		CHD_my_canvas.create_text(310, 300, text="3) Do you thing your heart beat is rapid than usual ?",
							  font=("helvetica", 15), fill="black")

		CHD_but_5 = Radiobutton(CHD_my_canvas, text="yes", variable=CHD_r_3, value="yes",
							fill="white", radius=8)
		CHD_but_5.put(120, 350)

		CHD_but_6 = Radiobutton(CHD_my_canvas, text="no", variable=CHD_r_3, value="no",
							fill="white", radius=8)
		CHD_but_6.put(220, 350)

		# CHD_r_3.set("yes")

		# question 4:
		CHD_my_canvas.create_text(220, 400, text="4) Do you feel extreme fatigue ?",
							  font=("helvetica", 15), fill="black")

		CHD_but_7 = Radiobutton(CHD_my_canvas, text="yes", variable=CHD_r_4, value="yes",
							fill="white", radius=8)
		CHD_but_7.put(120, 450)

		CHD_but_8 = Radiobutton(CHD_my_canvas, text="no", variable=CHD_r_4, value="no",
							fill="white", radius=8)
		CHD_but_8.put(220, 450)

		# CHD_r_4.set("yes")

		# question 5:
		CHD_my_canvas.create_text(220, 500, text="5) Do you faint during exersise ?",
							  font=("helvetica", 15), fill="black")

		CHD_but_9 = Radiobutton(CHD_my_canvas, text="yes", variable=CHD_r_5, value="yes",
							fill="white", radius=8)
		CHD_but_9.put(120, 550)

		CHD_but_10 = Radiobutton(CHD_my_canvas, text="no", variable=CHD_r_5, value="no",
							 fill="white", radius=8)
		CHD_but_10.put(220, 550)

		# CHD_r_5.set("male")

		# question 6:
		CHD_my_canvas.create_text(240, 600, text="6) Do you thik your breath is short ?",
							  font=("helvetica", 15), fill="black")

		CHD_but_11 = Radiobutton(CHD_my_canvas, text="yes", variable=CHD_r_6, value="yes",
							 fill="white", radius=8)
		CHD_but_11.put(120, 650)

		CHD_but_12 = Radiobutton(CHD_my_canvas, text="no", variable=CHD_r_6, value="no",
							 fill="white", radius=8)
		CHD_but_12.put(220, 650)

		# CHD_r_6.set("yes")

		# question 7:
		CHD_my_canvas.create_text(900, 100, text="7) Do you have swelling in legs, tummy or ankels ?",
							  font=("helvetica", 15), fill="black")

		CHD_but_13 = Radiobutton(CHD_my_canvas, text="yes", variable=CHD_r_7, value="yes",
							 fill="white", radius=8)
		CHD_but_13.put(720, 150)

		CHD_but_14 = Radiobutton(CHD_my_canvas, text="no", variable=CHD_r_7, value="no",
							 fill="white", radius=8)
		CHD_but_14.put(820, 150)

		# CHD_r_7.set("yes")

		# Creating object for prolog
		CHD_obj = ph.Prog()

		def calculate_fatality_risk():
			global fatality_r
			
			CHD_que_1 = CHD_r_1.get()
			CHD_que_2 = CHD_r_2.get()
			CHD_que_3 = CHD_r_3.get()
			CHD_que_4 = CHD_r_4.get()
			CHD_que_5 = CHD_r_5.get()
			CHD_que_6 = CHD_r_6.get()
			CHD_que_7 = CHD_r_7.get()

			print(CHD_que_1)
			print(CHD_que_2)
			print(CHD_que_3)
			print(CHD_que_4)
			print(CHD_que_5)
			print(CHD_que_6)
			print(CHD_que_7)
			
			fatality_r = CHD_obj.diagnose_congenital_heart_disease(CHD_que_1,CHD_que_2, CHD_que_3, CHD_que_4, CHD_que_5, CHD_que_6, CHD_que_7, risk_factor)


			print("Returned value is : " + str(fatality_r))

			print("Your fatality risk is : " + str(fatality_r) + "%")

			message_CHD_res = messagebox.showinfo("Risk factor ", "Your fatality risk is : " + str(fatality_r) + "%")
			if message_CHD_res == 'ok':
				if fatality_r > 0 :
					root_CHD.destroy()
					Result.GUI_result("Congenital Heart Disease", fatality_r, risk_factor, res)
				else:
					root_CHD.destroy()
					CAD.GUI_CAD(risk_factor, res)
					#Result.GUI_result("Unkown", fatality_r, risk_factor)
				print("Back here in GUI_CHD")

			

		but_To_result = ttk.Button(CHD_my_canvas, text="submit", width=18, command=calculate_fatality_risk)
		CHD_my_canvas.create_window(870, 550, window=but_To_result)


		


		root_CHD.mainloop()

#CHD_obj = GUI_CHD(40)
