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
    
    def fctObj(self,lst):
        fct = 0
        for i in range(len(lst)):
            if lst[i] == True:
                fct += self.objets[i].getValeur()
        return fct
    
    def poids(self,lst):
        fct = 0
        for i in range(len(lst)):
            if lst[i] == True:
                fct += self.objets[i].getPoids()
        return fct
    
    def hamming(self,a,i):
        lst = a.copy()
        lst[i] = not lst[i]
        return lst
    
    def neighboors(self,lst):
        l = []
        fct = []
        n = len(lst)
        for i in range(n):
            x = self.hamming(lst, i)
            if self.poids(x) <= self.capacite:
                l.append(x)
                fct.append(self.fctObj(x))
        return l,fct
        
        
        
    def descente(self):
        s = self.glouton2()
        i = 0
        while True:
            i += 1
            if i == 50:
                print(i)
                return s
            neighbors,fct = self.neighboors(s.getInstance())
            index = fct.index(max(fct))
            newSol = neighbors[index]
            if self.fctObj(s.getInstance()) > fct[index]:
                return s
            s = Solution(newSol,fct[index])
        
      
    # def boltzmane(self,s0,s,T):
    #     if T != 0:
    #         return math.exp((self.fonctionObjectif(s0)-self.fonctionObjectif(s))/T)
    #     return 1
    
    # def recuitSimule(self,start,T):
    #     fct = []
    #     ch = []
    #     s0 = self.glouton1(start)
    #     s = self.glouton1(start+3)
    #     n = len(s0.getChemin())
    #     T = [2**(-i) for i in range(T)]
    #     for i in T:
    #         while True:
    #             i = random.randint(0, n-2)
    #             j = random.randint(i+1, n-1)
    #             s = Solution(self.twoOpt(s0.getChemin(),i,j),self.fonctionObjectif(self.twoOpt(s0.getChemin(),i,j)))
    #             r = random.random()
    #             if r < self.boltzmane(s0.getChemin(), s.getChemin(), i):
    #                 fct.append(s.getFct())
    #                 ch.append(s.getChemin())
    #                 s0 = s
    #                 break
    #     index = fct.index(min(fct))
    #     return Solution(ch[index],fct[index])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
