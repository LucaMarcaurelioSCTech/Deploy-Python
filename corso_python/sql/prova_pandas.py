import pandas as pd

# 1. Carico il CSV
# Nota: se il tuo CSV usa il punto e virgola invece della virgola, aggiungi sep=';'
df = pd.read_csv("contatti.csv") 

# 2. Trasformo in lista di dizionari per il ciclo
lista_utenti = df.to_dict(orient='records')

# Esempio di cosa ti ritrovi in mano:
# [
#   {'nome': 'Luca', 'cognome': 'Rossi', 'email': 'luca@test.it'},
#   {'nome': 'Marco', 'cognome': 'Bianchi', 'email': 'marco@test.it'}
# ]

# 3. Ora puoi ciclare esattamente come avevi pensato
for utente in lista_utenti:
    # Estraggo i dati usando i nomi delle colonne del CSV come chiavi
    n = utente['nome']
    c = utente['cognome']
    e = utente['email']
    p = utente['password']
    
    # ... qui fai la tua request per l'immagine ...
    # ... qui fai l'insert nel DB ...
    print(f"Inserito {n} {c}")