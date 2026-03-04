from PIL import Image, PngImagePlugin

INPUT_PNG = "clean copy/clean img stego_text_01.png"
OUTPUT_PNG = "stego/ztxt/clean_img_ztxt_injected.png"
PAYLOAD_FILE = "payloads/base64/plain_5k_b64.txt"

with open(PAYLOAD_FILE, "r", encoding="utf-8", errors="ignore") as f:
    payload = f.read()

img = Image.open(INPUT_PNG)

meta = PngImagePlugin.PngInfo()
meta.add_text("Comment", payload)  # Pillow may compress → zTXt

img.save(OUTPUT_PNG, pnginfo=meta)

print("zTXt-like compressed metadata injected")