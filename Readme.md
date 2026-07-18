# Audio Preprocessing Pipeline

A modular audio preprocessing pipeline developed for the AIISH Environmental Sound Detection Project.

This project prepares raw environmental sound recordings for training deep learning models such as YAMNet. The pipeline standardizes audio recordings, organizes the dataset, and generates metadata required for model training.

---

## Project Structure

```text
Audio Preprocessing Pipeline/
│
├── Data Collection/
├── Processed Data/
├── Duration Standardized Data/
├── Renamed Data/
│
├── metadata/
│   └── metadata.csv
│
├── src/
│   ├── inspection/
│   ├── preprocessing/
│   ├── duration/
│   ├── renaming/
│   ├── metadata/
│   └── utils/
│
├── tests/
├── README.md
└── requirements.txt
```

---

## Pipeline Overview

```text
Raw Dataset
      │
      ▼
Inspection
      │
      ▼
Preprocessing
      │
      ▼
Duration Standardization
      │
      ▼
Renaming
      │
      ▼
Metadata Generation
      │
      ▼
Training Dataset
```

---

## Modules

### 1. Dataset Inspection

Inspects the raw dataset and reports:

- Number of classes
- Number of audio files
- Supported file formats
- Empty folders

Run:

```bash
python -m src.inspection.inspect_dataset
```

---

### 2. Audio Preprocessing

Standardizes all raw audio files.

Operations performed:

- Convert stereo to mono
- Resample audio to 16 kHz
- Normalize audio amplitude
- Trim leading and trailing silence

Output:

```
Processed Data/
```

This folder contains uniformly preprocessed audio files that are ready for duration standardization.

Run:

```bash
python -m src.preprocessing.preprocess_dataset
```

---

### 3. Duration Standardization

Ensures consistent recording durations.

Rules:

- Audio ≤ 60 seconds → Keep unchanged
- Audio > 60 seconds → Split into overlapping clips
- Audio > 300 seconds → Flag for manual review

Output:

```
Duration Standardized Data/
```

This folder contains audio recordings after duration standardization while preserving the original folder hierarchy.

Run:

```bash
python -m src.duration.standardize_duration
```

---

### 4. Audio Renaming

Renames every audio file using a standardized naming convention.

Example:

```
baby_crying_001.wav
glass_breaking_015.wav
train_horn_042.wav
```

Output:

```
Renamed Data/
```

This folder contains the final audio dataset with standardized filenames for easier dataset management and training.

Run:

```bash
python -m src.renaming.rename_dataset
```

---

### 5. Metadata Generation

Generates a metadata CSV describing every audio file in the dataset.

Generated columns:

- filename
- filepath
- label
- environment
- duration (in seconds)

Output:

```
metadata/metadata.csv
```

This metadata file is used during dataset analysis and model training.

Run:

```bash
python -m src.metadata.generate_metadata
```

---

## Final Dataset

After the pipeline is completed, the dataset consists of:

```
Renamed Data/
```

and

```
metadata/metadata.csv
```

The audio files are standardized, consistently named, and accompanied by metadata, making the dataset ready for machine learning workflows.

---

## Installation

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Current Status

Completed modules:

- Dataset Inspection
- Audio Preprocessing
- Duration Standardization
- Audio Renaming
- Metadata Generation

---

## License

This project is intended for educational and research purposes.
