import pyxel

class Player:
    def __init__(self):
        self.x = 32
        self.y = 32
        self.speed = 10
        self.nb_mauvaise_reponse = 0
        self.nb_bonne_reponse = 0
        self.pv = 5
        self.pvmax = self.pv

    def move(self):
        if pyxel.btnp(pyxel.KEY_UP):
            if self.y - self.speed > 0:
                self.y -= self.speed
        if pyxel.btnp(pyxel.KEY_DOWN):
            if self.y + self.speed < 256:
                self.y += self.speed
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.x + self.speed < 256:
                self.x += self.speed
        if pyxel.btnp(pyxel.KEY_LEFT):
            if self.x - self.speed > 0:
                self.x -= self.speed

    def victoire(self):
        self.score += 1

    def plus_nb_bonne_reponse(self):
        self.nb_bonne_reponse += 1

    def plus_nb_mauvaise_reponse(self):
        self.nb_mauvaise_reponse += 1
        self.pv -= 1
