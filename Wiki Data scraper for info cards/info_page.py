import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO
import card_maker_class

def info_page(var, info, picture):
    LARGEFONT = ("Verdana", 35)
    SMALLFONT = ("Verdana", 12)

    HEIGHT = 800
    WIDTH = 800

    root = tk.Tk()
    frame3 = tk.Frame(root, height=HEIGHT, width=WIDTH)
    frame3.pack()

    title = tk.Label(root, text=var, font=LARGEFONT)
    title.place(rely=.025, relwidth=1)

    response = requests.get(picture)
    image1 = Image.open(BytesIO(response.content))
    image1 = image1.resize((round(image1.size[0] * 0.5), round(image1.size[1] * 0.5)))
    test = ImageTk.PhotoImage(image1)

    label1 = tk.Label(root, image=test)
    label1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.6)

    T = tk.Message(root, text=info, font=SMALLFONT)
    T.pack()

    button = tk.Button(root, text="Back", command = lambda: root.destroy())
    button.place(rely=.05, relx=.05)
    root.mainloop()


def generate_page(string):
    card = card_maker_class.Card(string)

    info_page(card.title, card.text, card.image)

