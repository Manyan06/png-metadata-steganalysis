from PIL import Image, PngImagePlugin

# Paths
INPUT_PNG = "clean copy/clean img stego_text_01.png"
OUTPUT_PNG = "clean copy/clean_img_text_injected.png"
PAYLOAD_FILE = "payloads/base64/plain_100_b64.txt"

# Read payload safely (force UTF-8, ignore junk if any)
with open(PAYLOAD_FILE, "r", encoding="utf-8", errors="ignore") as f:
    payload = f.read()

# Load image
img = Image.open(INPUT_PNG)

# Create PNG metadata (tEXt chunk)
meta = PngImagePlugin.PngInfo()
meta.add_text("Description", payload)

# Save new image with metadata
img.save(OUTPUT_PNG, pnginfo=meta)

print("tEXt metadata injected successfully")