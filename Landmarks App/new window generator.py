from tkinter import *
from tkinter.ttk import *
import card_maker_class
from PIL import ImageTk, Image
import requests
from io import BytesIO
import random

LARGEFONT = ("Verdana", 35)
SMALLFONT = ("Verdana", 12)

list = [("Parthenon", "Parthenon"),("Petra", "Petra"), ("Big Ben","Big_Ben"),("Space Needle", "Space_Needle"),("Terracotta Army","Terracotta_Army"),("Colloseum","Colloseum"),
        ('Eiffel Tower', 'Eiffel_Tower'),('Golden Gate Bridge', 'Golden_Gate'),("Mount Everest", "Everest"), ("Great Wall of China", "Great_Wall_of_China"),
        ("Empire State Building", 'Empire_State_Building'),('Great Pyramid of Giza','Great_Pyramid_of_Giza'),("Crater Lake", 'Crater_Lake')]

generated = random.sample(range(0,len(list)),8)


class NewWindow(Toplevel):

    def __init__(self, master=None, string = None):
        card = card_maker_class.Card(string)
        super().__init__(master=master)
        self.title("Info Page")

        var = card.title
        info = card.text
        title = Label(self, text=var, font=LARGEFONT)
        title.pack()

        label1 = Label(self, text ="image")
        label1.pack()

        T = Message(self, text=info, font=SMALLFONT)
        T.pack()





master = Tk()

master.geometry("800x800")

label = Label(master, text="Landmarks")
label.pack(side=TOP, pady=10)


btn = Button(master,
             text=list[generated[0]][0])
btn2 = Button(master,
             text=list[generated[1]][0])
btn3 = Button(master,
             text=list[generated[2]][0])
btn4 = Button(master,
             text=list[generated[3]][0])
btn5 = Button(master,
             text=list[generated[4]][0])
btn6 = Button(master,
             text=list[generated[5]][0])
btn7 = Button(master,
             text=list[generated[6]][0])
btn8 = Button(master,
             text=list[generated[7]][0])


btn.bind("<Button>",
         lambda e: NewWindow(master, list[generated[0]][1]))
btn2.bind("<Button>",
         lambda e: NewWindow(master,list[generated[1]][1]))
btn3.bind("<Button>",
         lambda e: NewWindow(master,list[generated[2]][1]))
btn4.bind("<Button>",
         lambda e: NewWindow(master,list[generated[3]][1]))
btn5.bind("<Button>",
         lambda e: NewWindow(master,list[generated[4]][1]))
btn6.bind("<Button>",
         lambda e: NewWindow(master,list[generated[5]][1]))
btn7.bind("<Button>",
         lambda e: NewWindow(master,list[generated[6]][1]))
btn8.bind("<Button>",
         lambda e: NewWindow(master,list[generated[7]][1]))



btn.pack(pady=10)
btn2.pack(pady=10)
btn3.pack(pady=10)
btn4.pack(pady=10)
btn5.pack(pady=10)
btn6.pack(pady=10)
btn7.pack(pady=10)
btn8.pack(pady=10)



mainloop()