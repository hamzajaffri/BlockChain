import os, json, base64
from crypto_utils import encrypt_json, decrypt_json, sha256_hex
from db import get_conn

WALLET_FILE = "wallet_hd.enc"

def create_wallet(password):
    if os.path.exists(WALLET_FILE):
        print("Wallet exists! Use load_wallet()")
        return
    seed = os.urandom(32).hex()
    priv = sha256_hex(seed)
    wallet = {"seed": seed, "priv": priv, "balance": 0.0}
    enc = encrypt_json(wallet, password)
    with open(WALLET_FILE, "wb") as f:
        f.write(enc)
    print(f"Wallet created! Save your seed: {seed}")

def load_wallet(password):
    with open(WALLET_FILE, "rb") as f:
        data = f.read()
    return decrypt_json(data, password)
