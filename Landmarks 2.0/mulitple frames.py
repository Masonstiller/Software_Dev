import tkinter as tk
import card_maker_class
from PIL import ImageTk, Image
import requests
from io import BytesIO
import random

LARGEFONT = ("Verdana", 35, "bold")
MIDFONT = ("Verdana", 20, "bold")
SMALLFONT = ("Verdana", 10)

instructions = "Welcome to the Landmarks App. Choose an option below to learn more about it. Go back to refresh your options."

cur = 0
list = [("Parthenon", "Parthenon"),("Petra", "Petra"), ("Big Ben","Big_Ben"),("Space Needle", "Space_Needle"),("Terracotta Army","Terracotta_Army"),("Colloseum","Colloseum"),
        ('Eiffel Tower', 'Eiffel_Tower'),('Golden Gate Bridge', 'Golden_Gate'),("Mount Everest", "Everest"), ("Great Wall of China", "Great_Wall_of_China"),
        ("Empire State Building", 'Empire_State_Building'),('Great Pyramid of Giza','Great_Pyramid_of_Giza'),("Crater Lake", 'Crater_Lake')]
# setup
root = tk.Tk()
root.geometry("450x1000")
root.config(bg = '#78c4bd')
root.title("Landmarks")

# create frames
menuFrame = tk.Frame(root)
menuFrame.grid(row=0, column=0)
menuFrame.config(bg = '#78c4bd')
itemFrame = tk.Frame(root)
itemFrame.grid(row=0, column=1)
itemFrame.config(bg = '#78c4bd')

def generate():
    generated = random.sample(range(0,len(list)),8)
    return generated


def clear(object):
    slaves = object.grid_slaves()
    for x in slaves:
        x.destroy()

def start_screen():
    indices = generate()
    clear(itemFrame)
    clear(menuFrame)
    tk.Label(itemFrame, bg='#78c4bd', text="Landmarks", font=LARGEFONT, fg='#2A4542').grid(row=0, column=0)
    tk.Button(itemFrame, text="start", command=lambda: menu1(indices)).grid(row=1, column=0, padx=172)


def menu1(indices):
    clear(itemFrame)
    clear(menuFrame)
    tk.Label(itemFrame, bg='#78c4bd', text="Landmarks", font=LARGEFONT, fg='#2A4542').grid(row=0, column=0)
    tk.Message(itemFrame, text=instructions, font = SMALLFONT, bg = '#78c4bd', width = 200 ).grid(row=1, column=0)
    tk.Button(menuFrame, text="back", command=lambda :start_screen()).grid(row=1, column=0)
    tk.Button(itemFrame, text=list[indices[0]][0], command=lambda: card(indices,0)).grid(row=2, column=0, padx = 152, pady = 5)
    tk.Button(itemFrame, text=list[indices[1]][0], command=lambda: card(indices,1)).grid(row=3, column=0,  padx = 152, pady = 5)
    tk.Button(itemFrame, text=list[indices[2]][0], command=lambda: card(indices,2)).grid(row=4, column=0,  padx = 152, pady = 5)
    tk.Button(itemFrame, text=list[indices[3]][0], command=lambda: card(indices,3)).grid(row=5, column=0, padx = 152, pady = 5)
    tk.Button(itemFrame, text=list[indices[4]][0], command=lambda: card(indices,4)).grid(row=6, column=0,  padx = 152, pady = 5)
    tk.Button(itemFrame, text=list[indices[5]][0], command=lambda: card(indices,5)).grid(row=7, column=0,  padx = 152, pady = 5)
    tk.Button(itemFrame, text=list[indices[6]][0], command=lambda: card(indices,6)).grid(row=8, column=0,  padx = 152, pady = 5)
    tk.Button(itemFrame, text=list[indices[7]][0], command=lambda: card(indices,7)).grid(row=9, column=0,  padx = 152, pady = 5)

def card(indices,option):
    index = indices[option]
    data = list[index]
    clear(itemFrame)
    clear(menuFrame)

    one = card_maker_class.Card(data[1])
    title = one.title
    if len(title) <= 12:
       tk.Label(itemFrame,bg ='#78c4bd', text= one.title, font = LARGEFONT, fg ='#2A4542').grid(row=0, column=0)
    else:
        tk.Label(itemFrame, bg='#78c4bd', text=one.title, font=MIDFONT, fg='#2A4542').grid(row=0, column=0)

    response = requests.get(one.image)
    image1 = Image.open(BytesIO(response.content))
    image1.thumbnail((360,600))
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(itemFrame, image=test)
    label1.image = test
    label1.grid(row =2, column=0,pady = 15)

    T = tk.Message(itemFrame, text=one.text, font = SMALLFONT, width =300, bg='#78c4bd')
    T.grid(row=3, column=0)

    tk.Button(menuFrame, text="Back", command=lambda:menu1(indices)).grid(row=0, column=0)


indices = generate()
tk.Label(itemFrame, bg='#78c4bd', text="Landmarks", font=LARGEFONT, fg='#2A4542').grid(row=0, column=0)
tk.Button(itemFrame, text="start", command= lambda:menu1(indices)).grid(row=1, column=0,padx = 212)
tk.mainloop()



