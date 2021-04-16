import tkinter as tk
from random import randint

fenetre = tk.Tk()
fenetre.title("exo 12")
fenetre.geometry("500x500")
fenetre.configure(bg="gray")

def create(e):
    can.create_rectangle(randint(100,400), randint(0,400), randint(100,400), randint(0,400))
def erase(e):
    can.delete(ALL)
    
aff = tk.Button(fenetre, text = "Afficher")
aff.pack(side = "left")
aff.bind("<Button-1>", create)

eff = tk.Button(fenetre, text = "Effacer")
eff.pack(side = "left")
eff.bind("<Button-1>", erase)



# Canvas
can = tk.Canvas(fenetre, width = 400, height = 500, bg="ivory")
can.pack()

can.create_rectangle(x1,y1,x2,y2, bg="red")


