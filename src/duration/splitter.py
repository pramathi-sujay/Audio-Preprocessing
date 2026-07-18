"""
splitter.py

Splits an audio signal into overlapping windows.
"""

import numpy as np

from .config import (
    WINDOW_DURATION,
    OVERLAP_DURATION,
    MIN_CLIP_DURATION,
)


def split_audio(
    audio: np.ndarray,
    sample_rate: int,
    window_duration: float = WINDOW_DURATION,
    overlap_duration: float = OVERLAP_DURATION,
) -> list[np.ndarray]:
    """
    Split an audio signal into overlapping clips.

    Parameters
    ----------
    audio : np.ndarray
        Audio waveform.

    sample_rate : int
        Sampling rate of the audio.

    window_duration : float
        Length of each clip in seconds.

    overlap_duration : float
        Overlap between consecutive clips in seconds.

    Returns
    -------
    list[np.ndarray]
        List of audio clips.
    """

    if overlap_duration >= window_duration:
        raise ValueError(
            "Overlap duration must be smaller than window duration."
        )

    window_samples = int(window_duration * sample_rate)
    overlap_samples = int(overlap_duration * sample_rate)
    stride = window_samples - overlap_samples

    min_clip_samples = int(MIN_CLIP_DURATION * sample_rate)

    clips = []

    start = 0

    while start < len(audio):

        end = start + window_samples

        clip = audio[start:end]

        # Ignore extremely small leftover clips
        if len(clip) >= min_clip_samples:
            clips.append(clip)

        start += stride

    return clips