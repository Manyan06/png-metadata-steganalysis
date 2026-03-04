import os

KEY = 0x5A

# Directory where this script lives (dataset root)
ROOT = os.path.dirname(os.path.abspath(__file__))

def xor_file(inp, out):
    with open(inp, "rb") as f:
        data = f.read()
    encoded = bytes(b ^ KEY for b in data)
    with open(out, "wb") as f:
        f.write(encoded)

files = [
    (os.path.join(ROOT, "payloads", "plain", "plain_100.txt"),
     os.path.join(ROOT, "payloads", "xor", "plain_100_xor.bin")),

    (os.path.join(ROOT, "payloads", "plain", "plain_1k.txt"),
     os.path.join(ROOT, "payloads", "xor", "plain_1k_xor.bin")),

    (os.path.join(ROOT, "payloads", "plain", "plain_5k.txt"),
     os.path.join(ROOT, "payloads", "xor", "plain_5k_xor.bin")),
]

for src, dst in files:
    xor_file(src, dst)