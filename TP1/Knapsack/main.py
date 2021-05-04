import numpy as np
from Objet import *
from SacDos import *
from Solution import *



if __name__ == "__main__":
   
    obj = Objet(0,0)
    lst = obj.generateTest(100) 
    s = SacDos(lst,100)


    sol1 = s.glouton1()
    sol2 = s.glouton2()
    # print(sol1.getInstance())
    print(sol1.getValeur())
    print("*****************************************")
    # print(sol2.getInstance())
    print(sol2.getValeur())

