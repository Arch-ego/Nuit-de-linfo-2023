import pyxel
from player import Player
from monster import Monster
from villager import Villager
from random import choice

class Jeu:
    def __init__ (self):
        self.player = Player()
        self.etat = "move"
        self.adv = None
        self.list_monster = [Monster(),Monster(),Monster(),Monster(),Monster()]
        self.list_villager = [Villager(20, 0),Villager(40, 0),Villager(60, 0),Villager(80, 0),Villager(100, 0)]
        pyxel.init(256, 256, title="Nom", fps=30, quit_key=pyxel.KEY_ESCAPE)
        pyxel.run(self.update, self.draw)

    def deplacement_monstre(self):
        for m in self.list_monster:
            pos = []
            if m.x < 218:
                pos.append("d")
                if m.x > 32:
                    pos.append("g")
                if m.y < 218:
                    pos.append("b")
                if m.y > 144:
                    pos.append("h")
            if len(pos) != 0:
                res = choice(pos)
                if res == "d":
                    m.x += 16
                elif res == "g":
                    m.x -= 16
                elif res == "h":
                    m.y -= 16
                elif res == "b":
                    m.y += 16

    def check_collision(self):
        for m in self.list_monster:
            if m.x <= self.player.x+16 and m.y <= self.player.y+16 and m.x+16 >= self.player.x and m.y+16 >= self.player.y:
                self.etat = "combat"
                self.battle(m)
                self.adv = m

    def battle(self, monster:Monster):
        if pyxel.btnp(pyxel.KEY_1):
            if monster.bonne_number == 1:
                self.player.plus_nb_bonne_reponse()
            else:
                self.player.plus_nb_mauvaise_reponse()
        elif pyxel.btnp(pyxel.KEY_2):
            if monster.bonne_number == 2:
                self.player.plus_nb_bonne_reponse()
            else:
                self.player.plus_nb_mauvaise_reponse()
        elif pyxel.btnp(pyxel.KEY_3):
            if monster.bonne_number == 3:
                self.player.plus_nb_bonne_reponse()
            else:
                self.player.plus_nb_mauvaise_reponse()
        elif pyxel.btnp(pyxel.KEY_4):
            if monster.bonne_number == 4:
                self.player.plus_nb_bonne_reponse()
            else:
                self.player.plus_nb_mauvaise_reponse()    
    
    def update(self):
        if self.etat == "move":
            self.player.move()
            if pyxel.frame_count % 30 == 1:
                self.deplacement_monstre()
            self.check_collision()
        elif self.etat == "combat":
            self.battle(self.adv)

    def draw(self):
        pyxel.cls(0)
        if self.etat == "move":
            pyxel.rect(self.player.x, self.player.y, 16, 16, 3)
            for m in self.list_monster:
                pyxel.rect(m.x, m.y, 16, 16, 7)
            for v in self.list_villager:
                pyxel.rect(v.x, v.y, 16, 16, 8)
        elif self.etat == "combat":
            pyxel.text(10, 10, f" le polluant affirme que {self.adv.affirmation}", 1)
            pyxel.text(10, 20, "Quelle est la vraie affirmation ?", 1)
            pyxel.text(10, 30, f"1 : {self.adv.reponse1}", 1)
            pyxel.text(10, 40, f"2 : {self.adv.reponse2}", 1)
            pyxel.text(10, 50, f"3 : {self.adv.reponse3}", 1)
            pyxel.text(10, 60, f"4 : {self.adv.reponse4}", 1)
            pyxel.text(10, 70, "quelle est l'information correcte ?", 2)

Jeu()
