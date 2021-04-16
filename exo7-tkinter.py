import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("500x500")
fenetre.title("heyyyyyy")

texte = "salut"
def txt():
    global texte
    if texte == "salut":
        texte = "ca va?"
    else:
        texte = "salut"
    return(texte)

def action_clic(e):
    l1.config(text = txt())
    
l1 = tk.Label(text = "salut")
l1.grid(row=0,column=0)
b = tk.Button(fenetre,text="clique !")
b.grid(row=0,column=1,rowspan=2)
b.bind("<Button-1>",action_clic)

fenetre.mainloop()


