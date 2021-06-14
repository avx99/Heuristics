import numpy as np
from Objet import *
from SacDos import *
from Solution import *



if __name__ == "__main__":
   
    obj = Objet(0,0)
    lst = obj.generateTest(100) 
    s = SacDos(lst,150)

    for i in lst:
        print(i)
    sol1 = s.glouton1()
    print("**************glouton******************")
    sol2 = s.glouton2()
    # print(sol2.getInstance())
    print(sol2.getValeur())
    
    
    
    print("**************descente******************")
    sol3 = s.descente()
    # print(sol3.getInstance())
    print(sol3.getValeur())    
    # print(s.poids(sol3.getInstance()))    
    
    
    
    
    print("**************recuit******************")
    rec = s.recuitSimule(100)
    # print(rec.getInstance())
    print(rec.getValeur())  
    # print(s.poids(rec.getInstance()))  

    # neighbors,fct = s.neighboors(sol1.getInstance())