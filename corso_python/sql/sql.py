import connessionesql as con
import pandas
import sqlite3
import os
from sqlalchemy import create_engine
import pymysql

cur = con.cursor
dbname = "rubrica"
cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")

cur.execute(f"USE {dbname}")

cur.execute("""
CREATE TABLE IF NOT EXISTS utenti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(256),
    cognome VARCHAR(256),
    email VARCHAR(256),
    password VARCHAR(256)
)
"""
)

