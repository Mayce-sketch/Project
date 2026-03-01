#29/09/2024

# Importer les modules
from random import *
from tkinter import*
fenetre=Tk() # cree une fenetre
fenetre.title('Ma fenêtre')
fenetre.config(bg='cyan',width=900,height=600)

# Définir tout les variables
ListeEquipes = ['PSG', 'OM', 'OL']
ListeSponsors = ['Nike', 'Adidas', 'Puma']
B1, B2, B3, B4, B5, B6, B7, B8, B9, ligne1, ligne2, ligne3 = 1, 2, 3, 4, 5, 6, 7, 8, 9 , 1, 2, 3
compteur1, deja_passer1, deja_passer2, deja_passer3, compteur2, compteur3, erreur1, erreur2, erreur3= 0, 0, 0, 0 ,0, 0, 0, 0, 0
Liste1,Liste2,Liste3 = [],[],[]
dictionnaire1, dictionnaire2 = {}, {}
# definition pour interface du mode d emploie plus le texte qui est assosier
def mode_enploie():
    global compteur3
    # verification pour voir si le mode d enploie est deja actif
    if compteur3 == 0:
        Texplication.config(text="Vous vous trouvez dans un algorithme qui reprend les traits de Gale-Shapley. \n" "Il faut cliquer sur les boutons de chaque ligne pour ensuite les valider. \n"
                                 "" "Vous devrez le faire pour chaque ligne, puis valider. \n" "Ensuite, il faudra le refaire une deuxième fois pour que le programme calcule \n"
                                 "" "et vous indique quel est le meilleur sponsor par rapport aux équipes.", height=5, font=('times', 17, 'bold'))
        Texplication.place(x=450,y=300,anchor="c")
        Mode_emploie.config(text= "RETOURE")
        Tequipe.place_forget()
        Eurreur.place_forget()
        Aleatiore.place_forget()
        Vos_choixL.place_forget()
        Vos_choixB.place_forget()
        texte1.place_forget()
        texte2.place_forget()
        texte3.place_forget()
        button1.place_forget()
        button2.place_forget()
        button3.place_forget()
        button4.place_forget()
        button5.place_forget()
        button6.place_forget()
        button7.place_forget()
        button8.place_forget()
        button9.place_forget()
        valider_button1.place_forget()
        valider_button2.place_forget()
        valider_button3.place_forget()
        compteur3 = compteur3 + 1
    elif compteur3 == 1: # si le mode enploie est deja actif on l enleve
        compteur3 = 0
        reaparition()
# definition pour faire reaparetre les element sur la fenetre
def reaparition():
        # place tout les label / bouton
        Texplication.config(text="cliquer sur les different sponsor \npour choisir les preference des equipes en fonction de different sponsor",
                             height=2, font=('times', 15, 'bold'))
        Texplication.place(x=450, y=20, anchor="c")
        Tequipe.place(x=50, y=20, anchor="w")
        Eurreur.place_forget()
        Aleatiore.place(x=50, y=510)
        Mode_emploie.config(text="MODE D'ENPLOIE")
        Mode_emploie.place(x=900, y=20, anchor="e")
        Vos_choixL.place_forget()
        Vos_choixB.place_forget()
        texte1.place(x=50, y=100, anchor="w")
        texte2.place(x=50, y=280, anchor="w")
        texte3.place(x=50, y=460, anchor="w")
        button1.place(x=200, y=100, anchor="w")
        button2.place(x=400, y=100, anchor="w")
        button3.place(x=600, y=100, anchor="w")
        button4.place(x=200, y=280, anchor="w")
        button5.place(x=400, y=280, anchor="w")
        button6.place(x=600, y=280, anchor="w")
        button7.place(x=200, y=460, anchor="w")
        button8.place(x=400, y=460, anchor="w")
        button9.place(x=600, y=460, anchor="w")
        valider_button1.place(x=770, y=100, anchor="w")
        valider_button2.place(x=770, y=280, anchor="w")
        valider_button3.place(x=770, y=460, anchor="w")
# faire les liste equipe aleatione et les mettre dans les dico assosicer
def generer_preference_aleatoires():
    # Mélanger les listes
    shuffle(ListeEquipes)
    # Créer les dictionnaires de préférences
    dictionnaire1 = {ListeSponsors[i]: ListeEquipes for i in range(len(ListeSponsors))}
    dictionnaire2 = {ListeEquipes[i]: ListeSponsors for i in range(len(ListeEquipes))}
    # Afficher les résultats
    print("\nDictionnaire 1 (Préférences des sponsors):")
    print(dictionnaire1)
    print("Dictionnaire 2 (Préférences des équipes):")
    print(dictionnaire2)
    return dictionnaire1 ,dictionnaire2

# cree une les couples aleatoirement
def Aleatoire():
     dico1 , dico2 = generer_preference_aleatoires() # cree des dico aleatoire
     gale_shapley(dico1,dico2) # faire l algoritme de gale shapley
     fin() # afichage des resultats
# definition pour changer le nom sur les bouton et les recuperer
def suivant(numero_bouton,quel_bouton):
    text = quel_bouton.cget("text") # on recuper le texte accosier au bouton appuier
    # si 1 et si le text est egale au premier element de la liste ListeEquipes alors on le change pour le deusieme element de la liste
    # inssi de sute pour les different if
    if numero_bouton == 1 :
        if text == ListeEquipes[0]:
            quel_bouton.config(text=ListeEquipes[1])
        if text == ListeEquipes[1]:
            quel_bouton.config(text=ListeEquipes[2])
        if text == ListeEquipes[2]:
            quel_bouton.config(text=ListeEquipes[0])
        quel_bouton.place(x=200, y=100, anchor="w")
    if numero_bouton == 2 :
        if text == ListeEquipes[0]:
            quel_bouton.config(text=ListeEquipes[1])
        if text == ListeEquipes[1]:
            quel_bouton.config(text=ListeEquipes[2])
        if text == ListeEquipes[2]:
            quel_bouton.config(text=ListeEquipes[0])
        quel_bouton.place(x=400, y=100, anchor="w")
    if numero_bouton == 3 :
        if text == ListeEquipes[0]:
            quel_bouton.config(text=ListeEquipes[1])
        if text == ListeEquipes[1]:
            quel_bouton.config(text=ListeEquipes[2])
        if text == ListeEquipes[2]:
            quel_bouton.config(text=ListeEquipes[0])
        quel_bouton.place(x=600, y=100, anchor="w")
    if numero_bouton == 4 :
        if text == ListeEquipes[0]:
            quel_bouton.config(text=ListeEquipes[1])
        if text == ListeEquipes[1]:
            quel_bouton.config(text=ListeEquipes[2])
        if text == ListeEquipes[2]:
            quel_bouton.config(text=ListeEquipes[0])
        quel_bouton.place(x=200, y=280, anchor="w")
    if numero_bouton == 5 :
        if text == ListeEquipes[0]:
            quel_bouton.config(text=ListeEquipes[1])
        if text == ListeEquipes[1]:
            quel_bouton.config(text=ListeEquipes[2])
        if text == ListeEquipes[2]:
            quel_bouton.config(text=ListeEquipes[0])
        quel_bouton.place(x=400, y=280, anchor="w")
    if numero_bouton == 6 :
        if text == ListeEquipes[0]:
            quel_bouton.config(text=ListeEquipes[1])
        if text == ListeEquipes[1]:
            quel_bouton.config(text=ListeEquipes[2])
        if text == ListeEquipes[2]:
            quel_bouton.config(text=ListeEquipes[0])
        quel_bouton.place(x=600, y=280, anchor="w")
    if numero_bouton == 7 :
        if text == ListeEquipes[0]:
            quel_bouton.config(text=ListeEquipes[1])
        if text == ListeEquipes[1]:
            quel_bouton.config(text=ListeEquipes[2])
        if text == ListeEquipes[2]:
            quel_bouton.config(text=ListeEquipes[0])
        quel_bouton.place(x=200, y=460, anchor="w")
    if numero_bouton == 8 :
        if text == ListeEquipes[0]:
            quel_bouton.config(text=ListeEquipes[1])
        if text == ListeEquipes[1]:
            quel_bouton.config(text=ListeEquipes[2])
        if text == ListeEquipes[2]:
            quel_bouton.config(text=ListeEquipes[0])
        quel_bouton.place(x=400, y=460, anchor="w")
    if numero_bouton == 9 :
        if text == ListeEquipes[0]:
            quel_bouton.config(text=ListeEquipes[1])
        if text == ListeEquipes[1]:
            quel_bouton.config(text=ListeEquipes[2])
        if text == ListeEquipes[2]:
            quel_bouton.config(text=ListeEquipes[0])
        quel_bouton.place(x=600, y=460, anchor="w")
# definition pour valider les differnet ligne et pour voir si n a pas fait d eureur
def Est_valide(ligne):
    global compteur1, deja_passer1 , deja_passer2, deja_passer3, Liste1, Liste2, Liste3, compteur2, dictionnaire1, dictionnaire2, erreur1, erreur2, erreur3
    # si la linge = 1 et que les different texte on par le meme texte on les ajoute a une liste
    if ligne == 1:
        text1 = button1.cget("text")
        text2 = button2.cget("text")
        text3 = button3.cget("text")
        if text1 != text2 and text1 != text3 and text2 != text3:
            erreur1 = 0
            if Liste1 != []:
                Liste1 = []
            Liste1.append(text1)
            Liste1.append(text2)
            Liste1.append(text3)
            if deja_passer1 == 0:
                compteur1 = compteur1 + 1
                deja_passer1 = deja_passer1 + 1
        else: # si a fait une eurreur alors on lui affiche
            erreur1 = 1
        Afficher_erreur(1)
    if ligne == 2:
        text1 = button4.cget("text")
        text2 = button5.cget("text")
        text3 = button6.cget("text")
        if text1 != text2 and text1 != text3 and text2 != text3:
            erreur2 = 0
            if Liste2 != []:
                Liste2 = []
            Liste2.append(text1)
            Liste2.append(text2)
            Liste2.append(text3)
            if deja_passer2 == 0:
                compteur1 = compteur1 + 1
                deja_passer2 = deja_passer2 + 1
        else:
            erreur2 = 1
        Afficher_erreur(2)
    if ligne == 3:
        text1 = button7.cget("text")
        text2 = button8.cget("text")
        text3 = button9.cget("text")
        if text1 != text2 and text1 != text3 and text2 != text3:
            erreur3 = 0
            if Liste3 != []:
                Liste3 = []
            Liste3.append(text1)
            Liste3.append(text2)
            Liste3.append(text3)
            if deja_passer3 == 0:
                compteur1 = compteur1 + 1
                deja_passer3 = deja_passer3 + 1
        else:
            erreur3 = 1
        Afficher_erreur(3)
    # si l utilisateur a fait valider sur les tros ligne alors on recuper les texte les bouton pour les stoker dans un dictionnaire
    if compteur1 == 3 :
        text1 = button1.cget("text")
        text2 = button2.cget("text")
        text3 = button3.cget("text")
        text4 = button4.cget("text")
        text5 = button5.cget("text")
        text6 = button6.cget("text")
        text7 = button7.cget("text")
        text8 = button8.cget("text")
        text9 = button9.cget("text")
        Vos_choixL.config(text="Vos choix son :\n"+ListeSponsors[0]+" a pour preference "+ text1+","+text2+","+text3+"\n"
                                                +ListeSponsors[1]+" a pour preference "+ text4+","+text5+","+text6+"\n"
                                                +ListeSponsors[2]+" a pour preference "+ text7+","+text8+","+text9+"\n")
        if compteur2 != 1:
            dictionnaire1 = {ListeSponsors[0]: Liste1, ListeSponsors[1]: Liste2, ListeSponsors[2]: Liste3}
        else:
            dictionnaire2 = {ListeSponsors[0]: Liste1, ListeSponsors[1]: Liste2, ListeSponsors[2]: Liste3}
        print("Dictionnaire 1 (Préférences des équipes):")
        print(dictionnaire1)
        print("\nDictionnaire 2 (Préférences des sponsors):")
        print(dictionnaire2)
        Vos_choixL.place(x=300, y=510)
        Vos_choixB.place(x=600, y=510)
# definition pour afficher les eurreur
def Afficher_erreur(ligne_numero):
    global erreur1, erreur2, erreur3
    print(erreur1,erreur2,erreur3)
    # si il y a une eurreur on l affiche a l utilsateur
    if erreur1 == 0 and erreur2 == 0 and erreur3 == 0:
        Eurreur.place_forget()
    if erreur1 == 1:
        if ligne_numero == 1:
            y_position = 130
            Eurreur.place(x=750, y=y_position)
    if erreur2 == 1:
        if ligne_numero == 2:
            y_position = 340
            Eurreur.place(x=750, y=y_position)
    if erreur3 == 1:
        if ligne_numero == 3:
            y_position = 500
        Eurreur.place(x=750, y=y_position)
# definition qui inverse ListeSponsors et ListeEquipes pour tout changer
def tout_invserse():
    global ListeSponsors, ListeEquipes
    ListeSponsors, ListeEquipes = ListeEquipes, ListeSponsors
    enlever_ou_changer()
# definition pour reaficher les element sur la fenetre car on a changer ListeSponsors et ListeEquipes
def enlever_ou_changer():
    global texte1, texte2, texte3, button1, button2, button3, button4, button5, button6, button7, button8, button, valider_button1, valider_button2, valider_button3, compteur1, deja_passer1, deja_passer2, deja_passer3, compteur2
    compteur1, deja_passer1, deja_passer2, deja_passer3 = 0, 0, 0, 0
    if compteur2  != 1 : # si sa a deja changer alors on me change pas
        # place tout les label / bouton
        Texplication.config(text="cliquer sur les different equipes \n"
                                 "pour choisir les preference des sponsor en fonction de different equipes",height=2, font=('times', 15, 'bold'))
        Texplication.place(x=450, y=20, anchor="c")
        Tequipe.config(text="Lise\nSponsor", height=2, font=('times', 15, 'bold'))
        Tequipe.place(x=50, y=20, anchor="w")
        Eurreur.place_forget()
        Aleatiore.place(x=50, y=510)
        Vos_choixL.place_forget()
        Vos_choixB.place_forget()
        # Mise à jour des Labels (texte1, texte2, texte3)
        texte1.config(text=ListeSponsors[0] + " :")
        texte1.place(x=50, y=100, anchor="w")
        texte2.config(text=ListeSponsors[1] + " :")
        texte2.place(x=50, y=280, anchor="w")
        texte3.config(text=ListeSponsors[2] + " :")
        texte3.place(x=50, y=460, anchor="w")
        # Mise à jour des Buttons (button1 à button9)
        button1.config(text=ListeEquipes[0], command=Bonton1)
        button1.place(x=200, y=100, anchor="w")
        button2.config(text=ListeEquipes[1], command=Bonton2)
        button2.place(x=400, y=100, anchor="w")
        button3.config(text=ListeEquipes[2], command=Bonton3)
        button3.place(x=600, y=100, anchor="w")
        button4.config(text=ListeEquipes[0], command=Bonton4)
        button4.place(x=200, y=280, anchor="w")
        button5.config(text=ListeEquipes[1], command=Bonton5)
        button5.place(x=400, y=280, anchor="w")
        button6.config(text=ListeEquipes[2], command=Bonton6)
        button6.place(x=600, y=280, anchor="w")
        button7.config(text=ListeEquipes[0], command=Bonton7)
        button7.place(x=200, y=460, anchor="w")
        button8.config(text=ListeEquipes[1], command=Bonton8)
        button8.place(x=400, y=460, anchor="w")
        button9.config(text=ListeEquipes[2], command=Bonton9)
        button9.place(x=600, y=460, anchor="w")
        # Positionnement des boutons de validation (valider_button1 à valider_button3)
        valider_button1.place(x=770, y=100, anchor="w")
        valider_button2.place(x=770, y=280, anchor="w")
        valider_button3.place(x=770, y=460, anchor="w")
        compteur2 = compteur2 + 1
    else:
        gale_shapley(dictionnaire1,dictionnaire2)  # faire l algoritme de gale shapley
        fin() # afichage des resultats
# definition pour l agoritme de gale shapley
def gale_shapley(pref_sponsors,pref_equipes):
    global gale_shapley_prefs
    # Initialisation des variable
    gale_shapley_prefs = {}
    proposers_state = {}
    sponsor_prefs = {}
    equipes_libres = {}
    aucune_equipe_libre = False  # Drapeau indiquant s'il n'y a plus d'équipes libres
    # Initialiser l'état des propositions de chaque équipe
    for equipe in pref_equipes:
        proposers_state[equipe] = 0  # Aucun sponsor donc = 0
        equipes_libres[equipe] = True  # Toutes les équipes sont initialement libres
    # Initialiser les préférences des sponsors avec des index
    for sponsor in pref_sponsors:
        sponsor_prefs[sponsor] = {}
        index = 0
        for equipe in pref_sponsors[sponsor]:
            sponsor_prefs[sponsor][equipe] = index
            index = index + 1
    # Boucle principale de l'algorithme
    while not aucune_equipe_libre:
        # Recherche d'une équipe libre
        equipe = None
        trouve = False  # Drapeau pour signaler si une équipe libre a été trouvée
        for e in equipes_libres:
            if equipes_libres[e] and not trouve:
                equipe = e
                trouve = True  # Une équipe libre a été trouvée, on sortira de la boucle
        # S'il n'y a plus d'équipe libre, sortir de la boucle
        if not trouve:  # Si aucune équipe libre n'a été trouvée
            aucune_equipe_libre = True
        else:
            # L'équipe propose au sponsor suivant dans sa liste
            index_sponsor = proposers_state[equipe]
            sponsors_pref = pref_equipes[equipe]
            sponsor = sponsors_pref[index_sponsor]
            # Faire la proposition au sponsor
            if sponsor not in gale_shapley_prefs:
                # Si le sponsor n'est pas encore couplé, former un couple
                gale_shapley_prefs[sponsor] = equipe
                equipes_libres[equipe] = False
            else:
                # Si le sponsor est déjà couplé,on  vérifit ses préférences
                equipe_actuelle = gale_shapley_prefs[sponsor]
                if sponsor_prefs[sponsor][equipe] < sponsor_prefs[sponsor][equipe_actuelle]:
                    # Le sponsor préfère la nouvel équipe, donc change de couple
                    gale_shapley_prefs[sponsor] = equipe
                    equipes_libres[equipe] = False
                    equipes_libres[equipe_actuelle] = True
            # Mettre à jour l'état de proposition de l'équipe
            proposers_state[equipe] = proposers_state[equipe] + 1
    return print(gale_shapley_prefs)
# definition pour afficher les resultat
def fin():
    global gale_shapley_prefs
    print("ok")
    couples = "Les couples obtenus sont : "
    # Parcourir le dictionnaire pour construire la chaîne
    for sponsor in gale_shapley_prefs:
        equipe = gale_shapley_prefs[sponsor]
        couples = couples +sponsor + ": " + equipe + ", "
    # Supprimer la dernière virgule et l'espace
    couples = couples[:-2]
    # Mettre à jour le texte du label Texplication
    Texplication.config(text=couples)
    Texplication.place(x=450, y=300, anchor="c")
    # Mettre à jour le texte du label Tequipe et changer sa position
    Tequipe.config(text="Votre association :")
    Tequipe.place(x=450, y=60, anchor="c")  # Changer la position Y pour éviter le chevauchement
    Eurreur.place_forget()
    Aleatiore.place_forget()
    Mode_emploie.place_forget()
    Vos_choixL.place_forget()
    Vos_choixB.place_forget()
    texte1.place_forget()
    texte2.place_forget()
    texte3.place_forget()
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    button5.place_forget()
    button6.place_forget()
    button7.place_forget()
    button8.place_forget()
    button9.place_forget()
    valider_button1.place_forget()
    valider_button2.place_forget()
    valider_button3.place_forget()
# definiton Bouton : permet de savoir c est quel bouton avec des attribut pres defini
def Bonton1():
    suivant(B1,button1)
def Bonton2():
    suivant(B2,button2)
def Bonton3():
    suivant(B3,button3)
def Bonton4():
    suivant(B4,button4)
def Bonton5():
    suivant(B5,button5)
def Bonton6():
    suivant(B6,button6)
def Bonton7():
    suivant(B7,button7)
def Bonton8():
    suivant(B8,button8)
def Bonton9():
    suivant(B9,button9)
# definiton Valide : permet de savoir c est quel ligne avec des attribut pres defini
def Valider1():
    Est_valide(ligne1)
def Valider2():
    Est_valide(ligne2)
def Valider3():
    Est_valide(ligne3)

# place tout les label / bouton
Texplication = Label(fenetre,text="cliquer sur les different sponsor \npour choisir les preference des equipes en fonction de different sponsor",height=2,font=('times',15,'bold'))
Texplication.place(x=450,y=20,anchor="c")
Tequipe = Label(fenetre,text="Lise\nEquipe",height=2,font=('times',15,'bold'))
Tequipe.place(x=50,y=20,anchor="w")
Eurreur = Label(fenetre,text=" Il y a une eurreur\n dans vos choix,\n veuillez changer\n votre réponse.",bg="cyan",fg="red",height=4,font=('times',12,'bold'))
Eurreur.place_forget()
Aleatiore = Button(fenetre,text="Aleatiore",height=2,font=('times',15,'bold'),command=Aleatoire)
Aleatiore.place(x=50,y=510)
Mode_emploie = Button(fenetre,text="MODE D'ENPLOIE",height=2,font=('times',10,'bold'),command=mode_enploie)
Mode_emploie.place(x=900,y=20,anchor="e")
Vos_choixL = Label(fenetre, text="", height=4, font=('times', 10, 'bold'))
Vos_choixL.place_forget()
Vos_choixB = Button(fenetre,text="Suivant",height=2,font=('times',15,'bold'),command=tout_invserse)
Vos_choixB.place_forget()
# texte
texte1 = Label(fenetre, text=ListeSponsors[0]+" :", height=2, font=('times', 15, 'bold'))
texte1.place(x=50, y=100, anchor="w")
texte2 = Label(fenetre, text=ListeSponsors[1]+" :", height=2, font=('times', 15, 'bold'))
texte2.place(x=50, y=280, anchor="w")
texte3 = Label(fenetre, text=ListeSponsors[2]+" :", height=2, font=('times', 15, 'bold'))
texte3.place(x=50, y=460, anchor="w")
# bouton
button1 = Button(fenetre, text=ListeEquipes[0], height=2, font=('times', 15, 'bold'),command=Bonton1)
button1.place(x=200, y=100, anchor="w")
button2 = Button(fenetre, text=ListeEquipes[1], height=2, font=('times', 15, 'bold'),command=Bonton2)
button2.place(x=400, y=100, anchor="w")
button3 = Button(fenetre, text=ListeEquipes[2], height=2, font=('times', 15, 'bold'),command=Bonton3)
button3.place(x=600, y=100, anchor="w")
button4 = Button(fenetre, text=ListeEquipes[0], height=2, font=('times', 15, 'bold'),command=Bonton4)
button4.place(x=200, y=280, anchor="w")
button5 = Button(fenetre, text=ListeEquipes[1], height=2, font=('times', 15, 'bold'),command=Bonton5)
button5.place(x=400, y=280, anchor="w")
button6 = Button(fenetre, text=ListeEquipes[2], height=2, font=('times', 15, 'bold'),command=Bonton6)
button6.place(x=600, y=280, anchor="w")
button7 = Button(fenetre, text=ListeEquipes[0], height=2, font=('times', 15, 'bold'),command=Bonton7)
button7.place(x=200, y=460, anchor="w")
button8 = Button(fenetre, text=ListeEquipes[1], height=2, font=('times', 15, 'bold'),command=Bonton8)
button8.place(x=400, y=460, anchor="w")
button9 = Button(fenetre, text=ListeEquipes[2], height=2, font=('times', 15, 'bold'),command=Bonton9)
button9.place(x=600, y=460, anchor="w")
# bouton Valider
valider_button1 = Button(fenetre, text="Valider", height=2, font=('times', 15, 'bold'),command=Valider1)
valider_button1.place(x=770, y=100, anchor="w")
valider_button2 = Button(fenetre, text="Valider", height=2, font=('times', 15, 'bold'),command=Valider2)
valider_button2.place(x=770, y=280, anchor="w")
valider_button3 = Button(fenetre, text="Valider", height=2, font=('times', 15, 'bold'),command=Valider3)
valider_button3.place(x=770, y=460, anchor="w")

fenetre.mainloop()