#11/11/2024
from tkinter import *
from random import  *

class Coord:
    def __init__(self, c, l):
        self.c = c
        self.l = l
    def __add__(self, other):
        return Coord(self.c + other.c, self.l + other.l)
    def __sub__(self, other):
        return Coord(self.c - other.c, self.l - other.l)
    def __str__(self):
        return "(" + str(self.c)+ "," + str(self.l)+")"
class Carre:
    def __init__(self, position, couleur):
        self.coord = position
        self.couleur = couleur
        self.dessin = DessineCarre(position, couleur)
    def pose(self,position):
        self.coord = position
        DeplaceCarre(self.dessin,position)
    def translate(self,vecteur):
        self.coord = self.coord + vecteur
        self.pose(self.coord)
    def tourne(self,position):
        # Realise le quart de tour par rapport à position
        x = self.coord.l + position.c - position.l
        y = position.c + position.l - self.coord.c
        self.coord = Coord(x,y)
        self.pose(self.coord)
    def retourne(self,position):
        # Realise la symetrie horizontal suivant un axe passant par position
        x = self.coord.c
        y = 2 * position.l - self.coord.l
        self.coord = Coord(x,y)
        self.pose(self.coord)
class Piece():
    def __init__(self, liste_coords, couleur):
        self.couleur = couleur
        self.position_initiale = liste_coords[0]
        self.carres = [Carre(position,couleur) for position in liste_coords]
    def pose(self,position):
        centre = self.carres[0].coord
        for carre in self.carres : carre.translate(position - centre)
    def translate(self,vecteur):
        for carre in self.carres : carre.translate(vecteur)
    def tourne(self):
        centre = self.carres[0].coord
        for carre in self.carres: carre.tourne(centre)
    def retourne(self):
        centre = self.carres[0].coord
        for carre in self.carres: carre.retourne(centre)


# Fonction pour dessiner un carre sur le Canvas
def DessineCarre(position, couleur):
    x, y = position.c, position.l
    carre_id = canvas.create_rectangle(x, y, x + taille_cellule, y + taille_cellule, fill=couleur) # cree un rectengle
    return carre_id

# Fonction pour deplacer le carre sur le Canvas
def DeplaceCarre(carre_id, position):
    x, y = position.c, position.l  # Notez l'ordre ici (c, l)
    canvas.coords(carre_id, x, y, x + taille_cellule, y + taille_cellule) # deplace le carre

# Fonction pour cree les blocs
def creer_blocs(nombre_blocs):
    global positions_blocs_stokees, cases_occupees_uniques
    cases_occupees_uniques = []
    # Liste contenent les cases autour de la grille qui réservées pour afficher les numéros de ligne et de colonne
    positions_blocs_stokees = (
            [(taille_cellule, j * taille_cellule + taille_cellule) for j in range(colonnes)]  # coter haut
            + [(i * taille_cellule + taille_cellule, taille_cellule) for i in range(lignes)]  # coter gauche
    )
    # Positions disponibles pour les blocs (les cases interieures seulement)
    positions_possibles = [(i, j) for i in range(1, lignes) for j in range(1, colonnes)]

    # selection des positions aleatoires pour les blocs parmi les positions disponibles
    positions_blocs = sample(positions_possibles, nombre_blocs)

    for ligne, colonne in positions_blocs:
        # Dessiner le bloc
        rayon = taille_cellule/3  # Rayon du cercle
        x_centre = decalage_y + ligne * taille_cellule + taille_cellule / 2
        y_centre = decalage_x + colonne * taille_cellule + taille_cellule / 2

        # Dessiner le cercle rouge au centre de la case
        canvas.create_oval(x_centre - rayon, y_centre - rayon,
                           x_centre + rayon, y_centre + rayon,
                           fill="#f0dc8e", outline="black")  # Cree le cercles rouges

        # Stocker la position du bloc
        positions_blocs_stokees.append(
            (ligne * taille_cellule + taille_cellule, colonne * taille_cellule + taille_cellule))
        # liste des case occuper
        cases_occupees_uniques.append(positions_blocs_stokees)
    print("Positions des blocs : ", positions_blocs_stokees)

# Fonction pour verifier la grille
def verifier_grille_complete():
    global positions_blocs_stokees, cases_occupees_uniques, nb_cout, cases_libres
    cases_occupees_uniques = []  # Reinitialiser la liste des cases occupees uniques
    #print("Positions des blocs :", positions_blocs_stokees)

    # Nombre total de cases à occuper
    cases_internes = []
    for i in range(taille_cellule, taille_cellule * 7 + 1, taille_cellule):  # Lignes
        for j in range(taille_cellule, taille_cellule * 7 + 1, taille_cellule):  # Colonnes
            cases_internes.append((i, j))
    #print("cases internes" ,cases_internes)

    # Ajoute les positions des blocs aux cases occupées
    for bloc in positions_blocs_stokees:
        if bloc not in cases_occupees_uniques:
            cases_occupees_uniques.append(bloc)

    # Ajoute les positions des pièces de jeu aux cases occupées
    for nom_piece, positions_piece in emplacements_pieces.items():
        for pos in positions_piece:
            if pos not in cases_occupees_uniques:
                cases_occupees_uniques.append(pos)

    #print("Cases occupees uniques :", cases_occupees_uniques)

    # Trouver des cases internes non occupées
    cases_libres = [case for case in cases_internes if case not in cases_occupees_uniques]
    Case(len(cases_libres)) # Afficher le nombre de cases libres
    # si toute les casse sont occuper
    if not cases_libres:
        Lattention.place_forget()
        print("Toutes les cases de la grille sont occupees !")
        Lfini.config(text="Tu as reussit en "+ str(nb_cout) + " cout !!! \n Felicitation")
        Lfini.place(x=450,y=50,anchor ="c")

    else:
        print("Il reste", len(cases_libres), "cases libres dans la grille.")
        #print("Positions des cases libres :", cases_libres)

# Fonction pour verifier les limites
def verifier_limites(Quel_Piece, limite_gauche, limite_droite, limite_haut, limite_bas, direction):
    if Quel_Piece is not None:
        for carre in Quel_Piece.carres:
            nouvelle_l = carre.coord.l  # Ligne
            nouvelle_c = carre.coord.c  # Colonne

            # Verification des bords de la grille en fonction de la direction
            if direction == "haut" and nouvelle_l <= limite_haut:
                print("La piece atteint le haut :", (nouvelle_l, nouvelle_c))
                return False
            if direction == "bas" and nouvelle_l >= limite_bas:
                print("La piece atteint le bas :", (nouvelle_l, nouvelle_c))
                return False
            if direction == "gauche" and nouvelle_c <= limite_gauche:
                print("La piece atteint la gauche :", (nouvelle_l, nouvelle_c))
                return False
            if direction == "droite" and nouvelle_c >= limite_droite:
                print("La piece atteint la droite :", (nouvelle_l, nouvelle_c))
                return False
    return True

#  Fonction pour les deplacements
def haut(event):
    global Quel_Piece, nb_cout
    if Quel_Piece is not None:
        # une fois par touche apuier
        Lattention.config(text="la piece vas vers le haut")
        if verifier_limites(Quel_Piece, 40, 800, 40, 280, "haut"): # si la limite
            nb_cout = nb_cout + 1
            Cout(nb_cout) # Mes a jour le nombre de cout
            Quel_Piece.translate(Coord(0, -vitesse)) # deplace la piece
        else:
            Lattention.config(text="La piece ne peut pas aller plus en haut")

def bas(event):
    global Quel_Piece, nb_cout
    if Quel_Piece is not None:
        # une fois par touche apuier
        Lattention.config(text="la piece vas vers le bas")
        if verifier_limites(Quel_Piece, 40, 800, 40, 280, "bas"):  # si la limite
            nb_cout = nb_cout + 1
            Cout(nb_cout)  # Mes a jour le nombre de cout
            Quel_Piece.translate(Coord(0, vitesse)) # deplace la piece
        else:
            Lattention.config(text="La piece ne peut pas aller plus en bas")

def gauche(event):
    global Quel_Piece, nb_cout
    if Quel_Piece is not None:
        # une fois par touche apuier
        Lattention.config(text="la piece vas vers la gauche")
        if verifier_limites(Quel_Piece, 40, 800, 40, 280, "gauche"):  # si la limite
            nb_cout = nb_cout + 1
            Cout(nb_cout)  # Mes a jour le nombre de cout
            Quel_Piece.translate(Coord(-vitesse, 0)) # deplace la piece
        else:
            Lattention.config(text="La piece ne peut pas aller plus à gauche")

def droite(event):
    global Quel_Piece, nb_cout
    if Quel_Piece is not None:
        # une fois par touche apuier
        Lattention.config(text="la piece vas vers la droite")
        if verifier_limites(Quel_Piece, 40, 800, 40, 280, "droite"):  # si la limite
            nb_cout = nb_cout + 1
            Cout(nb_cout)  # Mes a jour le nombre de cout
            Quel_Piece.translate(Coord(vitesse, 0)) # deplace la piece
        else:
            Lattention.config(text="La piece ne peut pas aller plus à droite")


# Rotation et retournement
def tourner(event):
    global Quel_Piece, nb_cout
    if Quel_Piece is not None:
        nb_cout = nb_cout + 1
        Cout(nb_cout) # Mes a jour le nombre de cout
        Lattention.config(text="On tourne la piece")
        Quel_Piece.tourne() # deplace la piece

def retourner(event):
    global Quel_Piece, nb_cout
    if Quel_Piece is not None:
        nb_cout = nb_cout + 1
        Cout(nb_cout) # Mes a jour le nombre de cout
        Lattention.config(text="On retourne la piece")
        Quel_Piece.retourne() # deplace la piece

def select_piece(event):
    global Quel_Piece,Selectionner
    if Selectionner == 1: # variable pour verifier si une autre piece n'est pas deja selectonner
        #print(event.char)
        if event.char == "1" or event.char == "&":
            Quel_Piece = pieces[0]  # Sélectionne la première pièce
            Lattention.config(text="Pièce 1 sélectionnée")
        elif event.char == "2" or event.char == "é":
            Quel_Piece = pieces[1]  # Sélectionne la deuxième pièce
            Lattention.config(text="Pièce 2 sélectionnée")
        elif event.char == "3" or event.char == '"':
            Quel_Piece = pieces[2]  # Sélectionne la troisième pièce
            Lattention.config(text="Pièce 3 sélectionnée")
        elif event.char == "4" or event.char == "'":
            Quel_Piece = pieces[3]  # Sélectionne la quatrième pièce
            Lattention.config(text="Pièce 4 sélectionnée")
        elif event.char == "5" or event.char == "(":
            Quel_Piece = pieces[4]  # Sélectionne la cinquième pièce
            Lattention.config(text="Pièce 5 sélectionnée")
        elif event.char == "6" or event.char == "-":
            Quel_Piece = pieces[5]  # Sélectionne la sixième pièce
            Lattention.config(text="Pièce 6 sélectionnée")
        elif event.char == "7" or event.char == "è":
            Quel_Piece = pieces[6]  # Sélectionne la septième pièce
            Lattention.config(text="Pièce 7 sélectionnée")
        elif event.char == "8" or event.char == "_":
            Quel_Piece = pieces[7]  # Sélectionne la huitième pièce
            Lattention.config(text="Pièce 8 sélectionnée")
        elif event.char == "9" or event.char == "ç":
            Quel_Piece = pieces[8]  # Sélectionne la neuvième pièce
            Lattention.config(text="Pièce 9 sélectionnée")
        Selectionner = 0
    else:
        Lattention.config(text="il faut appuiter sur Entrer pour changer de piece")

# Fonction pour desactiver le deplacement de la piece
def deselect_piece(event):
    global Quel_Piece,positions_blocs_stokees,Selectionner
    if Quel_Piece is not None:
        # Recuperer les emplacements de la piece dans un dictionnaire
        emplacements_pieces[Quel_Piece.couleur] = [(carre.coord.c, carre.coord.l) for carre in Quel_Piece.carres]
        print("Emplacements de la piece", Quel_Piece.couleur, ":", emplacements_pieces[Quel_Piece.couleur])
        if  verification(emplacements_pieces,positions_blocs_stokees):
            Quel_Piece = None  # Deselectionne la piece
            Lattention.config(text="Deplacement de la piece desactive")
            Selectionner = 1
            verifier_grille_complete()

def verification(emplacements_pieces,positions_blocs_stokees):
    #print(emplacements_pieces)
    #print(positions_blocs_stokees)
    #Verifie que toutes les coordonnees des emplacements des pieces sont differente des coordonnees des blocs stockes.
    # Parcourir chaque piece et ses coordonnees
    for couleur in emplacements_pieces:  # Parcourt chaque couleur de piece
        coords_piece = emplacements_pieces[couleur]  # Obtient les coordonnees de la piece

        for coord in coords_piece:  # Pour chaque coordonnee de la piece
            # Verifier si la coordonnee de la piece est dans les blocs
            for bloc in positions_blocs_stokees:
                if coord == bloc:
                    Lattention.config(text="Collision detectee avec le bloc à la position "+str(coord))
                    return False  # Il y a un chevauchement avec un bloc

    # Verification des coordonnees des pieces entre elles
    toutes_coords = []  # Liste pour stocker toutes les coordonnees des pieces

    # Rassembler toutes les coordonnees des pieces
    for couleur in emplacements_pieces:  # Parcourt chaque couleur de piece
        coords_piece = emplacements_pieces[couleur]  # Obtient les coordonnees de la piece

        for coord in coords_piece:  # Pour chaque coordonnee de la piece
            toutes_coords.append(coord)  # Ajoute la coordonnee à la liste

    # Verifier les chevauchements entre les pieces
    for i in range(len(toutes_coords)):
        for j in range(i + 1, len(toutes_coords)):
            if toutes_coords[i] == toutes_coords[j]:  # Verifie si deux pieces touchent
                Lattention.config(text="Collision detectee avec le bloc à la position "+str(toutes_coords[i]))
                print("Collision detectee entre les pieces à la position", toutes_coords[i])
                return False  # Il y a un chevauchement entre pieces
    return True  # Pas de chevauchement
# Fonction pour le nombre de cout du joueur
def Cout(nb_cout):
    Lcout.config(text = "Nombre de cout : " + str(nb_cout))
# Fonction pour le nombre de case restente du joueur
def Case(cases_libres):
    Lcase.config(text = "Il reste " + str(cases_libres) + " cases")

# Creation de la fenetre
fenetre = Tk()
fenetre.config(width=900, height=600, bg="#fcf3cf")
taille_cellule = 40 # taille du jeu
# Creation du canvas
canvas = Canvas(fenetre, width=900, height=taille_cellule*9,bg="#fcf3cf")
canvas.place(x=0, y=taille_cellule*2,anchor ="nw")  # Positionnez le canvas où vous voulez

# Dimensions de la grille du jeu
lignes, colonnes = 7, 7

# Decalage pour placer la grille
decalage_x = taille_cellule  # Decalage horizontal
decalage_y = taille_cellule  # Decalage vertical

# Dessiner la grille
for i in range(lignes):
    for j in range(colonnes):
        x1 = decalage_x + j * taille_cellule
        y1 = decalage_y + i * taille_cellule
        x2 = x1 + taille_cellule
        y2 = y1 + taille_cellule
        canvas.create_rectangle(x1, y1, x2, y2, outline="black") # cree les case du jeu

        # Ajouter les numeros de ligne/colonne en excluant le coin haut-gauche
        if i == 0 and j != 0:  # Numeros des colonnes, en enlevent la premiere case
            canvas.create_text(x1 + taille_cellule / 2, y1 + taille_cellule / 2, text=str(j), font=("Arial", 12))
        elif j == 0 and i != 0:  # Numeros des lignes, en enlevent la premiere case
            canvas.create_text(x1 + taille_cellule / 2, y1 + taille_cellule / 2, text=str(i), font=("Arial", 12))

# Appel de la fonction pour creer 7 blocs aleatoires
creer_blocs(7)

# vitesse des piece
vitesse = taille_cellule
# Liste des coordonnees pour tout les piece
pieces = [
    Piece([Coord(taille_cellule*9,taille_cellule*3)],"#FF4C4C"),# Premiere piece
    Piece([Coord(taille_cellule*9,taille_cellule),Coord(taille_cellule*10,taille_cellule)],"#FF6F61"), # deusieme piece
    Piece([Coord(taille_cellule*12,taille_cellule*4),Coord(taille_cellule*13,taille_cellule*4),Coord(taille_cellule*14,taille_cellule*4)],"#FFCC4C"), # troisieme piece
    Piece([Coord(taille_cellule*13,taille_cellule*2),Coord(taille_cellule*14,taille_cellule*2),Coord(taille_cellule*15,taille_cellule*2),Coord(taille_cellule*16,taille_cellule*2)], "#99FF4C"),  # quatrieme piece

    Piece([Coord(taille_cellule*13,taille_cellule*6),Coord(taille_cellule*13,taille_cellule*7),Coord(taille_cellule*14,taille_cellule*7)],"#4CFF8A"), # cinquieme piece
    Piece([Coord(taille_cellule*19,taille_cellule*7),Coord(taille_cellule*20,taille_cellule*7),Coord(taille_cellule*20,taille_cellule*6),Coord(taille_cellule*20,taille_cellule*5)],"#4CCFFF"), # sisieme piece
    Piece([Coord(taille_cellule*9,taille_cellule*6),Coord(taille_cellule*9,taille_cellule*7),Coord(taille_cellule*10,taille_cellule*6),Coord(taille_cellule*10,taille_cellule*7)],"#4C9EFF"), # septieme piece
    Piece([Coord(taille_cellule*18,taille_cellule),Coord(taille_cellule*19,taille_cellule),Coord(taille_cellule*19,taille_cellule*2),Coord(taille_cellule*20,taille_cellule)],"#A24CFF"), # huitieme piece
    Piece([Coord(taille_cellule*16,taille_cellule*6),Coord(taille_cellule*17,taille_cellule*6),Coord(taille_cellule*17,taille_cellule*5),Coord(taille_cellule*18,taille_cellule*5)], "#FF4C8A"),  # neuvieme piece
]
Quel_Piece = None
emplacements_pieces = {}  # Dictionnaire pour stocker les positions des pieces
# Remplir le dictionnaire emplacements_pieces avec les coordonnees des pieces
for piece in pieces:
    emplacements_pieces[piece.couleur] = [(carre.coord.c, carre.coord.l) for carre in piece.carres]

# Affichage du dictionnaire emplacements_pieces pour verification
print("Postion des pieces",emplacements_pieces)
Selectionner = 1
nb_cout = 0
cases_libres = 29
# creation des label
# Titre
Ltitre = Label(fenetre, text = "Genuis Square",font=("Arial", 15))
Ltitre.place(x=450,y = 10,anchor = "c")
# nombre de cout
Lcout = Label(fenetre, text="Nombre de cout : " + str(nb_cout),font=("Arial", 15))
Lcout.place(x=0,y=0)
# nombre de case
Lcase = Label(fenetre,text="Il reste "+ str(cases_libres) + " cases",font=("Arial", 15))
Lcase.place(x=900,y=0,anchor = "ne")
# les differnent satut du jeu
Lattention = Label(fenetre, text="Vous aurait ici les informations de la partie",font=("Arial", 15))
Lattention.place(x=450,y =65,anchor = "c")

# Label pour les Commandes

Linfo_commande1 = Label(fenetre, text="Commandes :", bg="#fcf3cf", fg="red", font=("Arial", 12 ))
Linfo_commande1.place(x=450, y=460, anchor="c")

# Ligne 1: Sélection des pièces
Linfo_commande2 = Label(fenetre, text="1. Sélection :", bg="#fcf3cf", fg="#333", font=("Arial", 12 ))
Linfo_commande2.place(x=145, y=485)


# Plusieru label pour avoir des couleur differente
Linfo_piece1 = Label(fenetre, text="& / 1  :", bg="#fcf3cf", fg="#333", font=("Arial", 12))  # Texte normal
Linfo_piece1.place(x=250, y=475)

Linfo_piece1_2 = Label(fenetre, text="Rouge", bg="#fcf3cf", fg="#FF4C4C", font=("Arial", 12 ))  # Rouge
Linfo_piece1_2.place(x=300, y=475)

Linfo_piece2 = Label(fenetre, text="|  é / 2  :", bg="#fcf3cf", fg="#333", font=("Arial", 12 ))  # Texte normal
Linfo_piece2.place(x=350, y=475)

Linfo_piece2_2 = Label(fenetre, text="Corail", bg="#fcf3cf", fg="#FF6F61", font=("Arial", 12 ))  # Corail
Linfo_piece2_2.place(x=410, y=475)

Linfo_piece3 = Label(fenetre, text='|  " / 3  :', bg="#fcf3cf", fg="#333", font=("Arial", 12 ))  # Texte normal
Linfo_piece3.place(x=460, y=475)

Linfo_piece3_2 = Label(fenetre, text="Jaune", bg="#fcf3cf", fg="#FFCC4C", font=("Arial", 12 ))  # Jaune
Linfo_piece3_2.place(x=520, y=475)

Linfo_piece4 = Label(fenetre, text="|  ' / 4  :", bg="#fcf3cf", fg="#333", font=("Arial", 12 ))  # Texte normal
Linfo_piece4.place(x=570, y=475)

Linfo_piece4_2 = Label(fenetre, text="Lime", bg="#fcf3cf", fg="#99FF4C", font=("Arial", 12 ))  # Lime
Linfo_piece4_2.place(x=630, y=475)

Linfo_piece5 = Label(fenetre, text="|  ( / 5  :", bg="#fcf3cf", fg="#333", font=("Arial", 12 ))  # Texte normal
Linfo_piece5.place(x=680, y=475)

Linfo_piece5_2 = Label(fenetre, text="Menthe ", bg="#fcf3cf", fg="#4CFF8A", font=("Arial", 12 ))  # Menthe
Linfo_piece5_2.place(x=740, y=475)

Linfo_piece6 = Label(fenetre, text=" - / 6   :", bg="#fcf3cf", fg="#333", font=("Arial", 12))
Linfo_piece6.place(x=250, y=500)

Linfo_piece6_2 = Label(fenetre, text="Cyan", bg="#fcf3cf", fg="#4CCFFF", font=("Arial", 12))
Linfo_piece6_2.place(x=300, y=500)

Linfo_piece7 = Label(fenetre, text="|  è / 7  :", bg="#fcf3cf", fg="#333", font=("Arial", 12))
Linfo_piece7.place(x=350, y=500)

Linfo_piece7_2 = Label(fenetre, text="Bleu", bg="#fcf3cf", fg="#4C9EFF", font=("Arial", 12))
Linfo_piece7_2.place(x=410, y=500)

Linfo_piece8 = Label(fenetre, text="|  _ / 8  :", bg="#fcf3cf", fg="#333", font=("Arial", 12))
Linfo_piece8.place(x=460, y=500)

Linfo_piece8_2 = Label(fenetre, text="Violet", bg="#fcf3cf", fg="#A24CFF", font=("Arial", 12))
Linfo_piece8_2.place(x=520, y=500)

Linfo_piece9 = Label(fenetre, text="|  ç / 9  :", bg="#fcf3cf", fg="#333", font=("Arial", 12))
Linfo_piece9.place(x=570, y=500)

Linfo_piece9_2 = Label(fenetre, text="Rose", bg="#fcf3cf", fg="#FF4C8A", font=("Arial", 12))
Linfo_piece9_2.place(x=630, y=500)

# Autres instructions
Linfo_commande3 = Label(fenetre, text="2. Déplacements : Utiliser 'Z','Q','S' et 'Q' ou les flèches directionnelle pour vous Deplacer\n"
                                      " ainsi que 'T' et 'R' pour Tourner et Retourner la piece", bg="#fcf3cf", fg="#333", font=("Arial", 13))
Linfo_commande3.place(x=450, y=548, anchor="c")

Linfo_commande5 = Label(fenetre, text="3. Valider : Valider la position avec Entree", bg="#fcf3cf", fg="#333", font=("Arial", 12))
Linfo_commande5.place(x=430, y=585,anchor = "e")

Linfo_commande7 = Label(fenetre, text="4. Objectif : Remplir la grille !", bg="#fcf3cf", fg="#333", font=("Arial", 12 ))
Linfo_commande7.place(x=470, y=585,anchor = "w")

# Label pour l'affichage de fin
Lfini = Label(fenetre, text = "",bg="#fcf3cf",font=("Arial", 15))
Lfini.place_forget()

# Recuper les touches pour sélectionner des pièces en utilisant les événements de pression de touche

fenetre.bind("1", select_piece)  # Touche '1' pour selectionner la premiere piece
fenetre.bind("2", select_piece)  # Touche '2' pour selectionner la deuxieme piece
fenetre.bind("3", select_piece)  # Touche '3' pour selectionner la troisieme piece
fenetre.bind("4", select_piece)  # Touche '4' pour selectionner la quatieme piece
fenetre.bind("5", select_piece)  # Touche '5' pour selectionner la cinquieme piece
fenetre.bind("6", select_piece)  # Touche '6' pour selectionner la sieme piece
fenetre.bind("7", select_piece)  # Touche '7' pour selectionner la septeme piece
fenetre.bind("8", select_piece)  # Touche '8' pour selectionner la huiteme piece
fenetre.bind("9", select_piece)  # Touche '9' pour selectionner la neufieme piece

fenetre.bind("<KeyPress-ampersand>", select_piece)  # Touche '&' pour selectionner la premiere piece
fenetre.bind("<KeyPress-eacute>", select_piece)     # Touche 'é' pour selectionner la deuxieme piece
fenetre.bind("<KeyPress-quotedbl>", select_piece)   # Touche '"' pour selectionner la troisieme piece
fenetre.bind("<KeyPress-apostrophe>", select_piece) # Touche "'" pour selectionner la quatieme piece
fenetre.bind("<KeyPress-parenleft>", select_piece)  # Touche '(' pour selectionner la cinquieme piece
fenetre.bind("<KeyPress-minus>", select_piece)      # Touche '-' pour selectionner la sieme piece
fenetre.bind("<KeyPress-egrave>", select_piece)     # Touche 'è' pour selectionner la septeme piece
fenetre.bind("<KeyPress-underscore>", select_piece) # Touche '_' pour selectionner la huiteme piece
fenetre.bind("<KeyPress-ccedilla>", select_piece)   # Touche 'ç' pour selectionner la neufieme piece

# Les deplacements
fenetre.bind("<Up>", haut)      # Touche pour deplacer la piece vers le haut
fenetre.bind("<Down>", bas)     # Touche pour deplacer la piece vers le bas
fenetre.bind("<Left>", gauche)  # Touche pour deplacer la piece vers le gauche
fenetre.bind("<Right>", droite) # Touche pour deplacer la piece vers le droite
fenetre.bind("z", haut)         # Touche pour deplacer la piece vers le haut
fenetre.bind("s", bas)          # Touche pour deplacer la piece vers le bas
fenetre.bind("q", gauche)       # Touche pour deplacer la piece vers le gauche
fenetre.bind("d", droite)       # Touche pour deplacer la piece vers le droite
fenetre.bind("t",tourner)       # Touche pour tourner la piece
fenetre.bind("r",retourner)     # Touche pour retourner la piece
fenetre.bind("<Return>", deselect_piece)  # Touche Entree pour desactiver le deplacement

fenetre.mainloop()