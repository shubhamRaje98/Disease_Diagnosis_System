from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox
import covidpython1 as ph
import resultcovid as Result

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

'''class Radiobutton:
    def __init__(self, canvas, text="", variable=None, value=0, radius=10,fill="black"):
        
        self.canvas = canvas
        self.variable = variable
        self.fill=fill
        self.text=text
        self.value=value
        self.radius=radius
        self.variable.trace("w", self.redraw)
        self.circle = None

    def put(self, x, y):
        self.x = x
        self.y = y
        self.canvas.create_circle(x, y, self.radius, outline=self.fill)
        self.canvas.create_text(x + 2*self.radius, y, text=self.text,fill=self.fill, anchor="w")
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
                    self.circle = None'''

class GUI_Prog:
    def __init__(self, res):
        root = Tk()
        root.title("Covid Diagnosis")
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
        r_11 = StringVar()
        r_12 = StringVar()
        r_13= StringVar()
        r_14 = StringVar()
        r_15 = StringVar()
        r_16= StringVar()

        # Setting up Canvas:
        my_canvas = Canvas(root)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        img = Image.open("background.png")
        img = img.resize((1500, 1280), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(img)
        my_canvas.create_image(0, 0, image=bg, anchor="nw")

        my_canvas.create_text(640, 15, text="Answer some question",font=("Times", 20), fill="white")


        my_canvas.create_text(175, 50, text="1) Have been travelled in last 30 days?",font=("helvetica", 15), fill="black")
        but_1 = Radiobutton(my_canvas, text="yes", variable=r_1, value="yes",fill="black", radius=8)
        
        but_1.put(90, 85)

        but_2 = Radiobutton(my_canvas, text="no", variable=r_1, value="no",fill="black", radius=8)
        but_2.put(180, 85)

        my_canvas.create_text(215, 130, text="2) Have you been in contact with covid patient?",font=("helvetica", 15), fill="black")
        but_3 = Radiobutton(my_canvas, text="yes", variable=r_2, value="yes",fill="black", radius=8)
        but_3.put(90, 165)

        but_4 = Radiobutton(my_canvas, text="no", variable=r_2, value="no",fill="black", radius=8)
        but_4.put(180, 165)

        my_canvas.create_text(170, 210, text="3) Do you live in contaminated zone?",font=("helvetica", 15), fill="black")
        but_5 = Radiobutton(my_canvas, text="yes", variable=r_3, value="yes",fill="black", radius=8)
        but_5.put(90, 245)

        but_6 = Radiobutton(my_canvas, text="no", variable=r_3, value="no",fill="black", radius=8)
        but_6.put(180, 245)

        my_canvas.create_text(270, 290, text="4) Do you have difficulty in breathing or shortness of breath?",font=("helvetica", 15), fill="black")
        but_7 = Radiobutton(my_canvas, text="yes", variable=r_4, value="yes",fill="black", radius=8)

        but_7.put(90, 325)
        but_8 = Radiobutton(my_canvas, text="no", variable=r_4, value="no",fill="black", radius=8)
        but_8.put(180, 325)
        my_canvas.create_text(185, 370, text="5)Do you have pain or pressure in chest?",font=("helvetica", 15), fill="black")
        but_9 = Radiobutton(my_canvas, text="yes", variable=r_5, value="yes",fill="black", radius=8)
        but_9.put(90, 405)

        but_10 = Radiobutton(my_canvas, text="no", variable=r_5, value="no",fill="black", radius=8)
        but_10.put(180, 405)

        my_canvas.create_text(200, 450, text="6) Have you lost your speech or movement?",font=("helvetica", 15), fill="black")
        but_11 = Radiobutton(my_canvas, text="yes", variable=r_6, value="yes",fill="black", radius=8)
        but_11.put(90, 485)

        but_12 = Radiobutton(my_canvas, text="no", variable=r_6, value="no",fill="black", radius=8)
        but_12.put(180, 485)

        my_canvas.create_text(105, 530, text="7) Do you have fever?",font=("helvetica", 15), fill="black")
        but_13 = Radiobutton(my_canvas, text="yes", variable=r_7, value="yes",fill="black", radius=8)
        but_13.put(90, 565)

        but_14 = Radiobutton(my_canvas, text="no", variable=r_7, value="no",fill="black", radius=8)
        but_14.put(180, 565)

        my_canvas.create_text(125, 610, text="8) Do you have dry cough?",font=("helvetica", 15), fill="black")
        but_15 = Radiobutton(my_canvas, text="yes", variable=r_8, value="yes",fill="black", radius=8)
        but_15.put(90, 645)

        but_16 = Radiobutton(my_canvas, text="no", variable=r_8, value="no",fill="black", radius=8)
        but_16.put(180, 645)

        my_canvas.create_text(830, 50, text="9) Do you feel tiredness ?",font=("helvetica", 15), fill="black")
        but_17 = Radiobutton(my_canvas, text="yes", variable=r_9, value="yes",fill="black", radius=8)
        but_17.put(820, 85)

        but_18 = Radiobutton(my_canvas, text="no", variable=r_9, value="no",fill="black", radius=8)
        but_18.put(920, 85)

        my_canvas.create_text(850, 130, text="10) Do you feel aches or pain?",font=("helvetica", 15), fill="black")
        but_19 = Radiobutton(my_canvas, text="yes", variable=r_10, value="yes",fill="black", radius=8)
        but_19.put(820, 165)

        but_20 = Radiobutton(my_canvas, text="no", variable=r_10, value="no",fill="black", radius=8)
        but_20.put(920, 165)

        my_canvas.create_text(845, 210, text="11) Do you have sore throat?",font=("helvetica", 15), fill="black")
        but_21 = Radiobutton(my_canvas, text="yes", variable=r_11, value="yes",fill="black", radius=8)
        but_21.put(820, 245)
        but_22 = Radiobutton(my_canvas, text="no", variable=r_11, value="no",fill="black", radius=8)
        but_22.put(920, 245)

        my_canvas.create_text(850, 290, text="12) Have you lost your taste?",font=("helvetica", 15), fill="black")
        but_23 = Radiobutton(my_canvas, text="yes", variable=r_12, value="yes",fill="black", radius=8)
        but_23.put(820, 325)
        but_24 = Radiobutton(my_canvas, text="no", variable=r_12, value="no",fill="black", radius=8)
        but_24.put(920, 325)

        my_canvas.create_text(850, 370, text="13) Do you have headache?",font=("helvetica", 15), fill="black")
        but_25 = Radiobutton(my_canvas, text="yes", variable=r_13, value="yes",fill="black", radius=8)
        but_25.put(820, 405)

        but_26 = Radiobutton(my_canvas, text="no", variable=r_13, value="no",fill="black", radius=8)
        but_26.put(920, 405)

        my_canvas.create_text(820, 450, text="14) Do you diarrhea?",font=("helvetica", 15), fill="black")
        but_27 = Radiobutton(my_canvas, text="yes", variable=r_14, value="yes",fill="black", radius=8)
        but_27.put(820, 485)
        but_28 = Radiobutton(my_canvas, text="no", variable=r_14, value="no",fill="black", radius=8)
        but_28.put(920, 485)

        my_canvas.create_text(860, 530, text="15) Do you have conjunctivitis?",font=("helvetica", 15), fill="black")
        but_29 = Radiobutton(my_canvas, text="yes", variable=r_15, value="yes",fill="black", radius=8)
        but_29.put(820, 565)
        but_30 = Radiobutton(my_canvas, text="no", variable=r_15, value="no",fill="black", radius=8)
        but_30.put(920, 565)

        my_canvas.create_text(865, 610, text="16) Do you have rashes on skin?",font=("helvetica", 15), fill="black")
        but_31 = Radiobutton(my_canvas, text="yes", variable=r_16, value="yes",fill="black", radius=8)
        but_31.put(820, 645)
        but_32 = Radiobutton(my_canvas, text="no", variable=r_16, value="no",fill="black", radius=8)
        but_32.put(920, 645)
        arr_obj=ph.prog()
        def calculate_covid_risk():
            global corisk
            arr_que_1 =r_1.get()
            arr_que_2 =r_2.get()
            arr_que_3 =r_3.get()
            arr_que_4 =r_4.get()
            arr_que_5 =r_5.get()
            arr_que_6 =r_6.get()
            arr_que_7 =r_7.get()
            arr_que_8 =r_8.get()
            arr_que_9 =r_9.get()
            arr_que_10 =r_10.get()
            arr_que_11 =r_11.get()
            arr_que_12 =r_12.get()
            arr_que_13 =r_13.get()
            arr_que_14 =r_14.get()
            arr_que_15 =r_15.get()
            arr_que_16 =r_16.get()
            corisk=arr_obj.covid_diagnosis1(arr_que_1,arr_que_2,arr_que_3,arr_que_4,arr_que_5,arr_que_6,arr_que_7,arr_que_8,arr_que_9,arr_que_10,arr_que_11,arr_que_12,arr_que_13,arr_que_14,arr_que_15,arr_que_16)

            
            print("return value",str(corisk))
            message_arr_res = messagebox.showinfo("click","click on ok to continue")
            if message_arr_res == 'ok':
                root.destroy()
                Result.GUI_result("Covid_19",corisk, res)
        but_To_result = ttk.Button(my_canvas, text="submit", width=18, command=calculate_covid_risk)
        my_canvas.create_window(1200, 590, window=but_To_result)

                   
        root.mainloop()

#obj=GUI_Prog()        

            

            

	
                    
	

	
