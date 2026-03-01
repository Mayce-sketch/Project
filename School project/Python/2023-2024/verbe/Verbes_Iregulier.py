#03/03/2024
from tkinter import *
from random import *

fenetre = Tk()
fenetre.config(width=600, height=500, bg="cyan")
fenetre.title("Verbes Iregulier")
# metre les variable a 0
nom_utilisateur = ""
liste_verbe_presant = []
manche, Smanche, Stotal, Siconection, Nquestion = 0, 0, 0, 0, 0


def dico_fichier(nom_fichier):  # cree un dico pour les verbe
    liste_dictionnaires = []
    fichier = open(nom_fichier, "r")
    lignes = fichier.readlines()[1:]  # Ignorer la première ligne qui contient les entêtes
    for ligne in lignes:
        valeurs = ligne.split(';')  # Utiliser ';' comme délimiteur
        # Vérifier si la ligne contient suffisamment de valeurs
        if len(valeurs) == 4:
            dictionnaire = {
                'infinitif': valeurs[0],
                'preterit': valeurs[1],
                'past perfect': valeurs[2],
                'francais': valeurs[3]
            }
            # Ajouter le dictionnaire à la liste
            liste_dictionnaires.append(dictionnaire)
    fichier.close()
    return liste_dictionnaires

liste_dictionnaires = dico_fichier("verbes.csv")  # recupere les donner
liste_verbes = dico_fichier("verbes.csv")
liste_fr = [d['francais'] for d in liste_verbes]  # Création d'une liste de verbes en français à partir des données obtenue
verbe = choice(liste_fr)
while verbe in liste_verbe_presant: # Boucle pour garantir que le verbe choisi n'est pas déjà présent dans la liste
    verbe = choice(liste_fr)
liste_verbe_presant.append(verbe) # Ajout du verbe choisi à la liste

def sauvegarder_utilisateur(login, mdp, score, question):  # pour sauvgarder un utilisateur
    fichier = open('utilisateurs.csv', 'a', encoding='utf-8')
    fichier.write(login + ";" + mdp + ";" + str(score) + ";" + str(question) + "\n")
    fichier.close()

def verifier_identifiants(nom_utilisateur, mdp):  # pour verifer si l identifant et corecte
    fichier = open('utilisateurs.csv', 'r', encoding='utf-8')
    lignes = fichier.readlines()
    fichier.close()
    for ligne in lignes:
        utilisateur, mot_de_passe, score, question = ligne.split(';')
        if utilisateur == nom_utilisateur and mot_de_passe == mdp:
            return int(score), int(question)
    return

def conection():  # affichage pour la conection
    Ltitre.place_forget()
    Lexplication.place_forget()
    Lscore.config(text="tu as " + str(Stotal) + " point \n et tu as repondut a " + str(Nquestion) + " question")
    Lscore.place(x=300, y=350, anchor="c")
    Bjouer.place_forget()
    Lnom.place(x=150, y=150, anchor="c")
    Lmdp.place(x=150, y=200, anchor="c")
    Lconecter.place(x=300, y=100, anchor="c")
    RInom.place(x=300, y=150, anchor="c")
    RImdp.place(x=300, y=200, anchor="c")
    Bidentifient.place_forget()
    Bretour.place(x=600, y=0, anchor="ne")
    Bvaliderconection.place(x=300, y=400, anchor="c")
    Bvalider.place_forget()
    Linfinitif.place_forget()
    Lpreterit.place_forget()
    Lpast_perfect.place_forget()
    Rinfinitif.place_forget()
    Rpreterit.place_forget()
    Rpast_perfect.place_forget()
    Lexplication.place_forget()
    Bidentifient.place_forget()
    Bconection.place_forget()
    Bsauvgarder.place_forget()
    Linfo.place_forget()

# Cette fonction vérifie les identifiants saisis par l'utilisateur lors de la connexion.
def valider_conection():
    global Siconection, Stotal, nom_utilisateur, Nquestion
    nom_utilisateur = RInom.get()
    mdp = RImdp.get()
    if not nom_utilisateur == "" or not mdp == "":
        resultat = verifier_identifiants(nom_utilisateur, mdp)
        if resultat:  # Vérifier si le résultat est évalué comme True (c'est-à-dire s'il n'est pas vide)
            score, question = resultat
            Lidentifient.config(text=nom_utilisateur)
            Siconection = 1
            Stotal = score
            Nquestion = question
            commencer()
        else:
            print("Erreur: Identifiants incorrects")
            Linfo.place(x=300, y=450, anchor="c")
    else:
        Linfo.place(x=300, y=450, anchor="c")


def identifier(): # affichage pour l identifant
    Ltitre.place_forget()
    Lexplication.place_forget()
    Lscore.config(text="tu as " + str(Stotal) + " point \n et tu as repondut a " + str(Nquestion) + " question")
    Lscore.place(x=300, y=350, anchor="c")
    Bjouer.place_forget()
    Lnom.place(x=150, y=150, anchor="c")
    Lmdp.place(x=150, y=200, anchor="c")
    Lidentifier.place(x=300, y=100, anchor="c")
    RCnom.place(x=300, y=150, anchor="c")
    RCmdp.place(x=300, y=200, anchor="c")
    Bidentifient.place_forget()
    Bretour.place(x=600, y=0, anchor="ne")
    Bvalideridentifient.place(x=300, y=400, anchor="c")
    Bvalider.place_forget()
    Linfinitif.place_forget()
    Lpreterit.place_forget()
    Lpast_perfect.place_forget()
    Rinfinitif.place_forget()
    Rpreterit.place_forget()
    Rpast_perfect.place_forget()
    Lexplication.place_forget()
    Bidentifient.place_forget()
    Bconection.place_forget()
    Bsauvgarder.place_forget()
    Linfo.place_forget()
def valideridentifient():
    global Smanche, Stotal, Siconection, Nquestion, nom_utilisateur
    nom_utilisateur = RCnom.get()
    rep_mdp = RCmdp.get()
    if not nom_utilisateur == "" or not rep_mdp == "":
        sauvegarder_utilisateur(nom_utilisateur, rep_mdp, Stotal, Nquestion)  # Sauvegarde de l'utilisateur
        Lidentifient.config(text=nom_utilisateur)
        Siconection = 1
        commencer()
    else:
        Linfo.config(text="vous devais devais donner un mon et un mdp")
        Linfo.place(x=300, y=450, anchor="c")

def commencer(): # pour commence le jeu
    global nom_utilisateur, Stotal, Nquestion, verbe
    Lexplication.place_forget()
    Bjouer.place_forget()
    Bvalider.place(x=300, y=400, anchor="c")
    Linfinitif.place(x=50, y=200)
    Lpreterit.place(x=50, y=250)
    Lpast_perfect.place(x=50, y=300)
    Rinfinitif.place(x=240, y=210)
    Rpreterit.place(x=240, y=260)
    Rpast_perfect.place(x=240, y=310)
    Lexplication.config(text="traduiser le verbe: " + str(verbe))
    Lexplication.place(x=300, y=125, anchor="c")
    Bidentifient.place(x=600, y=0, anchor="ne")
    Bconection.place(x=600, y=40, anchor="ne")
    Lscore.config(text="ton score est de " + str(Stotal)+"\n et ut as repondut a " + str(Nquestion) + " question")
    Lscore.place(x=300, y=470, anchor="c")
    Bsauvgarder.place(x=600, y=500, anchor="se")
    Linfo.place_forget()
    Lconecter.place_forget()
    Lidentifier.place_forget()
    Lnom.place_forget()
    Lmdp.place_forget()
    RCnom.place_forget()
    RCmdp.place_forget()
    RInom.place_forget()
    RImdp.place_forget()
    Bretour.place_forget()
    Bvalideridentifient.place_forget()
    Bvaliderconection.place_forget()
def valider(): # pour valider c est proposition
    global Stotal, manche, Smanche, nom_utilisateur, Nquestion, verbe
    Smanche = 0
    Nquestion = Nquestion + 1
    rep_infinitif = Rinfinitif.get()
    rep_preterit = Rpreterit.get()
    rep_past_perfect = Rpast_perfect.get()
    for verbe in liste_dictionnaires:
        if verbe['francais'] == liste_verbe_presant[-1]:
            if rep_infinitif == verbe['infinitif']: # verifit si le verbe donner par l utilisateur corespond au bon verbe
                Smanche = Smanche + 1
            if rep_preterit == verbe['preterit']:
                Smanche = Smanche + 1
            if rep_past_perfect == verbe['past perfect']:
                Smanche = Smanche + 1
    verbe = choice(liste_fr)   # rechoisie un verbe
    while verbe in liste_verbe_presant:
        verbe = choice(liste_fr)
    liste_verbe_presant.append(verbe)
    Stotal = Stotal + Smanche
    manche = manche + 1
    Lexplication.config(text="traduiser le verbe: " + str(verbe))
    Lscore.config(text="tu as obtenue " + str(Smanche) + " sur 3\n tu as au total " + str(Stotal) + " point \n et tu a repondut a " + str(Nquestion) + " question")
    Lscore.place(x=300, y=470, anchor="c")


def sauvgarder():
    global Siconection, nom_utilisateur
    print(nom_utilisateur)
    if Siconection == 1:
        modifier_score_utilisateur(nom_utilisateur, Stotal, Nquestion)
    else:
        Linfo.config(text="pour sauvgarder\n vous devez êtres connecté")
        Linfo.place(x=600, y=450, anchor="se")

def modifier_score_utilisateur(nom_utilisateur, nouveau_score, nouveau_question):
    fichier = open('utilisateurs.csv', 'r', encoding='utf-8')
    lignes = fichier.readlines()
    fichier.close()
    fichier = open('utilisateurs.csv', 'w', encoding='utf-8')
    for ligne in lignes:
        valeurs = ligne.split(';')
        if len(valeurs) >= 4:
            utilisateur, mot_de_passe, score, question = valeurs[0], valeurs[1], valeurs[2], valeurs[3].strip()
            print(valeurs[0], valeurs[1], valeurs[2], valeurs[3])
            if not score:
                score = '0'
                print("pas score")
            if not question:
                question = '0'
                print("pas question")
            print(utilisateur, "nom_uilisateur :" + nom_utilisateur)
            if utilisateur == nom_utilisateur:
                score = str(nouveau_score)
                question = str(nouveau_question)
                print("ok")
                print(valeurs[0], valeurs[1], valeurs[2], valeurs[3])
            print(score, question)
            fichier.write(utilisateur + ";" + mot_de_passe + ";" + score + ";" + question + "\n")
        else:
            fichier.write(ligne)
    fichier.close()

# les label
Ltitre = Label(fenetre, text="Quiz", width=10, height=2, bg="cyan", font=("nomtserrat", 20, ""))
Ltitre.place(x=300, y=50, anchor="c")
Lexplication = Label(fenetre, text="un verbre en francais va vous etre donne aleatoirement\net vous allez devoir trouver sa traduction en anglais\n(infinitif, preterit, past perfect)", width=75, height=3, bg="cyan", font=("", 15, ""))
Lexplication.place(x=300, y=150, anchor="c")
Lscore = Label(fenetre, text="tu as obtenue " + str(Smanche) + "sur" + str(3 * manche) + "\n tu as au total " + str(Stotal) + "sur" + str(3 * manche))
Lscore.place_forget()
Lidentifient = Label(fenetre, text="pas conecter")
Lidentifient.place(x=0, y=0, anchor="nw")
Linfo = Label(fenetre, text="identifient incorecte")
Linfo.place_forget()
Linfinitif = Label(fenetre, text="infinitif: ", bg="cyan", font=("", 15, ""))
Linfinitif.place_forget()
Lpreterit = Label(fenetre, text="preterit: ", bg="cyan", font=("", 15, ""))
Lpreterit.place_forget()
Lpast_perfect = Label(fenetre, text="past perfect: ", bg="cyan", font=("", 15, ""))
Lpast_perfect.place_forget()
Lidentifier = Label(fenetre, text="s'identifier")
Lidentifier.place_forget()
Lconecter = Label(fenetre, text="se conecter")
Lconecter.place_forget()
Lnom = Label(fenetre, text="nom utilisateur: ")
Lnom.place_forget()
Lmdp = Label(fenetre, text="mot de passe: ")
Lmdp.place_forget()
# les boutons
Bjouer = Button(fenetre, text="Jouer", width=10, height=2, bg="red", font=("", 15, ""), command=commencer)
Bjouer.place(x=300, y=300, anchor="c")
Bvalider = Button(fenetre, text="valider", width=10, height=2, bg="red", font=("", 15, ""), command=valider)
Bvalider.place_forget()
Bidentifient = Button(fenetre, text="s'identifier", width=17, height=2, bg="blue", command=identifier)
Bidentifient.place(x=600, y=0, anchor="ne")
Bconection = Button(fenetre, text="se conecter", width=17, height=2, bg="blue", command=conection)
Bconection.place(x=600, y=40, anchor="ne")
Bretour = Button(fenetre, text="retoure", width=10, height=2, bg="blue", command=commencer)
Bretour.place_forget()
Bvalideridentifient = Button(fenetre, text="confirmer", bg="red", font=("", 15, ""), command=valideridentifient)
Bvalideridentifient.place_forget()
Bvaliderconection = Button(fenetre, text="confirmer", bg="red", font=("", 15, ""), command=valider_conection)
Bvaliderconection.place_forget()
Bsauvgarder = Button(fenetre, text="sauvgarder", width=17, height=2, bg="blue", command=sauvgarder)
Bsauvgarder.place(x=600, y=500, anchor="se")
# les entry
Rinfinitif = Entry()
Rinfinitif.place_forget()
Rpreterit = Entry()
Rpreterit.place_forget()
Rpast_perfect = Entry()
Rpast_perfect.place_forget()
RCnom = Entry()  # reponce conection de nom
RCnom.place_forget()
RCmdp = Entry()  # reponce conection de mot de passe
RCmdp.place_forget()
RInom = Entry()  # reponce indentification de nom
RInom.place_forget()
RImdp = Entry()  # reponce indentification de mot de passe
RImdp.place_forget()
fenetre.mainloop()