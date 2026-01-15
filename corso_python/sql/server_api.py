from flask import Flask, request, jsonify
import pymysql
import pandas as pd
import base64
import io
import requests 
from . import connessionesql as con 
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, ComplexModel

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)


cur = con.cursor
sql_insert = "INSERT INTO utenti (nome, cognome, email, password, immagini) VALUES (%s, %s, %s, %s , %s)"

def scarica_immagine_gatto():
    """Scarica l'immagine e la converte in base64. Ritorna la stringa o None."""
    try:
        r = requests.get('https://cataas.com/cat', timeout=3)
        if r.status_code == 200:
            r64 = base64.b64encode(r.content)
            return r64.decode('utf-8')
    except:
        pass
    return None

#Parte Soap

class UtenteRisposta(ComplexModel):
    nome = Unicode
    cognome = Unicode
    email = Unicode
    password = Unicode
    immagine_64 = Unicode

class ServizioSoap(ServiceBase):
    @rpc(Unicode,Unicode,Unicode,Unicode,_returns=Unicode)
    def registrazione_soap(ctx, nome, cognome, email, password):
        r64string =scarica_immagine_gatto()

        try:
            cur.execute(sql_insert, (nome, cognome, email, password, r64string))
            con.connection.commit()
            return "Success: Utente registrato correttamente via SOAP"
        except Exception as err:
            return f"Error: {str(err)}"
        

    @rpc(Unicode,Unicode, _returns=UtenteRisposta)
    def login_soap(ctx, email, password):
        cur.execute("SELECT * FROM utenti WHERE email = %s AND password = %s", (email, password))
        utente = cur.fetchone()

        risposta = UtenteRisposta

        if utente:
            risposta.status = "success"
            risposta.messaggio = "Login effettuato"
            risposta.nome = utente[1]    
            risposta.cognome = utente[2] 
            risposta.immagine_b64 = utente[5] 
        else:
            risposta.status = "error"
            risposta.messaggio = "Credenziali errate"
        
        return risposta
soap_app = Application(
    [ServizioSoap],
    tns='snake.api.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)
wsgi_soap_app = WsgiApplication(soap_app)

#Parte Rest

@app.route('/api/registrazione', methods=['POST'])
def registrazione():
    dati = request.json
    if not dati:
        return jsonify({"status": "error", "message": "Nessun dato ricevuto"}), 400
    
    n = dati.get('nome')
    c = dati.get('cognome')
    e = dati.get('email')
    p = dati.get('password')

    r64string = scarica_immagine_gatto()

    try:
        cur.execute(sql_insert, (n, c, e, p, r64string))
        con.connection.commit()
        return jsonify({"status": "success", "message": "Utente registrato correttamente"}), 200
    except Exception as err:
        return jsonify({"status": "error", "message": str(err)}), 500
    
@app.route('/api/login', methods=['POST'])
def login():
    dati = request.json
    if not dati:
        return jsonify({"status": "error", "message": "Nessun dato ricevuto"}), 400
    
    e = dati.get('email')
    p = dati.get('password') 
    
    cur.execute("SELECT * FROM utenti WHERE email = %s AND password = %s", (e, p))
    utente = cur.fetchone()

    if utente:
        return jsonify({
            "status": "success",
            "user": {"nome": utente[1], "cognome": utente[2], "immagine": utente[5]}
        }), 200
    else:
        return jsonify({"status": "error", "message": "Email o password errati"}), 401

@app.route('/api/upload_csv', methods=['POST'])
def upload_csv():
    dati = request.json
    contenuto_b64 = dati.get('file_b64')

    if not contenuto_b64:
        return jsonify({"status": "error", "message": "Manca il file Base64"}), 400

    try:
        file_bytes = base64.b64decode(contenuto_b64)
        csv_buffer = io.BytesIO(file_bytes)
        df = pd.read_csv(csv_buffer)
        
        lista_utenti = df.to_dict(orient='records')
        conta = 0 
        errori = 0
        
        for utente in lista_utenti:
            n = utente['nome']
            c = utente['cognome']
            e = utente['email']
            p = utente['password']
            
            
            r64string = scarica_immagine_gatto()

            try:
                cur.execute(sql_insert, (n, c, e, p, r64string))
                conta += 1
            except Exception as err:
                errori += 1
                print(f"Errore riga: {err}")
        
        con.connection.commit()
        
        return jsonify({
            "status": "success", 
            "message": f"Operazione finita. Inseriti: {conta}. Errori: {errori}"
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": f"Errore lettura CSV: {str(e)}"}), 500

@app.route('/api/elimina', methods=['POST'])
def elimina():
    dati = request.json
    e = dati.get("email")
    p = dati.get("password")

    cur.execute("DELETE FROM utenti WHERE email = %s and password = %s", (e , p))
    con.connection.commit()
    
    if cur.rowcount > 0:
        return jsonify({"status": "success", "message": "Account eliminato"}), 200
    else:
        return jsonify({"status": "error", "message": "Account non trovato o password errata"}), 404
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, { '/api/soap' : wsgi_soap_app })


if __name__ == "__main__":
    print("REST disponibile su: http://localhost:5000/api/rest/...")
    print("SOAP WSDL su:      http://localhost:5000/api/soap/?wsdl")
    app.run(host='0.0.0.0', port=5000, debug=True)