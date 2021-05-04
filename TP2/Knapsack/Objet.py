import random


class Objet:
    def __init__(self,valeur,poids):
        self.valeur = valeur
        self.poids = poids
    
    def setValeur(self,valeur):
        self.valeur = valeur
    
    def setPoids(self,poids):
        self.poids = poids
    
    def getValeur(self):
        return self.valeur
    
    def getPoids(self):
        return self.poids   
    
    def generateTest(self,n):
        lst = []
        for i in range(n):
            lst.append(Objet(random.randint(1,22),random.randint(1,22)))
        return lst