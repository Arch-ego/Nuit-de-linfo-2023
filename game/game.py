import pyxel, json
from player import Player
from monster import Monster
from villager import Villager
from random import choice, shuffle, randint
from os.path import join, dirname, realpath

coupe = lambda x: (x[:len(x)//2], x[len(x)//2:])

class Jeu:
    def __init__ (self):
        self.player = Player()
        self.etat = "start"
        self.adv = None
        self.pnj = None
        self.list_monster = []
        self.list_villager = [Villager(10, 20),Villager(5, 60),Villager(60, 10),Villager(60, 50),Villager(90, 90)]
        pyxel.init(256, 256, title="Ecodève.exe", fps=30, quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("static/my_resource.pyxres")
        pyxel.playm(0, 1000, True)
        pyxel.run(self.update, self.draw)
    
    def creation_monstre(self):
        with open(join(join(dirname(realpath(__file__)),'database'), "data.json"), "r") as file:
            data = json.load(file)
        for _ in range(5):
            i = randint(0, len(data))
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
            pyxel.text(5, 10, f"Le polluant affirme que :", 1)
            pyxel.text(5, 20, f"{coupe(coupe(self.adv.facts)[0])[0]}", 2)
            pyxel.text(5, 30, f"{coupe(coupe(self.adv.facts)[0])[1]}", 2)
            pyxel.text(5, 40, f"{coupe(coupe(self.adv.facts)[1])[0]}", 2)
            pyxel.text(5, 50, f"{coupe(coupe(self.adv.facts)[1])[1]}", 2)
            pyxel.text(5, 70, "Quelle est la vraie affirmation ?", 1)
            pyxel.text(5, 80, f"1 : {coupe(coupe(self.adv.reponse1)[0])[0]}", 3)
            pyxel.text(5, 90, f"{coupe(coupe(self.adv.reponse1)[0])[1]}", 3)
            pyxel.text(5, 100, f"{coupe(coupe(self.adv.reponse1)[1])[0]}", 3)
            pyxel.text(5, 110, f"{coupe(coupe(self.adv.reponse1)[1])[1]}", 3)
            pyxel.text(5, 120, f"2: {coupe(coupe(self.adv.reponse2)[0])[0]}", 3)
            pyxel.text(5, 130, f"{coupe(coupe(self.adv.reponse2)[0])[1]}", 3)
            pyxel.text(5, 140, f"{coupe(coupe(self.adv.reponse2)[1])[0]}", 3)
            pyxel.text(5, 150, f"{coupe(coupe(self.adv.reponse2)[1])[1]}", 3)
            pyxel.text(5, 160, f"3 : {coupe(coupe(self.adv.reponse3)[0])[0]}", 3)
            pyxel.text(5, 170, f"{coupe(coupe(self.adv.reponse3)[0])[1]}", 3)
            pyxel.text(5, 180, f"{coupe(coupe(self.adv.reponse3)[1])[0]}", 3)
            pyxel.text(5, 190, f"{coupe(coupe(self.adv.reponse3)[1])[1]}", 3)
            pyxel.text(5, 200, f"4: {coupe(coupe(self.adv.reponse4)[0])[0]}", 3)
            pyxel.text(5, 210, f"{coupe(coupe(self.adv.reponse4)[0])[1]}", 3)
            pyxel.text(5, 220, f"{coupe(coupe(self.adv.reponse4)[1])[0]}", 3)
            pyxel.text(5, 230, f"{coupe(coupe(self.adv.reponse4)[1])[1]}", 3)
            pyxel.text(5, 240, "quelle est l'information correcte ?", 2)
        elif self.etat == "talking":
            pyxel.cls(0)
            with open(join(join(dirname(realpath(__file__)),'database'), "data.json"), "r") as file:
                data = json.load(file)
            pyxel.text(5, 10, " Le villageois affirme que", 1)
            pyxel.text(5, 20, f"{coupe(coupe(data['sessions']['uuid'][self.list_villager.index(self.pnj)]['correctResponse'])[0])[0]}", 2)
            pyxel.text(5, 30, f"{coupe(coupe(data['sessions']['uuid'][self.list_villager.index(self.pnj)]['correctResponse'])[0])[1]}", 2)
            pyxel.text(5, 40, f"{coupe(coupe(data['sessions']['uuid'][self.list_villager.index(self.pnj)]['correctResponse'])[1])[0]}", 2)
            pyxel.text(5, 50, f"{coupe(coupe(data['sessions']['uuid'][self.list_villager.index(self.pnj)]['correctResponse'])[1])[1]}", 2)
            pyxel.text(5, 60, "Appuie sur E pour retourner sur le jeu", 3)
        if len(self.list_monster) == 0:
            pyxel.cls(0)
            pyxel.text(100, 130, "Vous avez gagne!", 8)

Jeu()