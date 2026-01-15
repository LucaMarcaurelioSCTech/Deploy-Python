from flask import Flask, request, jsonify
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import requests
import base64
import pymysql
import connessionesql as con
import io
from PIL import Image, ImageTk
import pandas as pd
import server_api



def bo():
    cur = con.cursor

    def aggiungiaccount():
        
        percorso_file = filedialog.askopenfilename(title="Selezione il file da aggiungere", filetypes=[("File CSV","*.csv"), ("Tutti i file","*.*")])
        if not percorso_file:
            return
        
        df = pd.read_csv(percorso_file)
            
        lista_utenti = df.to_dict(orient='records')
        i = 0
        for utente in lista_utenti :
            n = utente['nome']
            c = utente['cognome']
            e = utente['email']
            p = utente['password']
            
            try:
                r = requests.get('https://cataas.com/cat', timeout=5)
                if r.status_code == 200:
                    r64 = base64.b64encode(r.content)
                    r64string = r64.decode('utf-8')
                else:
                    r64string = None
                    
                cur.execute(sql_insert, (n, c, e, p, r64string))
                con.connection.commit()
                
                
            except Exception as err:
                messagebox.showerror("Errore", f"Problema tecnico: {err}")
            i +=1
        messagebox.showinfo("Successo", f"Registrazione di {i} completata! Ora fai il login.")
        seleziona_finestra(finestra_login)

    sql_insert = "INSERT INTO utenti (nome, cognome, email, password, immagini) VALUES (%s, %s, %s, %s , %s)"
    immagine = None
    def registrazione():
        n = entry_nome.get()
        c = entry_cognome.get()
        e = entry_email_reg.get()
        p = entry_pass_reg.get()
        
        if not n or not c or not e or not p:
            messagebox.showerror("Errore", "Compila tutti i campi!")
            return

        try:
            r = requests.get('https://cataas.com/cat', timeout=5)
            if r.status_code == 200:
                r64 = base64.b64encode(r.content)
                r64string = r64.decode('utf-8')
            else:
                r64string = None
                
            cur.execute(sql_insert, (n, c, e, p, r64string))
            con.connection.commit()
            messagebox.showinfo("Successo", "Registrazione completata! Ora fai il login.")
            seleziona_finestra(finestra_login)
            
        except Exception as err:
            messagebox.showerror("Errore", f"Problema tecnico: {err}")

    def login():
        e = entry_email_login.get()
        p = entry_pass_login.get()

        cur.execute("SELECT * FROM utenti WHERE email = %s AND password = %s", (e, p))
        utente = cur.fetchone()
        
        if utente:
            global email_corrente
            email_corrente = e 

            if utente[5]:
                seleziona_immagine(utente[5])
            else:
                immagine_profilo.config(text="Nessuna immagine", image="")
            
            messagebox.showinfo("Benvenuto", f"Login effettuato! Ciao {utente[1]}") 
            seleziona_finestra(finestra_area_personale)
        else:
            messagebox.showerror("Errore", "Email o Password errati")

    def seleziona_immagine(immagine_stringa):
        global immagine

        b64 = base64.b64decode(immagine_stringa)

        immagine_come_file = io.BytesIO(b64)

        conversione_jpeg = Image.open(immagine_come_file)

        conversione_jpeg = conversione_jpeg.resize((200,200))

        immagine = ImageTk.PhotoImage(conversione_jpeg)

        immagine_profilo.config(image=immagine)
        immagine_profilo.image = immagine
        return None


    def delete():
        risposta = messagebox.askyesno("Attenzione", "Sei sicuro di voler cancellare il tuo account?")
        if risposta:
            cur.execute("DELETE FROM utenti WHERE email = %s", (email_corrente,))
            con.connection.commit()
            messagebox.showinfo("Fatto", "Account eliminato.")
            seleziona_finestra(finestra_login)

    def logout():
        entry_email_login.delete(0, tk.END)
        entry_pass_login.delete(0, tk.END)
        seleziona_finestra(finestra_login)




    root = tk.Tk()
    root.title("Gestionale Utenti")
    root.geometry("500x500")


    finestra_home = tk.Frame(root, bg="lightblue")
    finestra_reg = tk.Frame(root, bg="lightgreen")
    finestra_login = tk.Frame(root, bg="orange")
    finestra_area_personale = tk.Frame(root, bg="lightyellow")

    def seleziona_finestra(finestra):
        finestra_home.pack_forget()
        finestra_reg.pack_forget()
        finestra_login.pack_forget()
        finestra_area_personale.pack_forget()

        finestra.pack(fill="both", expand=True)


    tk.Label(finestra_home, text="Cosa vuoi fare?", font=("Arial", 14), bg="lightblue").pack(pady=40)
    tk.Button(finestra_home, text="Registrati", command=lambda: seleziona_finestra(finestra_reg), width=20).pack(pady=5)
    tk.Button(finestra_home, text="Accedi", command=lambda: seleziona_finestra(finestra_login), width=20).pack(pady=5)


    tk.Label(finestra_reg, text="REGISTRAZIONE", font=("Arial",14), bg="lightgreen").pack(pady=20)

    tk.Label(finestra_reg, text="Nome:", bg="lightgreen").pack()
    entry_nome = tk.Entry(finestra_reg)
    entry_nome.pack()

    tk.Label(finestra_reg, text="Cognome:", bg="lightgreen").pack()
    entry_cognome = tk.Entry(finestra_reg)
    entry_cognome.pack()

    tk.Label(finestra_reg, text="Email:", bg="lightgreen").pack()
    entry_email_reg = tk.Entry(finestra_reg)
    entry_email_reg.pack()

    tk.Label(finestra_reg, text="Password:", bg="lightgreen").pack()
    entry_pass_reg = tk.Entry(finestra_reg, show="*")
    entry_pass_reg.pack()

    tk.Button(finestra_reg, text="Conferma Registrazione", command=registrazione, width=20).pack(pady=20)
    tk.Button(finestra_reg, text="Indietro", command=lambda: seleziona_finestra(finestra_home)).pack(pady=20)


    tk.Label(finestra_login, text="LOGIN", font=("Arial", 20), bg="orange").pack(pady=20)

    tk.Label(finestra_login, text="Email:", bg="orange").pack()
    entry_email_login = tk.Entry(finestra_login)
    entry_email_login.pack()

    tk.Label(finestra_login, text="Password:", bg="orange").pack()
    entry_pass_login = tk.Entry(finestra_login, show="*") 
    entry_pass_login.pack()


    tk.Button(finestra_login, text="Accedi", command=login, width=20).pack(pady=10)
    tk.Button(finestra_login, text="Non hai un account? Registrati", command=lambda: seleziona_finestra(finestra_reg)).pack(pady=5)
    tk.Button(finestra_login, text="Indietro", command=lambda: seleziona_finestra(finestra_home)).pack(pady=15)



    tk.Label(finestra_area_personale, text="AREA PRIVATA", font=("Arial", 20), bg="lightyellow").pack(pady=30)

    immagine_profilo = tk.Label(finestra_area_personale)
    immagine_profilo.pack(pady=15)


    tk.Button(finestra_area_personale, text="Aggiungi Account", command= lambda : aggiungiaccount()).pack(pady=10)
    tk.Button(finestra_area_personale, text="Elimina il mio Account", command=delete, bg="red", fg="white").pack(pady=10)
    tk.Button(finestra_area_personale, text="Logout", command=logout).pack(pady=10)


    seleziona_finestra(finestra_home)

    root.mainloop()




if __name__ == "__main__":
    x = 0
    while (x !="3"):
        cur = con.cursor
        x = input("Scrivere 1 per usare l'interfaccia grafica, 2 per il server , 3 per chiudere l'applicazione: ")
        if (x=="1"):
            bo()
        elif (x=="2"):
            print("Avvio Server API...")
            print("NOTA: Per fermare il server e tornare al menu, premi CTRL+C nel terminale.")
            server_api.app.run(host='0.0.0.0', port=5000)
        elif (x=="3"):
            break
        elif (x != "1" or x != "2" or x != "3"):
            print("Hai inserito il valore sbagliato, riprova")
            continue