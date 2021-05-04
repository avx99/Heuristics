import numpy as np
from Objet import *
from SacDos import *
from Solution import *



if __name__ == "__main__":
   
    obj = Objet(0,0)
    lst = obj.generateTest(10) 
    s = SacDos(lst,15)


    sol1 = s.glouton1()
    sol2 = s.glouton2()
    print(sol1.getInstance())
    print(sol1.getValeur())

    
    sol3 = s.descente()
    
    print("*****************************************")
    print(sol3.getInstance())
    print(sol3.getValeur())    
    neighbors,fct = s.neighboors(sol1.getInstance())