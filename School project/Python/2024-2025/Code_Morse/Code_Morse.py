#23/01/2025
from tkinter import *
from pygame import mixer # pour le son
import time # pour le son

class Arbre:
    def __init__(self, valeur=None):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

class File:
    def __init__(self):
        self.elements = []

    def enfiler(self, element):
        self.elements.append(element)

    def defiler(self):
        if not self.est_vide():
            return self.elements.pop(0)
        return None

    def est_vide(self):
        return len(self.elements) == 0

    def contenu(self):
        return self.elements


def construire_arbre():
    racine = Arbre()
    codes = [
        ("A", "°-"), ("B", "-°°°"), ("C", "-°-°"), ("D", "-°°"),
        ("E", "°"), ("F", "°°-°"), ("G", "--°"), ("H", "°°°°"),
        ("I", "°°"), ("J", "°---"), ("K", "-°-"), ("L", "°-°°"),
        ("M", "--"), ("N", "-°"), ("O", "---"), ("P", "°--°"),
        ("Q", "--°-"), ("R", "°-°"), ("S", "°°°"), ("T", "-"),
        ("U", "°°-"), ("V", "°°°-"), ("W", "°--"), ("X", "-°°-"),
        ("Y", "-°--"), ("Z", "--°°")
    ]
    for lettre, code in codes:
        ajouter_noeud(racine, lettre, code)
    return racine

def ajouter_noeud(arbre, lettre, code):
    noeud = arbre
    for element in code:
        if element == '°':
            if noeud.gauche is None:
                noeud.gauche = Arbre()
            noeud = noeud.gauche
        else:
            if noeud.droite is None:
                noeud.droite = Arbre()
            noeud = noeud.droite
    noeud.valeur = lettre

def afficher_file(file):
    contenu = ""
    elements = file.contenu()  # Récupère les éléments de la file
    for i in range(len(elements)):
        contenu += elements[i]
        if i < len(elements) - 1:  # Ajoute un espace sauf après le dernier élément
            contenu += " "
    return contenu

def decodage(arbre, cmorse):
    if arbre is None:
        return ""
    if cmorse == "":
        return arbre.valeur
    if cmorse[0] == "°":
        return decodage(arbre.gauche, cmorse[1:])
    if cmorse[0] == "-":
        return decodage(arbre.droite, cmorse[1:])

def codage(A, L, parcouru="", selectionne=""):
    if A == None:
        return ""
    if A != None:
        if A.valeur == L:
            selectionne = parcouru
            return selectionne
        Rep = codage(A.gauche, L, parcouru + "°", selectionne)
        if Rep != "":
            return Rep
        return codage(A.droite, L, parcouru + "-", selectionne)
# def pour si l utilisateur met une minuscule
def convertir_en_majuscule(texte):
    # Dictionnaire de  minuscules a majuscules
    correspondance = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E',
        'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
        'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
        'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
        'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y',
        'z': 'Z'
    }
    resultat = ""
    for caractere in texte:
        if caractere in correspondance:  # Si c'est une minuscule
            resultat += correspondance[caractere]  # Convertir en majuscule
        else:
            resultat += caractere  # Garder inchangés les majuscules et autres caractères
    return resultat
# def pour verifier si l utilisateur met des lettre
def verifier(texte):
    if not texte:  # Vérifie si le texte est vide
        return False
    for c in texte:
        if c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':  # Vérifie que les caractères sont des majuscules
            return False
    return True  # Si tous les caractères sont valides

def traiter_texte(texte): # regroupe les deux presedente def
    # Convertir le texte en majuscule
    texte_majuscule = convertir_en_majuscule(texte)
    # Vérifier si le texte est valide
    if verifier(texte_majuscule):
        print("Le texte est valide et en majuscule :", texte_majuscule)
        return True, texte_majuscule
    else:
        print("Erreur : le texte contient des caractères invalides.")
        return False, texte_majuscule  # Retourner texte_majuscule  si c'est incorecte
# def pour verifier si l utilisateur met des ° ou des -
def verifier_morse(texte):
    codes = [
        ("A", "°-"), ("B", "-°°°"), ("C", "-°-°"), ("D", "-°°"),
        ("E", "°"), ("F", "°°-°"), ("G", "--°"), ("H", "°°°°"),
        ("I", "°°"), ("J", "°---"), ("K", "-°-"), ("L", "°-°°"),
        ("M", "--"), ("N", "-°"), ("O", "---"), ("P", "°--°"),
        ("Q", "--°-"), ("R", "°-°"), ("S", "°°°"), ("T", "-"),
        ("U", "°°-"), ("V", "°°°-"), ("W", "°--"), ("X", "-°°-"),
        ("Y", "-°--"), ("Z", "--°°")
    ]
    if texte == [""]:
        return False
    valid_morse = [morse for letter, morse in codes]
    for cmorse in texte:
        if cmorse not in valid_morse:
            return False
    return True

def encoder():
    # vider les file si elle sont encore plaine
    while not file1.est_vide():
        file1.defiler()
    while not file2.est_vide():
        file2.defiler()
    texte = entree.get()
    valide, texte_majuscule = traiter_texte(texte)  # verifier si le texte et bon
    if valide:  # Si le texte est valide 
        for lettre in texte_majuscule:
            file1.enfiler(lettre)
            file2.enfiler(codage(arbre, lettre))
        afficher_files()
        label_t3.place_forget()
    else:
        label_t3.config(text="Il faut mettre des lettres")  # Message d'erreur si le texte contient des caractères non valides
        label_t3.place(x=150,y=55 ,anchor="c")

def decoder():
    while not file1.est_vide():
        file1.defiler()
    while not file2.est_vide():
        file2.defiler()
    texte = entree_morse.get().split(" ")
    print(texte)
    if verifier_morse(texte):   # verifier si le texte(morse) et bon
        for cmorse in texte:
            file2.enfiler(cmorse)
            file1.enfiler(decodage(arbre, cmorse))
        afficher_files()
        label_t3.place_forget()
    else:
        label_t3.config(text="Il faut utiliser ° ou - et les combinaison valider en morse")  # Message d'erreur si le texte contient des caractères non valides
        label_t3.place(x=150,y=175 ,anchor="c")


# pour afficher les mot/code morse
def afficher_files():
    global mot_alfabet, mot_morse
    label_f1.config(text=afficher_file(file1))
    label_f2.config(text=afficher_file(file2))
    mot_alfabet= afficher_file(file1)
    mot_morse = afficher_file(file2)
    print(afficher_file(file1))
    print(afficher_file(file2))



### bonus le son

def jouer_son(cmorse):
    mixer.init() # permet d apeller tout sa dont a besoin mixer(de pygame) pour fonctionner : frequency, size, channels et buffer
    for element in cmorse:
        if element == '°':
            mixer.Sound("Son/dot.wav").play() # joue le musique
            time.sleep(0.2)  # Pause entre les caractères
        elif element == '-':
            mixer.Sound("Son/dash.wav").play()
            time.sleep(0.4)  # Pause entre les caractères
        time.sleep(0.2)  # Pause entre les sons

# def pour eviter que le son se declanche direct lors du lancement du programme
def jouer_morse_code():
    global mot_morse
    morse_code = mot_morse
    if morse_code != "":
        print(morse_code)
        jouer_son(morse_code)
    else:
        label_t3.config(text="Il faut un code morse")
        label_t3.place(x=150, y=335, anchor="c")

### creation tinker

fenetre = Tk()
fenetre.config(width=300, height=400, bg="cyan")
fenetre.title("Alfabet <--> Morse")
arbre = construire_arbre()
file1 = File()
file2 = File()

mot_alfabet, mot_morse = "", ""

label_t1 = Label(fenetre, text="Texte alphabétique :")
label_t1.place(x= 150 ,y =35,anchor="c")
entree = Entry(fenetre)
entree.place(x= 150, y = 75, anchor="c")
bouton_b1 = Button(fenetre, text="Encoder", command=encoder)
bouton_b1.place(x= 150, y = 115, anchor="c")
label_t2 = Label(fenetre, text="Texte Morse :")
label_t2.place(x= 150 ,y =155,anchor="c")
entree_morse = Entry(fenetre)
entree_morse.place(x= 150, y = 195, anchor="c")
bouton_b2 = Button(fenetre, text="Décoder", command=decoder)
bouton_b2.place(x= 150, y = 235, anchor="c")
label_f1 = Label(fenetre, text="F1: ")
label_f1.place(x= 150, y = 275, anchor="c")
label_f2 = Label(fenetre, text="F2: ")
label_f2.place(x= 150, y = 315, anchor="c")
label_t3 = Label(fenetre, text="",bg="cyan",fg="red")
label_t3.place_forget()
# Bouton pour jouer le son
bouton_s = Button(fenetre, text="Jouer Son",command=jouer_morse_code)
bouton_s.place(x=150, y=355,anchor="c")

fenetre.mainloop()



