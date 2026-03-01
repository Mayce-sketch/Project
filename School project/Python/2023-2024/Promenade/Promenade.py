#08/02/2024
from tkinter import *
fenetre = Tk()
fenetre.config(width=600, height=500, bg="cyan")
fenetre.title("Promenade")
Canevas = Canvas(fenetre, width=603, height=405, bg='green')
Canevas.place(x=-2, y=95)
# inisiation des variables
score, choux, nb_deplacements, anime = 0,0,0,0
position_Choux,image_Choux,traces_de_pas = [] ,  [] ,  []
# les images inportes
a_e_0 = PhotoImage(file="image_animaux/lapin/a e 0.png")
a_e_1 = PhotoImage(file="image_animaux/lapin/a e 1.png")
a_e_2 = PhotoImage(file="image_animaux/lapin/a e 2.png")
a_w_0 = PhotoImage(file="image_animaux/lapin/a w 0.png")
a_w_1 = PhotoImage(file="image_animaux/lapin/a w 1.png")
a_w_2 = PhotoImage(file="image_animaux/lapin/a w 2.png")
a_n_0 = PhotoImage(file="image_animaux/lapin/a n 0.png")
a_n_1 = PhotoImage(file="image_animaux/lapin/a n 1.png")
a_n_2 = PhotoImage(file="image_animaux/lapin/a n 2.png")
a_s_0 = PhotoImage(file="image_animaux/lapin/a s 0.png")
a_s_1 = PhotoImage(file="image_animaux/lapin/a s 1.png")
a_s_2 = PhotoImage(file="image_animaux/lapin/a s 2.png")
pas_lapin_B = PhotoImage(file="image_animaux/lapin/pas lapin B.png")
pas_lapin_D = PhotoImage(file="image_animaux/lapin/pas lapin D.png")
pas_lapin_G = PhotoImage(file="image_animaux/lapin/pas lapin G.png")
pas_lapin_H = PhotoImage(file="image_animaux/lapin/pas lapin H.png")
cible = PhotoImage(file="image_animaux/lapin/cible.png")
cood_des_lapin = Canevas.create_image(300, 200, image=a_s_0)
image_pas_lapin = Canevas.create_image(300,200)

# pour deplacer l'animal
def deplacer_lapin(dx, dy):
    global nb_deplacements
    x, y = Canevas.coords(cood_des_lapin)
    x += dx
    y += dy
    Canevas.coords(cood_des_lapin, x, y)
    nb_deplacements += 1
    if nb_deplacements % 5 == 0: # si 5 alors on fait les trace de pas
        creer_trace_de_pas(x, y)
# pour faire les trace de pas
def creer_trace_de_pas(x, y):
    orientation = Canevas.itemcget(cood_des_lapin, "image")  # Obtenez l'orientation actuelle de l'animal
    pas_image = ""
    if orientation == str(a_n_0) or orientation == str(a_n_1)  or orientation == str(a_n_2): # si haut
        pas_image = pas_lapin_H
    elif orientation == str(a_s_0) or orientation == str(a_s_1) or orientation == str(a_s_2): # si bas
        pas_image = pas_lapin_B
    elif orientation == str(a_w_0) or orientation == str(a_w_1) or orientation == str(a_w_2): # si gauche
        pas_image = pas_lapin_G
    elif orientation == str(a_e_0) or orientation == str(a_e_1) or orientation == str(a_e_2): # si droite
        pas_image = pas_lapin_D
    if pas_image:
        trace_pas = Canevas.create_image(x, y, image=pas_image)
        traces_de_pas.append(trace_pas)

def droite(event):
    global anime
    anime_animaux(a_e_0,a_e_1,a_e_2) # animation pour le perso
    x_lapin, y_lapin = Canevas.coords(cood_des_lapin)[:2]
    if x_lapin <= 600: # si pas hors limite
        deplacer_lapin(10, 0)
    else:
        Canevas.coords(cood_des_lapin, 0, y_lapin)
    verifier_choux_texte(x_lapin, y_lapin) # on regarde si il peux enlever l'alimant
def gauche(event):
    global anime
    anime_animaux(a_w_0, a_w_1, a_w_2)
    x_lapin, y_lapin = Canevas.coords(cood_des_lapin)[:2]
    if x_lapin >= 0:
        deplacer_lapin(-10, 0)
    else:
        Canevas.coords(cood_des_lapin, 600, y_lapin)
    verifier_choux_texte(x_lapin, y_lapin)
def haut(event):
    global anime
    anime_animaux(a_n_0, a_n_1, a_n_2)
    x_lapin, y_lapin = Canevas.coords(cood_des_lapin)[:2]
    if y_lapin >= 5:
        deplacer_lapin(0, -10)
    else:
        Canevas.coords(cood_des_lapin, x_lapin, 405)
    verifier_choux_texte(x_lapin, y_lapin)
def bas(event):
    global anime
    anime_animaux(a_s_0, a_s_1, a_s_2)
    x_lapin, y_lapin = Canevas.coords(cood_des_lapin)[:2]
    if y_lapin <= 405:
        deplacer_lapin(0, 10)
    else:
        Canevas.coords(cood_des_lapin, x_lapin, 5)
    verifier_choux_texte(x_lapin, y_lapin)
# annimation de l'animal
def anime_animaux(image1,image2,image3):
    global anime
    if anime == 0:
        Canevas.itemconfig(cood_des_lapin, image=image1)
    elif anime == 2:
        Canevas.itemconfig(cood_des_lapin, image=image2)
    elif anime == 1:
        Canevas.itemconfig(cood_des_lapin, image=image3)
    anime = anime + 1
    if anime == 3:
        anime = 0
# poser la nouriture
def boutonSouris(event):
    global choux
    if choux < 3:
        if 20 <= event.x <= 585 and 20 <= event.y <= 390: # pour eviter que l on place un alimant en dehors
            image_Choux = Canevas.create_image(event.x, event.y, image=cible)
            choux = choux + 1
            position_Choux.append([event.x, event.y, image_Choux])
            print("position du choux: ",position_Choux)
# enlever la nouriture
def enlever_choux(event):
    
    x_lapin, y_lapin = Canevas.coords(cood_des_lapin)[:2]
    i = len(position_Choux) - 1
    while i >= 0:
        chou_x, chou_y, chou_image = position_Choux[i]
        if x_lapin + 30 >= chou_x >= x_lapin - 30 and y_lapin + 30 >= chou_y >= y_lapin - 30: # si l'animal est a coter de alimant
            Canevas.delete(chou_image)
            position_Choux.pop(i)
            effacer_choux.place_forget()
            global score
            score = score + 1
            print("position du choux: ", position_Choux)
            texte_score.config(text="Le score est " + str(score) + "/3")
            if score == 3:
                victoire.place(x=300, y=225, anchor="c")
        i = i - 1
# mettre/ enlever le text pour l utilisateur
def verifier_choux_texte(x_lapin, y_lapin):
    i = len(position_Choux) - 1
    while i >= 0:
        chou_x, chou_y, chou_image = position_Choux[i]
        if x_lapin + 30 >= chou_x >= x_lapin - 30 and y_lapin + 30 >= chou_y >= y_lapin - 30: # si a coter 
            effacer_choux.place(x=x_lapin-22.5, y=y_lapin+20) # place un text pour l utilisateur
        elif  x_lapin + 40 >= chou_x >= x_lapin - 40 and y_lapin + 40 >= chou_y >= y_lapin - 40: # si pas coter 
            effacer_choux.place_forget() # enlever le texte
        i -= 1

# changer l animale
def changer_d_animaux():
    global a_e_0,a_e_1,a_e_2,a_w_0,a_w_1,a_w_2,a_n_0,a_n_1,a_n_2,a_s_0,a_s_1,a_s_2,pas_lapin_B,pas_lapin_D,pas_lapin_G,pas_lapin_H,cible
    nom_animal = autre_annimaux.get()  # Obtenir la valeur de l'Entry
    if nom_animal == "lapin" or nom_animal == "ours" or nom_animal == "poule":
        # on redefinit les variable des images en fonction
        if nom_animal == "lapin":
            a_e_0 = PhotoImage(file="image_animaux/lapin/a e 0.png")
            a_e_1 = PhotoImage(file="image_animaux/lapin/a e 1.png")
            a_e_2 = PhotoImage(file="image_animaux/lapin/a e 2.png")
            a_w_0 = PhotoImage(file="image_animaux/lapin/a w 0.png")
            a_w_1 = PhotoImage(file="image_animaux/lapin/a w 1.png")
            a_w_2 = PhotoImage(file="image_animaux/lapin/a w 2.png")
            a_n_0 = PhotoImage(file="image_animaux/lapin/a n 0.png")
            a_n_1 = PhotoImage(file="image_animaux/lapin/a n 1.png")
            a_n_2 = PhotoImage(file="image_animaux/lapin/a n 2.png")
            a_s_0 = PhotoImage(file="image_animaux/lapin/a s 0.png")
            a_s_1 = PhotoImage(file="image_animaux/lapin/a s 1.png")
            a_s_2 = PhotoImage(file="image_animaux/lapin/a s 2.png")
            pas_lapin_B = PhotoImage(file="image_animaux/lapin/pas lapin B.png")
            pas_lapin_D = PhotoImage(file="image_animaux/lapin/pas lapin D.png")
            pas_lapin_G = PhotoImage(file="image_animaux/lapin/pas lapin G.png")
            pas_lapin_H = PhotoImage(file="image_animaux/lapin/pas lapin H.png")
            cible = PhotoImage(file="image_animaux/lapin/cible.png")
        elif nom_animal == "ours":
            a_e_0 = PhotoImage(file="image_animaux/ours/a e 0.png")
            a_e_1 = PhotoImage(file="image_animaux/ours/a e 1.png")
            a_e_2 = PhotoImage(file="image_animaux/ours/a e 2.png")
            a_w_0 = PhotoImage(file="image_animaux/ours/a w 0.png")
            a_w_1 = PhotoImage(file="image_animaux/ours/a w 1.png")
            a_w_2 = PhotoImage(file="image_animaux/ours/a w 2.png")
            a_n_0 = PhotoImage(file="image_animaux/ours/a n 0.png")
            a_n_1 = PhotoImage(file="image_animaux/ours/a n 1.png")
            a_n_2 = PhotoImage(file="image_animaux/ours/a n 2.png")
            a_s_0 = PhotoImage(file="image_animaux/ours/a s 0.png")
            a_s_1 = PhotoImage(file="image_animaux/ours/a s 1.png")
            a_s_2 = PhotoImage(file="image_animaux/ours/a s 2.png")
            pas_lapin_B = PhotoImage(file="image_animaux/ours/pas ours B.png")
            pas_lapin_D = PhotoImage(file="image_animaux/ours/pas ours D.png")
            pas_lapin_G = PhotoImage(file="image_animaux/ours/pas ours G.png")
            pas_lapin_H = PhotoImage(file="image_animaux/ours/pas ours H.png")
            cible = PhotoImage(file="image_animaux/ours/cible 177.png")
        elif nom_animal == "poule":
            a_e_0 = PhotoImage(file="image_animaux/poule/a e 0.png")
            a_e_1 = PhotoImage(file="image_animaux/poule/a e 1.png")
            a_e_2 = PhotoImage(file="image_animaux/poule/a e 2.png")
            a_w_0 = PhotoImage(file="image_animaux/poule/a w 0.png")
            a_w_1 = PhotoImage(file="image_animaux/poule/a w 1.png")
            a_w_2 = PhotoImage(file="image_animaux/poule/a w 2.png")
            a_n_0 = PhotoImage(file="image_animaux/poule/a n 0.png")
            a_n_1 = PhotoImage(file="image_animaux/poule/a n 1.png")
            a_n_2 = PhotoImage(file="image_animaux/poule/a n 2.png")
            a_s_0 = PhotoImage(file="image_animaux/poule/a s 0.png")
            a_s_1 = PhotoImage(file="image_animaux/poule/a s 1.png")
            a_s_2 = PhotoImage(file="image_animaux/poule/a s 2.png")
            pas_lapin_B = PhotoImage(file="image_animaux/poule/pas poule B.png")
            pas_lapin_D = PhotoImage(file="image_animaux/poule/pas poule D.png")
            pas_lapin_G = PhotoImage(file="image_animaux/poule/pas poule G.png")
            pas_lapin_H = PhotoImage(file="image_animaux/poule/pas poule H.png")
            cible = PhotoImage(file="image_animaux/poule/cible 147.png")
        Canevas.itemconfig(cood_des_lapin, image=a_s_0)
        recommencer() # on recommence car on change de perso
    else:
        label_animaux.config(text="Vous devez choisir entre le mot lapin, ours ou poule")
# pour recommencer
def recommencer(): # tout est remie comme au depart sauf le choix du perso
    global score, choux, nb_deplacements, traces_de_pas
    score, choux, nb_deplacements = 0, 0, 0
    victoire.place_forget()
    Canevas.coords(cood_des_lapin, 250, 250)
    Canevas.itemconfig(cood_des_lapin, image=a_s_0)
    # Supprimer toutes les images de pas
    for i in range(len(position_Choux) - 1, -1, -1):
        chou_x, chou_y, chou_image = position_Choux[i]
        Canevas.delete(chou_image)
        position_Choux.pop(i)
    for trace_pas in traces_de_pas:
        Canevas.delete(trace_pas)
    traces_de_pas = []  # Réinitialiser la liste des traces
    effacer_choux.place_forget()
    texte_score.config(text="Le score est " + str(score) + "/3")
    label_animaux.config(text="Vous pouvez choisir entre le lapin, l'ours ou la poule")
    label_animaux.place(x=325, y=60, anchor="n")


texte_score = Label(fenetre, text="Le score est " + str(score) + "/3", width=13, height=2)
texte_score.place(x=595, y=22.5, anchor="ne")
label_animaux = Label(fenetre,text="Vous pouvez choisir entre le lapin, l'ours ou la poule")
label_animaux.place(x=325,y=60,anchor="n")

changer_d_animaux = Button(fenetre, text="valider", width=10, height=1,command=changer_d_animaux)
changer_d_animaux.place(x=390, y=25)

effacer_choux = Label(fenetre,text="entrer", width=5, height=1, font=("times", 10, "bold"), bg="cyan")
recomencer = Button(fenetre, text="recommencer", width=10, height=1,font=("times", 15, "bold"),command=recommencer)
recomencer.place(x=20, y=30)

victoire = Label(fenetre, text="victoire", width=6, height=1, font=("times", 30, "bold"), bg="cyan")

autre_annimaux=Entry(width=20)
autre_annimaux.place(x=200,y=25)

fenetre.bind("<z>", haut)
fenetre.bind("<s>", bas)
fenetre.bind("<q>", gauche)
fenetre.bind("<d>", droite)
fenetre.bind("<Button-1>", boutonSouris)
fenetre.bind("<Return>", enlever_choux)

fenetre.mainloop()
