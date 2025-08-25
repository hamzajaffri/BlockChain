import json, time
from db import get_conn
from crypto_utils import sha256_hex, merkle_root
from config import CFG

def add_block(transactions):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT hash FROM blocks ORDER BY id DESC LIMIT 1")
    prev = c.fetchone()
    prev_hash = prev[0] if prev else '0'*64
    block = {
        "timestamp": time.time(),
        "transactions": transactions,
        "nonce": 0,
        "previous_hash": prev_hash
    }
    target = '0'*CFG["difficulty"]
    while True:
        block["hash"] = sha256_hex(json.dumps(block))
        if block["hash"][:CFG["difficulty"]] == target:
            break
        block["nonce"] += 1
    c.execute("INSERT INTO blocks (timestamp, transactions, nonce, hash, previous_hash) VALUES (?,?,?,?,?)",
              (block["timestamp"], json.dumps(transactions), block["nonce"], block["hash"], block["previous_hash"]))
    conn.commit()
    conn.close()
    return block

def mine_one():
    txs = [{"amount": CFG["reward"], "receiver": "local_wallet", "sender": "0"}]
    return add_block(txs)

def get_balance(address):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT transactions FROM blocks")
    txs = c.fetchall()
    balance = 0.0
    for t in txs:
        for tx in json.loads(t[0]):
            if tx["receiver"] == address:
                balance += tx["amount"]
            if tx["sender"] == address:
                balance -= tx["amount"]
    conn.close()
    return balance
