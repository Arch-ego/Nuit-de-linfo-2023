from random import randint

class Monster:
    def __init__(self, facts, reponse1, reponse2, reponse3, reponse4, good_response):
        self.x = randint(32, 218)
        self.y = randint(144, 218)
        self.left = False
        self.facts = facts
        self.reponse1 = reponse1
        self.reponse2 = reponse2
        self.reponse3 = reponse3
        self.reponse4 = reponse4
        self.good_response = good_response