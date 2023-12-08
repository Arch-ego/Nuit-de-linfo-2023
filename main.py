import pyxel, json, sqlite3
from player import Player
from monster import Monster
from villager import Villager
from random import choice, shuffle
from os.path import join, dirname, realpath

con = sqlite3.connect(join(join(dirname(realpath(__file__)),'database'), "ndl.db"), check_same_thread=False)
cur = con.cursor()

print(cur.execute("SELECT * FROM Game;").fetchall())
class Jeu:
    def __init__ (self):
        self.player = Player()
        self.etat = "start"
        self.adv = None
        self.pnj = None
        self.list_monster = []
        self.list_villager = [Villager(10, 20),Villager(5, 60),Villager(60, 10),Villager(60, 50),Villager(90, 90)]
        pyxel.init(256, 256, title="Nom", fps=30, quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("static/my_resource.pyxres")
        pyxel.playm(0, 1000, True)
        pyxel.run(self.update, self.draw)
    
    def creation_monstre(self):
        with open(join(join(dirname(realpath(__file__)),'database'), "data.json"), "r") as file:
            data = json.load(file)
        for i in range(5):
            response: list = [r for r in data["sessions"]["uuid"][i]["badResponses"]]
            response.append(data["sessions"]["uuid"][i]["correctResponse"])
            shuffle(response)
            self.list_monster.append(Monster(data["sessions"]["uuid"][i]["monsterDialog"], response[0], response[1], response[2], response[3], response.index(data["sessions"]["uuid"][i]["correctResponse"])+1))
        
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
                    m.left = False
                elif res == "g":
                    m.x -= 16
                    m.left = True
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
        for v in self.list_villager:
            if v.x <= self.player.x+16 and v.y <= self.player.y+16 and v.x+16 >= self.player.x and v.y+16 >= self.player.y:
                self.etat = "talking"
                self.pnj = v

    def battle(self, monster:Monster):
        if pyxel.btnp(pyxel.KEY_1):
            if monster.good_response == 1:
                self.player.victoire()
                self.list_monster.remove(monster)
            self.etat = "move"
            self.player.x, self.player.y = 32, 32
        elif pyxel.btnp(pyxel.KEY_2):
            if monster.good_response == 2:
                self.player.victoire()
                self.list_monster.remove(monster)
            self.etat = "move"
            self.player.x, self.player.y = 32, 32
        elif pyxel.btnp(pyxel.KEY_3):
            if monster.good_response == 3:
                self.player.victoire()
                self.list_monster.remove(monster)
            self.etat = "move"
            self.player.x, self.player.y = 32, 32
        elif pyxel.btnp(pyxel.KEY_4):
            if monster.good_response == 4:
                self.player.victoire()
                self.list_monster.remove(monster)
            self.etat = "move"
            self.player.x, self.player.y = 32, 32
    
    def check_talk(self):
        if pyxel.btnp(pyxel.KEY_E):
            self.etat = "move"
            self.player.x, self.player.y = 32, 32
    def update(self):
        if self.etat == "start":
            self.creation_monstre()
            self.etat = "move"
        if self.etat == "move":
            self.player.move()
            if pyxel.frame_count % 30 == 1:
                self.deplacement_monstre()
            self.check_collision()
        elif self.etat == "combat":
            self.battle(self.adv)
        elif self.etat == "talking":
            self.check_talk()

    def draw(self):
        pyxel.bltm(0, 0, 0, 15, 15, 256, 256)
        if self.etat == "move":
            if self.player.back:
                pyxel.blt(self.player.x, self.player.y, 0, 35, 37, 9, 11, 7)
            else:
                pyxel.blt(self.player.x, self.player.y, 0, 19, 37, 9, 11, 7)
            for m in self.list_monster:
                if m.left:
                    pyxel.blt(m.x, m.y, 0, 35, 58, 9, 7, 7)
                else:
                    pyxel.blt(m.x, m.y, 0, 51, 58, 9, 7, 7)

            for v in self.list_villager:
                pyxel.blt(v.x, v.y, 0, 51, 37, 8, 11, 7)
        elif self.etat == "combat":
            pyxel.cls(0)
            pyxel.text(10, 10, f" le polluant affirme que {self.adv.facts}", 1)
            pyxel.text(10, 20, "Quelle est la vraie affirmation ?", 1)
            pyxel.text(10, 30, f"1 : {self.adv.reponse1}", 1)
            pyxel.text(10, 40, f"2 : {self.adv.reponse2}", 1)
            pyxel.text(10, 50, f"3 : {self.adv.reponse3}", 1)
            pyxel.text(10, 60, f"4 : {self.adv.reponse4}", 1)
            pyxel.text(10, 70, "quelle est l'information correcte ?", 2)
        elif self.etat == "talking":
            pyxel.cls(0)
            with open(join(join(dirname(realpath(__file__)),'database'), "data.json"), "r") as file:
                data = json.load(file)
                
            pyxel.text(10, 10, " Le villageois affirme que", 1)
            pyxel.text(10, 20, f"{data['sessions']['uuid'][self.list_villager.index(self.pnj)]['NPCDialog']}", 1)
            pyxel.text(10, 30, "Appuie sur E pour retourner sur le jeu", 3)
        if len(self.list_monster) == 0:
            pyxel.cls(0)
            pyxel.text(100, 130, "Vous avez gagne!", 8)

Jeu()