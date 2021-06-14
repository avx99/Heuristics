import numpy as np
import random
from TSP import *
from Solution import *
import time



if __name__ == '__main__':
    tsp = TSP(280,1,100)
    # print(tsp.getCouts())

    # print("*******glouton**********")
    # start_time10 = time.time()
    # sol = tsp.glouton1(2)
    # # print(sol.getChemin())
    # print(sol.getFct())
    # print("glouton : " + str(time.time() - start_time10))
    # print("*******descente*********")
    # start_time11 = time.time()
    # desc = tsp.descente(2)
    # # print(desc.getChemin())
    # print(desc.getFct())
    # print("descente : " + str(time.time() - start_time11))
    # print("******recuit************")
    # start_time13 = time.time()
    # rec = tsp.recuit(2)
    # # print(rec.getChemin())
    # print(rec.getFct())
    # print("recuit : " + str(time.time() - start_time13))
    # print("*******tabouOPT*******")
    # start_time1 = time.time()
    # tabOPT = tsp.optimizedTabou(2,2)
    # # print(tabOPT.getChemin())
    # print(tabOPT.getFct())
    # print("Tabou optimized : "+ str(time.time() - start_time1))
    # print("*******tabou**********")
    # start_time2 = time.time()
    # tab = tsp.tabou(2)
    # # print(tab.getChemin())
    # print(tab.getFct())
    # print("Tabou : " + str(time.time() - start_time2))
    # print("*******VNS*********")
    # start_time3 = time.time()
    # vns = tsp.VNS(2)
    # # print(vns.getChemin())
    # print(vns.getFct())
    # print("vns : " + str(time.time() - start_time3))
    print("*****Genetique*********")
    start_time31 = time.time()
    gen = tsp.geneticAlgorithm("inversion")
    # print(vns.getChemin())
    print(gen.getFct())
    print("genetique : " + str(time.time() - start_time31))
    
    
    
    
    
    
    
    
    
    
    # for i in range(100):
    # chemin,fct = tsp.generateNeighbors(list(range(10)))
    # cheminT,fctT = tsp.generateNeighborsTabou(list(range(1000)),[])

    
    # sss = tsp.descenteVNS(tab)
    # sss1 = tsp.voisinage(sss.getChemin(),0)
    # print("*************")
    # c = sol.getChemin()
    # print("path :      " + str(c))
    # for i in range(50000):
    #     twoOpt = tsp.two_opt(c)
    #     print("two-opt : " + str(twoOpt))

    # for i in range(50000):
    #     threeopt = tsp.three_opt(c)
    #     print("three-opt : " + str(threeopt))


    # lst = tsp.generatePopulation(10,5)
    
    # T = 10000
    # t = T
    # # T = [2**(-i) for i in range(T)]
    # T = [t - i for i in range(T)]
    # for i in T:
    #     # print(i)
    #     print(tsp.boltzmaneX(random.randint(1,200), random.randint(1,200), i))

    # lll,fct = tsp.generateNeighbors(list(range(10)))

