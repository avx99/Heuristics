import numpy as np
import random
from Solution import *
import math


class TSP:
    def __init__(self,n,mn,mx):
        # np.random.seed(0)
        a = np.random.randint(mn,mx,size=(n,n))
        np.fill_diagonal(a, 0)
        self.couts = a

        
    def setCouts(self,couts):
        self.couts = couts
    
    def getCouts(self):
        return self.couts
    
    def fonctionObjectif(self,chemin):
        n = len(self.couts)
        s = self.couts[chemin[-1],chemin[0]]
        for i in range(n-1):
            s = s + self.couts[chemin[i],chemin[i+1]]
        return s
    
    def glouton1(self,start):
        n = len(self.couts)
        # start = random.randint(0, n-1)
        visited = []
        visited.append(start)
        mx = np.amax(self.couts)
        while len(visited) != n:
            lst = np.copy(self.couts[visited[-1]])
            for i in visited:
                lst[i] = mx
            index = np.where(lst == min(lst))
            visited.append(index[0][0])
            lst = None
        return Solution(visited,self.fonctionObjectif(visited))
    
    def twoOpt(self,lst,i,j):
        if i >= j:
            return lst
        l = lst[i:j+1]
        l = l[::-1]
        return lst[:i] + l + lst[j+1:]
    
    def generateNeighbors(self,lst):
        l = []
        fct = []
        n = len(lst)
        for i in range(n-1):
            for j in range(i+1,n):
                l.append(self.twoOpt(lst, i, j))
                fct.append(self.fonctionObjectif(l[-1]))
        return l,fct
        
    def descente(self,start):
        s = self.glouton1(start)
        i = 0
        while True:
            i += 1
            if i == 50:
                print(i)
                return s
            neighbors,fct = self.generateNeighbors(s.getChemin())
            index = fct.index(min(fct))
            newSol = neighbors[index]
            if s.getFct() < fct[index]:
                # print(str(s.getFct())+" < "+str(fct[index])+"   i :  "+str(i))
                return s
            s = Solution(newSol,fct[index])
        
      
    def boltzmane(self,s0,s,T):
        if T != 0:
            return math.exp((self.fonctionObjectif(s0)-self.fonctionObjectif(s))/T)
        return 1
    
    def recuitSimule(self,start,T):
        # random.seed(0)
        fct = []
        ch = []
        s0 = self.glouton1(start)
        n = len(s0.getChemin())
        # T = [2**(-i) for i in range(T)]
        t = T
        T = [t - i for i in range(T)]
        for i in T:
            while True:
                i = random.randint(0, n-2)
                j = random.randint(i+1, n-1)
                s = Solution(self.twoOpt(s0.getChemin(),i,j),self.fonctionObjectif(self.twoOpt(s0.getChemin(),i,j)))
                r = random.random()
                if r < self.boltzmane(s0.getChemin(), s.getChemin(), i):
                    fct.append(s.getFct())
                    ch.append(s.getChemin())
                    s0 = s
                    break
        index = fct.index(min(fct))
        return Solution(ch[index],fct[index])
        
        
        
        
        
    def recuitSimuleWithoutTable(self,start,T):
        # random.seed(0)
        s0 = self.glouton1(start)
        n = len(s0.getChemin())
        # T = [2**(-i) for i in range(T)]
        t = T
        T = [t - i for i in range(T)]
        for i in T:
            while True:
                i = random.randint(0, n-2)
                j = random.randint(i+1, n-1)
                s = Solution(self.twoOpt(s0.getChemin(),i,j),self.fonctionObjectif(self.twoOpt(s0.getChemin(),i,j)))
                r = random.random()
                if r < self.boltzmane(s0.getChemin(), s.getChemin(), i):
                    s0 = s
                    break
        return s
        
        
        
        