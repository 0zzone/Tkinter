import tkinter as tk

fenetre = tk.Tk()
fenetre.title("exo 15")
fenetre.geometry("500x500")

xb = 100
yb = 130
xb1 = xb+35
yb1 = yb+35
def clic(event):
    global xb, yb, xb1, yb1
    balle = can.create_oval(xb, yb, xb1, yb1, fill="red")
    yb = yb+35
    yb1 = yb1+35
    xb = 100
    xb1 = xb + 35
    fenetre.after(200, clic)


    

    
can = tk.Canvas(fenetre, width=400, height=500, bg="ivory")
can.pack(side="right")




b = tk.Button(fenetre, text="démarrer")
b.pack(side= "left")
b.bind("<Button-1>", clic)



fenetre.mainloop()
