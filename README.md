# Metadata-Based Steganalysis of PNG Images Using Machine Learning

## Overview

Digital images can hide covert information not only in pixels but also in **metadata fields**. PNG images support metadata chunks such as `tEXt`, `zTXt`, and `iTXt`, which can be abused to store hidden payloads without modifying the visual content of the image.

This project demonstrates a **proof-of-concept steganalysis system** that detects hidden payloads embedded in PNG metadata using **machine learning**. Instead of analyzing pixel patterns, the approach focuses entirely on metadata characteristics, making it lightweight and interpretable.

The system constructs a **controlled dataset** by injecting encoded payloads into PNG metadata fields and then extracts statistical metadata features to train a classifier capable of distinguishing **clean images from metadata-stego images**.

---

# Key Objectives

- Demonstrate how PNG metadata can be used to hide payloads
- Build a **controlled experimental dataset** containing clean and stego images
- Extract statistical features from metadata
- Train a machine learning model to detect hidden metadata payloads
- Provide a reproducible pipeline for metadata-based steganalysis research

---

# Project Pipeline
Clean PNG Image
        │
        ▼
Payload Generation (plain / base64 / XOR / AES)
        │
        ▼
Metadata Injection (tEXt / zTXt chunks)
        │
        ▼
Labeled Dataset Creation
        │
        ▼
Metadata Feature Extraction
        │
        ▼
Machine Learning Classification


---

# Dataset Structure

dataset/
│
├── clean/
│   └── clean_img.png
│
├── stego_text/
│   └── clean_img_text_injected.png
│
└── stego_ztxt/
    └── clean_img_ztxt_injected.png


Dataset labels are stored in:

metadata/dataset_labels.csv


---

# Extracted Features

The classifier uses metadata-based statistical features such as:

- **Number of metadata keys**
- **Total metadata length**
- **Average metadata value length**
- **Shannon entropy of metadata values**
- **ASCII character ratio**

These features capture **structural anomalies introduced by hidden payloads**.

---

# Machine Learning Model

A **Logistic Regression classifier** is used for proof-of-concept detection.

## Classification Task


Clean PNG vs Stego PNG


The classifier is trained on **metadata feature vectors extracted from each image**.

---

# Repository Structure

png-metadata-steganalysis/
│
├── dataset/
│   ├── clean/
│   ├── stego_text/
│   └── stego_ztxt/
│
├── payloads/
│   ├── plain/
│   ├── base64/
│   ├── xor/
│   └── aes/
│
├── scripts/
│   ├── inject_png_text_chunk_pillow.py
│   ├── inject_png_ztxt_chunk_pillow.py
│   ├── extract_metadata_features.py
│   ├── train_classifier.py
│   ├── xor_encode.py
│   ├── aes_encode.py
│   └── verify_png_text.py
│
├── metadata/
│   ├── dataset_labels.csv
│   ├── features.csv
│   └── payload_manifest.csv
│
├── requirements.txt
└── README.md

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/png-metadata-steganalysis.git
cd png-metadata-steganalysis

Install dependencies:

pip install -r requirements.txt

Running the Pipeline
1️⃣ Extract Metadata Features
python extract_metadata_features.py

This generates:
metadata/features.csv

2️⃣ Train the Classifier
python train_classifier.py

The model evaluates whether an image is clean or contains hidden metadata payloads.

Example Feature Output
image_path,label,num_meta_keys,total_meta_len,avg_value_len,mean_entropy,mean_ascii_ratio
clean/clean_img.png,clean,0,0,0,0,0
stego_text/clean_img_text_injected.png,stego_text,1,264,264,3.62,0.5
stego_ztxt/clean_img_ztxt_injected.png,stego_ztxt,1,13640,13640,3.68,0.5

# Limitations

This project is intended as a research prototype and has several limitations:

Small experimental dataset

Only PNG metadata chunks analyzed

Only basic machine learning models tested

Real-world malware samples are not included

# Future Work

Larger datasets

Additional metadata chunk types (iTXt)

Deep learning based anomaly detection

Integration into digital forensic tools

# Related Work

Research on steganography detection traditionally focuses on pixel-domain steganalysis, where hidden data modifies image statistics. However, metadata-based steganography remains a less explored attack surface.

Several studies have demonstrated the possibility of embedding information in image metadata such as EXIF fields and PNG text chunks. Traditional steganalysis approaches often fail to detect such payloads because they analyze visual content rather than structural metadata.

This project explores a metadata-centric detection approach, using statistical features extracted from metadata fields and machine learning classification to distinguish clean images from metadata-stego images.

This project demonstrates the feasibility of metadata-based steganalysis using machine learning.

# Author

Project developed as part of research exploration in cybersecurity and steganalysis.

# License

This project is released for educational and research purposes.