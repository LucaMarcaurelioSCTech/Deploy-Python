import os
import pandas
import sqlite3

print(os.getcwd())
os.chdir(r"C:\Users\lmarc\OneDrive\Desktop")
print(os.getcwd())
tabella = []
while (True):
    print("scrivere 0 nel momento in cui si vuole terminare l'inserimento")
    listatemporanea = []
    x = input("Inserisci il nome che vuoi inserie nella lista: ")
    if(x == "0"):
        break
    listatemporanea.append(x)
    y = input("Inserisci il cognome che vuoi inserie nella lista: ")
    if (y == "0"):
        break
    listatemporanea.append(y)
    w = input("Inserisci la data di nascita desiderata: ")
    if(w == "0"):
        break
    listatemporanea.append(w)
    z = input("Inserisci il luogo di nascita desiderato: ")
    if (z == "0"):
        break
    listatemporanea.append(z)

    
    tabella.append(listatemporanea)

df = pandas.DataFrame(tabella,columns=["Nome" , "Cognome","Data di Nascita","Luogo di Nascita"])
df.to_csv("rubrica_nomi.csv", index=False)



con = sqlite3.connect("test.db")
print(con.total_changes)
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER, name TEXT, age INTEGER)")
cursor.execute("INSERT INTO example VALUES (1 , Luca , 21)")
cursor.execute("INSERT INTO example VALUES (2, 'bob', 30)")
cursor.execute("INSERT INTO example VALUES (3, 'eve', 40)")

con.commit()
print(con.total_changes)

con.close()