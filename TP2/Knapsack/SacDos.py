from Solution import *
from Objet import *
import random
import time
import math

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
        p = 0
        while True:
            index = lst.index(max(lst))
            s = s + self.objets[index].getPoids()
            if s > self.capacite:
                break
            lst[index] = min(lst)
            instance[index] = True
            fctObj = fctObj + self.objets[index].getValeur()
            p = p + self.objets[index].getPoids()
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
        
        
    def neighboorsRecuit(self,lst):
        n = len(lst)
        for i in range(n):
            x = self.hamming(lst, i)
            if self.poids(x) <= self.capacite:
                return x
        
    def descente(self):
        s = self.glouton2()
        i = 0
        while True:
            i += 1
            if i == 50:
                return s
            neighbors,fct = self.neighboors(s.getInstance())
            index = fct.index(max(fct))
            newSol = neighbors[index]
            if self.fctObj(s.getInstance()) > fct[index]:
                return s
            s = Solution(newSol,fct[index])
        
      
    def boltzmane(self,s0,s,T):
        if T != 0:
            return math.exp((self.fctObj(s0)-self.fctObj(s))/T)
        return 0
    
    def recuitSimule(self,T):
        fct = []
        ch = []
        s0 = self.glouton2()
        n = len(s0.getInstance())
        t = T
        # T = [2**(-i) for i in range(T)]
        T = [t-i for i in range(T)]
        for i in T:
            while True:
                x = self.neighboorsRecuit(s0.getInstance())
                s = Solution(x,self.fctObj(x))
                r = random.random()
                if r < self.boltzmane(s0.getInstance(), s.getInstance(), i):
                    fct.append(self.fctObj(s.getInstance()))
                    ch.append(s.getInstance())
                    s0 = s
                    break
        index = fct.index(max(fct))
        return Solution(ch[index],fct[index])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
