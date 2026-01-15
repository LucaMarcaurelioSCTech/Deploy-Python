from abc import ABC, abstractmethod
from random import randint

class Personaggio(ABC):
    def __init__(self, nome, vita_max):
        self.nome = nome
        self.vita = vita_max
        self.vita_max = vita_max
        self.in_difesa = False 

    @abstractmethod
    def attacca(self, bersaglio): 
        pass

    def difesa(self):
        self.in_difesa = True 
        print(f" {self.nome} alza la guardia!")

class DarkWraith(Personaggio):
    def attacca(self, bersaglio):
        if bersaglio.in_difesa:
            print(f" {self.nome} attacca, ma {bersaglio.nome} BLOCCA il colpo!")
            return 
        danno = randint(1, 20)
        if danno == 20:
            danno_totale = danno * 2
            print("COLPO CRITICO!")
            bersaglio.vita -= danno_totale
            print(f"{self.nome} esplode infliggendo {danno_totale} danni a {bersaglio.nome}!")
        elif danno < 5:
            print(f"{self.nome} non riesce a scalfire l'armatura di {bersaglio.nome}.")
        else:
            bersaglio.vita -= danno
            print(f"{self.nome} esplode infliggendo {danno} danni a {bersaglio.nome}.")

class Berserk(Personaggio):
    def attacca(self, bersaglio):
        if bersaglio.in_difesa:
            print(f" {self.nome} attacca, ma {bersaglio.nome} BLOCCA il colpo!")
            return 

        danno = randint(1, 20)
        if danno == 20:
            danno_totale = danno * 2
            print(" COLPO CRITICO!")
            bersaglio.vita -= danno_totale
            print(f"{self.nome} Urla DEMACIAAAAAA infliggendo {danno_totale} danni!")
        elif danno < 5:
            print(f"{self.nome} colpisce di striscio.")
        else:
            bersaglio.vita -= danno
            print(f"{self.nome} Urla DEMACIAAAAAA infliggendo {danno} danni!")

class Demone(Personaggio):
    def attacca(self, bersaglio):
        if bersaglio.in_difesa:
            print(f" {self.nome} attacca, ma {bersaglio.nome} BLOCCA il colpo!")
            return

        danno = randint(1, 20)
        if danno == 20:
            danno_totale = danno * 2
            print(" COLPO CRITICO DEL DEMONE!")
            bersaglio.vita -= danno_totale
            print(f"{self.nome} attacca brutalmente infliggendo {danno_totale} danni!")
        elif danno < 5:
            print(f"{self.nome} manca il bersaglio.")
        else:
            bersaglio.vita -= danno
            print(f"{self.nome} attacca infliggendo {danno} danni.")


finegioco = "si" 

while finegioco == "si":
    
    u235 = DarkWraith("u235", 70) 
    garen = Berserk("Garen", 70)
    demone = Demone("Ainz", 100)
    
    turno = 0
    giocatore_attivo = None 

    try:
        scelta = int(input("Inserisci 1 per usare Berserker, 2 per usare DarkWraith: "))
    except ValueError:
        scelta = 1 
    
    if scelta == 1:
        giocatore_attivo = garen
    else:
        giocatore_attivo = u235
    
    print(f"Hai scelto {giocatore_attivo.nome}")
    
    print("Tiri un dado per l'iniziativa...")
    turn_player = randint(1, 6) >= randint(1, 6)
    if turn_player: print("Inizi tu!") 
    else: print("Inizia il demone!")

    while demone.vita > 0 and giocatore_attivo.vita > 0:
        turno += 1
        print(f"\n--- TURNO {turno} ---")
        print(f"Vita {giocatore_attivo.nome}: {giocatore_attivo.vita} | Vita {demone.nome}: {demone.vita}")

        
        giocatore_attivo.in_difesa = False
        demone.in_difesa = False

        if turn_player:
            
            scelta_azione = input("1 per Attaccare, 2 per Difendere: ")
            if scelta_azione == "1":
                giocatore_attivo.attacca(demone)
            else:
                giocatore_attivo.difesa()
            
            
            if demone.vita > 0:
                print("Il demone reagisce...")
               
                if randint(1, 2) == 1:
                    demone.attacca(giocatore_attivo)
                else:
                    demone.difesa()
        
        else:
            
            print("Il demone agisce per primo!")
            azione_demone = randint(1, 2)
            if azione_demone == 1:
                demone.attacca(giocatore_attivo)
            else:
                demone.difesa()
            
            
            if giocatore_attivo.vita > 0:
                scelta_azione = input("Tocca a te! 1 per Attaccare, 2 per Difendere: ")
                if scelta_azione == "1":
                    giocatore_attivo.attacca(demone)
                else:
                    giocatore_attivo.difesa()

        if demone.vita <= 0:
            print(" HAI VINTO!!")
        elif giocatore_attivo.vita <= 0:
            print(" SEI MORTO.")

    finegioco = input("\nScrivere 'si' per giocare ancora: ")