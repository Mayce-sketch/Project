import pyxel
from random import *

Ennemis = []
Score = 0
vie = 3
fram_enemie = 35
nb_enemie = 0

def spawn_ennemies():
    global Ennemis
    resu = randint(0,1)
    if resu == 0 :
        Ennemis.append(Ennemi(128,48))
    else:
        Ennemis.append(Ennemi(128, 80))
def clean_up():
    global Ennemis
    for ennemi in Ennemis:
        if ennemi.x > 130 or ennemi.x < -10:
            Ennemis.remove(ennemi)

def contact(x_joueur, y_joueur, x_ennemi, y_ennemi):
    flag = False
    if (x_ennemi - 9 <= x_joueur <= x_ennemi + 9) and (y_ennemi - 9 <= y_joueur  <= y_ennemi + 9):
        flag = True
    return flag
class App:
    def __init__(self):
        pyxel.init(128,128,fps=45, title="Nuit du Code")
        pyxel.load("2.pyxres")
        self.joueur = Joueur(10,40)
        self.Flag = True
        pyxel.run(self.update,self.draw)
    def update(self):
        global Score, vie, fram_enemie, nb_enemie
        if self.Flag == True:
            Score = Score + 4
            if Score % 1600 == 0 :
                vie = vie + 1
            self.joueur.update()
            if pyxel.frame_count % fram_enemie == 0:
                spawn_ennemies()
            for ennemi in Ennemis:
                ennemi.update()
            for ennemi in Ennemis:
                if contact(self.joueur.x, self.joueur.y, ennemi.x, ennemi.y):
                    Ennemis.remove(ennemi)
                    vie = vie - 1
            clean_up()
            if nb_enemie <= 0.5:
                nb_enemie = nb_enemie + 0.01
            elif nb_enemie >= 0.5 and fram_enemie >= 20.5:
                    nb_enemie = 0
                    fram_enemie = fram_enemie - 0.5




    def draw(self):
        if self.Flag == True:
            pyxel.cls(13)
            pyxel.bltm(0, 0, 0 ,pyxel.frame_count%256, 0,128, 128)
            self.joueur.draw()
            for ennemi in Ennemis:
                ennemi.draw()
            pyxel.text(0, 0, "Score : " + str(Score//100),0)
            pyxel.text(44, 105, "Commande : " ,0)
            pyxel.text(7, 112.5, "fleche haut/bas/gauche/droite " ,0)
            pyxel.text(7, 120, "une vie tout les 16 points ;) " ,0)
            if vie > 0:
                pyxel.text(100, 0, "vie : " + str(vie), 0)
            elif Score == 120:
                pyxel.text(44, 20, "Victory: ", 0)
                self.Flag = False
            else:
                pyxel.text(44, 20, "You are dead: ", 0)
                self.Flag = False
class Joueur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            if not self.x <=2 :
                self.x = self.x - 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x >=110 :
                self.x = self.x - 2
            self.x = self.x + 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y = 72
        if pyxel.btn(pyxel.KEY_UP):
            self.y = 40
        self.nb_pas = (pyxel.frame_count // 4) % 2
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0 + self.nb_pas * 16, 8, 16,24,2)
class Ennemi:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nb_pas = 0
    def update(self):
        self.x = self.x - 1
        self.nb_pas = (pyxel.frame_count // 4) % 2
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 64 + self.nb_pas * 16,16 ,-16, 16, 2)

App()