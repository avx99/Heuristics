import numpy as np
import random
from TSP import *
from Solution import *


if __name__ == '__main__':
    tsp = TSP(10,1,100)
    # print(tsp.getCouts())
    print()
    print("*******glouton**********")
    print()
    sol = tsp.glouton1(2)
    print(sol.getChemin())
    print(sol.getFct())
    print()
    print("*******descente*********")
    print()
    desc = tsp.descente(2)
    print(desc.getChemin())
    print(desc.getFct())
    print()
    print("******recuit************")
    print()
    rec = tsp.recuitSimule(2,1000)
    print(rec.getChemin())
    print(rec.getFct())
    print()
    print("**********************")
    print()