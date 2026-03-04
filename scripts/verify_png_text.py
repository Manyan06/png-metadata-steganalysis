from PIL import Image

img = Image.open("stego/ztxt/clean_img_ztxt_injected.png")
info = img.info

print("Metadata keys:", info.keys())

if "Comment" in info:
    print("Compressed metadata FOUND (zTXt behavior)")
    print("Payload length:", len(info["Comment"]))
    print("First 60 chars:", info["Comment"][:60])
else:
    print("No compressed metadata found")