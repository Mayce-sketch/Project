#08/09/2023
print("\n")
print("Vous êtes dans la vie d'un nouvel employé d'un restaurant à Paris."
      "C'est votre premier jour aujourd'hui.")
print("Vous entrez dans le restaurant. Vous voyez vos nouveaux collègues et vous demande.")
print("")
nom = input("-Comment tu t'appelle ? ")
test = input("Ton nom est bien "+nom+" ?(oui/non) ")
while test != "oui" and test != "non":
    print("Il faut que tu me dise oui ou non.")
    test = input("Ton nom est bien " + nom + " ?(oui/non) ")
while test == "non":
    nom = input("Redonne moi ton nom. ")
    test = input("Ton nom est bien "+nom+" ?(oui/non) ")
    while test != "oui" and test != "non":
        print("Il faut que tu me dise oui ou non")
        test = input("Ton non est bien " + nom + " ?(oui/non) ")
print("-OK salut", nom, ",moi c'est tom.")
print("D'ailleurs le patron te cherche va le voir,"
      " je crois qu'il a du travaille pour toi.")
print("-Ok, je vais le voir.")
print("Bonjour, moi c'est lucas, c'est toi", nom, "?")
print("Oui c'est moi.")
print("")
nombre1 = str(input("Tu veux faire de la cuisine (repondre 0)""\n"
                    "ou mettre la table pour les clients (repondre 1) ? "))
while nombre1 != str(0) and nombre1 != str(1):
    nombre1 = str(input("Tu doit donner un nombre entre 0 et 1. "))
travaille = int(nombre1) == 0
if travaille == True:
    print("-Ok alors va te laver les main et commence a faire la vaisselle.")
    print("-J'y vais tout de suite.")
    print("Apres avoir terminer la vaisselle je vais voir le patron.")
    print("-J'ai fini la vaisselle.Qu'est ce que je fait maintenant ?")
    print("")
    nombre2 = str(input("-Tu peux soi nous aider a nétoyer les tables (repondre 0)""\n"
                        "ou soit aller jeter les déches à la poubelle  (repondre 1)."))
    while nombre2 != str(0) and nombre2 != str(1):
        nombre2 = input("Tu doit donner un nombre entre 0 et 1. ")
    tache1 = int(nombre2) == 0
    if tache1 == True:
        print("-Je m'en douter, après avoir fini"
              " tu pouras partir et ta premier jounée sera teminée.")
        print("-Je mis met tout de suite.")
        print("C'est bon j'ai enfin fini je vais pouvoir retre chez moi.")
        print("FIN")
    else:
        print("-Bon bat va sortir les poubelle du coup,après avoir fini"
              " tu pouras partir et ta premier jounée sera teminée.")
        print("C'est bon j'ai fini."
              " Je vais me laver les main et après je pourais retrer chez moi.")
        print("FIN")
else:
    print("-Ok vat mettre la table pour les clients alors.")
    print("-Ok")
    print("Après avoir fini de mette la tabe je vais retouner voir lucas.")
    print("-C'est bon lucas, j'ai fini de preparer les tables qu'est ce que je fais maintenant.")
    print("")
    nombre3 = str(input("Tu peux aller servir les client qui arrive (reponce 0)""\n"
                        "ou tu peux les places a des tables (reponce 1) ? "))
    while nombre3 != str(0) and nombre3 != str(1):
        nombre3 = input("Tu doit donner un nombre entre 0 et 1. ")
    tache2 = int(nombre3) == 0
    if tache2 == True:
        print("-Quand le servise sera terminer tu pouras partir,"
              " ta premiere journée sera terminé.")
        print("Après avoir terminer le sevise je parti pour rentrer chez moi.")
        print("FIN")
    else:
        print("Bon bat vat acceuillire les clients et place les aux tables.")
        print("Quand tout les clients seront parti tu pourras aussi partir .")
        print("C'est bon il y a plus personne, je peux m'en aller.")
        print("FIN")






