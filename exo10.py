# Importation des bibliothèques
import tkinter as tk
from random import randint

# Réalisation de la fenêtre graphique
fenetre = tk.Tk()
fenetre.title("Exo 10")
fenetre.geometry("500x500")

# Texte de titre
label = tk.Label(fenetre, text = "Veuillez devinez le nombre", font = ("Times","25","underline"))
label.pack()

# Consigne pour l'intrvalle à laquelle le nombre aléatoire choisi appartient
# Pour guider le joueur
consigne = tk.Label(fenetre, text = "Le nombre est compris entre 0 et 100, bonne chance !", fg = "silver", font =("Times", "15", "italic"))
consigne.pack()

# Le joueur rentre le nombre dans un champ de saisie ici
champ = tk.Entry(fenetre)
champ.pack()


# Cette fonction permet au joueur de rejouer
def restart(e, label, consigne, champ):
    """Cette fonction permet de relancer une nouvelle partie en re-affichant
        des éléments cachés lorque le joeur avait trouvé le nombre correct"""
    label.config(text = "Veuillez devinez le nombre")
    label.pack()
    consigne.pack()
    champ.pack()


# Cette fonction va réaliser les test et dire si le joueur a gagné ou non
nombre = randint(0,100)
s = 0
def verif(e):
    """Cett fonction est le coeur du programme, c'est elle qui va réaliser
        la série de test selon le nombre rentré du joueur"""
    global nombre
    global s
    if champ.get().isnumeric():
        n = champ.get()
        champ.delete(0, "end")
        if int(n) < nombre:
            label1.config(text = "Plus grand", fg="red")
            label.config(text = "Ancien nombre: " + n, fg="green", font = ("Helvetica", "15"))
            s = s + 1
        if int(n) > nombre:
            label1.config(text = "Plus petit", fg = "red")
            label.config(text = "Ancien nombre: " + n, fg="green", font = ("Helvetica", "15"))
            s = s + 1
        if int(n) > 100 or int(n) < 0:
            label1.config(text = "Le nombre doit etre compris entre 0 et 100", fg="red")
            label.config(text = "Veuillez deviner le nombre", fg="black")
            s = s + 1
        if int(n) == nombre:
            label1.config(text = "Gagné !", font = ("Helvetica", "30", "bold"))
            score.config(text = "Vous avez devine le nombre en " + str(s) + " essais !", font = ("Helvetica", "16", "italic"))
            
            # Supression des widgets et création d'un boutton pour pouvoir rejouer
            b.destroy()
            champ.destroy()
            consigne.destroy()
            label.destroy()
            rej = tk.Button(fenetre, text ="Rejouer")
            rej.pack()
            nombre = randint(0,100)
            rej.bind("<Button-1>", restart)
            

            # Evaluation de la performance du joueur selon son nombre d'essais
            if s <= 5:
                result.config(text = "Comme un pro !", fg = "grey")
            if s > 5 and s <= 10:
                result.config(text = "Tu te debrouille bien !", fg = "grey")
            if s > 10 and s <= 15:
                result.config(text = "Je suis sur que tu peux mieux faire !", fg = "grey")
            if s > 15:
                result.config(text = "Allez on recommence !", fg = "grey")
            return nombre
    else:
        label1.config(text = "Vous devez choisir un nombre", fg="red")


# Création du boutton qui va lancer la fonction "verif", le coeur du programme
b = tk.Button(fenetre, text = "Essayer")
b.bind("<Button-1>", verif)
b.pack()

# Affichage vide d'un texte qui sera remplacé par "plus grand" ou "plus petit"
label1 = tk.Label(fenetre, text = "")
label1.pack()

# Système qui va indiquer à la toute fin du programme la performance du joueur (son nombre d'essais)
score = tk.Label(fenetre, text= "")
score.pack()


# Systeme qui va dire sa performance selon son nombre d'essais
result = tk.Label(fenetre, text = "", fg="white")
result.pack()

fenetre.mainloop()
