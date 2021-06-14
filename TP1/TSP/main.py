import numpy as np
import random
from TSP import *
from Solution import *


if __name__ == '__main__':
    tsp = TSP(10,1,20)
    print(tsp.getCouts())
    sol = tsp.glouton1()
    print(sol.getChemin())
    print(sol.getFct())
    
    
    