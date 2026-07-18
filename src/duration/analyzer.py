"""
analyzer.py

Analyzes the duration of an audio file and determines
whether it should be kept, split, or flagged.
"""

from enum import Enum
from pathlib import Path

import soundfile as sf

from .config import WINDOW_DURATION, VERY_LONG_DURATION


# ==========================================================
# Duration Actions
# ==========================================================

class DurationAction(Enum):
    KEEP = "keep"
    SPLIT = "split"
    FLAG = "flag"


# ==========================================================
# Duration Analyzer
# ==========================================================

def analyze_duration(audio_path: Path) -> tuple[DurationAction, float]:
    """
    Analyze the duration of an audio file.

    Parameters
    ----------
    audio_path : Path
        Path to the audio file.

    Returns
    -------
    tuple
        (DurationAction, duration_in_seconds)

        KEEP  -> Audio duration <= WINDOW_DURATION
        SPLIT -> WINDOW_DURATION < Audio duration <= VERY_LONG_DURATION
        FLAG  -> Audio duration > VERY_LONG_DURATION
    """

    info = sf.info(audio_path)
    duration = info.duration

    if duration <= WINDOW_DURATION:
        return DurationAction.KEEP, duration

    elif duration <= VERY_LONG_DURATION:
        return DurationAction.SPLIT, duration

    else:
        return DurationAction.FLAG, duration