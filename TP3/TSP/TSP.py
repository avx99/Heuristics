import numpy as np
import random
from Solution import *
import math


class TSP:
    def __init__(self,n,mn,mx):
        a = np.random.randint(mn,mx,size=(n,n))
        np.fill_diagonal(a, 0)
        self.couts = a
        
    def distance(self,i,j):
        return self.couts[i,j]
        
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
        # start = random.randint(0, n-1)
        visited = []
        visited.append(start)
        mx = np.amax(self.couts) + 1
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
        # j = random.randint(1, n-1)
        for i in range(n-1):
            for j in range(i+1,n):
                l.append(self.twoOpt(lst, i, j))
                fct.append(self.fonctionObjectif(l[-1]))
        return l,fct
    
    
    def generateNeighborsTabou(self,lst,tabou):
        l = []
        fct = []
        n = len(lst)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if self.twoOpt(lst, i, j) not in tabou:
                    l.append(self.twoOpt(lst, i, j))
                    fct.append(self.fonctionObjectif(l[-1]))
        return l,fct
        
    def descente(self,start):
        s = self.glouton1(start)
        i = 0
        while i != 100:
            i += 1
            neighbors,fct = self.generateNeighbors(s.getChemin())
            index = fct.index(min(fct))
            newSol = neighbors[index]
            if s.getFct() < fct[index]:
                return s
            s = Solution(newSol,fct[index])
        return s
        
      
    def descenteVPop(self,x):
        s = x
        i = 0
        while i != 100:
            i += 1
            neighbors,fct = self.generateNeighbors(s.getChemin())
            index = fct.index(min(fct))
            newSol = neighbors[index]
            if s.getFct() < fct[index]:
                return s
            s = Solution(newSol,fct[index])
        return s        
    
    
    def boltzmane(self,s0,s,T):
        x = self.fonctionObjectif(s)
        x0 = self.fonctionObjectif(s0)
        if T > 0.001:
            return np.exp((x0-x)/T)
        else:
            if (x0-x) == 0:
                return 1
            elif (x0-x) > 0:
                return 1
            else:
                return 0
        
    def boltzmaneX(self,s0,s,T):
        # if T != 0:
        return np.exp((s0-s)/T)
        # return 1
    
    def recuitSimule(self,start,T):
        fct = []
        ch = []
        s0 = self.glouton1(start)
        n = len(s0.getChemin())
        t = T
        # T = [2**(-i) for i in range(T) if 2**(-i) >= 0.1]
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

########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################

    def fluctuation(self, trajet, i,j):
        Min = min(i,j)
        Max = max(i,j)
        trajet[Min:Max] = trajet[Min:Max].copy()[::-1]
        return trajet
    
    def metropolis(self,trajet,T,E1,E2,i,j):
        if E1 <= E2:
            E2 = E1  # énergie du nouvel état = énergie système
        else:
            dE = E1-E2
            if random.uniform(0,1) > np.exp(-dE/T):                   # la fluctuation est retenue avec  
                trajet = self.fluctuation(trajet, i,j)         # la proba p. sinon retour trajet antérieur
            else:
                E2 = E1 # la fluctuation est retenue 
        return E2,trajet
    
    def recuit(self,start):
        T0 = 10
        Tmin = 1e-2
        kmax = 1e4
        
        T = T0
        k = 0
        s = self.glouton1(start).getChemin()
        
        # calcul de l'énergie initiale du système (la distance initiale à minimiser)
        Ec = self.fonctionObjectif(s)
        N =  len(s)
        while T > Tmin:
                # choix de deux villes différentes au hasard
                i = random.randint(1,N-1)
                j = random.randint(1,N -1)
                if i == j: continue
                
                # création de la fluctuation et mesure de l'énergie
                s = self.fluctuation(s,i,j) 
                Ef = self.fonctionObjectif(s)   
                Ec, s = self.metropolis(s,T,Ef,Ec,i,j)
                
    
                # application de la loi de refroidissement    
                k += 1
                T = T0*np.exp(-k/kmax)
        
        return Solution(s,self.fonctionObjectif(s))



########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
    

    

    def tabou(self,start):
        tabou = [] #Solution
        ltabou = [] #chemin
        s = self.glouton1(start)
        i = 0
        while i != 100:
            i = i + 1
            neighbors,fct = self.generateNeighborsTabou(s.getChemin(),ltabou)
            index = fct.index(min(fct))            
            newSol = neighbors[index]
            tabou.append(Solution(newSol,fct[index]))
            ltabou.append(newSol)
            s = Solution(newSol,fct[index])
        lst = [tabou[j].getFct() for j in range(len(tabou))]
        index = lst.index(min(lst))
        return tabou[index]
            
    
    def optimizedTabou(self,start,size):
        tabou = []
        ltabou = []
        s = self.glouton1(start)
        i = 0
        while i != 100:
            i = i + 1
            neighbors,fct = self.generateNeighborsTabou(s.getChemin(),ltabou)
            index = fct.index(min(fct))            
            newSol = neighbors[index]
            tabou.append(Solution(newSol,fct[index]))
            ltabou.append(newSol)
            if len(ltabou) == size:
                lst = [tabou[j].getFct() for j in range(len(tabou))]
                index = lst.index(min(lst))
                x = tabou[index]
                y = tabou[index].getChemin()
                tabou = []
                ltabou = []
                tabou.append(x)
                ltabou.append(y)
                
            s = Solution(newSol,fct[index])
        lst = [tabou[j].getFct() for j in range(len(tabou))]
        index = lst.index(min(lst))
        return tabou[index]
    
    def two_opt(self,tour):
        n = len(tour)
        i = random.randint(0, n-2)
        j = random.randint(i+1, n-1)
        return self.twoOpt(tour,i,j)
    


    def three_opt(self,p, broad=False):
        n = len(p)
        # choose 3 unique edges defined by their first node
        a, c, e = random.sample(range(n+1), 3)
        # without loss of generality, sort
        a, c, e = sorted([a, c, e])
        b, d, f = a+1, c+1, e+1
    
        if broad == True:
            which = random.randint(0, 7) # allow any of the 8
        else:
            which = random.choice([3, 4, 5, 6]) # allow only strict 3-opt
    
        # in the following slices, the nodes abcdef are referred to by
        # name. x:y:-1 means step backwards. anything like c+1 or d-1
        # refers to c or d, but to include the item itself, we use the +1
        # or -1 in the slice
        if which == 0:
            sol = p[:a+1] + p[b:c+1]    + p[d:e+1]    + p[f:] # identity
        elif which == 1:
            sol = p[:a+1] + p[b:c+1]    + p[e:d-1:-1] + p[f:] # 2-opt
        elif which == 2:
            sol = p[:a+1] + p[c:b-1:-1] + p[d:e+1]    + p[f:] # 2-opt
        elif which == 3:
            sol = p[:a+1] + p[c:b-1:-1] + p[e:d-1:-1] + p[f:] # 3-opt
        elif which == 4:
            sol = p[:a+1] + p[d:e+1]    + p[b:c+1]    + p[f:] # 3-opt
        elif which == 5:
            sol = p[:a+1] + p[d:e+1]    + p[c:b-1:-1] + p[f:] # 3-opt
        elif which == 6:
            sol = p[:a+1] + p[e:d-1:-1] + p[b:c+1]    + p[f:] # 3-opt
        elif which == 7:
            sol = p[:a+1] + p[e:d-1:-1] + p[c:b-1:-1] + p[f:] # 2-opt    
        return sol
    
    
    def four_opt(self,tour):
        n = len(tour) 
        a,b = n // 3 , 2*n // 3
        
        i1 = random.randint(a // 2, a)
        i2 = random.randint(0, i1-1)
        i3 = random.randint(a+((b-a) // 2), b)
        i4 = random.randint(a , i3-1)
        i5 = random.randint(b+((n-b) // 2), n-1)
        i6 = random.randint(b, i5-1)
        
        p1 = tour[0:a+1]
        p2 = tour[a+1:b+1]
        p3 = tour[b+1:]
        
        pp1 = self.twoOpt(p1, i2, i1)
        pp2 = self.twoOpt(p2, i4-(n//3),i3-(n//3))
        pp3 = self.twoOpt(p3, i6-(2*n//3),i5-(2*n//3)-1)

        return pp1+pp2+pp3
    
    def Vk(self,s,k):
        if k == 0:
            x0 = self.two_opt(s.getChemin())
            # print("2-opt")
            return Solution(x0,self.fonctionObjectif(x0))
        if k == 1:
            x1 = self.three_opt(s.getChemin())
            # print("3-opt")
            return Solution(x1,self.fonctionObjectif(x1))
        if k == 2:
            x2 = self.four_opt(s.getChemin())
            # print("4-opt")
            return Solution(x2,self.fonctionObjectif(x2))
        
    def descenteVNS(self,s0):
        s = s0
        i = 0
        while i != 100:
            i += 1
            neighbors,fct = self.generateNeighbors(s.getChemin())
            
            index = fct.index(min(fct))
            newSol = neighbors[index]
            if s.getFct() < fct[index]:
                return s
            s = Solution(newSol,fct[index])
        return s
    
    
    def VNS(self,start):
        s0 = self.glouton1(start)
        i = 0
        s = s0
        while i != 100:
            k = 0
            while k != 3:
                s1 = self.Vk(s,k)
                s2 = self.descenteVNS(s1)
                if s2.getFct() < s.getFct():
                    s = s2
                    k = 0
                else:
                    k = k + 1
            i += 1
        return s
        
        
    def generatePopulation(self,N=100):
        n = len(self.couts)
        s0 = self.glouton1(random.randint(0, n-1))
        lst = []
        fct = []
        for i in range(N):
            lst.append(self.Vk(s0, random.randint(1, 2)).getChemin())
            fct.append(self.fonctionObjectif(lst[-1]))
        return lst,fct
    
    
    def crossOver(self,father,mother,pt = None):
        n = len(self.couts)
        if pt == None:
            pt = random.randint(1, n-2)
        child1 = father[:pt].copy()
        child2 = mother[:pt].copy()
        tmp1 = []
        tmp2 = []
        
        for i in mother[::-1]:
            if i not in child1:
                tmp1.append(i)
                if len(tmp1) == n - pt:
                    break
        
        for j in father[::-1]:
            if j not in child2:
                tmp2.append(j)
                if len(tmp2) == n - pt:
                    break
        return child1+tmp1[::-1],child2+tmp2[::-1]
    
    
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
                index.append(ff.index(max(ff)))
                if len(index) == x:
                    break       
                ff[index[-1]] = mn
            for i in index:
                l.append(inds[i])
                f.append(fct[i])        
            return l,f
        if typeOfSelect == "crossOver":
            x = 2*pc
        if typeOfSelect == "population":
            x = N
        for i in fct:
            index.append(ff.index(min(ff)))
            if len(index) == x:
                break
            ff[index[-1]] = mx
        for i in index:
            l.append(inds[i])
            f.append(fct[i])
        return l,f
    
    def mutation(self,ind,fct,typeOfMutation):
        n = len(ind)
        if typeOfMutation == "descente":
            return self.descenteVPop(Solution(ind,fct))
        
        if typeOfMutation == "inversion":
            l = self.two_opt(ind)
            return Solution(l,self.fonctionObjectif(l))
        if typeOfMutation == "permutation":
            i = random.randint(0, n-2)
            j = random.randint(i+1, n-1)
            lst = ind.copy()
            lst[i],lst[j] = lst[j],lst[i]
            return Solution(lst,self.fonctionObjectif(lst)) 
        
    
    def geneticAlgorithm(self,mutationType):
        p0 = self.generatePopulation()
        p = p0
        t = 0
        while t != 50:
            
            crossOverList = self.selectAnyType(p[0], p[1], "crossOver")
            b = len(crossOverList[0])
            childs = []
            for i in range(0,len(crossOverList[0])-1,2):
                childs.append(self.crossOver(crossOverList[0][i], crossOverList[0][i+1])[0])
                childs.append(self.crossOver(crossOverList[0][i], crossOverList[0][i+1])[1])
            mutationList = self.selectAnyType(p[0], p[1], "mutation")
            a = len(mutationList[0])
            # print("before adding mut " + str(p[0]))
            for i in range(a):
                mutated = self.mutation(mutationList[0][i], mutationList[1][i], mutationType)
                p[0].append(mutated.getChemin())
                p[1].append(mutated.getFct())
            for i in range(b):
                p[0].append(childs[i])
                p[1].append(self.fonctionObjectif(childs[i]))          
            p = self.selectAnyType(p[0], p[1])
            t += 1 
        index = p[1].index(min(p[1]))
        return Solution(p[0][index], p[1][index])
        
        
        
        
        