import tkinter as tk
import card_maker_class
from PIL import ImageTk, Image
import requests
from io import BytesIO


string = "Cloud_Strife"
LARGEFONT = ("Verdana", 35, "bold")
MIDFONT = ("Verdana", 20, "bold")
SMALLFONT = ("Verdana", 10)

root = tk.Tk()
root.geometry("360x1000")
root.config(bg = '#78c4bd')

itemFrame = tk.Frame(root)
itemFrame.grid(row=0, column=1)
itemFrame.config(bg = '#78c4bd')

one = card_maker_class.Card(string)
title = one.title
if len(title) <= 12:
    tk.Label(itemFrame, bg='#78c4bd', text=one.title, font=LARGEFONT, fg='#2A4542').grid(row=0, column=0)
else:
    tk.Label(itemFrame, bg='#78c4bd', text=one.title, font=MIDFONT, fg='#2A4542').grid(row=0, column=0)

response = requests.get(one.image)
image1 = Image.open(BytesIO(response.content))
image1.thumbnail((400, 600))
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(itemFrame, image=test)
label1.image = test
label1.grid(row=2, column=0, pady=15)

T = tk.Message(itemFrame, text=one.text, font=SMALLFONT, width=300, bg='#78c4bd')
T.grid(row=3, column=0)

tk.mainloop()

