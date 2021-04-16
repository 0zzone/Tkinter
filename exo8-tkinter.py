import tkinter as tk

fenetre = tk.Tk()
fenetre.title("heyooo")
fenetre.geometry("700x400")

def clic(event):
    if champ.get().isnumeric():
        uni.config(text=chr(int(champ.get())))
    else:
        label1.config(text="Il faut choisir un nombre")

label = tk.Label(fenetre, text = "Entrer un numéro et le programme renverra son caractère unicode correspondant")
label.pack()

label1 = tk.Label(fenetre, text="Choisissez un nombre", bg="red")
label1.pack()

champ = tk.Entry(fenetre)
champ.bind("<Return>", clic)
champ.pack()

b = tk.Button(fenetre, text="valider")
b.pack()


uni = tk.Label(fenetre, text=" ")
uni.pack()
fenetre.mainloop()

