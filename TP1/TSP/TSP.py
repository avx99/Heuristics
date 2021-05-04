import numpy as np
import random
from Solution import *

class TSP:
    def __init__(self,n,mn,mx):
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
    
    def glouton1(self):
        n = len(self.couts)
        start = random.randint(0, n-1)
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