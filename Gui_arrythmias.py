from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox
import prog_heart_dia as ph
import Result_dia as Result
import Gui_CHD as CHD
#import stackOverflow_Gui as st

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

class GUI_arrythmias:

	def __init__(self, risk_factor, res):
		root_arr = Tk()
		root_arr.title("Diagnosis Arrythmias")
		cent = "1000x660+160+40"
		root_arr.geometry(cent)
		print("In GUI_arrythmias")

		arr_r_1 = StringVar()
		arr_r_2 = StringVar()
		arr_r_3 = StringVar()
		arr_r_4 = StringVar()		

		# Setting up Canvas
		arr_my_canvas = Canvas(root_arr)
		arr_my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

		#Background 
		arr_img = Image.open("background.png")
		arr_img = arr_img.resize((1800, 1280), Image.ANTIALIAS)
		arr_bg = ImageTk.PhotoImage(arr_img)
		arr_my_canvas.create_image(0, 0, image=arr_bg, anchor="nw")

		# Creating title text:
		arr_my_canvas.create_text(520, 40, text="Answer some question",
							  font=("Times", 20), fill="white")

		# quetion 1:
		arr_my_canvas.create_text(200, 100, text="1) Do you have fluttering in chest ?",
							  font=("helvetica", 15), fill="black")

		arr_but_1 = Radiobutton(arr_my_canvas, text="yes", variable=arr_r_1, value="yes",
							fill="white", radius=8)
		arr_but_1.put(90, 150)

		arr_but_2 = Radiobutton(arr_my_canvas, text="no", variable=arr_r_1, value="no",
							fill="white", radius=8)
		arr_but_2.put(180, 150)

		# arr_r_1.set("yes")

		# question 2:
		arr_my_canvas.create_text(180, 200, text="2) Do you have chest pain ?",
							  font=("helvetica", 15), fill="black")

		arr_but_3 = Radiobutton(arr_my_canvas, text="yes", variable=arr_r_2, value="yes",
							fill="white", radius=8)
		arr_but_3.put(90, 250)

		arr_but_4 = Radiobutton(arr_my_canvas, text="no", variable=arr_r_2, value="no",
							fill="white", radius=8)
		arr_but_4.put(180, 250)

		# arr_r_2.set("often")

		# question 3:
		arr_my_canvas.create_text(160, 300, text="3) Do you feel fainting ?",
							  font=("helvetica", 15), fill="black")

		arr_but_5 = Radiobutton(arr_my_canvas, text="yes", variable=arr_r_3, value="yes",
							fill="white", radius=8)
		arr_but_5.put(90, 350)

		arr_but_6 = Radiobutton(arr_my_canvas, text="no", variable=arr_r_3, value="no",
							fill="white", radius=8)
		arr_but_6.put(180, 350)

		# arr_r_3.set("often")

		# question 4:
		arr_my_canvas.create_text(150, 400, text="4) Do you feel dizzy ?",
							  font=("helvetica", 15), fill="black")

		arr_but_7 = Radiobutton(arr_my_canvas, text="yes", variable=arr_r_4, value="yes",
							fill="white", radius=8)
		arr_but_7.put(90, 450)

		arr_but_8 = Radiobutton(arr_my_canvas, text="no", variable=arr_r_4, value="no",
							fill="white", radius=8)
		arr_but_8.put(180, 450)

		# arr_r_4.set("often")

		# Creating arr_object of prog
		arr_obj = ph.Prog()

		def calculate_fatality_risk():

			#Taking response form radio button
			#global risk_factor
			global fatality_r
			
			arr_que_1 = arr_r_1.get()
			arr_que_2 = arr_r_2.get()
			arr_que_3 = arr_r_3.get()
			arr_que_4 = arr_r_4.get()

			print(arr_que_1)
			print(arr_que_2)
			print(arr_que_3)
			print(arr_que_4)
			
			fatality_r = arr_obj.diagnose_Arrythmias(arr_que_1,arr_que_2, arr_que_3, arr_que_4, risk_factor)


			print("Returned value is : " + str(fatality_r))

			print("Your fatality risk is : " + str(fatality_r) + "%")

			message_arr_res = messagebox.showinfo("Risk factor ", "Your fatality risk is : " + str(fatality_r) + "%")
			if message_arr_res == 'ok':
				if fatality_r > 0 :
					root_arr.destroy()
					Result.GUI_result("Arrythmias", fatality_r, risk_factor, res)
				else:
					root_arr.destroy()
					CHD.GUI_CHD(risk_factor, res)
					#Result.GUI_result("Unkown", fatality_r, risk_factor)
				print("Back here in GUI_arrythmias")


		but_To_result = ttk.Button(arr_my_canvas, text="submit", width=18, command=calculate_fatality_risk)
		arr_my_canvas.create_window(770, 550, window=but_To_result)



		root_arr.mainloop()

#arr_obj_1 = GUI_arrythmias(100)
