import pandas
import sqlite3
import os
from sqlalchemy import create_engine
import pymysql
host_db = 'host.docker.internal'

connection = pymysql.connect (    
host = host_db,
user = 'root',
password = '1234',
database = 'rubrica',
port = 3306 )

cursor = connection.cursor()

