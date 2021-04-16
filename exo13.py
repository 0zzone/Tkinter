import tkinter as tk
from random import randint

fenetre = tk.Tk()
fenetre.title("exo 13")
fenetre.geometry("500x500")

x1 = 100
y1 = 0
x2 = 300
y2 = 500

def create(e):
    global x1, x2
    line = can.create_line(x1,y1,x2,y2)
    x1 = x1 + 20
    x2 = x2 - 20
    return x1,x2



can = tk.Canvas(fenetre, height=500, width = 400, bg="ivory")
can.pack(side = "right")

b = tk.Button(fenetre, text="Tracer")
b.pack(side="left")
b.bind("<Button-1>", create)

