#04/01/2025
from tkinter import *
from math import *

# Categorie Recursif
def Recursif(): # fait aparaitre les choix pour la recursiviter
    Effacer_Tout()
    Texplication1.place(x=350, y=50 ,anchor="c")
    Bchoix1.place(x= 350, y = 200,anchor="c")
    Bchoix2.place(x= 350, y = 400,anchor="c")

# Sierpinsky
def Milieu(A, B): # calcule le mileu
    return {'x': (A['x'] + B['x']) // 2, 'y': (A['y'] + B['y']) // 2}

def Sierpinsky(A, B, C, n,c): # utilise la recursiviter pour Sierpinsky
    if n == 0:
        print(c)
        Canevas.create_polygon(A['x'], A['y'], B['x'], B['y'], C['x'], C['y'],fill=c)
    else:
        Sierpinsky(A, Milieu(A, B), Milieu(A, C), n - 1,c)
        Sierpinsky(B, Milieu(B, A), Milieu(B, C), n - 1,c)
        Sierpinsky(C, Milieu(C, A), Milieu(C, B), n - 1,c)

def Nombre_iteration_Sierpinsky(): # nombre maximun pour le choix Sierpinsky
    global nb_Sierpinsky
    nb_Sierpinsky = nb_Sierpinsky + 1
    if nb_Sierpinsky == 7:
        nb_Sierpinsky = 0
    print(nb_Sierpinsky)
    Bnombre_Sierpinsky.config(text=nb_Sierpinsky)

def Couleur_Sierpinsky():  # couleur pour le choix Sierpinsky
    global index_couleur,couleur_Sierpinsky
    # Met à jour l'index pour la prochaine couleur
    index_couleur = (index_couleur + 1) % len(liste_couleurs)
    # Met à jour le texte du bouton avec la nouvelle couleur
    Bcouleur_Sierpinsky.config(text=liste_couleurs[index_couleur])
    couleur_Sierpinsky = liste_couleurs[index_couleur]

def Pour_Sierpinsky():  # fait aparaitre les bouton pour Sierpinsky
    Bnombre_Sierpinsky.config(text=nb_Sierpinsky,command=Nombre_iteration_Sierpinsky)
    Bnombre_Sierpinsky.place(x=420, y=230, anchor="c")
    Tnombre_Sierpinsky.place(x=335, y=230, anchor="c")
    Tcouleur_Sierpinsky.place(x=335, y=260, anchor="c")
    Bcouleur_Sierpinsky.config(text=liste_couleurs[0],command=Couleur_Sierpinsky)
    Bcouleur_Sierpinsky.place(x=420, y=260, anchor="c")
    Bvalider_Sierpinsky.place(x=350, y=300, anchor="c")
def Valider_Sierpinsky(): # permet de valider le choix Sierpinsky
    global nb_Sierpinsky, couleur_Sierpinsky
    Effacer_Tout()
    print(couleur_Sierpinsky)
    couleurS = Couleur_Tout(couleur_Sierpinsky)
    print(couleurS)
    print(nb_Sierpinsky)
    Sierpinsky({'x': 5, 'y': 650}, {'x': 350, 'y': 5}, {'x': 695, 'y': 650}, nb_Sierpinsky, couleurS)


#  Flocon de Koch
class Point: # class Point pour le Flocon de Koch
    def __init__(self,x,y):
        self.x, self.y = x, y
class Vecteur: # class Vecteur pour le Flocon de Koch
    def __init__(self,A,B):
        self.A, self.B = A, B
        self.x, self.y = B.x - A.x, B.y - A.y
    def rot(self,angle):
        x = int(((cos(angle)*self.x-sin(angle)*self.y))/3)
        y = int(((sin(angle)*self.x+cos(angle)*self.y))/3)
        return Vecteur(Point(0, 0), Point(x, y))
    def homo(self,k):
        x, y = int(self.x * k), int(self.y * k)
        return Vecteur(Point(0, 0), Point(x, y))
    def dessine(self,c):
        xA, yA, xB, yB = self.A.x, self.A.y, self.B.x, self.B.y
        Canevas.create_line(xA, yA, xB, yB, fill=c, width=3)

def Segment(A1,A2,n,c): # def Segment pour cree des Segment et pouvoir faire le Flocon de Koch
    V = Vecteur(A1, A2)
    if n==0: V.dessine(c)
    else:
        A4 = Point(A1.x + V.homo(1/3).x , A1.y + V.homo(1/3).y)
        A5 = Point(A1.x + V.homo(2/3).x , A1.y + V.homo(2/3).y)
        A3 = Point(A4.x + V.rot(pi/3).x , A4.y + V.rot(pi/3).y)
        Segment(A1,A4,n-1,c)
        Segment(A4,A3,n-1,c)
        Segment(A3,A5,n-1,c)
        Segment(A5,A2,n-1,c)

def Nombre_iteration_Flocon(): # nombre maximun pour le choix Flocon
    global nb_Flocon
    nb_Flocon = nb_Flocon + 1
    if nb_Flocon == 7:
        nb_Flocon = 0
    print(nb_Flocon)
    Bnombre_Flocon.config(text=nb_Flocon)

def Couleur_Flocon():  # couleur pour le choix Flocon
    global index_couleur,couleur_Flocon
    # Met à jour l'index pour la prochaine couleur
    index_couleur = (index_couleur + 1) % len(liste_couleurs)
    # Met à jour le texte du bouton avec la nouvelle couleur
    Bcouleur_Flocon.config(text=liste_couleurs[index_couleur])
    couleur_Flocon = liste_couleurs[index_couleur]
def Pour_Flocon(): # fait aparaitre les bouton pour Flocon
    Bnombre_Flocon.config(text=nb_Flocon,command=Nombre_iteration_Flocon)
    Bnombre_Flocon.place(x=420, y=430, anchor="c")
    Tnombre_Flocon.place(x=335, y=430, anchor="c")
    Tcouleur_Flocon.place(x=335, y=460, anchor="c")
    Bcouleur_Flocon.config(text=liste_couleurs[0],command=Couleur_Flocon)
    Bcouleur_Flocon.place(x=420, y=460, anchor="c")
    Bvalider_Flocon.place(x=350, y=500, anchor="c")

def Valider_Flocon():  # permet de valider le choix Flocon
    global nb_Flocon,couleur_Flocon
    Effacer_Tout()
    n = 100
    A1, A2, A3 = Point(5+n, 650-n), Point(350, 5+n/4), Point(695-n, 650-n)
    couleurF = Couleur_Tout(couleur_Flocon)
    print(couleurF)
    print(nb_Flocon)
    Segment(A2, A1, nb_Flocon,couleurF)
    Segment(A1, A3, nb_Flocon,couleurF)
    Segment(A3, A2, nb_Flocon,couleurF)

# Categorie L_systeme

def L_systeme(): # fait aparaitre les choix pour le L_systeme
    Effacer_Tout()
    Texplication2.place(x=350, y=50 ,anchor="c")
    Bchoix3.place(x= 350, y = 100,anchor="c")
    Bchoix4.place(x= 350, y = 300,anchor="c")
    Bchoix5.place(x= 350, y = 500-40,anchor="c")

class File:  # class File pour le L_systeme
    def __init__(self):
        self.valeurs = []
    def enfile(self, valeur):
        self.valeurs.append(valeur)
    def defile(self):
        if self.valeurs:
            return self.valeurs.pop(0)
    def est_vide(self):
        return self.valeurs == []
    def longueur(self):
        return len(self.valeurs)
    def __str__(self):
        ch = ""
        for x in self.valeurs:
            ch = ch + " <- " + str(x)
        return  ch

class coord: # class coord pour le L_systeme
    def __init__(self,i,j):
        self.x = i
        self.y = j
    def __add__(self, other):
        return coord(self.x+ other.x, self.y+other.y)
    def __sub__(self, other):
        return coord(self.x - other.x, self.y - other.y)
    def __mul__(self, other:int):
        return coord( self.x * other, self.y * other)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return "( "+str(self.x)+" ; "+str(self.y)+" )"

class crayon: # class crayon pour le L_systeme
    def __init__(self, xx,  yy, couleur ):
        self.pos = coord(xx , yy )
        self.couleur = couleur
        self.ang = 0
        self.dir = coord(1,0)
    def tourne(self, angle):
        self.ang = self.ang + angle
        self.dir = coord(cos((self.ang/180)*pi), sin((self.ang/180)*pi))
    def avance(self,distance):
        p = self.pos
        self.pos = self.pos + self.dir * distance
        return Canevas.create_line(p.x,p.y,self.pos.x,self.pos.y,fill=self.couleur)

def iter_L_systeme(F1, regle, n): # def L_systeme pour cree la recursiviter
    if n == 0:
        return F1
    F2 = File()
    while not F1.est_vide():
        alpha = F1.defile()
        # Vérifiez chaque caractère dans alpha avant de l'utiliser
        if alpha in regle:
            for c in regle[alpha]:
                F2.enfile(c)
        else:
            # Si alpha n'est pas dans regle, ajoutez-le tel quel
            F2.enfile(alpha)
    return iter_L_systeme(F2, regle, n - 1)


# Gosper
def Nombre_iteration_Gosper(): # nombre maximun pour le choix Gosper

    global nb_Gosper
    nb_Gosper = nb_Gosper + 1
    if nb_Gosper == 5:
        nb_Gosper = 0
    print(nb_Gosper)
    Bnombre_Gosper.config(text=nb_Gosper)

def Couleur_Gosper(): # couleur pour le choix Gosper
    global index_couleur,couleur_Gosper
    # Met à jour l'index pour la prochaine couleur
    index_couleur = (index_couleur + 1) % len(liste_couleurs)
    # Met à jour le texte du bouton avec la nouvelle couleur
    Bcouleur_Gosper.config(text=liste_couleurs[index_couleur])
    couleur_Gosper = liste_couleurs[index_couleur]

def Pour_Gosper(): # fait aparaitre les bouton pour Gosper
    Bnombre_Gosper.config(text=nb_Gosper,command=Nombre_iteration_Gosper)
    Bnombre_Gosper.place(x=420, y=130, anchor="c")
    Tnombre_Gosper.place(x=335, y=130, anchor="c")
    Tcouleur_Gosper.place(x=335, y=160, anchor="c")
    Bcouleur_Gosper.config(text=liste_couleurs[0],command=Couleur_Gosper)
    Bcouleur_Gosper.place(x=420, y=160, anchor="c")
    Bvalider_Gosper.place(x=350, y=200, anchor="c")
def Valider_Gosper(): # permet de valider le choix Gosper
    global nb_Gosper, couleur_Gosper
    Effacer_Tout()
    print(couleur_Gosper)
    couleurG = Couleur_Tout(couleur_Gosper)
    print(couleurG)
    print(nb_Gosper)
    dessiner_Gosper(nb_Gosper, 10, couleurG)

def dessiner_Gosper(n, taille,c): # cree le dessin pour Gosper
    regle_gosper = {"début": 'A', 'A': 'ADBDDBGAGGAAGBD', 'B': 'GADBBDDBDAGGAGB'}
    schema_gosper = File()
    for d in regle_gosper['début']: schema_gosper.enfile(d)
    resultat_gosper = iter_L_systeme(schema_gosper, regle_gosper, n)
    crayon_gosper = crayon(450, 150, c)
    for d in resultat_gosper.valeurs:
        if d == "A" or d == "B":
            crayon_gosper.avance(taille)
        elif d == "D":
            crayon_gosper.tourne(60)
        elif d == "G":
            crayon_gosper.tourne(-60)

# Hilbert
def Nombre_iteration_Hilbert(): # nombre maximun pour le choix Hilbert
    global nb_Hilbert
    nb_Hilbert = nb_Hilbert + 1
    if nb_Hilbert == 6:
        nb_Hilbert = 0
    print(nb_Hilbert)
    Bnombre_Hilbert.config(text=nb_Hilbert)

def Couleur_Hilbert(): # couleur pour le choix Hilbert
    global index_couleur,couleur_Hilbert
    # Met à jour l'index pour la prochaine couleur
    index_couleur = (index_couleur + 1) % len(liste_couleurs)
    # Met à jour le texte du bouton avec la nouvelle couleur
    Bcouleur_Hilbert.config(text=liste_couleurs[index_couleur])
    couleur_Hilbert = liste_couleurs[index_couleur]

def Pour_Hilbert(): # fait aparaitre les bouton pour Hilbert
    Bnombre_Hilbert.config(text=nb_Hilbert,command=Nombre_iteration_Hilbert)
    Bnombre_Hilbert.place(x=420, y=330, anchor="c")
    Tnombre_Hilbert.place(x=335, y=330, anchor="c")
    Tcouleur_Hilbert.place(x=335, y=360, anchor="c")
    Bcouleur_Hilbert.config(text=liste_couleurs[0], command=Couleur_Hilbert)
    Bcouleur_Hilbert.place(x=420, y=360, anchor="c")
    Bvalider_Hilbert.place(x=350, y=400, anchor="c")

def Valider_Hilbert(): # permet de valider le choix Hilbert
    global nb_Hilbert, couleur_Hilbert
    Effacer_Tout()
    print(couleur_Hilbert)
    couleurH = Couleur_Tout(couleur_Hilbert)
    print(couleurH)
    print(nb_Hilbert)
    dessiner_Hilbert(nb_Hilbert, 10,couleurH)

def dessiner_Hilbert(n, taille,c): # cree le dessin pour Hilbert
    regle_hilbert = {"début": 'L', 'L': 'GRFDLFLDFRG', 'R': 'DLFGRFRGFLD'}
    schema_hilbert = File()
    for d in regle_hilbert['début']: schema_hilbert.enfile(d)
    resultat_hilbert = iter_L_systeme(schema_hilbert, regle_hilbert, n)
    crayon_hilbert = crayon(250, 450, c)
    for d in resultat_hilbert.valeurs:
        if d == "F":
            crayon_hilbert.avance(taille)
        elif d == "D":
            crayon_hilbert.tourne(90)
        elif d == "G":
            crayon_hilbert.tourne(-90)

# Choix utilisateur

def Nombre_iteration_utilisateur(): # nombre maximun pour le choix utilisateur
    global nb_utilisateur
    nb_utilisateur = nb_utilisateur + 1
    if nb_utilisateur == 6:
        nb_utilisateur = 0
    print(nb_utilisateur)
    Bnombre_utilisateur.config(text=nb_utilisateur)

def Couleur_utilisateur():# couleur pour le choix utilisateur
    global index_couleur,couleur_utilisateur
    # Met à jour l'index pour la prochaine couleur
    index_couleur = (index_couleur + 1) % len(liste_couleurs)
    # Met à jour le texte du bouton avec la nouvelle couleur
    Bcouleur_utilisateur.config(text=liste_couleurs[index_couleur])
    couleur_utilisateur = liste_couleurs[index_couleur]

def Choix_utilisateur(): # recupere les information donner par l utilisateur
    texte1 = Echoix_utilisateur.get()  # Récupère le texte saisi
    texte2 = Eregle_utilisateur1.get()
    texte3 = Eregle_utilisateur2.get()

    if Verifiacation_text(texte1) and Verifiacation_text(texte2) and Verifiacation_text(texte3):
        return texte1, texte2, texte3, True  # Retourne aussi True en cas de succès
    else:
        return False  # Retourne False en cas d'erreur

def Verifiacation_text(texte): # verifi si l utilisateur utilise les caractere adapter
    if not texte:  # Vérifie si le texte est vide
        return False
    for c in texte:
        if c not in 'ABDG':  # Si le caractère n'est pas dans 'ABDG', retourne False
            return False
    return True  # Si tous les caractères sont valides
def Pour_utilisateur(): # fait aparaitre les bouton pour utilisateur
    Bnombre_utilisateur.config(text=nb_utilisateur,command=Nombre_iteration_utilisateur)
    Bnombre_utilisateur.place(x=420, y=530-40, anchor="c")
    Tnombre_utilisateur.place(x=335, y=530-40, anchor="c")
    Tcouleur_utilisateur.place(x=335, y=560-40, anchor="c")
    Bcouleur_utilisateur.config(text=liste_couleurs[0], command=Couleur_utilisateur)
    Bcouleur_utilisateur.place(x=420, y=560-40, anchor="c")

    Tchoix_utilisateur.place(x=260, y=590 - 40, anchor="c")
    Echoix_utilisateur.place(x=590, y=590 - 40, anchor="c")
    Tregle_utilisateur.place(x=350, y=610 - 40, anchor="c")
    Tregle_utilisateur1.place(x=310, y=635 - 40, anchor="c")
    Eregle_utilisateur1.place(x=440, y=635 - 40, anchor="c")
    Tregle_utilisateur2.place(x=310, y=660 - 40, anchor="c")
    Eregle_utilisateur2.place(x=440, y=660 - 40, anchor="c")

    Bvalider_utilisateur.place(x=350, y=680, anchor="c")

def Valider_utilisateur(): # permet de valider le choix utilisateur
    global nb_utilisateur, couleur_utilisateur
    result = Choix_utilisateur()
    if result and result[3] == True:  # Vérifie si la fonction a retourné un tuple avec True à la fin
        Effacer_Tout()
        print(couleur_utilisateur)
        couleurH = Couleur_Tout(couleur_utilisateur)
        print(couleurH)
        print(nb_utilisateur)
        dep, reg1, reg2 = result[:3]  # Récupère les trois premiers éléments du tuple
        print(dep, " ", reg1, " ", reg2)
        dessiner_utilisateur(nb_utilisateur, 15, couleurH, dep, reg1, reg2)
    else:
        Tattention.place(x=350, y=670 - 20, anchor="c")

def dessiner_utilisateur(n, taille, c, dep, reg1, reg2): # cree le dessin pour utilisateur
    # Définir les règles pour l'utilisateur
    regle_utilisateur = {"début": dep, 'A': reg1, 'B': reg2}
    # Initialisation du schéma
    schema_utilisateur = File()
    for d in regle_utilisateur['début']:
        schema_utilisateur.enfile(d)
    # Appliquer les itérations du L-système
    resultat_utilisateur = iter_L_systeme(schema_utilisateur, regle_utilisateur, n)
    # Création d'un crayon pour dessiner
    crayon_utilisateur = crayon(150, 550, c)
    # Dessiner en fonction des résultats
    for d in resultat_utilisateur.valeurs:
        if d == "A" or d == "B" :
            crayon_utilisateur.avance(taille)
        elif d == "D" :
            crayon_utilisateur.tourne(90)
        elif d == "G":
            crayon_utilisateur.tourne(-90)

# Categorie Pliages

class Pile: # class File pour le Pliages
    def __init__(self):
        self.valeurs = []
    def empile(self, valeur):
        self.valeurs.append(valeur)
    def depile(self):
        if self.valeurs: return self.valeurs.pop()
    def est_vide(self):
        return self.valeurs == []
    def longueur(self):
        return len(self.valeurs)

    def chercher(self):
        # Retourne l'element au sommet de la pile sans le retirer
        if not self.est_vide():
            return self.valeurs[-1]
        return None
    def __str__(self):
        ch = ""
        for x in self.valeurs:
           ch = "| " + str(x) + " |" + "\n" + ch
        return ch + " ⎺⎺⎺⎺⎺⎺⎺⎺⎺\n"

def Pliages(): # fait aparaitre les choix pour les Pliages
    Effacer_Tout()
    Texplication3.place(x=350, y=50 ,anchor="c")
    Bchoix6.place(x= 350, y = 200,anchor="c")
    Bchoix7.place(x= 350, y = 400,anchor="c")

# Dragon

def Nombre_iteration_Dragon(): # nombre maximun pour le choix Dragon
    global nb_Dragon
    nb_Dragon = nb_Dragon + 1
    if nb_Dragon == 10:
        nb_Dragon = 0
    print(nb_Dragon)
    Bnombre_Dragon.config(text=nb_Dragon)

def Couleur_Dragon():# couleur pour le choix Dragon
    global index_couleur,couleur_Dragon
    # Met à jour l'index pour la prochaine couleur
    index_couleur = (index_couleur + 1) % len(liste_couleurs)
    # Met à jour le texte du bouton avec la nouvelle couleur
    Bcouleur_Dragon.config(text=liste_couleurs[index_couleur])
    couleur_Dragon = liste_couleurs[index_couleur]

def Pour_Dragon():# fait aparaitre les bouton pour Dragon
    Bnombre_Dragon.config(text=nb_Dragon, command=Nombre_iteration_Dragon)
    Bnombre_Dragon.place(x=420, y=230, anchor="c")
    Tnombre_Dragon.place(x=335, y=230, anchor="c")
    Tcouleur_Dragon.place(x=335, y=260, anchor="c")
    Bcouleur_Dragon.config(text=liste_couleurs[0], command=Couleur_Dragon)
    Bcouleur_Dragon.place(x=420, y=260, anchor="c")
    Bvalider_Dragon.place(x=350, y=300, anchor="c")

def Valider_Dragon(): # permet de valider le choix Dragon
    global nb_Dragon, couleur_Dragon
    Effacer_Tout()
    print(couleur_Dragon)
    couleurD = Couleur_Tout(couleur_Dragon)
    print(couleurD)
    print(nb_Dragon)
    MonCrayon = crayon(350, 300, couleurD)
    Pliage = PliageDragon(nb_Dragon)
    taille = 10
    dessiner_pliage(Pliage, MonCrayon, taille)

def PliageDragon(n, chemin = File()): # cree le motif pour le pliage dragon
    if chemin.est_vide() :
        chemin = File()
        chemin.enfile("D")
    if n == 0 : return chemin
    D, F, P = {"D": "G", "G": "D"}, File(), Pile()
    while not chemin.est_vide():
        c = chemin.defile()
        F.enfile(c)
        P.empile(D[c])
    F.enfile("D")
    while not P.est_vide():
        c = P.depile()
        F.enfile(c)
    return PliageDragon(n-1, F)

def dessiner_pliage(Pliage, crayon, taille): # dessin le pliage dragon
       while not Pliage.est_vide():
        a = Pliage.defile()
        if a == "D":
            crayon.tourne(90)
        elif a == "G":
            crayon.tourne(-90)
        crayon.avance(taille)

# Spirale

def Nombre_iteration_Spirale():# nombre maximun pour le choix Spirale
    global nb_Spirale
    nb_Spirale = nb_Spirale + 1
    if nb_Spirale == 10:
        nb_Spirale = 0
    print(nb_Spirale)
    Bnombre_Spirale.config(text=nb_Spirale)

def Couleur_Spirale():# couleur pour le choix Spirale
    global index_couleur,couleur_Spirale
    # Met à jour l'index pour la prochaine couleur
    index_couleur = (index_couleur + 1) % len(liste_couleurs)
    # Met à jour le texte du bouton avec la nouvelle couleur
    Bcouleur_Spirale.config(text=liste_couleurs[index_couleur])
    couleur_Spirale = liste_couleurs[index_couleur]

def Pour_Spirale():# fait aparaitre les bouton pour Spirale
    Bnombre_Spirale.config(text=nb_Spirale, command=Nombre_iteration_Spirale)
    Bnombre_Spirale.place(x=420, y=430, anchor="c")
    Tnombre_Spirale.place(x=335, y=430, anchor="c")
    Tcouleur_Spirale.place(x=335, y=460, anchor="c")
    Bcouleur_Spirale.config(text=liste_couleurs[0], command=Couleur_Spirale)
    Bcouleur_Spirale.place(x=420, y=460, anchor="c")
    Bvalider_Spirale.place(x=350, y=500, anchor="c")


def Valider_Spirale():# permet de valider le choix Spirale
    global nb_Spirale, couleur_Spirale
    Effacer_Tout()
    print(couleur_Spirale)
    couleurS = Couleur_Tout(couleur_Spirale)
    print(couleurS)
    print(nb_Spirale)
    MonCrayon = crayon(350, 200, couleurS)
    Pliage = PliageSpirale(nb_Spirale)
    taille = 20
    dessiner_pliage_spirale(Pliage, MonCrayon, taille)


def PliageSpirale(n, chemin=File()): # cree le motif pour le pliage Spirale
    if chemin.est_vide():
        chemin = File()
        chemin.enfile("A")  # On commence avec "A" comme symbole initial
    if n == 0:
        return chemin
    S = {"A": "AADB", "BGAG": "B"}
    F = File()  # File pour stocker la chaîne générée
    P = Pile()  # Pile utilisée pour les transformations
    while not chemin.est_vide():
        c = chemin.defile()
        if c in S:
            for char in S[c]:
                F.enfile(char)
        else:
            F.enfile(c)
    return PliageSpirale(n - 1, F)


def dessiner_pliage_spirale(pliage, crayon, taille, angle=90):  # dessin le pliage dragon
    global tour
    while not pliage.est_vide():
        c = pliage.defile()
        if c == "A":
            tour = (tour + taille)/2
            taille = tour
            crayon.avance(taille)
        elif c == "D":
            crayon.tourne(angle)
        elif c == "G":
            crayon.tourne(-angle)

# Pour Tout

def fenetre_basse(): # premiere fenetre
    Effacer_Tout()
    Bretour.place_forget()
    Tinfo.place(x=350, y=50, anchor="c")
    Bmethode1.place(x=350, y=200, anchor="c")
    Bmethode2.place(x=350, y=400, anchor="c")
    Bmethode3.place(x=350, y=600, anchor="c")
    Canevas.delete("all")

def Couleur_Tout(couleurs): # changer de couleur
    global couleur
    if couleurs == liste_couleurs[0]:
        couleur = "red"
    if couleurs == liste_couleurs[1]:
        couleur = "green"
    if couleurs == liste_couleurs[2]:
        couleur = "blue"
    if couleurs == liste_couleurs[3]:
        couleur = "yellow"
    if couleurs == liste_couleurs[4]:
        couleur = "orange"
    if couleurs == liste_couleurs[5]:
        couleur = "purple"
    if couleurs  == liste_couleurs[6]:
        couleur = "black"

    return couleur

def Effacer_Tout():  # effacer tout les element present
    Bretour.place(x=700, y=0, anchor="ne") # placer le bouton retour qui permet de revenir a la fenetre principal
    Tinfo.place_forget()
    Bmethode1.place_forget()
    Bmethode2.place_forget()
    Bmethode3.place_forget()
    Texplication1.place_forget()
    Texplication2.place_forget()
    Texplication3.place_forget()
    Bchoix1.place_forget()
    Bchoix2.place_forget()
    Bchoix3.place_forget()
    Bchoix4.place_forget()
    Bchoix5.place_forget()
    Bchoix6.place_forget()
    Bchoix7.place_forget()

    Bnombre_Sierpinsky.place_forget()
    Tnombre_Sierpinsky.place_forget()
    Bvalider_Sierpinsky.place_forget()
    Tcouleur_Sierpinsky.place_forget()
    Bcouleur_Sierpinsky.place_forget()

    Bnombre_Flocon.place_forget()
    Tnombre_Flocon.place_forget()
    Bvalider_Flocon.place_forget()
    Tcouleur_Flocon.place_forget()
    Bcouleur_Flocon.place_forget()

    Bnombre_Gosper.place_forget()
    Tnombre_Gosper.place_forget()
    Bvalider_Gosper.place_forget()
    Tcouleur_Gosper.place_forget()
    Bcouleur_Gosper.place_forget()

    Bnombre_Hilbert.place_forget()
    Tnombre_Hilbert.place_forget()
    Bvalider_Hilbert.place_forget()
    Tcouleur_Hilbert.place_forget()
    Bcouleur_Hilbert.place_forget()

    Bnombre_utilisateur.place_forget()
    Tnombre_utilisateur.place_forget()
    Tcouleur_utilisateur.place_forget()
    Bcouleur_utilisateur.place_forget()
    Tchoix_utilisateur.place_forget()
    Echoix_utilisateur.place_forget()
    Tregle_utilisateur.place_forget()
    Tregle_utilisateur1.place_forget()
    Eregle_utilisateur1.place_forget()
    Tregle_utilisateur2.place_forget()
    Eregle_utilisateur2.place_forget()
    Bvalider_utilisateur.place_forget()
    Tattention.place_forget()


    Bnombre_Dragon.place_forget()
    Tnombre_Dragon.place_forget()
    Bvalider_Dragon.place_forget()
    Tcouleur_Dragon.place_forget()
    Bcouleur_Dragon.place_forget()

    Bnombre_Spirale.place_forget()
    Tnombre_Spirale.place_forget()
    Bvalider_Spirale.place_forget()
    Tcouleur_Spirale.place_forget()
    Bcouleur_Spirale.place_forget()


# Création de la fenêtre
fenetre = Tk()
fenetre.config(height=700, width=700, bg="cyan")

Canevas = Canvas(fenetre, height=700, width=700, bg="cyan")
Canevas.place(x=0, y=0)

# inisalisation
tour,index_couleur = 0,0
nb_Sierpinsky ,nb_Flocon ,nb_Gosper ,nb_Hilbert ,nb_utilisateur ,nb_Dragon ,nb_Spirale = 1,1,1,1,1,1,1
liste_couleurs = ["Rouge", "Vert", "Bleu", "Jaune", "Orange", "Violet","noir"]
couleur_Sierpinsky,couleur_Flocon,couleur_Gosper,couleur_Hilbert,couleur_utilisateur,couleur_Dragon,couleur_Spirale =\
    liste_couleurs[0],liste_couleurs[0],liste_couleurs[0],liste_couleurs[0],liste_couleurs[0],liste_couleurs[0],liste_couleurs[0]


# Fenetre principal

Tinfo = Label(text="Bienvenue dans une interface permetent de tracer des fractals\n"
                   "avec les trois méthodes de génération deferente", font=("Arial", 13))
Tinfo.place(x=350, y=50 ,anchor="c")

Bmethode1 = Button(text="Mode : Fonction Récursives", font=("Arial", 13),command=Recursif)
Bmethode1.place(x= 350, y = 200,anchor="c")
Bmethode2 = Button(text="Mode : L_Systeme", font=("Arial", 13),command=L_systeme)
Bmethode2.place(x= 350, y = 400,anchor="c")
Bmethode3= Button(text="Mode :  Pliages", font=("Arial", 13),command=Pliages)
Bmethode3.place(x= 350, y = 600,anchor="c")

Bretour = Button(text="retour", font=("Arial", 13),command=fenetre_basse)
Bretour.place_forget()
# Fenetre secondaire n°1

# Recursif
Texplication1 = Label(text="Vous avez choisie le mode Fonction Récursives\n"
    "Vous pouvez donc choisir entre triangle de Sierpinsky ou le flocon de Koch.", font=("Arial", 13))
Texplication1.place_forget()
# triangle de Sierpinsky
Bchoix1 = Button(text= "triangle de Sierpinsky", font=("Arial", 13),command=Pour_Sierpinsky)
Bchoix1.place_forget()

Bnombre_Sierpinsky = Button(text=0, font=("Arial", 9))
Bnombre_Sierpinsky.place_forget()
Tnombre_Sierpinsky = Label(text="nombre d'iteration:", font=("Arial", 13))
Tnombre_Sierpinsky.place_forget()
Bvalider_Sierpinsky = Button(text="Valider", font=("Arial", 13),command=Valider_Sierpinsky)
Bvalider_Sierpinsky.place_forget()
Tcouleur_Sierpinsky = Label(text="Couleur:", font=("Arial", 13))
Tcouleur_Sierpinsky.place_forget()
Bcouleur_Sierpinsky = Button(text=liste_couleurs[0],font=("Arial", 13),command=Couleur_Sierpinsky)
Bcouleur_Sierpinsky.place_forget()


# Flocon de Koch
Bchoix2 = Button(text= "flocon de Koch", font=("Arial", 13),command=Pour_Flocon)
Bchoix2.place_forget()

Bnombre_Flocon = Button(text=0, font=("Arial", 9))
Bnombre_Flocon.place_forget()
Tnombre_Flocon = Label(text="nombre d'iteration:", font=("Arial", 13))
Tnombre_Flocon.place_forget()
Bvalider_Flocon = Button(text="Valider", font=("Arial", 13),command=Valider_Flocon)
Bvalider_Flocon.place_forget()
Tcouleur_Flocon = Label(text="Couleur:", font=("Arial", 13))
Tcouleur_Flocon.place_forget()
Bcouleur_Flocon = Button(text="", font=("Arial", 13),command=Couleur_Flocon)
Bcouleur_Flocon.place_forget()

# Fenetre secondaire n°2

# L_systeme
Texplication2 = Label(text="Vous avez choisie le mode L_systeme\n"
    "Vous pouvez donc choisir entre la courbe de Gosper ou la courbe de Hilbert .", font=("Arial", 13))
Texplication2.place_forget()


# Courbe de Gosper
Bchoix3 = Button(text= "Courbe de Gosper", font=("Arial", 13),command=Pour_Gosper)
Bchoix3.place_forget()

Bnombre_Gosper = Button(text=0, font=("Arial", 9))
Bnombre_Gosper.place_forget()
Tnombre_Gosper = Label(text="nombre d'iteration:", font=("Arial", 13))
Tnombre_Gosper.place_forget()
Bvalider_Gosper = Button(text="Valider", font=("Arial", 13),command=Valider_Gosper)
Bvalider_Gosper.place_forget()
Tcouleur_Gosper = Label(text="Couleur:", font=("Arial", 13))
Tcouleur_Gosper.place_forget()
Bcouleur_Gosper = Button(text=liste_couleurs[0],font=("Arial", 13),command=Couleur_Gosper)
Bcouleur_Gosper.place_forget()


# Courbe de Hilbert
Bchoix4 = Button(text= "Courbe de Hilbert", font=("Arial", 13),command=Pour_Hilbert)
Bchoix4.place_forget()

Bnombre_Hilbert = Button(text=0, font=("Arial", 9))
Bnombre_Hilbert.place_forget()
Tnombre_Hilbert = Label(text="nombre d'iteration:", font=("Arial", 13))
Tnombre_Hilbert.place_forget()
Bvalider_Hilbert = Button(text="Valider", font=("Arial", 13),command=Valider_Hilbert)
Bvalider_Hilbert.place_forget()
Tcouleur_Hilbert = Label(text="Couleur:", font=("Arial", 13))
Tcouleur_Hilbert.place_forget()
Bcouleur_Hilbert = Button(text="", font=("Arial", 13),command=Couleur_Hilbert)
Bcouleur_Hilbert.place_forget()


# Courbe de l utilisateur
Bchoix5 = Button(text= "Choix de l'utilisateur", font=("Arial", 13),command=Pour_utilisateur)
Bchoix5.place_forget()

Bnombre_utilisateur = Button(text=0, font=("Arial", 9))
Bnombre_utilisateur.place_forget()
Tnombre_utilisateur = Label(text="nombre d'iteration:", font=("Arial", 13))
Tnombre_utilisateur.place_forget()
Tcouleur_utilisateur = Label(text="Couleur:", font=("Arial", 13))
Tcouleur_utilisateur.place_forget()
Bcouleur_utilisateur = Button(text="", font=("Arial", 13),command=Couleur_utilisateur)
Bcouleur_utilisateur.place_forget()
Bvalider_utilisateur = Button(text="Valider", font=("Arial", 13),command=Valider_utilisateur)
Bvalider_utilisateur.place_forget()

Tchoix_utilisateur = Label(text="Choisiser votre mot inisial(peut contenir que les lettres A,B,D,G):", font=("Arial", 13))
Tchoix_utilisateur.place_forget()
Echoix_utilisateur = Entry(font=("Arial", 13))
Echoix_utilisateur.place_forget()
Tregle_utilisateur = Label(text="Choisiser votre regle(peut contenir que les lettres A,B,D,G):", font=("Arial", 13))
Tregle_utilisateur.place_forget()
Tregle_utilisateur1 = Label(text="A -→ ", font=("Arial", 13))
Tregle_utilisateur1.place_forget()
Tregle_utilisateur2 = Label(text="B -→ ", font=("Arial", 13))
Tregle_utilisateur2.place_forget()
Eregle_utilisateur1 = Entry(font=("Arial", 13))
Eregle_utilisateur1.place_forget()
Eregle_utilisateur2 = Entry(font=("Arial", 13))
Eregle_utilisateur2.place_forget()

Tattention = Label(text="Vous devais utiliser les lettres A,B,D,G(en majuscule)", font=("Arial", 13),fg = "red",bg="cyan")
Tattention.place_forget()
# Fenetre tersiere n°3

# Pliages
Texplication3 = Label(text="Vous avez choisie le mode Pliages \n"
    "Vous pouvez donc choisir entre fractal Dragon ou ???????.", font=("Arial", 13))
Texplication3.place_forget()
# Fractal Dragon
Bchoix6 = Button(text= "Fractal Dragon", font=("Arial", 13),command=Pour_Dragon)
Bchoix6.place_forget()

Bnombre_Dragon = Button(text=0, font=("Arial", 9))
Bnombre_Dragon.place_forget()
Tnombre_Dragon = Label(text="nombre d'iteration:", font=("Arial", 13))
Tnombre_Dragon.place_forget()
Bvalider_Dragon = Button(text="Valider", font=("Arial", 13),command=Valider_Dragon)
Bvalider_Dragon.place_forget()
Tcouleur_Dragon = Label(text="Couleur:", font=("Arial", 13))
Tcouleur_Dragon.place_forget()
Bcouleur_Dragon = Button(text=liste_couleurs[0],font=("Arial", 13),command=Couleur_Dragon)
Bcouleur_Dragon.place_forget()

# Spirale
Bchoix7 = Button(text= "Splirale", font=("Arial", 13),command=Pour_Spirale)
Bchoix7.place_forget()

Bnombre_Spirale = Button(text=0, font=("Arial", 9))
Bnombre_Spirale.place_forget()
Tnombre_Spirale = Label(text="nombre d'iteration:", font=("Arial", 13))
Tnombre_Spirale.place_forget()
Bvalider_Spirale = Button(text="Valider", font=("Arial", 13),command=Valider_Spirale)
Bvalider_Spirale.place_forget()
Tcouleur_Spirale = Label(text="Couleur:", font=("Arial", 13))
Tcouleur_Spirale.place_forget()
Bcouleur_Spirale = Button(text=liste_couleurs[0],font=("Arial", 13),command=Couleur_Spirale)
Bcouleur_Spirale.place_forget()

fenetre.mainloop()
