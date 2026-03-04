import csv
import math
from PIL import Image

LABELS_FILE = "dataset_labels.csv"
OUTPUT_FILE = "features.csv"


def entropy(s):
    if not s:
        return 0.0
    probs = [s.count(c) / len(s) for c in set(s)]
    return -sum(p * math.log2(p) for p in probs)


def ascii_ratio(s):
    if not s:
        return 0.0
    ascii_count = sum(1 for c in s if 32 <= ord(c) <= 126)
    return ascii_count / len(s)


rows = []

with open(LABELS_FILE, newline="") as f:
    reader = csv.DictReader(f)
    for r in reader:
        img_path = r["image_path"]
        label = r["label"]

        img = Image.open(img_path)
        info = img.info

        values = [v for v in info.values() if isinstance(v, str)]

        num_keys = len(values)
        total_len = sum(len(v) for v in values)
        avg_len = total_len / num_keys if num_keys else 0

        entropies = [entropy(v) for v in values]
        ascii_ratios = [ascii_ratio(v) for v in values]

        mean_entropy = sum(entropies) / len(entropies) if entropies else 0
        mean_ascii = sum(ascii_ratios) / len(ascii_ratios) if ascii_ratios else 0

        rows.append([
            img_path,
            label,
            num_keys,
            total_len,
            avg_len,
            mean_entropy,
            mean_ascii
        ])


with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "image_path", "label",
        "num_meta_keys", "total_meta_len", "avg_value_len",
        "mean_entropy", "mean_ascii_ratio"
    ])
    writer.writerows(rows)

print("Feature extraction completed → features.csv")