import pyxel

class Player:
    def __init__(self):
        self.x = 32
        self.y = 32
        self.score = 0
        self.back = False

    def move(self):
        if pyxel.btnp(pyxel.KEY_UP):
            if self.y - 10 > 0:
                self.y -= 10
            self.back = True
        if pyxel.btnp(pyxel.KEY_DOWN):
            if self.y + 10 < 256:
                self.y += 10
            self.back = False
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.x + 10 < 256:
                self.x += 10
        if pyxel.btnp(pyxel.KEY_LEFT):
            if self.x - 10 > 0:
                self.x -= 10

    def victoire(self):
        self.score += 1
