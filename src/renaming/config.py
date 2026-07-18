"""
config.py

Configuration settings for the renaming module.
"""

from pathlib import Path


# ==========================================================
# Directories
# ==========================================================

INPUT_DIR = Path("Duration Standardized Data")
OUTPUT_DIR = Path("Renamed Data")


# ==========================================================
# Supported Audio Formats
# ==========================================================

SUPPORTED_AUDIO_FORMATS = {
    ".wav",
}


# ==========================================================
# File Naming
# ==========================================================

FILE_NUMBER_PADDING = 3