import pyxel
from random import *

Ennemis = []
Tirs = []
Score = 0
vie = 3
def spawn_ennemies():
    global Ennemis
    Ennemis.append(Ennemi(128,randint(0,104)))
def clean_up():
    global Ennemis, Tirs
    for ennemi in Ennemis:
        if ennemi.x > 140 or ennemi.x < -10:
            Ennemis.remove(ennemi)
    for tir in Tirs:
        if tir.x > 140 or tir.x < -10:
            Tirs.remove(tir)
def contact(x_tir, y_tir, x_ennemi, y_ennemi):
    if (x_tir + 5 < x_ennemi) or (x_tir > x_ennemi + 14) or (y_tir + 5 < y_ennemi):
        return False
    else:
        return True
class App:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code")
        pyxel.load("shooter.pyxres")
        self.joueur = Joueur(60,60)
        pyxel.run(self.update, self.draw)

    def update(self):
       global Score, vie, vie_enemie
       self.joueur.update()
       if pyxel.frame_count % 20 == 0:
           spawn_ennemies()
       for ennemi in Ennemis:
           ennemi.update()
       for tirs in Tirs:
           tirs.update()
       for ennemi in Ennemis:
           for tir in Tirs:
               if contact(tir.x, tir.y, ennemi.x, ennemi.y):
                   Ennemis.remove(ennemi)
                   Tirs.remove(tir)
                   Score = Score + 1
       for ennemi in Ennemis:
               if contact(self.joueur.x, self.joueur.y, ennemi.x, ennemi.y):
                    Ennemis.remove(ennemi)
                    vie = vie - 1

       clean_up()

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0 ,pyxel.frame_count%128, 0,128, 128)
        self.joueur.draw()
        for ennemi in Ennemis:
            ennemi.draw()
        for tirs in Tirs:
            tirs.draw()
        pyxel.text(00, 00, "Score : " + str(Score),9)
        if vie > 0:
            pyxel.text(100, 00, "vie : " + str(vie),9)
        else:
            pyxel.text(50, 50, "You are dead: ", 9)

class Joueur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nb = 0
        self.vie = 3
        self.tire = 0
    def update(self):
        self.x = max(0, min(self.x, pyxel.width - 8))
        self.y = max(0, min(self.y, pyxel.height - 8))
        if pyxel.btn(pyxel.KEY_Z):
            self.y = self.y - 2
        if pyxel.btn(pyxel.KEY_S):
            self.y = self.y + 2
        if pyxel.btn(pyxel.KEY_Q):
            self.x =  self.x - 2
        if pyxel.btn(pyxel.KEY_D):
            self.x = self.x + 2
        if pyxel.btn(pyxel.KEY_SPACE):
            self.tire = self.tire + 1
            if self.tire == 5:
                Tirs.append(TirAmi(self.x,self.y))
                self.tire = 0


        self.nb_pas = (pyxel.frame_count // 4) % 2
        pyxel.blt(self.x, self.y, 1,0 + self.nb_pas * 16, 24,  16, 16, 5)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0 + self.nb_pas * 16, 24, 16, 16, 5)

class Ennemi:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nb_pas = 0
        self.vie = 1
    def update(self):
        self.x = self.x - 1
        self.nb_pas = (self.nb_pas + 1) % 4
        pyxel.blt(self.x, self.y, 0, 0 + self.nb_pas * 16, 136, -16, 16, 5)
    def draw(self):
        pyxel.blt(self.x, self.y, 0,  0 + self.nb_pas * 16, 136,-16, 16, 5)


class TirAmi:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nb_pas = 0
    def update(self):
        self.x = self.x + 2
        self.nb_pas = (self.nb_pas + 1) % 4
        pyxel.blt(self.x, self.y, 0, 33 + self.nb_pas * 8, 9, 6, 6, 5)
    def draw(self):
        pyxel.blt(self.x, self.y, 0,  33 + self.nb_pas * 8, 9, 6, 6, 5)


App()
