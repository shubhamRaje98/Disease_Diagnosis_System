from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox
import prog_heart_dia as ph
import Gui_arrythmias as Gui_arr

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


class GUI_Prog:
	def __init__(self, res):
		root = Tk()
		root.title("Risk Analysis")
		root.geometry("1200x750")
		r_1 = StringVar()
		r_2 = StringVar()
		r_3 = StringVar()
		r_4 = StringVar()
		r_5 = StringVar()
		r_6 = StringVar()
		r_7 = StringVar()
		r_8 = StringVar()
		r_9 = StringVar()
		r_10 = StringVar()


		# Setting up Canvas:
		my_canvas = Canvas(root)
		my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

		# Background:
		img = Image.open("background.png")
		img = img.resize((1500, 1280), Image.ANTIALIAS)
		bg = ImageTk.PhotoImage(img)
		my_canvas.create_image(0, 0, image=bg, anchor="nw")


		# Creating title text:
		my_canvas.create_text(650, 40, text="Answer some question",
							  font=("Times", 20), fill="white")

		# quetion 1:
		my_canvas.create_text(140, 100, text="1) Do you smoke?",
							  font=("helvetica", 15), fill="black")

		but_1 = Radiobutton(my_canvas, text="yes", variable=r_1, value="yes",
							fill="white", radius=8)
		but_1.put(90, 150)

		but_2 = Radiobutton(my_canvas, text="no", variable=r_1, value="no",
							fill="white", radius=8)
		but_2.put(180, 150)

		# r_1.set("yes")

		# question 2:
		my_canvas.create_text(260, 200, text="2) How often you have junk/unhealthy food ?",
							  font=("helvetica", 15), fill="black")

		but_3 = Radiobutton(my_canvas, text="often", variable=r_2, value="often",
							fill="white", radius=8)
		but_3.put(90, 250)

		but_4 = Radiobutton(my_canvas, text="rarely", variable=r_2, value="rarely",
							fill="white", radius=8)
		but_4.put(180, 250)

		# r_2.set("often")

		# question 3:
		my_canvas.create_text(260, 300, text="3) How often you do some physical activity ?",
							  font=("helvetica", 15), fill="black")

		but_5 = Radiobutton(my_canvas, text="often", variable=r_3, value="often",
							fill="white", radius=8)
		but_5.put(90, 350)

		but_6 = Radiobutton(my_canvas, text="rarely", variable=r_3, value="rarely",
							fill="white", radius=8)
		but_6.put(180, 350)

		# r_3.set("often")

		# question 4:
		my_canvas.create_text(250, 400, text="4) How often you feel stressed in daily life ?",
							  font=("helvetica", 15), fill="black")

		but_7 = Radiobutton(my_canvas, text="often", variable=r_4, value="often",
							fill="white", radius=8)
		but_7.put(90, 450)

		but_8 = Radiobutton(my_canvas, text="rarely", variable=r_4, value="rarely",
							fill="white", radius=8)
		but_8.put(180, 450)

		# r_4.set("often")

		# question 5:
		my_canvas.create_text(170, 500, text="5) What is your gender ?",
							  font=("helvetica", 15), fill="black")

		but_9 = Radiobutton(my_canvas, text="male", variable=r_5, value="male",
							fill="white", radius=8)
		but_9.put(90, 550)

		but_10 = Radiobutton(my_canvas, text="female", variable=r_5, value="female",
							 fill="white", radius=8)
		but_10.put(180, 550)

		# r_5.set("male")

		# question 6:
		my_canvas.create_text(280, 600, text="6) Do you have genetic history of heart disease ?",
							  font=("helvetica", 15), fill="black")

		but_11 = Radiobutton(my_canvas, text="yes", variable=r_6, value="yes",
							 fill="white", radius=8)
		but_11.put(90, 650)

		but_12 = Radiobutton(my_canvas, text="no", variable=r_6, value="no",
							 fill="white", radius=8)
		but_12.put(180, 650)

		# r_6.set("yes")

		# question 7:
		my_canvas.create_text(900, 100, text="7) Do you have diabetes ?",
							  font=("helvetica", 15), fill="black")

		but_13 = Radiobutton(my_canvas, text="yes", variable=r_7, value="yes",
							 fill="white", radius=8)
		but_13.put(820, 150)

		but_14 = Radiobutton(my_canvas, text="no", variable=r_7, value="no",
							 fill="white", radius=8)
		but_14.put(920, 150)

		# r_7.set("yes")

		# question 8:
		my_canvas.create_text(960, 200, text="8) What is your total cholesterol count ?",
							  font=("helvetica", 15), fill="black")

		but_15 = Radiobutton(my_canvas, text=">200", variable=r_8, value=">200",
							 fill="white", radius=8)
		but_15.put(820, 250)

		but_16 = Radiobutton(my_canvas, text="<200", variable=r_8, value="<200",
							 fill="white", radius=8)
		but_16.put(920, 250)

		# r_8.set(">200")

		# question 9:
		my_canvas.create_text(950, 300, text="9) Have you had heart attack before ?",
							  font=("helvetica", 15), fill="black")

		but_17 = Radiobutton(my_canvas, text="yes", variable=r_9, value="yes",
							 fill="white", radius=8)
		but_17.put(820, 350)

		but_18 = Radiobutton(my_canvas, text="no", variable=r_9, value="no",
							 fill="white", radius=8)
		but_18.put(920, 350)

		# r_9.set("yes")

		# question 10:
		my_canvas.create_text(910, 400, text="10) What is your BMI index ?",
							  font=("helvetica", 15), fill="black")

		but_19 = Radiobutton(my_canvas, text=">40", variable=r_10, value=">40",
							 fill="white", radius=8)
		but_19.put(820, 450)

		but_20 = Radiobutton(my_canvas, text="<40", variable=r_10, value="<40",
							 fill="white", radius=8)
		but_20.put(920, 450)

		# r_10.set(">40")

		# creating object of prog
		obj = ph.Prog()

		def calculate_risk():

			#Taking response form radio button
			global risk_factor
			
			que_1 = r_1.get()
			que_2 = r_2.get()
			que_3 = r_3.get()
			que_4 = r_4.get()
			que_5 = r_5.get()
			que_6 = r_6.get()
			que_7 = r_7.get()
			que_8 = r_8.get()
			que_9 = r_9.get()
			que_10 = r_10.get()

			print(que_1)
			print(que_2)
			print(que_3)
			print(que_4)
			print(que_5)
			print(que_6)
			print(que_7)
			print(que_8)
			print(que_9)
			print(que_10)

			tup = obj.calculate_risk_factor(que_1,que_2, que_3, que_4, que_5, que_6, que_7, que_8, que_9, que_10)

			risk = tup[0]
			total_no_questions = tup[1]

			print("Returned value is : " + str(risk))

			risk_factor = risk*(100/total_no_questions)
			print("Your risk of having heart related issue is : " + str(risk_factor) + "%")

			messagboxRes = messagebox.showinfo("Risk factor ", "Your risk of having heart related issue is : " + str(risk_factor) + "%")
			if messagboxRes == 'ok':
				root.destroy()
				print(risk_factor)
				Gui_arr.GUI_arrythmias(risk_factor, res)
				print("Back Here")

		# creating submit button
	   
		but = ttk.Button(my_canvas, text="submit", width=18, command=calculate_risk)
		my_canvas.create_window(870, 550, window=but)

			   
		root.mainloop()


#obj = GUI_Prog()
