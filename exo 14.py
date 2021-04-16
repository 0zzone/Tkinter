import tkinter as tk
from random import randint

fen = tk.Tk()
fen.title("exo 14")
fen.geometry("500x500")

demarre = 0

can = tk.Canvas(fen, height=500, width=350, bg="ivory")
can.pack(side = "right")

def clic(e):
    global demarre
    demarre = 1
    cre()
    
    
def cre():
    if demarre == 1:
        can.create_oval(randint(0,500), randint(0,500), randint(150,500), randint(0,500), fill="red")
        fen.after(200, cre)
            
def stop(e):
    global demarre
    demarre = 0
    cre()


b = tk.Button(fen, text="Démarrer")
b.pack(side="left")
b.bind("<Button-1>", clic)

b1 = tk.Button(fen, text="Arrêtter")
b1.pack(side="left")
b1.bind("<Button-1>", stop)



fen.mainloop()
