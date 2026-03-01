#27/12/2023
from tkinter import *
from random import *
fenetre = Tk()
# Initialisation des compteurs
fenetre.title("Pixel Art")
fenetre.config(bg="#BC1DE6", width=700, height=700)
canevas = Canvas(fenetre, bg="#E4D6FF", width=550, height=550)
# definire les variables
niveau = 0
niveaujeu = 1
carreblanc = []
carrenoir = []
carrerouge = []
carrerouge_foncer = []
carrerouge_clair = []
carrenoir_gris = []
carregris_foncer = []
carregris = []
carregris_clair = []
carrejaune = []
carreorange = []
carrebleu = []
carrebleu_claire = []
carreviolet = []
carrebeige = []
texteblanc = []
textenoir = []
texterouge = []
texterouge_foncer = []
texterouge_clair = []
textenoir_gris = []
textegris_foncer = []
textegris = []
textegris_clair = []
textejaune = []
texteorange = []
textebleu = []
textebleu_claire = []
texteviolet = []
textebeige = []
carre_tout = []
# les couleurs aleatoires
def choisir_couleur_aleatoire():
    # Retirer tous les boutons existants
    for bouton in couleur_liste:
        bouton.place_forget()
    # Liste temporaire pour stocker les boutons
    boutons_a_placer = []
    # Nombre total de boutons à afficher
    nombre_total_boutons = len(couleur_liste)
    # Mélanger la liste des couleurs disponibles
    shuffle(couleur_liste)
    # Ajouter les boutons à la liste temporaire
    for i in range(nombre_total_boutons):
        couleur_choisie = couleur_liste[i]
        boutons_a_placer.append((couleur_choisie, 660, 140 + i * 25))
    # Placer tous les boutons à la fin
    for bouton, x, y in boutons_a_placer:
        bouton.place(x=x, y=y, anchor="e")
# le niveau du jeu + son affichage
def changer_niveau():
    global niveau, niveaujeu
    niveau += 1
    niveaujeu += 1
    if niveau == 4:
        niveau = 1
        niveaujeu = 2
    elif niveau == 3:
        niveaujeu = 1
    Niveau.config(text=niveaujeu)
# changer de niveau
def nouvelle_partie():
    global niveau, niveaujeu, nombre_d_essaie, essaie_inter
    # etablire des variables
    nombre_d_essaie = 0
    essaie_inter = 0
    # placer le canevas + changer la couleur de fenetre
    canevas.place(x=15, y=75)
    fenetre.config(bg="#E4D6FF")
    # placer tout les boutons + affichage
    choisir_couleur_aleatoire()
    commencer_a_jouer.config(text="Nouvelle Partie", bg="white", activebackground="white", font=('Comic Sans MS', 10, 'bold'))
    commencer_a_jouer.place(x=675, y=50, anchor="e")
    nom_du_jeu.config(bg="white", font=('Comic Sans MS', 14, 'bold'))
    nom_du_jeu.place(x=300, y=25, anchor="c")
    valider.place(x=650, y=100, anchor="e")
    Phrase_niveau.config(text="Difficulté :\n" + str(niveaujeu), font=('Comic Sans MS', 8, 'bold'))
    Phrase_niveau.place(x=660, y=600, anchor="e")
    Score.config(text="nombre d essaie: " + str(nombre_d_essaie))
    Score.place(x=300, y=660, anchor="c")
    # enlever l affichage de victoire
    Niveau.place_forget()
    victoire.place_forget()
    changer_niveau()  # changer de niveau
    # enlever tout le canvas(texte + couleur)
    for carre in carre_tout:
        canevas.delete(carre)
    for texte in texteblanc + textenoir + texterouge + texterouge_foncer + texterouge_clair + textenoir_gris + textegris_foncer + textegris + textegris_clair + textejaune:
        canevas.delete(texte)
    # remettre tout a 0 + choisie le terrain de jeu
    new_comteur()
    if niveau == 1:
        terrain_de_jeu_niveau1()
    elif niveau == 2:
        terrain_de_jeu_niveau2()
    elif niveau == 3:
        terrain_de_jeu_niveau3()
# cree un cadrillage
def terrain_de_jeu_niveau1():  # niveau 1
    for x in range(30):  # cree axe x
        for y in range(30):  # cree axe y
            # pour faire apparetre les carres
            c = canevas.create_rectangle(20 + 17 * x, 20 + 17 * y, 20 + 17 * x + 18, 20 + 17 * y + 18, fill="White")
            # condition pour cree les different nombre sur les carres
            if ((0 < x < 3 or 26 < x < 29) and (y == 3) or (0 < x < 5 or 24 < x < 29) and (y == 4) or
                    (0 < x < 4 or 4 < x < 6 or 23 < x < 25 or 25 < x < 29) and (y == 5) or
                    (0 < x < 4 or 5 < x < 8 or 21 < x < 24 or 25 < x < 29) and (y == 6) or
                    (1 < x < 4 or 7 < x < 9 or 20 < x < 22 or 25 < x < 28) and (y == 7) or
                    (1 < x < 4 or 8 < x < 11 or (12 < x < 17) or 18 < x < 21 or 25 < x < 28) and (y == 8) or
                    (2 < x < 4 or 10 < x < 13 or 16 < x < 19 or 25 < x < 27) and (y == 9) or
                    (2 < x < 4 or 25 < x < 27) and (y == 10) or (3 < x < 5 or 24 < x < 26) and (y == 11) or
                    (4 < x < 6 or (6 < x < 8) or (21 < x < 23) or 23 < x < 25) and (y == 12) or
                    (5 < x < 7 or 22 < x < 24) and (y == 13 or y == 14) or
                    (4 < x < 6 or (8 < x < 11) or (18 < x < 21) or 23 < x < 25) and (y == 15) or
                    (4 < x < 6 or (7 < x < 9) or (9 < x < 12) or (17 < x < 20) or (20 < x < 22) or 23 < x < 25) and (y == 16) or
                    (4 < x < 6 or (7 < x < 12) or (17 < x < 22) or 23 < x < 25) and (y == 17) or
                    (4 < x < 6 or (8 < x < 11) or (13 < x < 16) or (18 < x < 21) or 23 < x < 25) and (y == 18) or
                    (3 < x < 5 or 24 < x < 26) and (y == 19) or
                    (3 < x < 5 or (11 < x < 13) or (13 < x < 16) or (16 < x < 18) or 24 < x < 26) and (y == 20) or
                    (3 < x < 5 or (12 < x < 17) or 24 < x < 26) and (y == 21) or
                    (4 < x < 6 or (12 < x < 14) or (15 < x < 17) or 23 < x < 25) and (y == 22) or
                    (5 < x < 7 or (12 < x < 14) or (15 < x < 17) or 22 < x < 24) and (y == 23) or
                    (6 < x < 9 or (13 < x < 16) or 20 < x < 23) and (y == 24) or
                    (8 < x < 12 or 17 < x < 21) and (y == 25) or (11 < x < 18) and (y == 26)):
                nombre = "1"  # = noir
                carrenoir.append(c)
                texte = canevas.create_text(20 + 10 + 17 * x, 20 + 10 + 17 * y, text=nombre)
                textenoir.append(texte)
            elif ((3 < x < 6 or 24 < x < 27) and (y == 5) or (3 < x < 7 or 23 < x < 27) and (y == 6) or
                  (3 < x < 8 or 21 < x < 27) and (y == 7) or (3 < x < 9 or 20 < x < 27) and (y == 8) or
                  (3 < x < 11 or (12 < x < 17) or 18 < x < 27) and (y == 9) or (3 < x < 27) and (y == 10) or
                  (4 < x < 26) and (y == 11) or (5 < x < 7 or (7 < x < 22) or 22 < x < 24) and (y == 12) or
                  (6 < x < 23) and (y == 13 or y == 14) or (5 < x < 9 or (10 < x < 19) or 20 < x < 24) and (y == 15) or
                  (5 < x < 8 or (11 < x < 18) or 21 < x < 24) and (y == 16 or y == 17) or
                  (5 < x < 9 or (10 < x < 14) or (15 < x < 19) or 20 < x < 24) and (y == 18) or
                  (4 < x < 7 or (8 < x < 21) or 22 < x < 25) and (y == 19) or
                  (4 < x < 6 or (9 < x < 12) or (12 < x < 14) or (15 < x < 17) or (17 < x < 20) or 23 < x < 25) and (y == 20) or
                  (4 < x < 6 or (9 < x < 13) or (16 < x < 20) or 23 < x < 25) and (y == 21) or
                  (5 < x < 7 or (8 < x < 13) or (16 < x < 21) or 22 < x < 24) and (y == 22) or
                  (5 < x < 13 or 16 < x < 24) and (y == 23) or (7 < x < 14 or 15 < x < 22) and (y == 24) or
                  (11 < x < 18) and (y == 25)):
                nombre = "2"  # = jaune
                carrejaune.append(c)
                texte = canevas.create_text(20 + 10 + 17 * x, 20 + 10 + 17 * y, text=nombre)
                textejaune.append(texte)
            elif ((6 < x < 9 or 20 < x < 23) and (y == 19 or y == 22) or (5 < x < 10 or 19 < x < 24) and (
                    y == 20 or y == 21) or
                  (13 < x < 16) and (y == 22 or y == 23)):
                nombre = "3"  # = rouge
                carrerouge.append(c)
                texte = canevas.create_text(20 + 10 + 17 * x, 20 + 10 + 17 * y, text=nombre)
                texterouge.append(texte)
            else:
                nombre = "0"  # = blanc
                carreblanc.append(c)
                texte = canevas.create_text(20 + 10 + 17 * x, 20 + 10 + 17 * y, text=nombre)
                texteblanc.append(texte)
            carre_tout.append(c)
def terrain_de_jeu_niveau2():
    for x in range(20):
        for y in range(20):
            c = canevas.create_rectangle(25 + 25 * x, 25 + 25 * y, 25 + 25 * x + 25, 25 + 25 * y + 25, fill="White")
            if ((6 < x < 13) and (y == 1 or y == 18) or (4 < x < 7 or 12 < x < 15) and (y == 2 or y == 17) or
                    (3 < x < 5 or 14 < x < 16) and (y == 3 or y == 16) or (2 < x < 4 or 15 < x < 17) and (y == 4 or y == 15) or
                    (4 < y < 7 or 12 < y < 15) and (x == 2 or x == 17) or (6 < y < 13) and (x == 1 or x == 18)):
                nombre = "1"
                carrenoir.append(c)
                texte = canevas.create_text(25 + 12.5 + 25 * x, 25 + 12.5 + 25 * y, text=nombre)
                textenoir.append(texte)
            elif ((6 < x < 13) and (y == 2) or (4 < x < 14) and (y == 3) or (3 < x < 5 or 6 < x < 15) and (y == 4) or
                  (2 < x < 4 or 7 < x < 15) and (y == 5 or y == 6) or (1 < x < 5 or 6 < x < 15) and (y == 7) or
                  (1 < x < 14) and (y == 8 or y == 9) or (2 < x < 13) and (y == 10) or (3 < x < 6 or 8 < x < 11) and (y == 11)):
                nombre = "2"
                carrerouge.append(c)
                texte = canevas.create_text(25 + 12.5 + 25 * x, 25 + 12.5 + 25 * y, text=nombre)
                texterouge.append(texte)
            elif ((13 < x < 15) and (y == 3) or (14 < x < 16) and (y == 4) or (14 < x < 17) and (y == 5 or y == 6) or
                  (13 < x < 18) and (y == 7) or (12 < x < 18) and (y == 8 or y == 9) or (1 < x < 3 or 11 < x < 18) and (y == 10) or
                  (2 < x < 4 or 10 < x < 17) and (y == 11) or (9 < x < 14) and (y == 12)):
                nombre = "3"
                carrerouge_foncer.append(c)
                texte = canevas.create_text(25 + 12.5 + 25 * x, 25 + 12.5 + 25 * y, text=nombre)
                texterouge_foncer.append(texte)
            elif (4 < x < 7) and (y == 4 or y == 7) or (3 < x < 5 or 6 < x < 8) and (y == 5 or y == 6):
                nombre = "4"
                carrerouge_clair.append(c)
                texte = canevas.create_text(25 + 12.5 + 25 * x, 25 + 12.5 + 25 * y, text=nombre)
                texterouge_clair.append(texte)
            elif ((1 < x < 3 or 5 < x < 9 or 16 < x < 18) and (y == 11) or (1 < x < 6 or 8 < x < 10 or 13 < x < 18) and (y == 12) or
                  (3 < x < 6 or 8 < x < 16) and (y == 13) or (8 < x < 14) and (y == 14)):
                nombre = "5"
                carrenoir_gris.append(c)
                texte = canevas.create_text(25 + 12.5 + 25 * x, 25 + 12.5 + 25 * y, text=nombre)
                textenoir_gris.append(texte)
            elif (2 < x < 4 or 9 < x < 17) and (y == 13) or (4 < x < 6 or 13 < x < 15) and (y == 14) or (5 < x < 9) and (y == 15):
                nombre = "6"
                carregris_foncer.append(c)
                texte = canevas.create_text(25 + 12.5 + 25 * x, 25 + 12.5 + 25 * y, text=nombre)
                textegris_foncer.append(texte)
            elif ((5 < x < 7 or 7 < x < 9) and (y == 12 or y == 14) or (15 < x < 17) and (y == 14) or (14 < x < 16) and (y == 15) or
                  (4 < x < 6 or 12 < x < 15) and (y == 16) or (6 < x < 13) and (y == 17)):
                nombre = "7"
                carregris.append(c)
                texte = canevas.create_text(25 + 12.5 + 25 * x, 25 + 12.5 + 25 * y, text=nombre)
                textegris.append(texte)
            elif (2 < x < 4 or 14 < x < 16) and (y == 14) or (3 < x < 5 or 8 < x < 15) and (y == 15) or (5 < x < 13) and (y == 16):
                nombre = "8"
                carregris_clair.append(c)
                texte = canevas.create_text(25 + 12.5 + 25 * x, 25 + 12.5 + 25 * y, text=nombre)
                textegris_clair.append(texte)
            else:
                nombre = "0"
                carreblanc.append(c)
                texte = canevas.create_text(25 + 12.5 + 25 * x, 25 + 12.5 + 25 * y, text=nombre)
                texteblanc.append(texte)
            carre_tout.append(c)
def terrain_de_jeu_niveau3():
    for x in range(29):
        for y in range(29):
            c = canevas.create_rectangle(30 + 17 * x, 30 + 17 * y, 30 + 17 * x + 18, 30 + 17 * y + 18, fill="White")
            if ((3 < x < 7 or 10 < x < 12) and (y == 0) or (3 < x < 7 or (7 < x < 9) or 9 < x < 11) and (y == 1) or
                    (4 < x < 7 or 7 < x < 9) and (y == 2) or (8 < x < 10) and (y == 3) or (9 < x < 11) and (y == 4) or
                    (25 < x < 27) and (y == 9) or (23 < x < 26) and (y == 10) or (23 < x < 25 or 27 < x < 29) and (y == 11) or
                    (22 < x < 25 or 25 < x < 29) and (y == 12) or (22 < x < 24 or (24 < x < 26) or 26 < x < 28) and (y == 13) or
                    (22 < x < 24 or (25 < x < 27) or 27 < x < 29) and (y == 14) or (21 < x < 23 or 26 < x < 28) and (y == 15) or
                    (22 < x < 24 or 27 < x < 29) and (y == 16) or (22 < x < 25 or 27 < x < 29) and (y == 17) or (26 < x < 28) and (y == 18)):
                nombre = "1"
                carrerouge.append(c)
                texte = canevas.create_text(30 + 10 + 17 * x, 30 + 10 + 17 * y, text=nombre)
                texterouge.append(texte)
            elif ((6 < x < 11) and (y == 0) or (6 < x < 8 or 8 < x < 10) and (y == 1) or (8 < x < 11) and (y == 2) or
                  (24 < x < 26) and (y == 11) or (23 < x < 25 or 25 < x < 27) and (y == 13) or (23 < x < 26) and (y == 14) or
                  (22 < x < 27) and (y == 15) or (24 < x < 27) and (y == 16) or (25 < x < 28) and (y == 17)):
                nombre = "2"
                carrejaune.append(c)
                texte = canevas.create_text(30 + 10 + 17 * x, 30 + 10 + 17 * y, text=nombre)
                textejaune.append(texte)
            elif ((12 < x < 16) and (y == 1) or (11 < x < 13 or 15 < x < 17) and (y == 2) or (15 < x < 17) and (y == 3) or
                  (11 < x < 13 or 16 < x < 18) and (y == 4) or (12 < x < 14 or 16 < x < 19) and (y == 5) or (17 < x < 19) and (y == 6) or
                  (10 < x < 12 or 18 < x < 20) and (y == 7) or (9 < x < 11 or (11 < x < 15) or (16 < x < 18) or 18 < x < 20) and (y == 8) or
                  (10 < x < 12 or (15 < x < 18) or 19 < x < 21) and (y == 9) or (11 < x < 15 or (15 < x < 17) or 17 < x < 21) and (y == 10) or
                  (11 < x < 13 or 15 < x < 17) and (10 < y < 14) or (2 < x < 4 or (4 < x < 6) or (10 < x < 12) or 15 < x < 17) and (y == 14) or
                  (5 < x < 7 or (9 < x < 11) or 16 < x < 18) and (y == 15) or
                  (2 < x < 4 or (5 < x < 7) or (8 < x < 10) or (16 < x < 18) or 21 < x < 23) and (y == 16) or
                  (3 < x < 5 or (6 < x < 9) or (17 < x < 19) or 19 < x < 21) and (y == 17) or
                  (4 < x < 6 or (8 < x < 10) or (18 < x < 20) or (x == 22 or x == 24 or x == 26)) and (y == 18) or
                  (3 < x < 9 or x == 17 or x == 21 or x == 24 or x == 26) and (y == 19) or
                  (1 < x < 4 or (7 < x < 9) or (17 < x < 21) or x == 23 or x == 26) and (y == 20) or
                  (0 < x < 2 or (5 < x < 9) or (17 < x < 19) or (20 < x < 23) or x == 25) and (y == 21) or
                  (0 < x < 2 or (4 < x < 6) or (7 < x < 9) or x == 19 or x == 24) and (y == 22) or
                  (0 < x < 2 or (3 < x < 5) or (7 < x < 9) or x == 20 or x == 23) and (y == 23) or
                  (0 < x < 2 or (3 < x < 5) or (8 < x < 10) or 20 < x < 23) and (y == 24) or
                  (0 < x < 2 or (4 < x < 6) or x == 10 or x == 16 or x == 21) and (y == 25) or
                  (1 < x < 6 or (x == 9) or (10 < x < 16) or x == 20) and (y == 26) or
                  (1 < x < 3 or (x == 8) or x == 12 or x == 16) and (y == 27) or
                  ((x == 3) or (x == 5) or (6 < x < 12) or x == 17 or x == 19 or x == 21) and (y == 28)):
                nombre = "3"
                carrenoir.append(c)
                texte = canevas.create_text(30 + 10 + 17 * x, 30 + 10 + 17 * y, text=nombre)
                textenoir.append(texte)
            elif ((x == 23) and (y == 1) or (x == 23 or x == 7 or 12 < x < 16) and (y == 2) or
                  (5 < x < 8 or x == 15 or 22 < x < 26) and (y == 3) or
                  (3 < x < 8 or x == 16 or 22 < x < 27) and (y == 4) or
                  (2 < x < 7 or x == 16 or x == 23 or (24 < x < 28)) and (y == 5) or
                  (2 < x < 5 or x == 6 or x == 16 or 21 < x < 24 or x == 27) and (y == 6) or
                  (1 < x < 4 or (5 < x < 8) or 15 < x < 19 or x == 22 or 26 < x < 29) and (y == 7) or
                  (x == 2 or (5 < x < 8) or x == 11 or 14 < x < 17 or x == 18 or 20 < x < 23 or x == 28) and (y == 8) or
                  (0 < x < 3 or (5 < x < 8) or 11 < x < 16 or 17 < x < 20 or 20 < x < 23 or x == 28) and (y == 9) or
                  (x == 1 or (5 < x < 8) or x == 15 or x == 21 or x == 28) and (y == 10) or
                  (-1 < x < 2 or (6 < x < 9) or 12 < x < 16 or 19 < x < 22) and (y == 11) or
                  (x == 0 or (6 < x < 10) or 12 < x < 16 or 18 < x < 21) and (y == 12) or
                  (x == 0 or (7 < x < 11) or 12 < x < 16 or 17 < x < 21 or x == 28) and (y == 13) or
                  (x == 0 or (8 < x < 11) or 11 < x < 16 or 16 < x < 20 or x == 27) and (y == 14) or
                  (x == 0 or x == 4 or x == 9 or 10 < x < 17 or 17 < x < 20 or x == 28) and (y == 15) or
                  (x == 0 or 3 < x < 6 or x == 9 or 9 < x < 17 or 17 < x < 19 or x == 24 or x == 27) and (y == 16) or
                  (x == 0 or 4 < x < 7 or 8 < x < 11 or 14 < x < 18 or x == 21 or x == 25) and (y == 17) or
                  (5 < x < 9 or 15 < x < 19 or 19 < x < 22 or x == 25) and (y == 18) or
                  (x == 16 or 17 < x < 21 or x == 25) and (y == 19) or
                  (3 < x < 8 or x == 17 or 23 < x < 26) and (y == 20) or
                  (1 < x < 6 or x == 17 or 18 < x < 21 or 22 < x < 25) and (y == 21) or
                  (1 < x < 5 or 5 < x < 8 or 16 < x < 19 or 19 < x < 24) and (y == 22) or
                  (1 < x < 4 or 4 < x < 8 or 16 < x < 20 or 20 < x < 23) and (y == 23) or
                  (x == 3 or 4 < x < 9 or 16 < x < 21) and (y == 24) or
                  (5 < x < 10 or 16 < x < 21) and (y == 25) or
                  (5 < x < 9 or 15 < x < 20) and (y == 26) or
                  (3 < x < 8 or 16 < x < 21) and (y == 27)):
                nombre = "4"
                carreorange.append(c)
                texte = canevas.create_text(30 + 10 + 17 * x, 30 + 10 + 17 * y, text=nombre)
                texteorange.append(texte)
            elif ((x == 24 and (y == 5) or
                  ((x == 5 or 23 < x < 27) and (y == 6)) or ((3 < x < 6 or 21 < x < 25 or x == 26) and (y == 7)) or
                  ((2 < x < 6 or 21 < x < 25 or x == 27) and (y == 8)) or ((2 < x < 6 or 21 < x < 25) or x == 27) and (y == 9)) or
                  ((x == 2 or 3 < x < 6 or 20 < x < 24 or x == 27) and (y == 10)) or
                  (3 < x < 7 or x == 22 or x == 27) and (y == 11) or
                  (x == 4 or x == 6 or x == 21 or x == 25) and (y == 12) or
                  (5 < x < 8 or x == 21) and (y == 13) or (6 < x < 9 or x == 20) and (y == 14) or
                  (x == 8 or x == 20) and (y == 15) or (x == 8 or x == 19) and (y == 16) or (x == 19) and (y == 17) or
                  (x == 23 or x == 28) and (y == 18) or (x == 22 or x == 28) and (y == 19) or (x == 21) and (y == 20)):
                nombre = "5"
                carrebleu.append(c)
                texte = canevas.create_text(30 + 10 + 17 * x, 30 + 10 + 17 * y, text=nombre)
                textebleu.append(texte)
            elif ((x == 25 and (y == 7 or y == 9)) or (24 < x < 27 and y == 8) or (x == 3 or x == 26) and (y == 10) or
                  (1 < x < 4 or x == 23 or x == 26) and (y == 11) or (0 < x < 4 or x == 5 or x == 22) and (y == 12) or
                  (0 < x < 6 or x == 22) and (y == 13) or (0 < x < 3 or x == 6 or 20 < x < 23) and (y == 14) or
                  (x == 1 or x == 7 or x == 21) and (y == 15) or (x == 7) and (y == 16)):
                nombre = "6"
                carrebleu_claire.append(c)
                texte = canevas.create_text(30 + 10 + 17 * x, 30 + 10 + 17 * y, text=nombre)
                textebleu_claire.append(texte)
            elif (10 < x < 14 and y == 6) or (12 < x < 15 and y == 7):
                nombre = "7"
                carregris_clair.append(c)
                texte = canevas.create_text(30 + 10 + 17 * x, 30 + 10 + 17 * y, text=nombre)
                textegris_clair.append(texte)
            elif x == 12 and y == 7:
                nombre = "8"
                carreviolet.append(c)
                texte = canevas.create_text(30 + 10 + 17 * x, 30 + 10 + 17 * y, text=nombre)
                texteviolet.append(texte)
            elif ((((10 < x < 15 and y == 17) or (9 < x < 16 and y == 18) or (8 < x < 16 and y == 19) or
                    (8 < x < 17 and 19 < y < 24) or (x == 2 or 9 < x < 17) and y == 24) or
                   (1 < x < 5 or 9 < x < 16) and y == 25) or x == 10 and y == 26 or 8 < x < 12 and y == 27):
                nombre = "9"
                carrebeige.append(c)
                texte = canevas.create_text(30 + 10 + 17 * x, 30 + 10 + 17 * y, text=nombre)
                textebeige.append(texte)
            elif (x == 13 and y == 3) or (12 < x < 16 and y == 4) or (13 < x < 16 and 4 < y < 7) or (x == 15 and y == 7):
                nombre = "10"
                carrerouge_foncer.append(c)
                texte = canevas.create_text(30 + 10 + 17 * x, 30 + 10 + 17 * y, text=nombre)
                texterouge_foncer.append(texte)
            else:
                nombre = "0"
                carreblanc.append(c)
                texte = canevas.create_text(30 + 10 + 17 * x, 30 + 10 + 17 * y, text=nombre)
                texteblanc.append(texte)
            carre_tout.append(c)
# mettre tout a 0
def new_comteur():
    global comteur_blanc, comteur_noir, comteur_rouge, comteur_rouge_foncer, comteur_rouge_clair, comteur_noir_gris, comteur_gris_foncer, comteur_gris, comteur_gris_clair, comteur_marron, comteur_orange, comteur_jaune, comteur_jaune_foncer, comteur_bleu_claire, comteur_bleu, comteur_beige, comteur_violet
    comteur_blanc = [-1]
    comteur_noir = [-1]
    comteur_rouge = [-1]
    comteur_rouge_foncer = [-1]
    comteur_rouge_clair = [-1]
    comteur_noir_gris = [-1]
    comteur_gris_foncer = [-1]
    comteur_gris = [-1]
    comteur_gris_clair = [-1]
    comteur_marron = [-1]
    comteur_orange = [-1]
    comteur_jaune = [-1]
    comteur_jaune_foncer = [-1]
    comteur_bleu_claire = [-1]
    comteur_bleu = [-1]
    comteur_beige = [-1]
    comteur_violet = [-1]
    blanc.config(text="")
    noir.config(text="")
    rouge.config(text="")
    rouge_foncer.config(text="")
    rouge_clair.config(text="")
    noir_gris.config(text="")
    gris_foncer.config(text="")
    gris.config(text="")
    gris_clair.config(text="")
    marron.config(text="")
    orange.config(text="")
    jaune.config(text="")
    jaune_foncer.config(text="")
    bleu_claire.config(text="")
    bleu.config(text="")
    beige.config(text="")
    violet.config(text="")
# enlever les boutons lorsque ils sont correcte
def c_est_pour_la_couleur(couleur):
    couleur.place_forget()
    couleur.config(text="")
# Verification
def validation():
    global nombre_d_essaie, essaie_inter, compteurvictoireb, compteurvictoiren, compteurvictoirej, compteurvictoirer, compteurvictoirerf, compteurvictoirefc, compteurvictoireng, compteurvictoiregf, compteurvictoireg, compteurvictoiregc, compteurvictoireo, compteurvictoirebl, compteurvictoirebc, compteurvictoirev, compteurvictoirebe
    # mettre a 0 les variable
    compteurvictoireb, compteurvictoiren, compteurvictoirej, compteurvictoirer, compteurvictoirerf, compteurvictoirerc, compteurvictoireng, compteurvictoiregf, compteurvictoireg, compteurvictoiregc, compteurvictoireo, compteurvictoirebl, compteurvictoirebc, compteurvictoirev, compteurvictoirebe = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    # augmente le nombre de coup
    nombre_d_essaie = nombre_d_essaie + 1
    Score.config(text="nombre d essaie: " + str(nombre_d_essaie))
    if niveau == 1:
        if comteur_blanc == [0]:  # si le nombre et a 0 pendant le niveau alors:
            for carre in carreblanc:  # on met les carre en blanc
                canevas.itemconfig(carre, outline="white")
            for texte in texteblanc:  # on enleve les 0 sur les carres
                canevas.itemconfig(texte, text="")
            c_est_pour_la_couleur(blanc)  # enlever le bouton blanc
            compteurvictoireb = 1  # mettre a 1 pour vour si on a eu bon
        if comteur_noir == [1]:  # la meme que pour le comteur_blanc
            for carre in carrenoir:
                canevas.itemconfig(carre, outline="white", fill="black")
            for texte in textenoir:
                canevas.itemconfig(texte, text="")
            c_est_pour_la_couleur(noir)
            compteurvictoiren = 1
        if comteur_jaune == [2]:
            for carre in carrejaune:
                canevas.itemconfig(carre, outline="white", fill="yellow")
            for texte in textejaune:
                canevas.itemconfig(texte, text="")
            c_est_pour_la_couleur(jaune)
            compteurvictoirej = 1
        if comteur_rouge == [3]:
            for carre in carrerouge:
                canevas.itemconfig(carre, outline="white", fill="red")
            for text in texterouge:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(rouge)
            compteurvictoirer = 1
        # si tu a tout bon pour le niveau 1
        if compteurvictoireb == 1 and compteurvictoiren == 1 and compteurvictoirej == 1 and compteurvictoirer == 1:
            victoire.config(text="VICTOIRE en\n" + str(nombre_d_essaie) + " essaie")  # afficher la victoire avec le nombre de coup
            victoire.place(x=300, y=650, anchor="c")
            Score.place_forget()  # enlever le score
    # pareil pour le niveau 2 et 3
    elif niveau == 2:
        if comteur_blanc == [0]:
            for carre in carreblanc:
                canevas.itemconfig(carre, outline="white")
            for texte in texteblanc:
                canevas.itemconfig(texte, text="")
            c_est_pour_la_couleur(blanc)
            compteurvictoireb = 1
        if comteur_noir == [1]:
            for carre in carrenoir:
                canevas.itemconfig(carre, outline="white", fill="black")
            for texte in textenoir:
                canevas.itemconfig(texte, text="")
            c_est_pour_la_couleur(noir)
            compteurvictoiren = 1
        if comteur_rouge == [2]:
            for carre in carrerouge:
                canevas.itemconfig(carre, outline="white", fill="red")
            for text in texterouge:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(rouge)
            compteurvictoirer = 1
        if comteur_rouge_foncer == [3]:
            for carre in carrerouge_foncer:
                canevas.itemconfig(carre, outline="white", fill="#962D1F")
            for text in texterouge_foncer:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(rouge_foncer)
            compteurvictoirerf = 1
        if comteur_rouge_clair == [4]:
            for carre in carrerouge_clair:
                canevas.itemconfig(carre, outline="white", fill="#F78D8D")
            for text in texterouge_clair:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(rouge_clair)
            compteurvictoirerc = 1
        if comteur_noir_gris == [5]:
            for carre in carrenoir_gris:
                canevas.itemconfig(carre, outline="white", fill="#464F4F")
            for text in textenoir_gris:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(noir_gris)
            compteurvictoireng = 1
        if comteur_gris_foncer == [6]:
            for carre in carregris_foncer:
                canevas.itemconfig(carre, outline="white", fill="#77777F")
            for text in textegris_foncer:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(gris_foncer)
            compteurvictoiregf = 1
        if comteur_gris == [7]:
            for carre in carregris:
                canevas.itemconfig(carre, outline="white", fill="#9F9FBF")
            for text in textegris:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(gris)
            compteurvictoireg = 1
        if comteur_gris_clair == [8]:
            for carre in carregris_clair:
                canevas.itemconfig(carre, outline="white", fill="#D9C9F1")
            for text in textegris_clair:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(gris_clair)
            compteurvictoiregc = 1
        if compteurvictoireb == 1 and compteurvictoiren == 1 and compteurvictoirer == 1 and compteurvictoirerc == 1 and compteurvictoireng == 1 and compteurvictoiregf == 1 and compteurvictoireg == 1 and compteurvictoiregc == 1:
            victoire.config(text="VICTOIRE en\n" + str(nombre_d_essaie) + " essaie")
            victoire.place(x=300, y=650, anchor="c")
            Score.place_forget()
    elif niveau == 3:
        if comteur_blanc == [0]:
            for carre in carreblanc:
                canevas.itemconfig(carre, outline="white")
            for texte in texteblanc:
                canevas.itemconfig(texte, text="")
            c_est_pour_la_couleur(blanc)
            compteurvictoireb = 1
        if comteur_rouge == [1]:
            for carre in carrerouge:
                canevas.itemconfig(carre, outline="white", fill="red")
            for text in texterouge:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(rouge)
            compteurvictoirer = 1
        if comteur_jaune == [2]:
            for carre in carrejaune:
                canevas.itemconfig(carre, outline="white", fill="yellow")
            for text in textejaune:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(jaune)
            compteurvictoirej = 1
        if comteur_noir == [3]:
            for carre in carrenoir:
                canevas.itemconfig(carre, outline="white", fill="black")
            for texte in textenoir:
                canevas.itemconfig(texte, text="")
            c_est_pour_la_couleur(noir)
            compteurvictoiren = 1
        if comteur_orange == [4]:
            for carre in carreorange:
                canevas.itemconfig(carre, outline="white", fill="#FF8F2C")
            for text in texteorange:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(orange)
            compteurvictoireo = 1
        if comteur_bleu == [5]:
            for carre in carrebleu:
                canevas.itemconfig(carre, outline="white", fill="#3C58FA")
            for text in textebleu:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(bleu)
            compteurvictoirebl = 1
        if comteur_bleu_claire == [6]:
            for carre in carrebleu_claire:
                canevas.itemconfig(carre, outline="white", fill="#4FB9FD")
            for text in textebleu_claire:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(bleu_claire)
            compteurvictoirebc = 1
        if comteur_gris_clair == [7]:
            for carre in carregris_clair:
                canevas.itemconfig(carre, outline="white", fill="#D9C9F1")
            for text in textegris_clair:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(gris_clair)
            compteurvictoiregc = 1
        if comteur_violet == [8]:
            for carre in carreviolet:
                canevas.itemconfig(carre, outline="white", fill="#B05CCF")
            for text in texteviolet:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(violet)
            compteurvictoirev = 1
        if comteur_beige == [9]:
            for carre in carrebeige:
                canevas.itemconfig(carre, outline="white", fill="#F0E691")
            for text in textebeige:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(beige)
            compteurvictoirebe = 1
        if comteur_rouge_foncer == [10]:
            for carre in carrerouge_foncer:
                canevas.itemconfig(carre, outline="white", fill="#962D1F")
            for text in texterouge_foncer:
                canevas.itemconfig(text, text="")
            c_est_pour_la_couleur(rouge_foncer)
            compteurvictoirerf = 1
        if compteurvictoireb == 1 and compteurvictoiren == 1 and compteurvictoirer == 1 and compteurvictoirerf == 1 and compteurvictoirej == 1 and compteurvictoireo == 1 and compteurvictoirebl == 1 and compteurvictoirebc == 1 and compteurvictoiregc == 1 and compteurvictoirev == 1 and compteurvictoirebe == 1:
            victoire.config(text="VICTOIRE en\n" + str(nombre_d_essaie) + " essaie")
            victoire.place(x=300, y=650, anchor="c")
            Score.place_forget()
# nombre de fois ou on peux cliquer sur un bouton avant qu il revient a "" en fonction du niveau
def cliquer(compteur, label):
    global x
    if niveau == 1:
        x = 4
    elif niveau == 2:
        x = 9
    elif niveau == 3:
        x = 11
    compteur[0] += 1
    if compteur[0] == x:
        compteur[0] = 0
        label.config(text="")
    else:
        label.config(text=compteur[0])
# tout les bouton avec leur nombre de click
def blanc_cliquer():
    cliquer(comteur_blanc, blanc)
def noir_cliquer():
    cliquer(comteur_noir, noir)
def rouge_cliquer():
    cliquer(comteur_rouge, rouge)
def rouge_foncer_cliquer():
    cliquer(comteur_rouge_foncer, rouge_foncer)
def rouge_clair_cliquer():
    global comteur_rouge_clair
    cliquer(comteur_rouge_clair, rouge_clair)
def noir_gris_cliquer():
    cliquer(comteur_noir_gris, noir_gris)
def gris_foncer_cliquer():
    cliquer(comteur_gris_foncer, gris_foncer)
def gris_cliquer():
    cliquer(comteur_gris, gris)
def gris_clair_cliquer():
    cliquer(comteur_gris_clair, gris_clair)
def marron_cliquer():
    cliquer(comteur_marron, marron)
def orange_cliquer():
    cliquer(comteur_orange, orange)
def jaune_cliquer():
    cliquer(comteur_jaune, jaune)
def jaune_foncer_cliquer():
    cliquer(comteur_jaune_foncer, jaune_foncer)
def bleu_claire_cliquer():
    cliquer(comteur_bleu_claire, bleu_claire)
def bleu_cliquer():
    cliquer(comteur_bleu, bleu)
def beige_cliquer():
    cliquer(comteur_beige, beige)
def violet_cliquer():
    cliquer(comteur_violet, violet)
# cree les differtents textes
nom_du_jeu = Label(fenetre, text="Pixelmon", bg="#BC1DE6", fg="black", font=('Comic Sans MS', 35, 'bold', 'underline'))
nom_du_jeu.place(x=350, y=100, anchor="c")
commencer_a_jouer = Button(fenetre, text="Commencer\nA\nJouer", bg="cyan", fg="black", activebackground="cyan", font=('Comic Sans MS', 40, 'bold'), command=nouvelle_partie)
commencer_a_jouer.place(x=350, y=350, anchor="c")
valider = Button(fenetre, text="valider", bg="white", fg="black", font=('Comic Sans MS', 9, 'bold'), command=validation)
Phrase_niveau = Label(fenetre, text="Choisie le niveuau de difficulter :", bg="cyan", fg="black", font=('Comic Sans MS', 15, 'bold'))
Phrase_niveau.place(x=350, y=525, anchor="c")
Niveau = Button(fenetre, text=niveaujeu, bg="cyan", fg="black", font=('Comic Sans MS', 15, 'bold'), command=changer_niveau)
Niveau.place(x=350, y=600, anchor="c")
Score = Label(fenetre)
victoire = Label(fenetre, text="VICTOIRE en", bg="white", fg="black", font=('Comic Sans MS', 25, 'bold'))
# tout les bouton de couleur  ( 2 pikachu(3) ; 1 pokeball (8) ; 3 dracaufeu (10) )
blanc = Button(fenetre, text="", width=15, height=2, bg="#FFFFFF", activebackground="#FFFFFF", font=('', 5, ''), command=blanc_cliquer)
noir = Button(fenetre, text="", width=15, height=2, bg="#000000", fg="white", activebackground="#000000", font=('', 5, ''), command=noir_cliquer)
rouge = Button(fenetre, width=15, height=2, bg="#F83526", activebackground="#F83526", font=('', 5, ''), command=rouge_cliquer)
rouge_clair = Button(fenetre, width=15, height=2, bg="#F78D8D", activebackground="#F78D8D", font=('', 5, ''), command=rouge_clair_cliquer)
rouge_foncer = Button(fenetre, text="", width=15, height=2, bg="#962D1F", activebackground="#962D1F", font=('', 5, ''), command=rouge_foncer_cliquer)
noir_gris = Button(fenetre, text="", width=15, height=2, bg="#464F4F", fg="white", activebackground="#464F4F", font=('', 5, ''), command=noir_gris_cliquer)
gris_foncer = Button(fenetre, width=15, height=2, bg="#77777F", activebackground="#77777F", font=('', 5, ''), command=gris_foncer_cliquer)
gris = Button(fenetre, width=15, height=2, bg="#9F9FBF", activebackground="#9F9FBF", font=('', 5, ''), command=gris_cliquer)
gris_clair = Button(fenetre, width=15, height=2, bg="#D9C9F1", activebackground="#D9C9F1", font=('', 5, ''), command=gris_clair_cliquer)
marron = Button(fenetre, text="", width=15, height=2, bg="#8A4708", activebackground="#8A4708", font=('', 5, ''), command=marron_cliquer)
orange = Button(fenetre, width=15, height=2, bg="#FF8F2C", activebackground="#FF8F2C", font=('', 5, ''), command=orange_cliquer)
jaune = Button(fenetre, width=15, height=2, bg="#FEFD0B", activebackground="#FEFD0B", font=('', 5, ''), command=jaune_cliquer)
jaune_foncer = Button(fenetre, width=15, height=2, bg="#FCD907", activebackground="#FCD907", font=('', 5, ''), command=jaune_foncer_cliquer)
bleu_claire = Button(fenetre, width=15, height=2, bg="#4FB9FD", activebackground="#4FB9FD", font=('', 5, ''), command=bleu_claire_cliquer)
bleu = Button(fenetre, width=15, height=2, bg="#3C58FA", activebackground="#3C58FA", font=('', 5, ''), command=bleu_cliquer)
beige = Button(fenetre, width=15, height=2, bg="#F0E691", activebackground="#F0E691", font=('', 5, ''), command=beige_cliquer)
violet = Button(fenetre, width=15, height=2, bg="#B05CCF", activebackground="#B05CCF", font=('', 5, ''), command=violet_cliquer)
# liste des couleur/boutton
couleur_liste = [blanc, noir, rouge, rouge_clair, rouge_foncer, noir_gris, gris_foncer, gris, gris_clair,
                 marron, orange, jaune, jaune_foncer, bleu_claire, bleu, beige, violet]
fenetre.mainloop()