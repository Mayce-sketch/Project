# 30/11/2023
from tkinter import *
fenetre = Tk() # Cree la fenetre
fenetre.title("Avatar")
fenetre.config(bg="aqua", width=800, height=600)
placement = Canvas(fenetre, bg="white", width=450, height=500)
placement.place(x=25, y=300, anchor="w")
# Mettre des variables a 0 car elle sont global
compteur_mimique = 0
compteur_mimique_accessoir = 0
compteur_accessoir = 0
test_yeux_mimique3 = 0
# Importation des images pour les boutons
Fichier_fleche_gauche = PhotoImage(file="Les_images/fleche_gauche.png")
Fichier_fleche_droite = PhotoImage(file="Les_images/fleche_droite.png")
Fichier_fleche_haut = PhotoImage(file="Les_images/fleche_haut.png")
Fichier_fleche_bas = PhotoImage(file="Les_images/fleche_bas.png")
Fichier_ecarter = PhotoImage(file="Les_images/Ecarter.png")
Fichier_rapprocher = PhotoImage(file="Les_images/Rapproché.png")
Fichier_Agrandir = PhotoImage(file="Les_images/Agrandir.png")
Fichier_Reduire = PhotoImage(file="Les_images/Réduire.png")
Fichier_Yeux = PhotoImage(file="Les_images/Yeux.png")
Fichier_Bouche = PhotoImage(file="Les_images/Bouche.png")
Fichier_Valider = PhotoImage(file="Les_images/Valider.png")
Fichier_Rien = PhotoImage(file="Les_images/Rien.png")
Fichier_epee = PhotoImage(file="Les_images/Le_pouvoir_de_l_epee.png")
Fichier_bombe = PhotoImage(file="Les_images/Le_pouvoir_de_la_bombe.png")
Fichier_marteau = PhotoImage(file="Les_images/Le_pouvoir_du_marteau.png")
Fichier_sommeil = PhotoImage(file="Les_images/Le_pouvoir_sommeil.png")
Fichier_trancheur = PhotoImage(file="Les_images/Le_pouvoir_du_trancheur.png")
# Le personnage, les elements qui le compose
pied_gauche = placement.create_oval(115, 300, 115 + 125, 300 + 55, fill="red")
pied_droit = placement.create_oval(215, 300, 215 + 125, 300 + 55, fill="red")
bras_gauche = placement.create_oval(90, 200, 90 + 100, 200 + 80, fill="pink", outline="black")
bras_droit = placement.create_oval(265, 200, 265 + 100, 200 + 80, fill="pink", outline="black")
corps = placement.create_oval(125, 150, 125 + 200, 150 + 200, fill="pink", outline="black")
bouche = placement.create_oval(217.5, 275, 217.5 + 15, 275 + 20, fill="dark red", outline="black")
joue_gauche = placement.create_oval(150, 255, 150 + 25, 255 + 20, fill="hot pink", outline="hot pink")
joue_droite = placement.create_oval(275, 255, 275 + 25, 255 + 20, fill="hot pink", outline="hot pink")
oeil_gauche = placement.create_oval(175, 180, 175 + 35, 180 + 70, fill="black", outline="black")
oeil_droit = placement.create_oval(241, 180, 241 + 35, 180 + 70, fill="black", outline="black")
xoeil_gauche, yoeil_gauche = [185, 185] # Je stock les coord des yeux
blanc_dans_oeil_gauche = placement.create_oval(xoeil_gauche, yoeil_gauche, xoeil_gauche + 15, yoeil_gauche + 30, fill="white", outline="black")
xoeil_droite, yoeil_droite = [251, 185] # Je stock les coord des yeux
blanc_dans_oeil_droit = placement.create_oval(xoeil_droite, yoeil_droite, xoeil_droite + 15, yoeil_droite + 30, fill="white", outline="black")
# I. Changer la couleur_corps du kirby
def changer_couleur_kirby(couleur_corps, couleur_pied, couleur_tache):
    placement.itemconfig(pied_gauche, fill=couleur_pied)
    placement.itemconfig(pied_droit, fill=couleur_pied)
    placement.itemconfig(bras_gauche, fill=couleur_corps)
    placement.itemconfig(bras_droit, fill=couleur_corps)
    placement.itemconfig(corps, fill=couleur_corps)
    placement.itemconfig(joue_gauche, fill=couleur_tache, outline=couleur_tache)
    placement.itemconfig(joue_droite, fill=couleur_tache, outline=couleur_tache)
    le_nom_du_perso.config(fg=couleur_corps)
# A. Les differentes couleurs
def changer_couleur_rouge():
    changer_couleur_kirby("red", "dark red", "dark red")
def changer_couleur_jaune():
    changer_couleur_kirby("yellow", "brown", "#FFD700")
def changer_couleur_vert():
    changer_couleur_kirby("light green", "brown", "green")
def changer_couleur_bleu():
    changer_couleur_kirby("cyan", "blue", "#00D7FF")
def changer_couleur_rose():
    changer_couleur_kirby("pink", "red", "hot pink")
# II. Les yeux
# A. Changer la position des yeux
# 1. Les directions
def mimique3_oeil_gauche_droite(): # Pour stock les nouvelles coord les yeux
    global xoeil_gauche, yoeil_gauche, xoeil_droite, yoeil_droite
    xoeil_gauche = placement.coords(blanc_dans_oeil_gauche)[0]
    yoeil_gauche = placement.coords(blanc_dans_oeil_gauche)[1]
    xoeil_droite = placement.coords(blanc_dans_oeil_droit)[0]
    yoeil_droite = placement.coords(blanc_dans_oeil_droit)[1]
def yeux_gauche_changer():
    if test_yeux_mimique3 != 1:
        x1 = placement.coords(blanc_dans_oeil_gauche)[0]
        x2 = placement.coords(blanc_dans_oeil_droit)[0]
        if x1 >= 185 and x2 >= 251:
            placement.move(blanc_dans_oeil_gauche, -5, 0)
            placement.move(blanc_dans_oeil_droit, -5, 0)
            mimique3_oeil_gauche_droite()
def yeux_droit_changer():
    if test_yeux_mimique3 != 1:
        x1 = placement.coords(blanc_dans_oeil_gauche)[0]
        x2 = placement.coords(blanc_dans_oeil_droit)[0]
        if x2 <= 251 and x1 <= 185:
            placement.move(blanc_dans_oeil_gauche, 5, 0)
            placement.move(blanc_dans_oeil_droit, 5, 0)
            mimique3_oeil_gauche_droite()
def yeux_haut_changer():
    if test_yeux_mimique3 != 1:
        y = placement.coords(blanc_dans_oeil_gauche)[1]
        if y >= 185:
            placement.move(blanc_dans_oeil_gauche, 0, -5)
            placement.move(blanc_dans_oeil_droit, 0, -5)
            mimique3_oeil_gauche_droite()
def yeux_bas_changer():
    if test_yeux_mimique3 != 1:
        y = placement.coords(blanc_dans_oeil_gauche)[1]
        if y <= 215:
            placement.move(blanc_dans_oeil_gauche, 0, 5)
            placement.move(blanc_dans_oeil_droit, 0, 5)
            mimique3_oeil_gauche_droite()
# 2. Ecarter/Rapprocher les yeux
def ecarter_yeux():
    if test_yeux_mimique3 != 1:
        x1 = placement.coords(blanc_dans_oeil_gauche)[0]
        x2 = placement.coords(blanc_dans_oeil_droit)[0]
        if x1 >= 185 and x2 <= 251:
            placement.move(blanc_dans_oeil_gauche, -5, 0)
            placement.move(blanc_dans_oeil_droit, 5, 0)
            mimique3_oeil_gauche_droite()
def rapprocher_yeux():
    if test_yeux_mimique3 != 1:
        x1 = placement.coords(blanc_dans_oeil_gauche)[0]
        x2 = placement.coords(blanc_dans_oeil_droit)[0]
        if x1 <= 185 and x2 >= 251:
            placement.move(blanc_dans_oeil_gauche, 5, 0)
            placement.move(blanc_dans_oeil_droit, -5, 0)
            mimique3_oeil_gauche_droite()
# B. La bouche
# 1. Les directions
def bouche_gauche_changer():
    x1, y1, x2, y2 = placement.coords(bouche)
    if x1 >= 202.5:
        placement.move(bouche, -5, 0)
def bouche_droite_changer():
    x1, y1, x2, y2 = placement.coords(bouche)
    if x2 + 5 <= 255:
        placement.move(bouche, 5, 0)
def bouche_haut_changer():
    x1, y1, x2, y2 = placement.coords(bouche)
    if y1 >= 260:
        placement.move(bouche, 0, -5)
def bouche_bas_changer():
    x1, y1, x2, y2 = placement.coords(bouche)
    if y2 + 5 <= 330:
        placement.move(bouche, 0, 5)
# 2. Agrandir/Reduire la bouche
def agrandir():
    x1, y1, x2, y2 = placement.coords(bouche)
    if x1 >= 185 and x2 <= 260 and y1 >= 255 and y2 <= 340:
        placement.coords(bouche, x1 - 5, y1 - 5, x2 + 5, y2 + 5)
def reduire():
    x1, y1, x2, y2 = placement.coords(bouche)
    if x1 <= x2 - 15 and y1 <= y2 - 20:
        placement.coords(bouche, x1 + 5, y1 + 5, x2 - 5, y2 - 5)
# C. Pour intervertire les yeux/bouche
def changer_yeux_bouche():
    chemin_image_actuelle = yeux_bouche.cget("image") # Mettre chemin_image_actuelle a l'image
    if chemin_image_actuelle == str(Fichier_Yeux): # Si l'image est Fichier_Yeux
        yeux_bouche.config(image=Fichier_Bouche)
        les_yeux.config(text="Déplace ta")
        # Changer toute les command pour les bouton de la bouche
        fleche_gauche_element.config(command=bouche_gauche_changer)
        fleche_droit_element.config(command=bouche_droite_changer)
        fleche_haut_element.config(command=bouche_haut_changer)
        fleche_bas_element.config(command=bouche_bas_changer)
        ecarter_les_yeux.config(image=Fichier_Agrandir, command=agrandir)
        raprocher_les_yeux.config(image=Fichier_Reduire, command=reduire)
    elif chemin_image_actuelle == str(Fichier_Bouche): # Si l'image est Fichier_Bouche
        yeux_bouche.config(image=Fichier_Yeux)
        les_yeux.config(text="Déplace tes")
        fleche_gauche_element.config(command=yeux_gauche_changer)
        fleche_droit_element.config(command=yeux_droit_changer)
        fleche_haut_element.config(command=yeux_haut_changer)
        fleche_bas_element.config(command=yeux_bas_changer)
        ecarter_les_yeux.config(image=Fichier_ecarter, command=ecarter_yeux)
        raprocher_les_yeux.config(image=Fichier_rapprocher, command=rapprocher_yeux)
# III. les mimique
# A. Pour definire le sens des mimique
# 1. Tout les mimiques
def mimique_gauche1():
    global bras_gauche
    placement.coords(bras_gauche, 100, 120, 100 + 80, 130 + 100)
def mimique_gauche2():
    global bras_droit
    placement.coords(bras_droit, 260, 120, 260 + 80, 120 + 100)
def mimique_gauche3():
    global oeil_gauche, oeil_droit, test_yeux_mimique3
    test_yeux_mimique3 = 1
    placement.coords(oeil_gauche, 175, 200, 175 + 35, 200 + 0)
    placement.coords(oeil_droit, 241, 200, 241 + 35, 200 + 0)
    placement.coords(blanc_dans_oeil_gauche, 0, 0, 0, 0)
    placement.coords(blanc_dans_oeil_droit, 0, 0, 0, 0)
def mimique_gauche4():
    global joue_gauche, joue_droite
    placement.coords(joue_gauche, 145, 250, 145 + 30, 250 + 35)
    placement.coords(joue_droite, 275, 250, 275 + 30, 250 + 35)
def mimique_droit1():
    global bras_gauche
    placement.coords(bras_gauche, 90, 200, 90 + 100, 200 + 80)
def mimique_droit2():
    global bras_droit
    placement.coords(bras_droit, 265, 200, 265 + 100, 200 + 80)
def mimique_droit3():
    global oeil_gauche, oeil_droit, xoeil_gauche, yoeil_gauche, xoeil_droite, yoeil_droite, test_yeux_mimique3
    test_yeux_mimique3 = 0
    placement.coords(oeil_gauche, 175, 180, 175 + 35, 180 + 70)
    placement.coords(oeil_droit, 241, 180, 241 + 35, 180 + 70)
    placement.coords(blanc_dans_oeil_gauche, xoeil_gauche, yoeil_gauche, xoeil_gauche + 15, yoeil_gauche + 30)
    placement.coords(blanc_dans_oeil_droit, xoeil_droite, yoeil_droite, xoeil_droite + 15, yoeil_droite + 30)
def mimique_droit4():
    global joue_gauche, joue_droite
    placement.coords(joue_gauche, 150, 255, 150 + 25, 255 + 20)
    placement.coords(joue_droite, 275, 255, 275 + 25, 255 + 20)
# 2. Le sens de mimique gauche/droite
def changer_mimique_gauche():
    changer_mimique("gauche")
def changer_mimique_droite():
    changer_mimique("droite")
# B. Pour changer les mimiques
def changer_mimique(direction):
    global compteur_mimique
    mimiques = [(mimique_droit4, mimique_droit1, "Classique"), (mimique_droit2, mimique_gauche1, "Bras gauche"),
                (mimique_droit1, mimique_gauche2, "Bras droit"), (mimique_gauche1, mimique_gauche2, mimique_droit3, "Etonnement"),
                (mimique_droit1, mimique_droit2, mimique_droit4, mimique_gauche3, "Je dort"), (mimique_gauche4, mimique_droit3, "Timide")]
    # Le compteur_mimique augmente ou diminue en fonction de la direction soit : gauche et droite
    if direction == "gauche":
        compteur_mimique = (compteur_mimique + 1) % len(mimiques)
    elif direction == "droite":
        compteur_mimique = (compteur_mimique - 1) % len(mimiques)
    # Récupère les fonctions et le texte associé à la nouvelle valeur de compteur_mimique
    mimique_functions = mimiques[compteur_mimique]
    mimique_functions[0]() # Appelle la première fonction et met à jour le texte
    text_mimique_change.config(text=mimique_functions[-1])
    # Si main et lever et ...
    if compteur_mimique == 1 or compteur_mimique == 3:
        # ...Si un accessoire avec se numéro on change la position de accessoire
        if compteur_mimique_accessoir == 1:
            epee_main_lever()
        elif compteur_mimique_accessoir == 2:
            bombe_main_lever()
        elif compteur_mimique_accessoir == 3:
            marteau_main_lever()
    else: # Sinon on le laisse ou remet en bas
        if compteur_mimique_accessoir == 1:
            epee()
        elif compteur_mimique_accessoir == 2:
            bombe()
        elif compteur_mimique_accessoir == 3:
            marteau()
        # apeller d autre fonction s'il y en a une
    if len(mimique_functions) >= 3:
        mimique_functions[1]()
    if len(mimique_functions) >= 4:
        mimique_functions[2]()
    if len(mimique_functions) >= 5:
        mimique_functions[3]()
# IV. Les accessoirs
# A. Creation des accessoires
def bonnet_de_epee():
    global pointe_vert, boule_jaune, chapeaux_vert, ligne_jaune, epee_manche, epee_lame, epee_garde
    pointe_vert = placement.create_arc(40, -10, 40 + 150, -10 + 220, start=-20, extent=20, fill="light green", outline="black")
    boule_jaune = placement.create_oval(100, 85, 100 + 30, 85 + 30, fill="yellow", outline="black")
    chapeaux_vert = placement.create_arc(160, 90, 160 + 130, 90 + 130, start=0, extent=180, fill="light green", outline="black")
    ligne_jaune = placement.create_rectangle(160, 150, 160 + 130, 150 + 19.5, fill="yellow", outline="black")
    # cree l'epee
    epee_manche = placement.create_rectangle(100, 210, 100 + 15, 210 + 45, fill="blue", outline="black")
    epee_lame = placement.create_arc(32.5, 35, 32.5 + 150, 35 + 170, start=-100, extent=20, fill="silver", outline="black")
    epee_garde = placement.create_rectangle(81.5, 200, 81.5 + 50, 200 + 15, fill="blue", outline="black")
def bonnet_de_bombe():
    global pointe_blue, etoile_jaune, etoile_vert, ligne_blanc, losange_jaune, losange_cyan, bombe_rond, surport_bombe, meche_bombe, etoile_bleu1, etoile_bleu2, etoile_bleu3
    pointe_blue = placement.create_polygon(170, 150, 280, 150, 225, 35, fill="#00008B", outline="black")
    etoile_jaune = placement.create_polygon(75 + 170, 15 + 100, 82 + 170, 35 + 100, 100 + 170, 40 + 100, 84 + 170, 45 + 100, 90 + 170, 60 + 100, 75 + 170, 50 + 100, 60 + 170, 60 + 100, 66 + 170, 45 + 100, 50 + 170, 40 + 100, 68 + 170, 35 + 100, fill="yellow", outline="black")
    etoile_vert = placement.create_polygon(75 + 140, 15 + 45, 82 + 140, 35 + 45, 100 + 140, 40 + 45, 84 + 140, 45 + 45, 90 + 140, 60 + 45, 75 + 140, 50 + 45, 60 + 140, 60 + 45, 66 + 140, 45 + 45, 50 + 150, 40 + 45, 68 + 140, 35 + 45, fill="light green", outline="black")
    ligne_blanc = placement.create_rectangle(160, 150, 160 + 130, 150 + 19.5, fill="white", outline="black")
    losange_jaune = placement.create_polygon(50 + 175, 30 + 110, 70 + 175, 50 + 110, 50 + 175, 70 + 110, 30 + 175, 50 + 110, fill="gold", outline="black")
    losange_cyan = placement.create_polygon(225, 150, 235, 160, 225, 170, 215, 160, fill="cyan", outline="black")
    # cree la bombe
    bombe_rond = placement.create_oval(50, 150, 50 + 100, 150 + 100, fill="#00015B", outline="black")
    surport_bombe = placement.create_rectangle(70, 150, 70 + 60, 150 + 10, fill="#71797E", outline="black")
    meche_bombe = placement.create_rectangle(95, 105, 95 + 10, 105 + 45, fill="#C4A484", outline="black")
    etoile_bleu1 = placement.create_polygon(50 + 20, 10 + 150, 55 + 20, 23 + 150, 67 + 20, 27 + 150, 56 + 20, 30 + 150, 60 + 20, 40 + 150, 50 + 20, 33 + 150, 40 + 20, 40 + 150, 44 + 20, 30 + 150, 33 + 22, 27 + 150, 45 + 20, 23 + 150, fill="blue", outline="black")
    etoile_bleu2 = placement.create_polygon(50 + 90, 10 + 175, 55 + 90, 23 + 175, 67 + 83, 27 + 175, 56 + 90, 30 + 175, 60 + 87, 40 + 172, 50 + 90, 33 + 175, 40 + 90, 40 + 175, 44 + 90, 30 + 175, 33 + 90, 27 + 175, 45 + 90, 23 + 175, fill="blue", outline="black")
    etoile_bleu3 = placement.create_polygon(50 + 40, 10 + 210, 55 + 40, 23 + 210, 67 + 40, 27 + 210, 56 + 40, 30 + 210, 60 + 40, 40 + 210, 50 + 40, 33 + 210, 40 + 40, 40 + 206, 44 + 40, 30 + 210, 33 + 40, 27 + 210, 45 + 40, 23 + 210, fill="blue", outline="black")
def bonnet_marteau():
    global ruband, rubanc_blanc1, rubanc_blanc2, rubanc_blanc3, manche1, manche2, marteau_boite, rond_marteau_devant, rond_marteau_derrier, etoile_devant, etoile_derrier
    ruband = placement.create_rectangle(175, 150, 175 + 100, 150 + 15, fill="blue", outline="black")
    rubanc_blanc1 = placement.create_rectangle(175, 150, 175 + 20, 150 + 15, fill="white", outline="black")
    rubanc_blanc2 = placement.create_rectangle(215, 150, 215 + 20, 150 + 15, fill="white", outline="black")
    rubanc_blanc3 = placement.create_rectangle(255, 150, 255 + 20, 150 + 15, fill="white", outline="black")
    # cree le marteau
    manche1 = placement.create_rectangle(100, 160, 100 + 15, 160 + 75, fill="#C4A484", outline="black")
    manche2 = placement.create_rectangle(100, 80, 100 + 15, 80 + 15, fill="#C4A484", outline="black")
    marteau_boite = placement.create_polygon(27, 80, 162, 102, 160, 170, 30, 155, fill="#C4A484", outline="black")
    rond_marteau_devant = placement.create_oval(15, 80, 25 + 20, 80 + 75, fill="hot pink", outline="black")
    rond_marteau_derrier = placement.create_oval(168, 105, 152 + 5, 105 + 65, fill="hot pink", outline="black")
    etoile_devant = placement.create_polygon(245 - 215, -35 + 115, 252 - 220, -30 + 135, 270 - 225, -30 + 140, 254 - 220, -30 + 145, 260 - 220, -30 + 170, 245 - 220, -30 + 150, 240 - 220, -30 + 175, 236 - 220, -30 + 145, 235 - 220, -30 + 140, 238 - 220, -30 + 135, fill="yellow", outline="black")
    etoile_derrier = placement.create_polygon(-82 + 245, -10 + 115, -87 + 252, 135, -102 + 270, 140, -87 + 254, 145, -93 + 260, 160, -80 + 245, 150, -70 + 230, 160, -76 + 236, 145, -63.5 + 220, 140, -80 + 238, 135, fill="yellow", outline="black")
def bonnet_sommeil():
    global pointe_violet, boule_blanc, chapeaux_violet, ligne_blanc, boule_jaune1, boule_jaune2, boule_jaune3, boule_jaune4, boule_jaune5, boule_jaune6, boule_jaune7, boule_jaune8
    pointe_violet = placement.create_arc(40, -10, 40 + 150, -10 + 220, start=-20, extent=20, fill="#E0B0FF", outline="black")
    boule_blanc = placement.create_oval(100, 85, 100 + 30, 85 + 30, fill="white", outline="black")
    boule_jaune1 = placement.create_oval(165, 100, 165 + 20, 100 + 20, fill="yellow", outline="black")
    boule_jaune2 = placement.create_arc(130, 105, 130 + 20, 105 + 20, start=335, extent=180, fill="yellow", outline="black")
    chapeaux_violet = placement.create_arc(160, 90, 160 + 130, 90 + 130, start=0, extent=180, fill="#E0B0FF", outline="black")
    boule_jaune3 = placement.create_oval(160, 140, 160 + 20, 140 + 20, fill="yellow", outline="black")
    boule_jaune4 = placement.create_oval(212, 140, 212 + 30, 140 + 30, fill="yellow", outline="black")
    boule_jaune5 = placement.create_oval(269.4, 140, 269.4 + 20, 140 + 20, fill="yellow", outline="black")
    boule_jaune6 = placement.create_oval(187.5, 120, 187.5 + 20, 120 + 20, fill="yellow", outline="black")
    boule_jaune7 = placement.create_oval(244.5, 120, 244.5 + 20, 120 + 20, fill="yellow", outline="black")
    boule_jaune8 = placement.create_arc(212, 76, 212 + 30, 76 + 30, start=185, extent=170, fill="yellow", outline="black")
    ligne_blanc = placement.create_rectangle(160, 150, 160 + 130, 150 + 19.5, fill="white", outline="black")
def chapeau_trancheur():
    global chapeaux_jaune, casquette_jaune, oeil_gauche_trancheur, oeil_droit_trancheur, blanc_dans_oeil_gauche_trancheur, blanc_dans_oeil_droit_trancheur, socle, scie
    chapeaux_jaune = placement.create_arc(160, 100, 160 + 130, 100 + 130, start=0, extent=180, fill="yellow", outline="black")
    casquette_jaune = placement.create_arc(160, 155, 160 + 130, 155 + 20, start=180, extent=180, fill="yellow", outline="black")
    oeil_gauche_trancheur = placement.create_oval(200, 115, 200 + 20, 115 + 40, fill="black", outline="black")
    oeil_droit_trancheur = placement.create_oval(230, 115, 230 + 20, 115 + 40, fill="black", outline="black")
    blanc_dans_oeil_gauche_trancheur = placement.create_oval(205, 115, 205 + 10, 115 + 20, fill="white", outline="black")
    blanc_dans_oeil_droit_trancheur = placement.create_oval(235, 115, 235 + 10, 115 + 20, fill="white", outline="black")
    socle = placement.create_rectangle(212.5, 91, 212.5 + 25, 91 + 10, fill="#788890", outline="black")
    scie = placement.create_polygon(212.5, 91, 220, 65, 222.5, 40, 230, 65, 237.5, 91, fill="#660000", outline="black")
# B. Si l'accessoirs et dans la main
# 1. Deplacer les accessoirs
def epee_main_lever():
    placement.coords(epee_manche, 120, 130, 120 + 15, 130 + 45)
    placement.coords(epee_lame, 52.5, -45, 52.5 + 150, -45 + 170)
    placement.coords(epee_garde, 101.5, 120, 101.5 + 50, 120 + 15)
def epee():
    placement.coords(epee_manche, 100, 210, 100 + 15, 210 + 45)
    placement.coords(epee_lame, 32.5, 35, 32.5 + 150, 35 + 170)
    placement.coords(epee_garde, 81.5, 200, 81.5 + 50, 200 + 15)
def bombe_main_lever():
    placement.coords(bombe_rond, 75, 75, 75 + 100, 75 + 100)
    placement.coords(surport_bombe, 95, 75, 95 + 60, 75 + 10)
    placement.coords(meche_bombe, 120, 30, 120 + 10, 30 + 45)
    placement.coords(etoile_bleu1, 75 + 20, -65 + 150, 80 + 20, -52 + 150, 92 + 20, -48 + 150, 81 + 20, -45 + 150, 85 + 20, -35 + 150, 75 + 20, -42 + 150, 65 + 20, -35 + 150, 69 + 20, -45 + 150, 58 + 22, -48 + 150, 70 + 20, -52 + 150)
    placement.coords(etoile_bleu2, 75 + 90, -65 + 175, 80 + 90, -52 + 175, 92 + 83, -48 + 175, 81 + 90, -45 + 175, 85 + 87, -35 + 172, 75 + 90, -42 + 175, 65 + 90, -35 + 175, 69 + 90, -45 + 175, 58 + 90, -48 + 175, 70 + 90, -52 + 175)
    placement.coords(etoile_bleu3, 75 + 40, -65 + 210, 80 + 40, -52 + 210, 92 + 40, -48 + 210, 81 + 40, -45 + 210, 85 + 40, -35 + 210, 75 + 40, -42 + 210, 65 + 40, -35 + 206, 69 + 40, -45 + 210, 58 + 40, -48 + 210, 70 + 40, -52 + 210)
def bombe():
    placement.coords(bombe_rond, 50, 150, 50 + 100, 150 + 100)
    placement.coords(surport_bombe, 70, 150, 70 + 60, 150 + 10)
    placement.coords(meche_bombe, 95, 105, 95 + 10, 105 + 45)
    placement.coords(etoile_bleu1, 50 + 20, 10 + 150, 55 + 20, 23 + 150, 67 + 20, 27 + 150, 56 + 20, 30 + 150, 60 + 20, 40 + 150, 50 + 20, 33 + 150, 40 + 20, 40 + 150, 44 + 20, 30 + 150, 33 + 22, 27 + 150, 45 + 20, 23 + 150)
    placement.coords(etoile_bleu2, 50 + 90, 10 + 175, 55 + 90, 23 + 175, 67 + 83, 27 + 175, 56 + 90, 30 + 175, 60 + 87, 40 + 172, 50 + 90, 33 + 175, 40 + 90, 40 + 175, 44 + 90, 30 + 175, 33 + 90, 27 + 175, 45 + 90, 23 + 175)
    placement.coords(etoile_bleu3, 50 + 40, 10 + 210, 55 + 40, 23 + 210, 67 + 40, 27 + 210, 56 + 40, 30 + 210, 60 + 40, 40 + 210, 50 + 40, 33 + 210, 40 + 40, 40 + 206, 44 + 40, 30 + 210, 33 + 40, 27 + 210, 45 + 40, 23 + 210)
def marteau():
    placement.coords(manche1, 100, 160, 100 + 15, 160 + 75)
    placement.coords(manche2, 100, 80, 100 + 15, 80 + 15)
    placement.coords(marteau_boite, 27, 80, 162, 102, 160, 170, 30, 155)
    placement.coords(rond_marteau_devant, 15, 80, 25 + 20, 80 + 75)
    placement.coords(rond_marteau_derrier, 168, 105, 152 + 5, 105 + 65)
    placement.coords(etoile_devant, 245 - 215, -35 + 115, 252 - 220, -30 + 135, 270 - 225, -30 + 140, 254 - 220, -30 + 145, 260 - 220, -30 + 170, 245 - 220, -30 + 150, 240 - 220, -30 + 175, 236 - 220, -30 + 145, 235 - 220, -30 + 140, 238 - 220, -30 + 135)
    placement.coords(etoile_derrier, -82 + 245, -10 + 115, -87 + 252, 135, -102 + 270, 140, -87 + 254, 145, -93 + 260, 160, -80 + 245, 150, -70 + 230, 160, -76 + 236, 145, -63.5 + 220, 140, -80 + 238, 135, )
def marteau_main_lever():
    placement.coords(manche1, 120, 100, 120 + 15, 100 + 75)
    placement.coords(manche2, 120, 20, 120 + 15, 20 + 15)
    placement.coords(marteau_boite, 47, 80 - 60, 182, 102 - 60, 180, 170 - 60, 50, 155 - 60)
    placement.coords(rond_marteau_devant, 15 + 20, 80 - 60, 25 + 20 + 20, 80 - 60 + 75)
    placement.coords(rond_marteau_derrier, 168 + 20, 105 - 60, 152 + 5 + 20, 105 + 65 - 60)
    placement.coords(etoile_devant, 245 - 215 + 20, -60 - 35 + 115, 252 - 220 + 20, -60 - 30 + 135, 270 - 225 + 20, -60 - 30 + 140, 254 - 220 + 20, -60 - 30 + 145, 260 - 220 + 20, -60 - 30 + 170, 245 - 220 + 20, -60 - 30 + 150, 240 - 220 + 20, -60 - 30 + 175, 236 - 220 + 20, -60 - 30 + 145, 235 - 220 + 20, -60 - 30 + 140, 238 - 220 + 20, -60 - 30 + 135)
    placement.coords(etoile_derrier, -82 + 245 + 20, -10 + 115 - 60, -87 + 252 + 20, 135 - 60, -102 + 270 + 20, 140 - 60, -87 + 254 + 20, 145 - 60, -93 + 260 + 20, 160 - 60, -80 + 245 + 20, 150 - 60, -70 + 230 + 20, 160 - 60, -76 + 236 + 20, 145 - 60, -63.5 + 220 + 20, 140 - 60, -80 + 238 + 20, 135 - 60, )
# C. Enlever les accessoirs
def sans_epee():
    enlever_epee = [epee_manche, epee_lame, epee_garde, pointe_vert, boule_jaune, chapeaux_vert, ligne_jaune]
    for element in enlever_epee:
        placement.coords(element, 0, 0, 0, 0)
def sans_bombe():
    enlever_bombe = [bombe_rond, surport_bombe, meche_bombe, etoile_bleu1, etoile_bleu2, etoile_bleu3, pointe_blue, etoile_jaune, etoile_vert, ligne_blanc, losange_jaune, losange_cyan]
    for element in enlever_bombe:
        placement.coords(element, 0, 0, 0, 0)
def sans_marteau():
    enlever_marteau = [ruband, rubanc_blanc1, rubanc_blanc2, rubanc_blanc3, manche1, manche2, marteau_boite, rond_marteau_devant, rond_marteau_derrier, etoile_devant, etoile_derrier]
    for element in enlever_marteau:
        placement.coords(element, 0, 0, 0, 0)
def sans_sommeil():
    enlever_sommeil = [pointe_violet, boule_blanc, chapeaux_violet, ligne_blanc, boule_jaune1, boule_jaune2, boule_jaune3, boule_jaune4, boule_jaune5, boule_jaune6, boule_jaune7, boule_jaune8]
    for element in enlever_sommeil:
        placement.coords(element, 0, 0, 0, 0)
def sans_trancheur():
    enlever_trancheur = [chapeaux_jaune, casquette_jaune, oeil_gauche_trancheur, oeil_droit_trancheur, blanc_dans_oeil_gauche_trancheur, blanc_dans_oeil_droit_trancheur, socle, scie]
    for element in enlever_trancheur:
        placement.coords(element, 0, 0, 0, 0)
# D. Pour changer les accessoirs
def accessoir():
    global compteur_mimique_accessoir, compteur_accessoir, compteur_mimique
    compteur_accessoir = (compteur_accessoir + 1) % 6 # On defini compteur_accessoir au bonne accessoir
    if compteur_accessoir == 0: # pour changer les accessoirs
        nom_des_accessoir.config(image=Fichier_Rien, width=50, height=25)
        sans_trancheur()
    elif compteur_accessoir == 1:
        nom_des_accessoir.config(image=Fichier_epee, width=50, height=40)
        compteur_mimique_accessoir = 1
        bonnet_de_epee()
        if compteur_mimique == 1 or compteur_mimique == 3:
            epee_main_lever()
    elif compteur_accessoir == 2:
        nom_des_accessoir.config(image=Fichier_bombe, width=50, height=40)
        compteur_mimique_accessoir = 2
        sans_epee()
        bonnet_de_bombe()
        if compteur_mimique == 1 or compteur_mimique == 3:
            bombe_main_lever()
    elif compteur_accessoir == 3:
        nom_des_accessoir.config(image=Fichier_marteau, width=50, height=40)
        compteur_mimique_accessoir = 3
        sans_bombe()
        bonnet_marteau()
        if compteur_mimique == 1 or compteur_mimique == 3:
            marteau_main_lever()
    elif compteur_accessoir == 4:
        nom_des_accessoir.config(image=Fichier_sommeil, width=50, height=40)
        compteur_mimique_accessoir = 4
        sans_marteau()
        bonnet_sommeil()
    elif compteur_accessoir == 5:
        nom_des_accessoir.config(image=Fichier_trancheur, width=50, height=40)
        compteur_mimique_accessoir = 5
        sans_sommeil()
        chapeau_trancheur()
# V. Le nom du personnage
# A. Demender le nom a l'utilisateur
def nom():
    nom_du_skine = entrer_du_nom.get()
    if et_lettre(nom_du_skine): # Si ultilisateur met un chifre/nombre
        le_nom_du_perso.config(text=nom_du_skine)
        le_nom_du_perso.place(x=250, y=490, anchor="c")
        # Change le nom Kirby en "nom_du_skine",(le nom que l'utilisateur a choisie)
        text_bonton_couleur.config(text="couleur de " + nom_du_skine)
        text_mimic.config(text="mimique de " + nom_du_skine)
        text_demandant_nom.place_forget()
        entrer_du_nom.place_forget()
        bouton_valider.place_forget()
        text_recomance.place_forget()
    else:
        # Met un mesage qui dit que c'est pas un bon nom
        text_recomance.config(text="Il faut rentrer un nom valide", font=("arial", 10, "bold"))
        text_recomance.place(x=410, y=13)
# 1. Verification du nom du nom
def et_lettre(lettre):
    if lettre == "":
        return False
    for caractere in lettre:
        if caractere not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&éèàâêôî-_ç'äö":
            return False
    return True
# VI. Les element, les texts et les boutons
text_bonton_couleur = Label(fenetre, text="Couleur du kirby", bg="black", fg="white", font=("arial", 10, "bold"))
text_bonton_couleur.place(x=635, y=60, anchor="c")
# A. les bouton pour changer la couleur
rouge = Button(fenetre, text="Rouge", width=6, height=2, bg="red", command=changer_couleur_rouge, activebackground="red")
rouge.place(x=529, y=90, anchor="n")
jaune = Button(fenetre, text="Jaune", width=6, height=2, bg="yellow", command=changer_couleur_jaune, activebackground="yellow")
jaune.place(x=584, y=90, anchor="n")
vert_claire = Button(fenetre, text="Vert", width=6, height=2, bg="light green", command=changer_couleur_vert, activebackground="light green")
vert_claire.place(x=638, y=90, anchor="n")
bleu = Button(fenetre, text="Bleu", width=6, height=2, bg="cyan", command=changer_couleur_bleu, activebackground="cyan")
bleu.place(x=692, y=90, anchor="n")
rose = Button(fenetre, text="Rose", width=6, height=2, bg="pink", command=changer_couleur_rose, activebackground="pink")
rose.place(x=746, y=90, anchor="n")
# B. Mimique du kirby
text_mimic = Label(fenetre, text="Mimique du kirby", bg="black", fg="white", font=("arial", 10, "bold"))
text_mimic.place(x=640, y=155, anchor="c")
text_mimique_change = Label(fenetre, text="Classique", bg="black", fg="white", font=("arial", 10, "bold"))
text_mimique_change.place(x=640, y=200, anchor="c")
# 1. Les boutton pour changer la mimique
fleche_gauche_mimique = Button(fenetre, image=Fichier_fleche_gauche, width=50, height=25, bg="blue", fg="white", activebackground="blue", command=changer_mimique_gauche)
fleche_gauche_mimique.place(x=525, y=185)
fleche_droit_mimique = Button(fenetre, image=Fichier_fleche_droite, width=50, height=25, bg="blue", fg="white", activebackground="blue", command=changer_mimique_droite)
fleche_droit_mimique.place(x=700, y=185)
# C. Deplacer les yeux
les_yeux = Label(fenetre, text="Deplace tes", bg="black", fg="white", font=("arial", 10, "bold"))
les_yeux.place(x=640, y=245, anchor="c")
# 1. Changer entre les yeux/bouche
yeux_bouche = Button(fenetre, image=Fichier_Yeux, width=50, height=25, bg="blue", fg="white", activebackground="blue", command=changer_yeux_bouche)
yeux_bouche.place(x=640, y=285, anchor="c")
# 2. Les boutton pour deplacer les yeux
fleche_gauche_element = Button(fenetre, image=Fichier_fleche_gauche, width=50, height=25, bg="blue", fg="white", activebackground="blue", command=yeux_gauche_changer)
fleche_gauche_element.place(x=588.5, y=370, anchor="c")
fleche_droit_element = Button(fenetre, image=Fichier_fleche_droite, width=50, height=25, bg="blue", fg="white", activebackground="blue", command=yeux_droit_changer)
fleche_droit_element.place(x=688.5, y=370, anchor="c")
fleche_haut_element = Button(fenetre, image=Fichier_fleche_haut, width=25, height=50, bg="blue", fg="white", activebackground="blue", command=yeux_haut_changer)
fleche_haut_element.place(x=638.5, y=340, anchor="c")
fleche_bas_element = Button(fenetre, image=Fichier_fleche_bas, width=25, height=50, bg="blue", fg="white", activebackground="blue", command=yeux_bas_changer)
fleche_bas_element.place(x=638.5, y=400, anchor="c")
# 3. Ecarter/Raprocher les yeux
ecarter_les_yeux = Button(fenetre, image=Fichier_ecarter, width=50, height=25, bg="blue", fg="white", activebackground="blue", command=ecarter_yeux)
ecarter_les_yeux.place(x=523.5, y=370, anchor="c")
raprocher_les_yeux = Button(fenetre, image=Fichier_rapprocher, width=50, height=25, bg="blue", fg="white", activebackground="blue", command=rapprocher_yeux)
raprocher_les_yeux.place(x=753.5, y=370, anchor="c")
# D. Bouton pour les accessoirs
text_accessoir = Label(fenetre, text="Choisissez votre accessoir ", bg="black", fg="white", font=("arial", 10, "bold"))
text_accessoir.place(x=551.5, y=455)
nom_des_accessoir = Button(fenetre, image=Fichier_Rien, width=50, height=25, bg="blue", fg="white", activebackground="blue", command=accessoir)
nom_des_accessoir.place(x=666.5, y=550, anchor="se")
# E. Pour demender le nom du kirby
le_nom_du_perso = Label(fenetre, bg="white", fg="pink", font=("times", 30, "italic bold"))
text_demandant_nom = Label(fenetre, text="Nom du kirby:", bg="black", fg="white", font=("arial", 10, "bold"))
text_demandant_nom.place(x=100, y=14)
# 1. Pour entre son nom
entrer_du_nom = Entry(fenetre, font=("arial", 10, "bold"))
entrer_du_nom.place(x=200, y=15)
# 2. Bouton pour valider le nom
bouton_valider = Button(fenetre, image=Fichier_Valider, width=50, height=25, bg="blue", fg="white", activebackground="blue", command=nom)
bouton_valider.place(x=350, y=10)
# 3. Prevention/Si le nom n'est pas correcte
text_recomance = Label(fenetre, text="Vous me pouvez choisir que une fois vote nom", bg="cyan", fg="red", font=("arial", 7, "bold"))
text_recomance.place(x=408, y=15)
fenetre.mainloop()