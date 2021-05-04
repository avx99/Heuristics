from Solution import *
from Objet import *
import random
import time

class SacDos:
    def __init__(self,objets,capacite):
        self.objets = objets
        self.capacite = capacite
        
    def setObjets(self,objets):
        self.objets = objets
    
    def setCapacite(self,capacite):
        self.capacite = capacite
    
    def getObjets(self):
        return self.objets
    
    def getCapacite(self):
        return self.capacite
    
    def glouton1(self): #return a solution obj

        # start_time = time.time()
        lst = [(i.getValeur()/i.getPoids()) for i in self.objets]
        instance = [False for i in range(len(self.objets))]
        s = 0
        fctObj = 0
        while True:
            index = lst.index(max(lst))
            s = s + self.objets[index].getPoids()
            if s > self.capacite:
                break
            lst[index] = min(lst)
            instance[index] = True
            fctObj = fctObj + self.objets[index].getValeur()
        # print(- start_time + time.time())
        return Solution(instance,fctObj)

    def glouton2(self): #return a solution obj
        # start_time = time.time()    
        lst = [i.getValeur() for i in self.objets]
        instance = [False for i in range(len(self.objets))]
        s = 0
        fctObj = 0
        while True:
            index = lst.index(max(lst))
            s = s + self.objets[index].getPoids()
            if s > self.capacite:
                break
            lst[index] = min(lst)
            instance[index] = True
            fctObj = fctObj + self.objets[index].getValeur()
        # print(- start_time + time.time())
        return Solution(instance,fctObj)
