import requests
from PIL import Image
from io import BytesIO

try:
       
    r = requests.get('https://cataas.com/cat', timeout=5)

    if r.status_code == 200:
            
            # 2. Carica i bytes in Pillow senza salvare file intermedi
            # BytesIO trasforma i bytes in un "file virtuale" in memoria
            image = Image.open(BytesIO(r.content))
            
            # 3. Conversione fondamentale: convert("RGB")
            # Se cataas ti manda un PNG con sfondo trasparente (RGBA),
            # il salvataggio in JPEG fallirebbe perché il JPEG non supporta la trasparenza.
            # Questo passaggio forza l'immagine a diventare opaca (RGB).
            image = image.convert("RGB")
            
            # 4. Salva il risultato finale
            image.save("gatto_convertito.jpg", "JPEG", quality=90)
            print("Successo! Immagine salvata come gatto_convertito.jpg")
            
    else:
        print(f"Errore nella richiesta: {r.status_code}")

except Exception as e:
    print(f"Si è verificato un errore: {e}")