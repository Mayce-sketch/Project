#17/10/2023
from random import *
total = 0
question_poser = 5
tour = 0
nombre1 = 0
naturel = 0
multiplier1 = 1
score = 0

def est_un_nombre(nombre):
    if nombre == "":
        return False
    for caractere in nombre:
        if caractere not in '0123456789':
            return False
    return True

def statut(notation):
    # je sais pas si j'ai le droit d'utiliser or donc je ne l'ai pas uiliser(1 et 2),(3 et 4)
    # elif notation == 1 or 2:
    if notation == 0:
        print("tu a obtenue aucune bonne reponce")
    elif notation == 1:
        print("tu a obtenue moins de la moitié de point")
    elif notation == 2:
        print("tu a obtenue moins de la moitié de point")
    elif notation == 3:
        print("tu as obtenue plus de la moitié des points")
    elif notation == 4:
        print("tu as obtenue plus de la moitié des points")
    elif notation == 5:
        print("tu as obtenue tout les bonnes reponce bravo")

print("\n")
print("Bonjour, vous aller passer un test de math avec different exercice:\n"
      "l'exercice 1 est plutot facile est l'exercice 3 et le plus difficile,"
      "(vous pouver a tout moment quiter le test avec 's'):")
choix = input("vous devais choisir entre:\nL'exercice'1'\nL'exercice'2'\nL'exercice'3'\n: ")
while str(choix) != str(1) and str(choix) != str(2) and str(choix) != str(3) and choix != "s":
    choix = input("vous devez entez un nombre entre 1,2 ou 3, ou quitter le test avec 's': ")

if choix == "s":
    print("Vous avez choisi de quitter l'exercice.")

# debut de l'exercice 1
if choix == str(1):
    resultat1 = ""
    print("vous avez choisi le niveau 1 ")
    choix_du_nombre = input("choisissez un nombre entier naturel et non nul: ")
    sortir = True
    while est_un_nombre(choix_du_nombre) == False and sortir:
        if choix_du_nombre == 's':
            print("Vous avez choisi de quitter l'exercice.")
            sortir = False
        else:
            print("Ce n'est pas un nombre valide. Veuillez réessayer.")
            choix_du_nombre = input("choisissez un nombre entier naturel et non nul:")
    if choix_du_nombre != "s":
        naturel = int(choix_du_nombre)
        while tour < question_poser and total < question_poser:
            print(choix_du_nombre, "x", multiplier1, "= ", end="")
            resultat1 = input("")
            if resultat1 != "s":
                if est_un_nombre(resultat1):
                    if int(resultat1) == int(choix_du_nombre) * multiplier1:
                        tour = tour + 1
                        multiplier1 = multiplier1 + 1
                        score = score + 1
                        total = total + 1
                        print("vous avez mis une bonne réponse. ")
                    else:
                        print("tu as mis une mauvaise réponse. ")
                        total = total + 1
                else:
                    print("Ce n'est pas un nombre valide.")
                    total = total + 1
            else:
                tour = tour + 10
                total = total + 1
    print("")
    print("votre score est de", score, "sur", total, ".")
    statut(score)

# debut de l'exercice 2
if choix == str(2):
    print("vous avez choisi le niveau 2")
    while tour < question_poser and total < question_poser:
        choix_du_nombre = (randint(1, 10))
        multiplier1 = randint(1, 10)
        print(choix_du_nombre, "x", multiplier1, "= ", end="")
        resultat1 = input("")
        if resultat1 != "s":
            if est_un_nombre(resultat1):
                if int(resultat1) == choix_du_nombre * multiplier1:
                    print("tu as mis une bonne reponce. ")
                    tour = tour + 1
                    multiplier1 = multiplier1 + 1
                    score = score + 1
                    total = total + 1
                else:
                    print("vous avez mis une mauvese reponce. ")
                    total = total + 1
            else:
                print("Ce n'est pas un nombre valide.")
                total = total + 1
        else:
            tour = tour + 10
            total = total + 1
    print("")
    print("votre score est de", score, "sur", total, ".")
    statut(score)

# debut de l'exercice 3
if choix == str(3):
    print("vous avez choisi le niveau 3")
    while tour < question_poser and total < question_poser:
        multiplicateur3 = (randint(1, 10))
        multiplier3 = randint(1, 10)
        addition = randint(1, 10)
        tirage2 = ""
        fois = "x"
        plus = "+"
        liste = [fois, plus]
        tirage1 = choice(liste)
        if tirage1 == fois:
            tirage2 = plus
            print(multiplicateur3, tirage1, multiplier3, tirage2, addition, "= ", end="")
        else:
            tirage2 = fois
            print(multiplicateur3, tirage1, multiplier3, tirage2, addition, "= ", end="")
        resultat3 = input("")
        if resultat3 != "s":
            if est_un_nombre(resultat3):
                if tirage1 == fois:
                    if int(resultat3) == multiplicateur3 * multiplier3 + addition:
                        multiplier3 = (randint(1, 10))
                        multiplicateur3 = (randint(1, 10))
                        addition = (randint(1, 10))
                        score = score + 1
                        tour = tour + 1
                        total = total + 1
                        print("tu as mis une bonne reponce. ")
                    else:
                        total = total + 1
                        print("vous mis une mauvaise reponce.")
                elif tirage1 == plus:
                    if int(resultat3) == multiplicateur3 + multiplier3 * addition:
                        multiplier3 = (randint(1, 10))
                        multiplicateur3 = (randint(1, 10))
                        addition = (randint(1, 10))
                        score = score + 1
                        tour = tour + 1
                        total = total + 1
                        print("tu as mis une bonne reponce. ")
                    else:
                        total = total + 1
                        print("vous mis une mauvaise reponce.")
            else:
                print("Ce n'est pas un nombre valide.")
                total = total + 1
        else:
            tour = tour + 10
            total = total + 1
    print("")
    print("votre score est de", score, "sur", total, ".")
    statut(score)
