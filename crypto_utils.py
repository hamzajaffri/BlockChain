import hashlib
import json
import os
import base64
from cryptography.fernet import Fernet

def sha256_hex(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def encrypt_json(obj, password):
    key = hashlib.sha256(password.encode()).digest()
    f = Fernet(base64.urlsafe_b64encode(key[:32]))
    return f.encrypt(json.dumps(obj).encode())

def decrypt_json(data, password):
    key = hashlib.sha256(password.encode()).digest()
    f = Fernet(base64.urlsafe_b64encode(key[:32]))
    return json.loads(f.decrypt(data).decode())

def merkle_root(txids):
    layer = [bytes.fromhex(x) for x in txids]
    while len(layer) > 1:
        if len(layer) % 2 != 0:
            layer.append(layer[-1])
        layer = [hashlib.sha256(layer[i] + layer[i+1]).digest() for i in range(0, len(layer), 2)]
    return layer[0].hex() if layer else '0'*64
