from random import randint

class Monster:
    def __init__(self):
        self.x = randint(0, 256)
        self.y = randint(128, 256)
        self.affirmation = "affirme"
        self.reponse1 = "reponse1"
        self.reponse2 = "reponse2"
        self.reponse3 = "reponse3"
        self.reponse4 = "reponse4"
        self.bonne_number = 1