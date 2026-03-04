import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

KEY = bytes.fromhex("00112233445566778899aabbccddeeff")
IV  = bytes.fromhex("0102030405060708090a0b0c0d0e0f10")

ROOT = os.path.dirname(os.path.abspath(__file__))

def aes_encrypt(inp, out):
    with open(inp, "rb") as f:
        data = f.read()
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    enc = cipher.encrypt(pad(data, AES.block_size))
    with open(out, "wb") as f:
        f.write(enc)

files = [
    (os.path.join(ROOT, "payloads", "plain", "plain_100.txt"),
     os.path.join(ROOT, "payloads", "aes",   "plain_100_aes.bin")),
    (os.path.join(ROOT, "payloads", "plain", "plain_1k.txt"),
     os.path.join(ROOT, "payloads", "aes",   "plain_1k_aes.bin")),
    (os.path.join(ROOT, "payloads", "plain", "plain_5k.txt"),
     os.path.join(ROOT, "payloads", "aes",   "plain_5k_aes.bin")),
]

for src, dst in files:
    aes_encrypt(src, dst)