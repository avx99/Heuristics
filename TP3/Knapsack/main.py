import numpy as np
from Objet import *
from SacDos import *
from Solution import *
import time


if __name__ == "__main__":
   
    obj = Objet(0,0)
    lst = obj.generateTest(500) 
    s = SacDos(lst,155)

    print("************glouton 1********************")
    start_time1 = time.time()
    sol1 = s.glouton1()
    # print(sol1.getInstance())
    print("valeur = " + str(sol1.getValeur()))
    print("poids = " + str(s.poids(sol1.getInstance())))
    print("temps en s :" + str(time.time() - start_time1))
    
    
    
    print("************glouton 2********************")
    start_time2 = time.time()
    sol2 = s.glouton2()
    # print(sol2.getInstance())
    print("valeur = " + str(sol2.getValeur()))  
    print("poids = " + str(s.poids(sol2.getInstance())))  
    print("temps en s :" + str(time.time() - start_time2))
    
    print("************descente********************")
    start_time3 = time.time()
    sol3 = s.descente()
    # print(sol2.getInstance())
    print("valeur = " + str(sol3.getValeur()))  
    print("poids = " + str(s.poids(sol3.getInstance())))  
    print("temps en s :" + str(time.time() - start_time3))
    
    # print("************recuit********************")
    # start_time4 = time.time()
    # sol4 = s.recuitSimule(10)
    # # print(sol2.getInstance())
    # print("valeur = " + str(sol4.getValeur()))  
    # print("poids = " + str(s.poids(sol4.getInstance())))  
    # print("temps en s :" + str(time.time() - start_time4))
    
    
    print("************tabou********************")
    start_time5 = time.time()
    sol5 = s.tabou(100)
    # print(sol2.getInstance())
    print("valeur = " + str(sol5.getValeur()))  
    print("poids = " + str(s.poids(sol5.getInstance())))  
    print("temps en s :" + str(time.time() - start_time5))
    
    
        
    print("************VNS********************")
    start_time6 = time.time()
    sol6 = s.VNS()
    # print(sol2.getInstance())
    print("valeur = " + str(sol6.getValeur()))  
    print("poids = " + str(s.poids(sol6.getInstance())))  
    print("temps en s :" + str(time.time() - start_time6))
    
    
    # sol2 = s.glouton2()
    # print("************Vk********************")
    # start_time6 = time.time()
    # sol6 = s.Vk(sol2, 2)
    # # print(sol2.getInstance())
    # print("valeur = " + str(sol6.getValeur()))  
    # print("poids = " + str(s.poids(sol6.getInstance())))  
    # print("temps en s :" + str(time.time() - start_time6))
    
    
    # sol1 = s.glouton1()
    # sol2 = s.glouton2()
    # a,b = s.crossOver(sol1.getInstance(),sol2.getInstance(),2)

    # l,f = s.generatePopulation(10)
    
    
    # ll,ff = s.selectAnyType(l,f,typeOfSelect="mutation",N=10,pc=5,pm=5)
    
    # s0 = s.mutation(ll[0],ff[0],"descente")
    
    # print("************genetic********************")    
    # p = s.geneticAlgorithm("permutation")
    
    # print("valeur = " + str(p.getValeur()))  
    # print("poids = " + str(s.poids(p.getInstance())))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    