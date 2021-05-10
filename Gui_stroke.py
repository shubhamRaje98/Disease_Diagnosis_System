from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox
import prog_heart_dia as ph
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


class GUI_Stroke:

    def __init__(self, risk_factor, res):

        root_Stroke = Tk()
        root_Stroke.title("Diagnosing stroke")
        cent = "1000x660+160+40"
        root_Stroke.geometry(cent)
        print("Here")

        Stroke_r_1 = StringVar()
        Stroke_r_2 = StringVar()
        Stroke_r_3 = StringVar()
        Stroke_r_4 = StringVar()
        Stroke_r_5 = StringVar()
        Stroke_r_6 = StringVar()
        Stroke_r_7 = StringVar()

        Stroke_my_canvas = Canvas(root_Stroke)
        Stroke_my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Background:

        Stroke_img = Image.open("background.png")
        Stroke_img = Stroke_img.resize((1800, 1280), Image.ANTIALIAS)
        Stroke_bg = ImageTk.PhotoImage(Stroke_img)
        Stroke_my_canvas.create_image(0, 0, image=Stroke_bg, anchor="nw")

        # Creating title text:
        Stroke_my_canvas.create_text(520, 40, text="Answer some question", font=("Times", 20), fill="white")

        # quetion 1:
        Stroke_my_canvas.create_text(310, 100, text="1) Do you have difficulty in walking due to weak muscels ?",
                                     font=("helvetica", 15), fill="black")

        Stroke_but_1 = Radiobutton(Stroke_my_canvas, text="yes", variable=Stroke_r_1, value="yes",
                                   fill="white", radius=8)
        Stroke_but_1.put(120, 150)

        Stroke_but_2 = Radiobutton(Stroke_my_canvas, text="no", variable=Stroke_r_1, value="no",
                                   fill="white", radius=8)
        Stroke_but_2.put(220, 150)

        # Stroke_r_1.set("yes")

        # question 2:
        Stroke_my_canvas.create_text(230, 200, text="2) Do you thin your vision is blummed ?",
                                     font=("helvetica", 15), fill="black")

        Stroke_but_3 = Radiobutton(Stroke_my_canvas, text="yes", variable=Stroke_r_2, value="yes",
                                   fill="white", radius=8)
        Stroke_but_3.put(120, 250)

        Stroke_but_4 = Radiobutton(Stroke_my_canvas, text="no", variable=Stroke_r_2, value="no",
                                   fill="white", radius=8)
        Stroke_but_4.put(220, 250)

        # Stroke_r_2.set("yes")

        # question 3:
        Stroke_my_canvas.create_text(240, 300, text="3) Have you experienced loss of speech ?",
                                     font=("helvetica", 15), fill="black")

        Stroke_but_5 = Radiobutton(Stroke_my_canvas, text="yes", variable=Stroke_r_3, value="yes",
                                   fill="white", radius=8)
        Stroke_but_5.put(120, 350)

        Stroke_but_6 = Radiobutton(Stroke_my_canvas, text="no", variable=Stroke_r_3, value="no",
                                   fill="white", radius=8)
        Stroke_but_6.put(220, 350)

        # Stroke_r_3.set("yes")

        # question 4:
        Stroke_my_canvas.create_text(205, 400, text="4) Do you feel fatigue or vertigo ?",
                                     font=("helvetica", 15), fill="black")

        Stroke_but_7 = Radiobutton(Stroke_my_canvas, text="yes", variable=Stroke_r_4, value="yes",
                                   fill="white", radius=8)
        Stroke_but_7.put(120, 450)

        Stroke_but_8 = Radiobutton(Stroke_my_canvas, text="no", variable=Stroke_r_4, value="no",
                                   fill="white", radius=8)
        Stroke_but_8.put(220, 450)

        # Stroke_r_4.set("yes")

        # question 5:
        Stroke_my_canvas.create_text(235, 500, text="5) Is your cognetive power decreased ?",
                                     font=("helvetica", 15), fill="black")

        Stroke_but_9 = Radiobutton(Stroke_my_canvas, text="yes", variable=Stroke_r_5, value="yes",
                                   fill="white", radius=8)
        Stroke_but_9.put(120, 550)

        Stroke_but_10 = Radiobutton(Stroke_my_canvas, text="no", variable=Stroke_r_5, value="no",
                                    fill="white", radius=8)
        Stroke_but_10.put(220, 550)

        # Stroke_r_5.set("yes")
        Stroke_obj = ph.Prog()

        def calculate_fatality_risk():
            global fatality_r

            Stroke_que_1 = Stroke_r_1.get()
            Stroke_que_2 = Stroke_r_2.get()
            Stroke_que_3 = Stroke_r_3.get()
            Stroke_que_4 = Stroke_r_4.get()
            Stroke_que_5 = Stroke_r_5.get()

            print(Stroke_que_1)
            print(Stroke_que_2)
            print(Stroke_que_3)
            print(Stroke_que_4)
            print(Stroke_que_5)

            fatality_r = Stroke_obj.diagnose_stroke(Stroke_que_1, Stroke_que_2, Stroke_que_3, Stroke_que_4, Stroke_que_5, risk_factor)

            print("Returned value is : " + str(fatality_r))

            print("Your fatality risk is : " + str(fatality_r) + "%")

            message_Stroke_res = messagebox.showinfo("Risk factor ", "Your fatality risk is : " + str(fatality_r) + "%")
            if message_Stroke_res == 'ok':
                if fatality_r > 0:
                    root_Stroke.destroy()
                    Result.GUI_result("Stroke", fatality_r, risk_factor, res)
                else:
                    root_Stroke.destroy()
                    Result.GUI_result("Unkown Disease", fatality_r, risk_factor, res)
                    #Result.GUI_result("Unkown", fatality_r, risk_factor)
                print("Back here in GUI_CHD")

        Stroke_but = ttk.Button(Stroke_my_canvas, text="submit", width=18, command=calculate_fatality_risk)
        Stroke_my_canvas.create_window(800, 580, window=Stroke_but)

        root_Stroke.mainloop()
    


#Stroke_obj = GUI_Stroke(30)
