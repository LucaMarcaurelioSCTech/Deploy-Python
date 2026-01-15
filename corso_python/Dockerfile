FROM python:3.12-slim

WORKDIR /app

# Copia e installa i requisiti
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il progetto (inclusa la cartella sql)
COPY . .

EXPOSE 5000

# COMANDO DI AVVIO
# Usiamo "python -m gunicorn" per essere sicuri che lo trovi.
# --chdir /app imposta la cartella base per sicurezza
# sql.server_api:app dice: cartella "sql", file "server_api.py", app Flask.
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "sql.server_api:app"]