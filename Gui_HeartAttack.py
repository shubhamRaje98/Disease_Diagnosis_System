from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox
import Result_dia as Result
import prog_heart_dia as ph
import Gui_stroke as stroke


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


class GUI_Heart_Attack:
    def __init__(self, risk_factor, res):
        HeartAtt_root = Tk()
        HeartAtt_root.title("Diagnosing Heart Attack")
        cent = "1000x680+160+40"
        HeartAtt_root.geometry(cent)
        #HeartAtt_root.geometry("1400x750")
        
        HeartAtt_r_1 = StringVar()
        HeartAtt_r_2 = StringVar()
        HeartAtt_r_3 = StringVar()
        HeartAtt_r_4 = StringVar()
        HeartAtt_r_5 = StringVar()
        HeartAtt_r_6 = StringVar()

        # Setting up Canvas:
        HeartAtt_my_canvas = Canvas(HeartAtt_root)
        HeartAtt_my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Background:
        HeartAtt_img = Image.open("background.png")
        HeartAtt_img = HeartAtt_img.resize((1500, 1280), Image.ANTIALIAS)
        HeartAtt_bg = ImageTk.PhotoImage(HeartAtt_img)
        HeartAtt_my_canvas.create_image(0, 0, image=HeartAtt_bg, anchor="nw")


        # Creating title text:
        HeartAtt_my_canvas.create_text(520, 40, text="Answer some question",
                              font=("Times", 20), fill="white")

        # quetion 1:
        HeartAtt_my_canvas.create_text(195, 100, text="1) Do you have Chest Pain ?",
                              font=("helvetica", 15), fill="black")

        HeartAtt_but_1 = Radiobutton(HeartAtt_my_canvas, text="yes", variable=HeartAtt_r_1, value="yes",
                            fill="white", radius=8)
        HeartAtt_but_1.put(120, 150)

        HeartAtt_but_2 = Radiobutton(HeartAtt_my_canvas, text="no", variable=HeartAtt_r_1, value="no",
                            fill="white", radius=8)
        HeartAtt_but_2.put(220, 150)

        #HeartAtt_r_1.set("yes")

        # question 2:
        HeartAtt_my_canvas.create_text(245, 200, text="2) Do you have shortness of breath ?",
                              font=("helvetica", 15), fill="black")

        HeartAtt_but_3 = Radiobutton(HeartAtt_my_canvas, text="yes", variable=HeartAtt_r_2, value="yes",
                            fill="white", radius=8)
        HeartAtt_but_3.put(120, 250)

        HeartAtt_but_4 = Radiobutton(HeartAtt_my_canvas, text="no", variable=HeartAtt_r_2, value="no",
                            fill="white", radius=8)
        HeartAtt_but_4.put(220, 250)

        #HeartAtt_r_2.set("yes")

        # question 3:
        HeartAtt_my_canvas.create_text(310, 300, text="3) Do you feel pain discomfort in neck / lower jaw ?",
                              font=("helvetica", 15), fill="black")

        HeartAtt_but_5 = Radiobutton(HeartAtt_my_canvas, text="yes", variable=HeartAtt_r_3, value="yes",
                            fill="white", radius=8)
        HeartAtt_but_5.put(120, 350)

        HeartAtt_but_6 = Radiobutton(HeartAtt_my_canvas, text="no", variable=HeartAtt_r_3, value="no",
                            fill="white", radius=8)
        HeartAtt_but_6.put(220, 350)

        #HeartAtt_r_3.set("yes")

        # question 4:
        HeartAtt_my_canvas.create_text(240, 400, text="4) Are sweating more than usual ?",
                              font=("helvetica", 15), fill="black")

        HeartAtt_but_7 = Radiobutton(HeartAtt_my_canvas, text="yes", variable=HeartAtt_r_4, value="yes",
                            fill="white", radius=8)
        HeartAtt_but_7.put(120, 450)

        HeartAtt_but_8 = Radiobutton(HeartAtt_my_canvas, text="no", variable=HeartAtt_r_4, value="no",
                            fill="white", radius=8)
        HeartAtt_but_8.put(220, 450)

        #HeartAtt_r_4.set("yes")

        # question 5:
        HeartAtt_my_canvas.create_text(210, 500, text="5) Do you sense palpitation ?",
                              font=("helvetica", 15), fill="black")

        HeartAtt_but_9 = Radiobutton(HeartAtt_my_canvas, text="yes", variable=HeartAtt_r_5, value="yes",
                            fill="white", radius=8)
        HeartAtt_but_9.put(120, 550)

        HeartAtt_but_10 = Radiobutton(HeartAtt_my_canvas, text="no", variable=HeartAtt_r_5, value="no",
                             fill="white", radius=8)
        HeartAtt_but_10.put(220, 550)

        #HeartAtt_r_5.set("male")

        # question 6:
        HeartAtt_my_canvas.create_text(180, 600, text="6)Do you feel nausea ?",
                              font=("helvetica", 15), fill="black")

        HeartAtt_but_11 = Radiobutton(HeartAtt_my_canvas, text="yes", variable=HeartAtt_r_6, value="yes",
                             fill="white", radius=8)
        HeartAtt_but_11.put(120, 650)

        HeartAtt_but_12 = Radiobutton(HeartAtt_my_canvas, text="no", variable=HeartAtt_r_6, value="no",
                             fill="white", radius=8)
        HeartAtt_but_12.put(220, 650)

        #HeartAtt_r_6.set("yes")
        HeartAtt_obj = ph.Prog()

        def calculate_fatality_risk():
            global fatality_r
            
            HeartAtt_que_1 = HeartAtt_r_1.get()
            HeartAtt_que_2 = HeartAtt_r_2.get()
            HeartAtt_que_3 = HeartAtt_r_3.get()
            HeartAtt_que_4 = HeartAtt_r_4.get()
            HeartAtt_que_5 = HeartAtt_r_5.get()
            HeartAtt_que_6 = HeartAtt_r_6.get()

            print(HeartAtt_que_1)
            print(HeartAtt_que_2)
            print(HeartAtt_que_3)
            print(HeartAtt_que_4)
            print(HeartAtt_que_5)
            
            fatality_r = HeartAtt_obj.diagnose_heart_attack(HeartAtt_que_1,HeartAtt_que_2, HeartAtt_que_3, HeartAtt_que_4, HeartAtt_que_5, HeartAtt_que_6, risk_factor)


            print("Returned value is : " + str(fatality_r))

            print("Your fatality risk is : " + str(fatality_r) + "%")

            message_HeartAtt_res = messagebox.showinfo("Risk factor ", "Your fatality risk is : " + str(fatality_r) + "%")
            if message_HeartAtt_res == 'ok':
                if fatality_r > 0 :
                    HeartAtt_root.destroy()
                    Result.GUI_result("Heart Attack", fatality_r, risk_factor, res)
                else:
                    HeartAtt_root.destroy()
                    stroke.GUI_Stroke(risk_factor, res)
                    #Result.GUI_result("Unkown", fatality_r, risk_factor)
                print("Back here in GUI_CHD")

       
        HeartAtt_but = ttk.Button(HeartAtt_my_canvas, text="submit", width=18, command=calculate_fatality_risk)
        HeartAtt_my_canvas.create_window(850, 650, window=HeartAtt_but)
       
        #obj.calculate_risk_factor(que_1,que_2, que_3, que_4, que_5, que_6, que_7, que_8, que_9, que_10) 
               
        HeartAtt_root.mainloop()


#obj = GUI_Heart_Attack(40)
