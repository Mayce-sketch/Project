#27/11/2024
from tkinter import *

class Pile:
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

class File:
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

# Prend en paramètre une expression entrée par l’utilisateur et retourne une file contenant les différents éléments de l’expression.
def ExpVersFile(expression):
    file = File()
    nombre,virgule = "", 0
    for caractere in expression:
        # Verifie si le caractere fait partie des chiffres (0 a 9)
        if "0" <= caractere <= "9":
            nombre = nombre + caractere
        else:
            if nombre:
                file.enfile(int(nombre))  # Ajouter le nombre
                nombre = ""
            if caractere != ",":
                file.enfile(caractere)  # Ajoute les caractere comme +, -, *, etc.
            else:
                virgule = 1 # ajout d une variable virgule pour verifier si l utilisateur utilise du postfixer
    # Ajouter le dernier nombre s'il existe
    if nombre:
        file.enfile(int(nombre))
    if virgule >= 1 :
        print("poste fixer")
        return EvaluePF(file)
    else:
        print("poste infixer")
        return IF_vers_PF(file)

# Prend en paramètre une file représentant une expression postfixée et retourne la valeur de l’expression
def EvaluePF(file):
    global texpression
    print(file)
    pile = Pile()
    while not file.est_vide():
        element = file.defile()
        # Verifie si l'element est un nombre
        if "0" <= str(element)[0] <= "9":
            pile.empile(int(element))
        else:
            if pile.est_vide():
                # Retourne None si il y a pas assez de nombre
                texpression =  "tu n'a pas assez de nombre pour fair une operation"
                calcule.config(text=texpression)
                reinisaliser()
                return None
            if element == "²": # Carre
                nombre3 = pile.depile()  # Depile le nombre pour le mettre au carre
                pile.empile(round(nombre3 ** 2,2))

            elif element == "³":  # Cube
                nombre3 = pile.depile()  # Depile le nombre pour le mettre au cube
                pile.empile(round(nombre3 ** 3,2))
            elif element == "√":  # Racine
                nombre3 = pile.depile()  # Depile le nombre pour le mettre a la racine carre
                pile.empile(round(nombre3 ** 0.5,2))


            else:  # Pour les operations  (addition, soustraction, multiplication, division)
                nombre2 = pile.depile()  # Depile le second nombre
                if pile.est_vide():
                    texpression = "tu as mal ecrit ton expretion"
                    calcule.config(text=texpression)
                    reinisaliser()
                    return None  # Pas assez d'operandes pour effectuer l'operation

                nombre1 = pile.depile()  # Depile le premier nombre
            # Effectuer l'operation
            if element == "+":
                pile.empile(round(nombre1 + nombre2,2))
            elif element == "-":
                pile.empile(round(nombre1 - nombre2,2))
            elif element == "*":
                pile.empile(round(nombre1 * nombre2,2))
            elif element == "÷":
                # Verifie que le nombre n'est pas egal a zero avant de diviser
                if nombre2 == 0:
                    texpression = "tu ne peux diviser par 0"
                    calcule.config(text=texpression)
                    reinisaliser()
                    return None
                pile.empile(round(nombre1 / nombre2, 2))  # Division arrondie a 2 decimales

    # Verifie qu'il reste un seul element dans la pile (le resultat final)
    if pile.longueur() != 1 :
        # Retourne None en cas d'erreur (expression malformee)
        texpression = "tu as mal ecrit ton expretion"
        calcule.config(text=texpression)
        reinisaliser()
        return None
    resultat = pile.depile() # on deplie le resultat pour le recuperer
    print(resultat)
    texpression.append(resultat)
    calcule.config(text=texpression)
    return resultat  # Retourne le resultat final

# Prend en paramètre une file représentant une expression infixée et retourne une file représentant l’expression infixée.
def IF_vers_PF(file):
    print(file)
    # Priorite des operateurs
    priorites = {"+": 1, "-": 1, "*": 2, "÷": 2, "²": 3,"³":3,"√":3}
    pile = Pile()  # Pile pour les operateurs
    sortie = File()  # File pour l'expression postfixee

    while not file.est_vide():
        element = file.defile()

        # Si l'element est un nombre, on l'ajoute e la file de sortie
        if "0" <= str(element)[0] <= "9":
            sortie.enfile(element)

        # Si l'element est une parenthese ouvrante, on l'empile
        elif element == "(":
            pile.empile(element)

        # Si l'element est une parenthese fermante
        elif element == ")":
            # On depile jusqu'e trouver une parenthese ouvrante
            while not pile.est_vide() and pile.chercher() != "(":
                sortie.enfile(pile.depile())
            if not pile.est_vide() and pile.chercher() == "(":
                pile.depile()  # On enleve la parenthese ouvrante
        # Si l'element est un operateur
        elif element in priorites:
            # Tant qu'il y a un operateur sur la pile avec une priorite superieure ou egale
            while (not pile.est_vide() and pile.chercher() != "(" and
                   priorites[element] <= priorites.get(pile.chercher(), 0)):
                sortie.enfile(pile.depile())
            # On empile l'operateur actuel
            pile.empile(element)

    # Depiler tous les operateurs restants dans la pile
    while not pile.est_vide():
        sortie.enfile(pile.depile())
    print("fin : ", sortie)
    return EvaluePF(sortie) # On renvoit au postfixer pour finir le calcule

# Detecte chaque bouton cliquer
def cliquer(event):
    global expression, texpression
    bouton = event.widget # recupere le bouton appuier
    texte = bouton.cget("text") # recupere le texte
    print(texte)
    if texte == "R": # si R on reinisalise
        reinisaliser()
        calcule.config(text=texpression)
    elif texte == "<": # si < on enleve le dernier element
        expression.pop()  # Supprimer le dernier element de la liste
        texpression.pop()
        calcule.config(text=texpression)

    elif texte == "=" or texte == "≡": # si = ou ≡ appuier sa donne le resultat
        texpression.append(texte)
        calcule.config(text=texpression)
        ExpVersFile(expression) # lance le calcule
    else:
        # Ajouter un chiffre ou operateur a l'expression
        expression.append(texte)
        texpression.append(texte)
        calcule.config(text=texpression)
# definition pour reinisaliser l'expretion
def reinisaliser():
    global expression, texpression
    # Reinitialiser les expressions
    texpression = []
    expression = []

# definition pour cree la calculatrice
def cree_calcualtrice():
    Ltexte = ["0","1","2","3","4","5","6","7","8","9","+","-","*","÷",",","²","³","√","(",")","<","R","=","≡"]
    x1, y1 = 25, 70  # Coordonnees de depart
    x2, y2 = 100, 100  # Decalages en x et y
    k,n = 0,0  # Initialisation de k pour contrôler le nombre de rectangles par ligne
    for i in range(5):
        for j in range(5 - k):
            bouton = Button(text=Ltexte[n],bg = "#46ff4c", font=("Arial", 12 ),width=4,height=2) # placer les boutons
            bouton.bind("<Button-1>", cliquer)
            bouton.place(x = x1, y = y1)
            x1 = x1 + x2
            n  = n + 1
        x1 = 25 # les decalages
        y1 = y1 + y2
        if i == 3: # les iragulariter (la ligne de 4 au lieu de 5)
            k = 1
    calcule.place(x = 250, y = 555,anchor = "c")
    Nom.place(x = 250, y = 30,anchor = "c")


# Creation de la fenetre
fenetre = Tk()
fenetre.config(width=500, height=600, bg="black")

# Creation du canvas
canevas = Canvas(fenetre, width=510, height=600,bg="cyan")
canevas.place(x=-5, y=0,anchor ="nw")

expression,texpression = [], []
Nom = Label(text="Calculatrice", font=("Arial", 15),bg = "#05c8fc")
Nom.place_forget()
calcule  =Label(text="Le calcule s'afichera ici", font=("Arial", 12),bg = "#05c8fc",width=50,height=2)
calcule.place_forget()

# appele la definition pour lancer la calculatrice
cree_calcualtrice()


fenetre.mainloop()