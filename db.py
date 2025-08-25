import sqlite3
from config import CFG

def get_conn():
    return sqlite3.connect(CFG["db_path"])

def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS blocks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        transactions TEXT,
        nonce INTEGER,
        hash TEXT,
        previous_hash TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS wallets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        address TEXT,
        balance REAL
    )''')
    conn.commit()
    conn.close()
