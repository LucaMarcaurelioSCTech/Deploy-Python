
"""
with open("isolamisteriosa.txt","rt") as f ,open("output.txt","w") as scr :
    contatore = 0
    for i in f.readlines():
        contatore +=1
        
        if contatore % 2 == 0 :
            scr.write(f"{contatore}: {i}")
"""
import numpy  
with open("isolamisteriosa.txt","rb") as f:
    punt = f.tell()
    nuovo = f.seek(119)
    parola = f.read(7)
    print(parola)
        

        
        

