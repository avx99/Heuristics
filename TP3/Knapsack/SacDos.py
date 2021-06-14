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
    
    def hamming1(self,a):
        i = random.randint(0, len(a) - 1)
        lst = a.copy()
        lst[i] = not lst[i]
        return lst
    
    def hamming2(self,a):
        i = 0
        j = 0
        while i == j:
            i = random.randint(0, len(a) - 1)
            j = random.randint(0, len(a) - 1)
        lst = a.copy()
        lst[i] = not lst[i]
        lst[j] = not lst[j]
        return lst
    
    def hamming3(self,a):
        i = 0
        j = 0
        k = 0
        while i == j and j == k:
            i = random.randint(0, len(a) - 1)
            j = random.randint(0, len(a) - 1)
            k = random.randint(0, len(a) - 1)
        lst = a.copy()
        lst[i] = not lst[i]
        lst[j] = not lst[j]
        lst[k] = not lst[k]
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
        s = self.glouton1()
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
        
      
    def boltzmane(self,s0,s,T):
        if T != 0:
            return math.exp((self.fctObj(s0)-self.fctObj(s))/T)
        return 1
    def neighboorsRecuit(self,lst):
        n = len(lst)
        for i in range(n):
            x = self.hamming(lst, i)
            if self.poids(x) <= self.capacite:
                return x
    
    def recuitSimule(self,T):
        fct = []
        ch = []
        s0 = self.glouton2()
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
    
    
    
    def generateNeighborsTabou(self,lst,tabou):
        l = []
        fct = []
        n = len(lst)
        for i in range(n):
            x = self.hamming(lst, i)
            if self.poids(x) <= self.capacite and x not in tabou:
                l.append(x)
                fct.append(self.fctObj(x))
        return l,fct

    def tabou(self,a):
        tabou = []
        ltabou = []
        s = self.glouton1()
        i = 0
        while i != 100:
            i = i + 1
            neighbors,fct = self.generateNeighborsTabou(s.getInstance(),ltabou)
            if (len(fct) == 0):
                break
            index = fct.index(max(fct))            
            newSol = neighbors[index]
            tabou.append(Solution(newSol,fct[index]))
            ltabou.append(newSol)
            if len(ltabou) == a:
                lst = [tabou[j].getValeur() for j in range(a)]
                index = lst.index(max(lst))
                x = tabou[index]
                tabou = []
                ltabou = []
                tabou.append(x)
                ltabou.append(x.getInstance())
            s = Solution(newSol,fct[index])
        lst = [tabou[j].getValeur() for j in range(len(tabou))]
        index = lst.index(max(lst))
        return tabou[index]
            
    
    
    def corrector(self,lst):
        l = lst.copy()
        n =  len(l)
        for i in range(n):
            if self.poids(l) <= self.capacite:
                return l
            else:
                if l[n-1-i] == True:
                    l[n-1-i] = False
    
    
    def Vk(self,s,k):
        if k == 0:
            x0 = self.hamming1(s.getInstance())
            while self.poids(x0) > self.capacite:
                x0 = self.hamming1(s.getInstance())
            return Solution(x0,self.fctObj(x0))
        if k == 1:
            x1 = self.hamming2(s.getInstance())
            while self.poids(x1) > self.capacite:
                x1 = self.hamming1(s.getInstance())
            return Solution(x1,self.fctObj(x1))
        if k == 2:
            x2 = self.hamming3(s.getInstance())
            while self.poids(x2) > self.capacite:
                x2 = self.hamming1(s.getInstance())
            return Solution(x2,self.fctObj(x2))
        
    def descenteVNS(self,s0):
        s = s0
        i = 0
        while True:
            i += 1
            if i == 50:
                print(i)
                return s
            neighbors,fct = self.neighboors(s.getInstance())
            if len(fct) == 0:
                return s
            index = fct.index(max(fct))
            newSol = neighbors[index]
            if self.fctObj(s.getInstance()) > fct[index]:
                return s
            s = Solution(newSol,fct[index])

    
    def VNS(self):
        s0 = self.glouton1()
        i = 0
        s = s0
        while i != 100:
            k = 0
            while k != 3:
                s1 = self.Vk(s,k)
                s2 = self.descenteVNS(s1)
                if s2.getValeur() > s.getValeur():
                    s = s2
                    k = 0
                else:
                    k = k + 1
            i += 1
            
            
        return s
          
    def generatePopulation(self,N=100):
        s0 = self.glouton1()
        lst = []
        fct = []
        for i in range(N):
            x = self.Vk(s0, random.randint(1, 2))
            lst.append(x.getInstance())
            fct.append(x.getValeur())
        return lst,fct
    
    
    def crossOver(self,father,mother,pt = None):
        n = len(father)
        if pt == None:
            pt = random.randint(1, n-2)
        child1 = father[:pt].copy() + mother[pt:].copy()
        child2 = mother[:pt].copy() + father[pt:].copy()
        
        child1 = self.corrector(child1)
        child2 = self.corrector(child2)
        
        
        return child1,child2

    
    
    def selectAnyType(self,inds,fct,typeOfSelect="population",N=100,pc=15,pm=30):
        #type = crossOver or mutation or population
        l = []
        f = []
        ff = fct.copy()
        mx = max(fct)
        mn = min(fct)
        x = 0
        index = []
        if typeOfSelect == "mutation":
            x = pm
            for i in fct:
                index.append(ff.index(min(ff)))
                if len(index) == x:
                    break
                ff[index[-1]] = mx
            for i in index:
                l.append(inds[i])
                f.append(fct[i])        
            return l,f
        if typeOfSelect == "crossOver":
            x = 2*pc
        if typeOfSelect == "population":
            x = N
        for i in fct:
            index.append(ff.index(max(ff)))
            if len(index) == x:
                break
            ff[index[-1]] = mn
        for i in index:
            l.append(inds[i])
            f.append(fct[i])
        return l,f
    
    def mutation(self,ind,fct,typeOfMutation):
        n = len(ind)
        if typeOfMutation == "descente":
            return self.descenteVNS(Solution(ind,fct))

        if typeOfMutation == "permutation":
            i = random.randint(0, n-2)
            j = random.randint(i+1, n-1)
            lst = ind.copy()
            lst[i],lst[j] = lst[j],lst[i]
            while self.poids(lst) > self.capacite:
                i = random.randint(0, n-2)
                j = random.randint(i+1, n-1)
                lst = ind.copy()
                lst[i],lst[j] = lst[j],lst[i]                
            return Solution(lst,self.fctObj(lst)) 
        
    
    def geneticAlgorithm(self,mutationType):
        p0 = self.generatePopulation()
        p = p0
        t = 0
        while t != 10:
            # print("1")
            crossOverList = self.selectAnyType(p[0], p[1], "crossOver")
            # print("2")
            b = len(crossOverList[0])
            # print("2.1")
            childs = []
            # print("2.2")
            for i in range(0,len(crossOverList[0])-1,2):
                # print("2.3")
                childs.append(self.crossOver(crossOverList[0][i], crossOverList[0][i+1])[0])
                # print("2.4")
                childs.append(self.crossOver(crossOverList[0][i], crossOverList[0][i+1])[1])
                # print("2.5")
            # print("3")
            mutationList = self.selectAnyType(p[0], p[1], "mutation")
            a = len(mutationList[0])
            # print("before adding mut " + str(p[0]))
            # print("4")
            for i in range(a):
                mutated = self.mutation(mutationList[0][i], mutationList[1][i], mutationType)
                p[0].append(mutated.getInstance())
                p[1].append(mutated.getValeur())
            # print("5")
            for i in range(b):
                p[0].append(childs[i])
                p[1].append(self.fctObj(childs[i]))   
            # print("6")
            p = self.selectAnyType(p[0], p[1])
            # print("7")
            t += 1 
        index = p[1].index(max(p[1]))
        return Solution(p[0][index], p[1][index])  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
