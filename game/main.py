import pyxel, math
from joueur import Joueur
from mob import aleatoire, Mob

#en attendant pyxel colision
colision = True

class Jeu:
    def __init__(self):
        self.joueur = Joueur()
        self.mob = Mob()

        #ârtie Noé Pyxel
        self.joueur = Joueur()
        pyxel.init(256, 256, title="Nom", fps=60, quit_key=pyxel.KEY_ESCAPE )
        pyxel.run(self.update, self.draw)
        pyxel.load("./ndc.pyxres")

    #partie Pyxel
    def update (self):
        self.joueur.move()
    #partie pyxel
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.joueur.x, self.joueur.y, 10, 10, 3)
        pyxel.bltm(0, 0, 0, 0, 0, 15, 15)




    def battle(self):
        print(f" le polluant affirme que {self.mob.fakenew}")
        print("Quelle est la vraie affirmation ?")
        print(f"1 : {self.joueur.bonne_reponse}")
        print(f"2 : {self.joueur.reponse2}")
        print(f"3 : {self.joueur.reponse3}")
        print(f"4 : {self.joueur.reponse4}")
        reponse = int(input("quelle est l'information correcte ? "))
        #actuellement pas aléatoire, ça sera forcement la première réponse
        if reponse == 1:
            print("vous avez éradiquer la fake nex !")
            self.joueur.plus_nb_bonne_reponse()
        else :
            print("vous vous êtes laissé avoir par la fake new !...")
            self.joueur.plus_nb_mauvaise_reponse()


    def run(self):
        if colision:
            print("vous avez rencontré un polluant !")
            self.joueur.battle()

jeu = Jeu()
jeu.run()
