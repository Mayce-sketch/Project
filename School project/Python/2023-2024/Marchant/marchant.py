#22/05/2024
from tkinter import *
fenetre = Tk()
fenetre.title("Marchant")
fenetre.config(bg="#FCD494", width=900, height=700)
nom_utilisateur = "Vous n'etes pas connetcter"
# petit text d'intro
categorie = "Bonjour vous êtes cher LA boite de jeux, ici vous pouvez trouver tous les jeux que vous voulez.\nPour cela, vous devez cliquer sur la plateforme qui vous convient."
# inisalisation des valeur
siHome_panier = 1
image, contenue, imageS, achat, Nbarticle, Pas_passer_categorie, Nbobj,panier = "","", "", 0,0,0,1,0
liste_images,liste_labelsImage,liste_labelsQuantiter, nbobjs = [], [], [], []
resultats = {}
PrixK, PrixMW, PrixMP, PrixAC,PrixTOTK , PrixBOTW, PrixP = 53.57,42.37,37.12,35.12,46.25,43.12,42.12
# resumer des different jeu
TresumerK = """Dans "Kirby et le Monde Oublié" sur Nintendo Switch, le monde est en péril et Kirby,\n malgré son apparence mignonne, est prêt à relever le défi. Le jeu offre une aventure en 3D où Kirby doit percer\n le mystère d'un monde dévasté et hostile pour sauver ses amis, les Waddle Dees.\nEn utilisant ses pouvoirs classiques et de nouveaux pouvoirs comme Foreuse et Explorateur,\nKirby affronte les obstacles et les ennemis.De plus, il peut se transformer en différents objets\n pour s'adapter à son environnement et débloquer des situations.\n Le jeu propose également un mode coopératif à deux joueurs avec Bandana Waddle Dee."""
TresumerMW = """Dans "Super Mario Bros. Wonder" sur Nintendo Switch, Mario et ses amis s'embarquent\n dans une toute nouvelle aventure pour sauver le royaume du Prince Florian, envahi par Bowser.\n Traversez des niveaux variés, sautez, nagez, courez et volez pour progresser tout en évitant les ennemis.\n Utilisez les pouvoirs classiques de Mario comme la boule de feu et découvrez de nouveaux pouvoirs comme\n la pomme d'éléphant pour vous transformer en éléphant et gagner en force.\n Chaque niveau réserve des surprises avec des éléments cachés et des transformations inattendues.\nJouez avec des personnages familiers comme Mario, Luigi, Toad, la princesse Peach,\n ainsi que la princesse Daisy et Yoshi.Profitez d'une aventure multijoueur locale jusqu'à 4 joueurs et\n partagez le plaisir en famille et entre amis."""
TresumerMP = """La série Mario Party arrive sur Nintendo Switch avec des mini-jeux et\n un gameplay dynamiques pour tous les joueurs ! Le jeu de plateau classique est enrichi\n de nouveaux éléments stratégiques, comme des dés uniques pour chaque personnage.\n Découvrez de nouvelles façons de jouer, avec des mini-jeux exploitant les fonctionnalités des Joy-Con et\n de nouveaux modes pour des moments de divertissement en famille ou entre amis.\n Affrontez jusqu'à quatre joueurs dans une course effrénée pour collecter des Étoiles sur le plateau.\n Connectez deux consoles Switch pour une expérience de jeu encore plus intense dans\n le mode "Salle de jeux de Toad". Pour la première fois,\n mesurez-vous à d'autres fans dans un mode de mini-jeux en ligne.\n Avec ces nouveautés et une multitude de mini-jeux inédits,\n Mario Party sur Switch vous garantit des fêtes endiablées avec des joueurs du monde entier."""
TresumerAC = """Laissez-vous tenter par une escapade sur une île déserte avec Animal Crossing: New Horizons et\n son mode "Évasion île déserte". Cette expérience vous offre la liberté ultime :\n créer votre propre paradis sur une île inhabitée et développer votre communauté à votre rythme.\n Commencez par ériger votre campement, puis explorez votre île, récoltez des ressources et\n fabriquez les objets qui vous plaisent. Faites également la connaissance des charmants habitants animaux\n qui pourraient décider de vous rejoindre dans cette aventure unique.\n Dans Animal Crossing: New Horizons, le choix est vôtre : échappez à l'agitation du monde moderne et\n créez votre propre havre de paix sur une île déserte."""
TresumerTOTK = """Plongez dans une nouvelle aventure épique avec The Legend of Zelda: Tears of the Kingdom,\n la suite tant attendue de The Legend of Zelda: Breath of The Wild.\n Explorez un Hyrule ravagé par les ténèbres en incarnant le légendaire héros,\n Link, dans sa quête pour retrouver la princesse Zelda disparue.\n Utilisez votre imagination et les nouveaux pouvoirs de Link pour créer des armes,\n des véhicules et interagir avec l'environnement afin de surmonter les défis et explorer le vaste monde ouvert.\n Préparez-vous à faire le grand saut dans cette aventure pleine de dangers et de découvertes."""
TresumerBOTW = """Découvrez un tout nouveau monde d'aventure dans The Legend of Zelda: Breath of the Wild.\n Ce jeu révolutionnaire de la célèbre série vous emmène dans un voyage inoubliable\n à travers le royaume d'Hyrule en ruines. Explorez des champs, des forêts et\n escaladez des sommets dans cette aventure à ciel ouvert qui bouleverse les conventions de la série.\n Préparez-vous à plonger dans un monde de découverte, d'exploration et\n d'aventure comme jamais auparavant dans The Legend of Zelda: Breath of the Wild."""
TresumerP = """Explorez la région de Kanto et vivez une toute nouvelle aventure avec Pokémon: Let's Go, Pikachu et\n Pokémon: Let's Go, Évoli sur Nintendo Switch. Incarnez un nouveau dresseur de Pokémon et\n lancez-vous dans un voyage palpitant. Attrapez une variété de Pokémon,\n engagez des combats passionnants et créez des liens avec vos créatures tout au long de votre périple.\nPlongez-vous dans le monde des Pokémon et découvrez les merveilles\n de la région de Kanto dans ce jeu captivant."""
# importation des images (logo)
LogoimageGrand = PhotoImage(file="image/home/MonLogoGrand.png")
LogoimagePetit = PhotoImage(file="image/home/MonLogoPetit.png")
# jeu Switch
kirby_and_the_forgotten_land = PhotoImage(file="image/Les jeu de la Switch/Kirby and the forgotten land.png")
Super_Mario_Party= PhotoImage(file="image/Les jeu de la Switch/super mario party.png")
Super_Mario_Wonder= PhotoImage(file="image/Les jeu de la Switch/super mario wonder.png")
The_Legend_of_Zelda_Tears_of_the_Kingdom = PhotoImage(file="image/Les jeu de la Switch/The Legende of  zelda tears of the Kingdom.png")
The_Legend_of_Zelda_Breath_of_the_Wild = PhotoImage(file="image/Les jeu de la Switch/The legende of zelda breath of the wild.png")
Animal_crossing_New_horizons = PhotoImage(file="image/Les jeu de la Switch/Animal Crossing.png")
Pokemon_Let_s_Go_Pikachu = PhotoImage(file="image/Les jeu de la Switch/Pokémon Let's Go, Pikachu.png")
# creation du 1er canvas
Canevasfenetre = Canvas(fenetre, bg="#FCD494", width=900-4, height=700-4)
Canevasfenetre.place(x=0,y=0)
# creation du 2eme canvas
Canevas2 = Canvas(fenetre, bg="#EDB353", width=900 - 4, height=400-4)
Canevas2.place(x=0, y=300)
# Pour revenir au Home
def Home():
    global Bkirby, BmarioW, BmarioP, BAnimal, BZbotw, BZtotk, BPokemon, Lacher_image, achat, Pas_passer_categorie, panier, siHome_panier, liste_labelsImage, liste_labelsQuantiter
    siHome_panier = 1
    # Contenu de la catégorie
    categorie = "Bonjour vous êtes cher LA boite de jeux, ici vous pouvez trouver tous les jeux que vous voulez.\nPour cela, vous devez cliquer sur la plateforme qui vous convient."
    if panier != 1:
        # Retirer toutes les images
        for label in liste_labelsImage:
            label.place_forget()
        for label in liste_labelsQuantiter:
            label.place_forget()
    # enlever tout les element de: Nintendo switch
    if Pas_passer_categorie !=0:
        Bkirby.place_forget()
        BmarioW.place_forget()
        BmarioP.place_forget()
        BAnimal.place_forget()
        BZbotw.place_forget()
        BZtotk.place_forget()
        BPokemon.place_forget()
    # Changer le logo pour un logo plus grand
    Canevasfenetre.itemconfig(Logo, image=LogoimageGrand)
    Canevasfenetre.coords(Logo, 450, 150)
    Lnom_utilisateur.place(x=0, y=0, anchor="nw")
    # place tout les element
    Lexplication.config(text=categorie)
    Lexplication.place(x=450, y=275, anchor="c")
    BPanier.place(x=813.5, y=0, anchor="ne")
    Bhome.place_forget()
    Bidentification.place(x=900, y=0, anchor="ne")
    Canevas2.config(height=400-4)
    Canevas2.place(y=300)
    LNintendo_switch.place(x=450, y=600, anchor="c")
    BimageNS.place(x=450, y=475, anchor="c")
    # enleve tout les element
    Bpayer.place_forget()
    if achat == 1:
        Lacher_image.place_forget()
        Lresumer.place_forget()
        Bacheter.place_forget()
        Lquantiter.place_forget()
        Equantiter.delete(0, "end")
        Equantiter.place_forget()
        LAttention.place_forget()
        achat = 0
    if panier == 1:
        #Lacher_image.place_forget()
        LNombre_objet.place_forget()
        LAttention.place_forget()
        panier = 0
    Lidentifier.place_forget()
    Lnom.place_forget()
    Lmdp.place_forget()
    Enom.place_forget()
    Emdp.place_forget()
    Bvalider1indentifier.place_forget()
    Bvalider2Cree.place_forget()
    Bcreecompte.place_forget()
    Linfo.place_forget()
    Bvaliderpemant.place_forget()
    Eachat.place_forget()
# quand on clique sur la categorie Nintendo switch
def LienNintendo_switch():
    global Bkirby, BmarioW, BmarioP, BAnimal, BZbotw, BZtotk, BPokemon, Pas_passer_categorie, siHome_panier
    Pas_passer_categorie = 1
    siHome_panier = 1
    categorie = "plate-forme : Nintendo switch\n\nPour acheter le jeu que vous désirez ,vous devez cliquer dessus. "
    BimageNS.place_forget()
    LNintendo_switch.place_forget()
    # on change le logo pour un logo plus petit et on replace
    Canevasfenetre.itemconfig(Logo, image=LogoimagePetit)
    Canevasfenetre.coords(Logo, 450, 75)
    Lexplication.config(text=categorie)
    Lexplication.place(x=450, y=160, anchor="c")
    Bhome.place(x=813.5, y=0, anchor="ne")
    Canevas2.config(height=500-4)
    Canevas2.place(y=200)
    # on place les jeu avec leur image
    Bkirby = Button(Canevas2, image=kirby_and_the_forgotten_land, width=143, height=215, command=acheter_kirby)
    Bkirby.place(x=75, y=20)
    BmarioW = Button(Canevas2, image=Super_Mario_Wonder, width=143, height=215, command=acheter_mario_wonder)
    BmarioW.place(x=175, y=250)
    BmarioP = Button(Canevas2, image=Super_Mario_Party, width=143, height=215, command=acheter_mario_party)
    BmarioP.place(x=275, y=20)
    BAnimal = Button(Canevas2, image=Animal_crossing_New_horizons, width=143, height=215,command=acheter_animal_crossing)
    BAnimal.place(x=375, y=250)
    BZbotw = Button(Canevas2, image=The_Legend_of_Zelda_Breath_of_the_Wild, width=143, height=215,command=acheter_zelda_botw)
    BZbotw.place(x=475, y=20)
    BZtotk = Button(Canevas2, image=The_Legend_of_Zelda_Tears_of_the_Kingdom, width=143, height=215,command=acheter_zelda_totk)
    BZtotk.place(x=575, y=250)
    BPokemon = Button(Canevas2, image=Pokemon_Let_s_Go_Pikachu, width=143, height=215, command=acheter_pokemon)
    BPokemon.place(x=675, y=20)
def ajouter_image(image, liste_images):
    # Vérifie si l'image n'est pas déjà dans la liste
    if image not in liste_images:
        # Ajoute l'image à la liste
        liste_images.append(image)
# different def pour les diferent jeu(Switch)
def acheter_kirby():
    global resumer
    resumer = TresumerK # mettre le resumer du jeu
    ajouter_image(kirby_and_the_forgotten_land, liste_images)
    Focus_Jeu(kirby_and_the_forgotten_land)  # mettre se jeu en grand
def acheter_mario_wonder():
    global resumer
    resumer = TresumerMW
    ajouter_image(Super_Mario_Wonder, liste_images)
    Focus_Jeu(Super_Mario_Wonder)
def acheter_mario_party():
    global resumer
    resumer = TresumerMP
    ajouter_image(Super_Mario_Party, liste_images)
    Focus_Jeu(Super_Mario_Party)
def acheter_zelda_botw():
    global resumer
    resumer = TresumerBOTW
    ajouter_image(The_Legend_of_Zelda_Breath_of_the_Wild, liste_images)
    Focus_Jeu(The_Legend_of_Zelda_Breath_of_the_Wild)
def acheter_zelda_totk():
    global resumer
    resumer = TresumerTOTK
    ajouter_image(The_Legend_of_Zelda_Tears_of_the_Kingdom, liste_images)
    Focus_Jeu(The_Legend_of_Zelda_Tears_of_the_Kingdom)
def acheter_animal_crossing():
    global resumer
    resumer = TresumerAC
    ajouter_image(Animal_crossing_New_horizons, liste_images)
    Focus_Jeu(Animal_crossing_New_horizons)
def acheter_pokemon():
    global resumer
    resumer = TresumerP
    ajouter_image(Pokemon_Let_s_Go_Pikachu, liste_images)
    Focus_Jeu(Pokemon_Let_s_Go_Pikachu)
# def pour avoir les jeu seul avec une petit explication ,et pour l'acheter
def Focus_Jeu(image):
    global Lacher_image, resumer, achat, Nbobj, liste_images, siHome_panier
    achat = 1
    siHome_panier = 0
    # Supprime tous les boutons et le label explicatif
    Bkirby.place_forget()
    BmarioW.place_forget()
    BmarioP.place_forget()
    BAnimal.place_forget()
    BZbotw.place_forget()
    BZtotk.place_forget()
    BPokemon.place_forget()
    Lexplication.place_forget()
    BPanier.place_forget()
    LAttention.place_forget()
    # Changer le logo pour un logo plus grand
    Canevasfenetre.itemconfig(Logo, image=LogoimageGrand)
    Bhome.place(x=813.5, y=0, anchor="ne")
    Canevasfenetre.coords(Logo, 450, 125)
    Canevas2.config(height=450 - 4)
    Canevas2.place(y=250)
    # Configure le label pour afficher l'image
    Lacher_image = Label(Canevas2, image=image, width=143, height=215)  # Définir la couleur de fond sur la couleur de l'arrière-plan du canevas
    Lacher_image.place(x=200, y=200, anchor="c")
    Lresumer.config(text=resumer)
    Lresumer.place(x=585, y=175, anchor="c")
    Lquantiter.place(x=435, y=325, anchor="c")
    Equantiter.place(x=435, y=375, anchor="c")
    Bacheter.place(x=725, y=350, anchor="c")
def Panier():
    global achat, resumer, TresumerK, TresumerMW, panier, siHome_panier, Nbarticle, liste_labelsImage, liste_labelsQuantiter, prix
    panier = 1
    categorie = "Votre panier"
    # Afficher/Supprime tous les boutons et le label explicatif
    Canevasfenetre.itemconfig(Logo, image=LogoimagePetit)
    Canevasfenetre.coords(Logo, 450, 75)
    Lexplication.config(text=categorie)
    Lexplication.place(x=450, y=160, anchor="c")
    Bhome.place(x=813.5, y=0, anchor="ne")
    Canevas2.config(height=500 - 4)
    Canevas2.place(y=200)
    BimageNS.place_forget()
    LNintendo_switch.place_forget()
    BPanier.place_forget()
    LAttention.place_forget()
    Linfo.place_forget()
    if Pas_passer_categorie !=0:
        Bkirby.place_forget()
        BmarioW.place_forget()
        BmarioP.place_forget()
        BAnimal.place_forget()
        BZbotw.place_forget()
        BZtotk.place_forget()
        BPokemon.place_forget()
    Lexplication.place_forget()
    Nbobj = Equantiter.get()
    LAttention.config(text="Tu doit mettre un nombre")
    LAttention.place(x=320, y=410)
    initial_i = 0  # Initialiser initial_i en dehors de la boucle
    if siHome_panier == 1 or est_Nombre(Nbobj):
        Bpayer.place(x=775, y=180, anchor="w")
        if Nbarticle == 0:
            contenue = "vide"
            categorie = "Votre panier de LA boite de jeux est " + contenue + " ."
        if siHome_panier == 0:
            Nbobj = int(Nbobj)
            nbobjs.append(Nbobj)
        # on change le logo pour un logo plus petit et on replace
        Canevasfenetre.itemconfig(Logo, image=LogoimagePetit)
        # Afficher/Supprime tous les boutons et le label explicatif
        Canevasfenetre.coords(Logo, 450, 75)
        Lexplication.config(text=categorie)
        Lexplication.place(x=450, y=160, anchor="c")
        Bhome.place(x=813.5, y=0, anchor="ne")
        Canevas2.config(height=500 - 4)
        Canevas2.place(y=200)
        LAttention.place_forget()
        if achat == 1:
            Lresumer.place_forget()
            Bacheter.place_forget()
            Lquantiter.place_forget()
            Equantiter.delete(0, "end")
            Equantiter.place_forget()
            Lacher_image.place_forget()
            achat = 0
        for i in range(len(liste_images)):
            # boucle pour faire aparetre les image dans le panier
            # Récupérer l'image à l'index i
            image = liste_images[i]
            #print(image)
            # Convertir l'image en une chaîne de caractères pour la comparaison
            image_str = str(image)
            # Vérifier si l'image est égale à pyimagex(element recuperer avec un print)
            if image_str == 'pyimage3':
                prix = PrixK
            elif image_str == 'pyimage4':
                prix = PrixMP
            elif image_str == 'pyimage5':
                prix = PrixMW
            elif image_str == 'pyimage6':
                prix = PrixTOTK
            elif image_str == 'pyimage7':
                prix = PrixBOTW
            elif image_str == 'pyimage8':
                prix = PrixAC
            elif image_str == 'pyimage9':
                prix = PrixP

            if image_str not in resultats:
                # Vérifie si l'index i est valide dans la liste nbobjs
                if len(nbobjs) > i:
                    # Récupère le Nbobj correspondant à cette image sous forme de chaîne
                    Nbobj_str = nbobjs[i]
                    if Nbobj_str:
                        # Convertit la chaîne en nombre flottant
                        Nbobj = float(Nbobj_str)
                        # Calcule le résultat en multipliant Nbobj par prix et en arrondissant à deux chiffres après la virgule
                        resultat = round(Nbobj * prix, 2)
                    else:
                        # Si Nbobj_str est vide, définit le résultat à 0.0
                        resultat = 0.0
                    # Stocke le résultat dans le dictionnaire des résultats pour cette image
                    resultats[image_str] = resultat
                else:
                    # Si l'index i n'est pas valide, définit le résultat à 0.0
                    resultat = 0.0
            else:
                # Si le résultat a déjà été calculé pour cette image, utilise le résultat existant
                resultat = resultats[image_str]

            if siHome_panier != 1:
                #augment le nombre d article
                Nbarticle = Nbarticle + 1
                siHome_panier = 1

            if Nbarticle >= 6:
                # Utiliser une position y différente si Nbarticle est 7 ou plus
                if i >= 7:
                    #mette le jeu choise en bas a gauche si il y a plus de place sur la premiere ligne
                    y_offset = 250
                else:
                    y_offset = 0
                # Réinitialiser i à sa position initiale si on passe en mode "+7"
                if initial_i == 0:
                    initial_i = i
                i -= initial_i
            else:
                y_offset = 0
            if nbobjs != []:
                # Créer un label pour afficher l'image
                LimagePanier = Label(Canevas2, image=image, width=143, height=215)
                # Placer le label en fonction de la position x de l'image dans la liste
                LimagePanier.place(x=150 * i + 75, y=110 + y_offset, anchor="c")
                LquantiterPanier = Label(Canevas2, text="Quantiter : " + str(nbobjs[i]) + " : " + str(resultat) + "€",bg="#EDB353", font=("Arial", 10, "italic"))
                LquantiterPanier.place(x=150 * i + 75, y=231 + y_offset, anchor="c")
                # Ajouter le label à la liste
                liste_labelsImage.append(LimagePanier)
                liste_labelsQuantiter.append(LquantiterPanier)
    else:
        if siHome_panier == 1:
            LAttention.place_forget()
    #print(liste_labelsImage)
    #print(liste_labelsQuantiter)
def Identification():
    # def pour pouvoir s'identifier
    global achat, resumer, TresumerK, TresumerMW, panier, siHome_panier, Nbarticle,nom_utilisateur
    if panier == 1:
        # Retirer toutes les images
        for label in liste_labelsImage:
            label.place_forget()
        for label in liste_labelsQuantiter:
            label.place_forget()
    if achat == 1:
        Lacher_image.place_forget()
        Lresumer.place_forget()
        Bacheter.place_forget()
        Lquantiter.place_forget()
        Equantiter.delete(0, "end")
        Equantiter.place_forget()
        LAttention.place_forget()
        achat = 0
    # Afficher/Supprime tous les boutons et le label explicatif
    Canevasfenetre.itemconfig(Logo, image=LogoimagePetit)
    Canevasfenetre.coords(Logo, 450, 100)
    Bhome.place(x=899.5, y=0, anchor="ne")
    Canevas2.config(height=500 - 4)
    Canevas2.place(y=200)
    Lnom_utilisateur.place_forget()
    Bidentification.place_forget()
    BimageNS.place_forget()
    LNintendo_switch.place_forget()
    BPanier.place_forget()
    LAttention.place_forget()
    Bpayer.place_forget()
    if Pas_passer_categorie != 0:
        Bkirby.place_forget()
        BmarioW.place_forget()
        BmarioP.place_forget()
        BAnimal.place_forget()
        BZbotw.place_forget()
        BZtotk.place_forget()
        BPokemon.place_forget()
    Lexplication.place_forget()
    Nbobj = Equantiter.get()
    Lidentifier.place(x=450,y=250,anchor="c")
    Lnom.place(x=250,y=345)
    Lmdp.place(x=250, y=417)
    Enom.place(x=450,y=350,anchor="c")
    Emdp.place(x=450, y=425,anchor="c")
    Bvalider1indentifier.place(x=450,y=525,anchor="c")
    Bcreecompte.place(x=450,y=650,anchor="c")
def Page_cree_compte():
    # Afficher/Supprime tous les boutons et le label explicatif
    # pour cree un compte
    Lidentifier.config(text="Cree un compte")
    Lidentifier.place(x=450, y=250, anchor="c")
    Lnom.place(x=250, y=345)
    Lmdp.place(x=250, y=417)
    Enom.place(x=450, y=350, anchor="c")
    Emdp.place(x=450, y=425, anchor="c")
    Bvalider2Cree.place(x=450, y=525, anchor="c")
    Linfo.place_forget()
    Bvalider1indentifier.place_forget()
    Bcreecompte.place_forget()
def Se_conecter():
    global nom_utilisateur, liste_labelsImage, liste_labelsQuantiter, nbobjs, liste_images
    nom_utilisateur = Enom.get()  # Récupère le nom d'utilisateur
    mdp = Emdp.get()  # et le mot de passe
    if not nom_utilisateur == "" or not mdp == "":  # Vérifie que le nom d'utilisateur et le mot de passe ne sont pas vides
        resultat = verifier_identifiants(nom_utilisateur, mdp)  # Vérifie les identifiants
        if resultat:  # Si les identifiants sont corrects
            # Décompose les résultats retournés par verifier_identifiants
            liste_labelsImage, liste_labelsQuantiter, nbobjs, liste_images = resultat
            Lnom_utilisateur.config(text=nom_utilisateur)
            Linfo.place_forget()
            Home()  # Appelle la fonction Home
        else:
            # Si les identifiants sont incorrects, affiche un message d'erreur
            Linfo.config(text="vous devez donner un nom et/ou un mdp correct")
            Linfo.place(x=450, y=575, anchor="c")
    else:
        # Si le nom d'utilisateur ou le mot de passe est vide, affiche un message d'erreur
        Linfo.config(text="vous devez donner un nom et un mdp")
        Linfo.place(x=450, y=575, anchor="c")
def verifier_identifiants(nom_utilisateur, mdp):  # Vérifie si l'identifiant est correct
    fichier = open('utilisateurs.csv', 'r', encoding='utf-8')  # Ouvre le fichier en lecture
    lignes = fichier.readlines()  # lit toutes les lignes du fichier
    fichier.close()  # Ferme le fichier
    for ligne in lignes:  # Parcourt chaque ligne du fichier
        # Décompose la ligne en ses différents éléments
        utilisateur, mot_de_passe, liste_labelsImage, liste_labelsQuantiter, nbobjs, liste_images = ligne.split(';')
        if utilisateur == nom_utilisateur and mot_de_passe == mdp:  # Si l'utilisateur et le mot de passe correspondent
            # Retourne les listes correspondantes sous forme de chaînes
            return str(liste_labelsImage), str(liste_labelsQuantiter), str(nbobjs), str(liste_images)
    return
def Cree_compte():
    global nom_utilisateur, liste_labelsImage, liste_labelsQuantiter, nbobjs, liste_images
    nom_utilisateur = Enom.get() # Récupère le nom d'utilisateur
    mdp = Emdp.get()  # et le mot de passe
    if not nom_utilisateur == "" or not mdp == "":  # Vérifie que le nom d'utilisateur et le mot de passe ne sont pas vides
        # Sauvegarde le nouvel utilisateur avec les données associées
        sauvegarder_utilisateur(nom_utilisateur, mdp, liste_labelsImage, liste_labelsQuantiter, nbobjs, liste_images)
        Lnom_utilisateur.config(text=nom_utilisateur)  # Met à jour le label avec le nom d'utilisateur
        Linfo.place_forget()  # Cache le label d'information
        Home()  # Appelle la fonction Home
    else:
        # Si le nom d'utilisateur ou le mot de passe est vide, affiche un message d'erreur
        Linfo.config(text="vous devez donner un nom et un mdp")
        Linfo.place(x=450, y=575, anchor="c")
def sauvegarder_utilisateur(login, mdp, liste_labelsImage, liste_labelsQuantiter, nbobjs, liste_images):  # Sauvegarde un utilisateur
    fichier = open('utilisateurs.csv', 'a', encoding='utf-8')  # Ouvre le fichier en mode ajout
    # Écrit les informations de l'utilisateur dans le fichier
    fichier.write(login + ";" + mdp + ";" + str(liste_labelsImage) + ";" + str(liste_labelsQuantiter) + ";" + str(nbobjs) + ";" + str(liste_images) + "\n")
    fichier.close()  # Ferme le fichier
def Payer():
    global achat, resumer, TresumerK, TresumerMW, panier, siHome_panier, Nbarticle, nom_utilisateur
    if nom_utilisateur != "Vous n'etes pas connetcter": # si l utilisateur et connecter
        if Nbarticle != 0: # si l utilisateur a pris un article
            if panier == 1:
                # Retirer toutes les images
                for label in liste_labelsImage:
                    label.place_forget()
                for label in liste_labelsQuantiter:
                    label.place_forget()
            # Afficher/Supprime tous les boutons et le label explicatif
            if achat == 1:
                Lacher_image.place_forget()
                Lresumer.place_forget()
                Bacheter.place_forget()
                Lquantiter.place_forget()
                Equantiter.delete(0, "end")
                Equantiter.place_forget()
                LAttention.place_forget()
                achat = 0
            Canevasfenetre.itemconfig(Logo, image=LogoimagePetit)
            Canevasfenetre.coords(Logo, 450, 100)
            Bhome.place(x=899.5, y=0, anchor="ne")
            Canevas2.config(height=500 - 4)
            Canevas2.place(y=200)
            Bidentification.place_forget()
            BimageNS.place_forget()
            LNintendo_switch.place_forget()
            BPanier.place_forget()
            LAttention.place_forget()
            if Pas_passer_categorie != 0:
                Bkirby.place_forget()
                BmarioW.place_forget()
                BmarioP.place_forget()
                BAnimal.place_forget()
                BZbotw.place_forget()
                BZtotk.place_forget()
                BPokemon.place_forget()
            Lexplication.config(text="votre code de carte bleue :")
            Lexplication.place(x=250, y=400, anchor="c")
            Eachat.place(x=450, y=400, anchor="c")
            Bvaliderpemant.place(x=450, y=500, anchor="c")
        else:
            Linfo.config(text="vous devais posserder des jeux pour pouvoir en acheter")
            Linfo.place(x=450, y=350, anchor="c")
    else:
        Linfo.config(text="vous devais vous connecter ou pouvoir acheter un jeu")
        Linfo.place(x=450, y=180, anchor="c")
        Identification()
def Acheter():
    numcarte = Eachat.get()  # Appeler la méthode get() pour obtenir le texte
    if est_Nombre(numcarte):
        print("vous avais acheter des article")
        Home()
    else:
        Linfo.config(text="Il faut rentrer des chiffres")
        Linfo.place(x=450, y=180, anchor="c")
def est_Nombre(nombre):
    if nombre == "":
        return False
    for caractere in nombre:
        if caractere not in "0123456789":
            return False
    return True
# importation de tout les logo principal des jeu + cration de leur label
Nintendo_switch = PhotoImage(file="image/home/Nintendo_switch.png")
BimageNS = Button(fenetre, image=Nintendo_switch, width=100, height=100,command=LienNintendo_switch)
BimageNS.place(x=450, y=475,anchor="c")
LNintendo_switch = Label(fenetre,text="Nintendo switch",bg="#EDB353",font=("Arial",12,"italic"))
LNintendo_switch.place(x=450,y= 600,anchor="c")
# Placement du logo
Logo = Canevasfenetre.create_image(450, 150, anchor="c", image=LogoimageGrand)
# label pour savoir si ultilisateur est connecter
Lnom_utilisateur = Label(fenetre,text=nom_utilisateur)
Lnom_utilisateur.place(x=0,y=0,anchor="nw")
# Boutton pour amener vers l'identification de l utilisateur
Bidentification = Button(fenetre,text="Identifier vous",bg="#07FFD9",command=Identification)
Bidentification.place(x=900,y=0,anchor="ne")
# identifier
Lidentifier = Label(fenetre,text="S'identifier",font=("Arial", 15, "italic"))
Lidentifier.place_forget()
Lnom = Label(fenetre, text="nom utilisateur: ")
Lnom.place_forget()
Lmdp = Label(fenetre, text="mot de passe: ")
Lmdp.place_forget()
Enom = Entry()
Enom.place_forget()
Emdp = Entry()
Emdp.place_forget()
Bvalider1indentifier = Button(fenetre,text="Valider",bg="#07FFD9",font=("Arial", 12, "italic"),command=Se_conecter)
Bvalider2Cree = Button(fenetre, text="Valider",bg="#07FFD9",font=("Arial", 12, "italic"),command=Cree_compte)
Bcreecompte = Button(fenetre,text=" Créer votre compte LA boite de jeux",bg="#07FFD9",font=("Arial", 12, "italic"),command=Page_cree_compte)
# Boutton qui amener vers le panier
BPanier = Button(fenetre,text="Panier",bg="#07FFD9",command=Panier)
BPanier.place(x=813.5,y=0,anchor="ne")
# Boutton pour ramener au Home
Bhome = Button(fenetre,text="Home",bg="#07FFD9",command=Home)
Bhome.place_forget()
# label pour expliquer
Lexplication = Label(fenetre, text=categorie, bg="#FCD494", font=("Arial", 12, "italic"))
Lexplication.place(x=450, y=275, anchor="c")
# resumer le jeu presant sur la fenetre
Lresumer = Label(Canevas2, text="", bg="#EDB353",font=("Arial", 9, "italic"))
Lresumer.place_forget()
# Pour ajouter au panier
Bacheter = Button(Canevas2,text="Ajouter au panier",bg="#86e22e",font=("Arial",20,"italic"),width=15,height=1,command=Panier)
Bacheter.place_forget()
Lquantiter = Label(Canevas2,text="Nombre d'aticle :",bg="#86e22e",font=("Arial",20,"italic"))
Lquantiter.place_forget()
# permet de mettre une quantiter
Equantiter = Entry(Canevas2,fg="black",bg="#86e22e",font=("Arial",20,"italic"),width=4)
Equantiter.place_forget()
LAttention = Label(Canevas2,text="",bg="#c86699",font=("Arial",15,"italic"))
LAttention.place_forget()
# panier
LNombre_objet = Label(Canevas2,text="Quantiter: "+str(Nbobj))
LNombre_objet.place_forget()
Linfo = Label(fenetre, text="",font=("Arial",12,"italic"))
Linfo.place_forget()
#pour acheter
Bpayer = Button(fenetre,text="Payer",bg="red",font=("Arial",15,"italic"),width=10,height=1,command=Payer)
Bpayer.place_forget()
Eachat = Entry()
Eachat.place_forget()
Bvaliderpemant = Button(fenetre,text="Payer",bg="red",font=("Arial",15,"italic"),width=10,height=1,command=Acheter)
Bvaliderpemant.place_forget()
fenetre.mainloop()