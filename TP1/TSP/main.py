import numpy as np
import random
from TSP import *
from Solution import *


if __name__ == '__main__':
    tsp = TSP(5,1,10)
    print(tsp.getCouts())
    sol = tsp.glouton1()
    print(sol.getChemin())
    print(sol.getFct())
    
    
    