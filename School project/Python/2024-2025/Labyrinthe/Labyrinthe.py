#13/04/2025
from tkinter import *
from random import *
from time import *

TAILLE ,elements_distances , labyrinthe, parcours_en_cours, decalage_x , decalage_y , hors_champ = 30, [],None,False, 0, 0, 0
COULEURS = {"mur": "black", "vide": "white", "entree": "blue", "sortie": "red", "visite": "yellow"}

# Classe pour représenter les coordonnées d'une cellule
class Coord:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, autre): return Coord(self.x + autre.x, self.y + autre.y)
    def __sub__(self, autre): return Coord(self.x - autre.x, self.y - autre.y)
    def __eq__(self, autre): return self.x == autre.x and self.y == autre.y
    def __str__(self): return "(" + str(self.x) + "," + str(self.y) + ")"

# Classe représentant une cellule du labyrinthe
class Cellule:
    def __init__(self, position):
        self.position = position
        self.murs = {"n": True, "e": True, "s": True, "w": True}  # murs nord, est, sud, ouest
        self.etat = "isole"  # pour la construction du labyrinthe
        self.distance = float('inf')  # distence infinit
        self.decouverte = False  # pour flood fill
    # desinier les different element
    def dessine(self, couleur):
        Carre(self.position, couleur)
        if self.murs["w"]: Ligne(self.position, Coord(0, 1))
        if self.murs["n"]: Ligne(self.position, Coord(1, 0))
        if self.murs["e"]: Ligne(self.position + Coord(1, 1), Coord(0, -1))
        if self.murs["s"]: Ligne(self.position + Coord(1, 1), Coord(-1, 0))

    def supprimer_mur(self, autre_cellule):
        correspondance = {"(0,-1)": "s", "(1,0)": "w", "(0,1)": "n", "(-1,0)": "e"}
        # calcul entre les positions des deux cellules
        difference = str(self.position - autre_cellule.position)
        # Si cette différence correspond à une direction, on supprime le mur entre les deux cellules.
        if difference in correspondance:
            self.murs[correspondance[difference]] = False  # on enlève le mur du côté
        # on refait la meme chose pour une autre cellule
        difference_inverse = str(autre_cellule.position - self.position)
        if difference_inverse in correspondance:
            autre_cellule.murs[correspondance[difference_inverse]] = False


# Classe du labyrinthe et des algorithmes de parcours
class Labyrinthe:
    direction = [
        {"mur": "e", "deplacement": Coord(1, 0)},
        {"mur": "s", "deplacement": Coord(0, 1)},
        {"mur": "w", "deplacement": Coord(-1, 0)},
        {"mur": "n", "deplacement": Coord(0, -1)}
    ]

    def __init__(self, N, canevas):
        self.N = N
        self.grille = [[Cellule(Coord(x, y)) for y in range(N)] for x in range(N)]
        self.entree = Coord(0, 0)
        self.sortie = Coord(N - 1, N - 1)
        self.canevas = canevas

    def dessine(self):
        for x in range(self.N):
            for y in range(self.N):
                couleur = COULEURS["vide"]
                if Coord(x, y) == self.entree:
                    couleur = COULEURS["entree"]
                elif Coord(x, y) == self.sortie:
                    couleur = COULEURS["sortie"]
                self.grille[x][y].dessine(couleur)

    def voisines(self, cellule):
        voisines_isolees = []
        for direction in self.direction:
            # on calcule des nouvelles coordonnées apres déplacement
            nx = cellule.position.x + direction["deplacement"].x
            ny = cellule.position.y + direction["deplacement"].y
            # Vérification que les coordonnées sont dans les limites de la grille
            if 0 <= nx < self.N and 0 <= ny < self.N:
                # Récupération de la cellule voisine a au nouvelles coordonnées
                voisine = self.grille[nx][ny]
                if voisine.etat == "isole":
                    voisines_isolees.append(voisine)
        # on renvoie de la liste des voisines isolées
        return voisines_isolees

    def creation(self):
        pile = Pile()
        cellule_depart = self.grille[0][0]
        cellule_depart.etat = "connexe"
        pile.empiler(cellule_depart)
        while not pile.est_vide():
            cellule_courante = pile.sommet()  # on obtient la cellule au sommet de la pile
            voisines = self.voisines(cellule_courante) # on obtient les voisines isolées de la cellule courante.
            # Si la cellule courante a des voisines isolées.
            if voisines:
                voisine = choice(voisines)
                # on supprime le mur entre la cellule courante et la cellule voisine.
                cellule_courante.supprimer_mur(voisine)
                voisine.etat = "connexe"
                pile.empiler(voisine)
            else:
                pile.depiler()
        self.dessine()

    def reseau(self):
        acces = {}
        # on parcourt toutes les cellules de la grille
        for x in range(self.N):
            for y in range(self.N):
                cellule = self.grille[x][y]
                voisins_accessibles = []
                # on teste chaque direction
                for direction in self.direction:
                    nx = x + direction["deplacement"].x
                    ny = y + direction["deplacement"].y
                    # on regarde si la nouvelle position est bien dans les limites de la grille
                    if 0 <= nx < self.N and 0 <= ny < self.N:
                        # si le mur dans cette direction est supprimé ,on peut passer
                        if not cellule.murs[direction["mur"]]:
                            # on ajoute la cellule voisine comme accessible
                            voisins_accessibles.append(self.grille[nx][ny])
                # on ajoute au dictionnaire la cellule et la liste de ses voisines accessibles
                acces[cellule] = voisins_accessibles
        return acces

    def dijkstra(self):
        for x in range(self.N):
            for y in range(self.N):
                self.grille[x][y].distance = float('inf') # toute les distance à infini
        cellule_depart = self.grille[self.entree.x][self.entree.y]
        cellule_depart.distance = 0
        a_traiter = [cellule_depart]  # liste des cellules à traiter
        while a_traiter:
            # on cherche la cellule avec la plus petite distance dans la liste
            min_index = 0
            for i in range(1, len(a_traiter)):
                if a_traiter[i].distance < a_traiter[min_index].distance:
                    min_index = i
            # on retire la cellule de la liste
            cellule_courante = a_traiter.pop(min_index)
            # pour chaque voisine accessible
            for voisine in self.reseau()[cellule_courante]:
                nouvelle_distance = cellule_courante.distance + 1
                # si cette nouvelle distance est plus courte que celle déjà obtenue
                if nouvelle_distance < voisine.distance:
                    voisine.distance = nouvelle_distance
                    a_traiter.append(voisine)
        cellule_courante = self.grille[self.sortie.x][self.sortie.y]  # on part de la sortie
        chemin = []
        # on vas vers l entree en suivant les distances decroissantes
        while cellule_courante.position != self.entree:
            chemin.append(cellule_courante)
            suivante = None
            for voisine in self.reseau()[cellule_courante]:
                # on cherche une voisine dont la distance est - 1
                if voisine.distance == cellule_courante.distance - 1 and suivante is None:
                    suivante = voisine
            if suivante:
                cellule_courante = suivante
            else:
                return []  # aucun chemin trouvé
        chemin.append(cellule_depart)  # on ajoute la cellule de départ à la fin du chemin
        # afficher le chemin
        for cellule in chemin:
            AfficheDistance(cellule.position + Coord(0, 0), cellule.distance, "green")
        return chemin

    def flood_fill(self):
        file_attente = File()
        cellule_sortie = self.grille[self.sortie.x][self.sortie.y]
        cellule_sortie.distance = 0
        cellule_sortie.decouverte = True
        file_attente.enfiler(cellule_sortie)
        # tant qu'il y a des cellules à explorer
        while not file_attente.est_vide():
            cellule_courante = file_attente.defiler()
            # on parcourt toutes les voisines accessible
            for voisine in self.reseau()[cellule_courante]:
                if not voisine.decouverte:
                    voisine.distance = cellule_courante.distance + 1
                    voisine.decouverte = True
                    file_attente.enfiler(voisine)
                    # affiche la distance de la cellule par rapport à la sortie
                    AfficheDistance(voisine.position + Coord(0, 0), voisine.distance, "blue")


    def parcours_flood_fill(self):
        chemin = []
        cellule_courante = self.grille[self.entree.x][self.entree.y]
        # tant que y a pas la sortie
        while cellule_courante.position != self.sortie:
            chemin.append(cellule_courante)
            # on parcourt toutes les voisines accessible
            for voisine in self.reseau()[cellule_courante]:
                if voisine.distance == cellule_courante.distance - 1:
                    cellule_courante = voisine
        chemin.append(self.grille[self.sortie.x][self.sortie.y])
        for cellule in chemin:
            AfficheDistance(cellule.position + Coord(0, 0), cellule.distance, "purple")

    def main_droite(self):
        cellule_courante = self.grille[self.entree.x][self.entree.y]
        chemin = [cellule_courante]
        ordre_directions = ["e", "s", "w", "n"]
        vecteurs_directions =   {"e": Coord(1, 0),
                                "s": Coord(0, 1),
                                "w": Coord(-1, 0),
                                "n": Coord(0, -1)}

        direction_actuelle = 0  # on commence en regardant vers l'est
        while cellule_courante.position != self.sortie:
            chemin.append(cellule_courante)
            avance_possible = False

            # on teste de tourner à droite
            direction_droite = (direction_actuelle + 1) % 4
            nom_droite = ordre_directions[direction_droite]
            pos_droite = cellule_courante.position + vecteurs_directions[nom_droite]
            if 0 <= pos_droite.x < self.N and 0 <= pos_droite.y < self.N:
                if not cellule_courante.murs[nom_droite]:
                    cellule_courante = self.grille[pos_droite.x][pos_droite.y]
                    direction_actuelle = direction_droite
                    avance_possible = True

            # sinon tout droit
            if not avance_possible:
                nom_tout_droit = ordre_directions[direction_actuelle]
                pos_tout_droit = cellule_courante.position + vecteurs_directions[nom_tout_droit]
                if 0 <= pos_tout_droit.x < self.N and 0 <= pos_tout_droit.y < self.N:
                    if not cellule_courante.murs[nom_tout_droit]:
                        cellule_courante = self.grille[pos_tout_droit.x][pos_tout_droit.y]
                        avance_possible = True

            # sinon on tourne à gauche jusqu'à pouvoir avancer
            if not avance_possible:
                essais = 0
                while essais < 3 and not avance_possible:
                    direction_actuelle = (direction_actuelle - 1) % 4
                    nom_gauche = ordre_directions[direction_actuelle]
                    pos_gauche = cellule_courante.position + vecteurs_directions[nom_gauche]
                    if 0 <= pos_gauche.x < self.N and 0 <= pos_gauche.y < self.N:
                        if not cellule_courante.murs[nom_gauche]:
                            cellule_courante = self.grille[pos_gauche.x][pos_gauche.y]
                            avance_possible = True
                    essais = essais + 1
            if not avance_possible:
                return
        chemin.append(self.grille[self.sortie.x][self.sortie.y])
        # Affichage du chemin avec la couleur définie dans le dictionnaire
        for cellule in chemin:
            cellule.dessine(COULEURS["visite"])
            self.canevas.update()
            sleep(0.05)

class Pile:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return len(self.elements) == 0

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
        if not self.est_vide():
            return self.elements.pop()
        return None

    def sommet(self):
        if not self.est_vide():
            return self.elements[-1]
        return None

class File:
    def __init__(self):
        self.elements = []

    def enfiler(self, element):
        self.elements.append(element)

    def defiler(self):
        return self.elements.pop(0)

    def est_vide(self):
        return len(self.elements) == 0

# Fonctions de dessin

def Carre(position, couleur):
    x = position.x * TAILLE + hors_champ
    y = position.y * TAILLE + hors_champ
    return canevas.create_rectangle(x, y, x + TAILLE, y + TAILLE, fill=couleur, width=0)

def Ligne(depart, deplacement):
    arrivee = depart + deplacement
    x1 = depart.x * TAILLE + hors_champ
    y1 = depart.y * TAILLE + hors_champ
    x2 = arrivee.x * TAILLE + hors_champ
    y2 = arrivee.y * TAILLE + hors_champ
    return canevas.create_line(x1, y1, x2, y2, fill=COULEURS["mur"], width=3)

def AfficheDistance(position, valeur, couleur):
    x = position.x * TAILLE + TAILLE // 2 + hors_champ
    y = position.y * TAILLE + TAILLE // 2 + hors_champ
    texte = canevas.create_text(x, y, text=str(valeur), fill=couleur)
    elements_distances.append(texte)
    return texte

def effacer_distances():
    for element in elements_distances:
        canevas.delete(element)
    while len(elements_distances) > 0:
        elements_distances.pop()

def creer_labyrinthe():
    global labyrinthe, TAILLE, hors_champ
    if not parcours_en_cours:
        label_erreur.config(text="Erreur : un parcours est en cours", fg="red")
        return
    taille_saisie = int(entry_N.get())
    TAILLE = int(entry_taille.get())
    if not taille_valide(taille_saisie, TAILLE):
        label_erreur.config(text="Erreur : labyrinthe trop grand (550x550 max)", fg="red")
        return
    else:
        label_erreur.config(text="")
    canevas.config(width=700, height=700)
    canevas.delete("all")
    hors_champ = 0
    labyrinthe = Labyrinthe(taille_saisie, canevas)
    labyrinthe.creation()


def lancement_dijkstra():
    if parcours_en_cours:
        label_erreur.config(text="Erreur : un parcours est en cours", fg="red")
        return
    if labyrinthe is None:
        label_erreur.config(text="Erreur : créez d'abord un labyrinthe", fg="red")
        return
    effacer_distances()
    labyrinthe.dijkstra()


def lancement_flood_fill():
    if parcours_en_cours:
        label_erreur.config(text="Erreur : un parcours est en cours", fg="red")
        return
    if labyrinthe is None:
        label_erreur.config(text="Erreur : créez d'abord un labyrinthe", fg="red")
        return
    effacer_distances()
    labyrinthe.flood_fill()
    labyrinthe.parcours_flood_fill()


def lancement_main_droite():
    global parcours_en_cours
    if labyrinthe is None:
        label_erreur.config(text="Erreur : créez d'abord un labyrinthe", fg="red")
        return
    if parcours_en_cours:
        label_erreur.config(text="Erreur : un parcours est déjà en cours", fg="red")
        return
    parcours_en_cours = True
    label_erreur.config(text="")
    effacer_distances()
    labyrinthe.main_droite()
    parcours_en_cours = False



# Vérification de la validité des dimensions du labyrinthe
def taille_valide(taille_labyrinthe, taille_cellule):
    # Calcul de la taille totale du labyrinthe
    largeur = taille_labyrinthe * taille_cellule
    hauteur = taille_labyrinthe * taille_cellule
    # Vérifie si la largeur ou la hauteur dépasse 700 pixels
    if largeur > 550 or hauteur > 550:
        return False
    return True

# Modification de la fonction creer_labyrinthe
def creer_labyrinthe():
    global labyrinthe, TAILLE, hors_champ, hors_champ
    taille_saisie = int(entry_N.get())  # Taille du labyrinthe N
    TAILLE = int(entry_taille.get())  # Taille de la cellule

    # Vérifie si la taille du labyrinthe et des cellules est valide
    if not taille_valide(taille_saisie, TAILLE):
        label_erreur.config(text="Erreur : labyrinthe trop grand (550x550 max)", fg="red")
        return
    else:
        label_erreur.config(text="")  # Efface le message si tout est ok
    canevas.config(width=700, height=700)
    canevas.delete("all")
    hors_champ = 3
    labyrinthe = Labyrinthe(taille_saisie, canevas)
    labyrinthe.creation()


# Interface Tkinter
fenetre = Tk()
fenetre.title("Projet Labyrinthe")
fenetre.config(height=700, width=700)

label_N = Label(fenetre, text="Taille du labyrinthe (N x N):")
label_N.place(x=10, y=10)

entry_N = Entry(fenetre, width=5)
entry_N.insert(0, "10")
entry_N.place(x=200, y=10)

label_taille = Label(fenetre, text="Taille d'une cellule:")
label_taille.place(x=10, y=40)

entry_taille = Entry(fenetre, width=5)
entry_taille.insert(0, "30")
entry_taille.place(x=200, y=40)

btn_creer = Button(fenetre, text="Créer Labyrinthe", command=creer_labyrinthe)
btn_creer.place(x=10, y=80)

btn_dijkstra = Button(fenetre, text="Dijkstra", command=lancement_dijkstra)
btn_dijkstra.place(x=130, y=80)

btn_flood = Button(fenetre, text="Flood Fill", command=lancement_flood_fill)
btn_flood.place(x=230, y=80)

btn_main = Button(fenetre, text="Main Droite", command=lancement_main_droite)
btn_main.place(x=330, y=80)

label_erreur = Label(fenetre, text="", fg="red")
label_erreur.place(x=270, y=25)

canevas = Canvas(fenetre)
canevas.place(x=150, y=150, width=700, height=700)

fenetre.mainloop()

