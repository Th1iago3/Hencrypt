import os
import zlib
import base64
import hashlib

class Encryption:
    def __init__(self):
        self.key = hashlib.sha256(os.urandom(64)).digest()

    def encrypt(self, data):
        d = zlib.compress(data, 9)
        x = bytes(d[i] ^ self.key[i % len(self.key)] for i in range(len(d)))
        return base64.b64encode(x).decode()

    def pack(self):
        return base64.b64encode(self.key).decode()
