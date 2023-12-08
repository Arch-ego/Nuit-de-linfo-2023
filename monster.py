from random import randint

class Monster:
    def __init__(self, facts, reponse1, reponse2, reponse3, reponse4, good_response):
        self.x = randint(32, 218)
        self.y = randint(144, 218)
        self.left = False
        self.facts:str = facts
        self.reponse1:str = reponse1
        self.reponse2:str = reponse2
        self.reponse3:str = reponse3
        self.reponse4:str = reponse4
        self.good_response:str = good_response