"""
saver.py

Saves processed audio clips to disk.
"""

from pathlib import Path

import soundfile as sf


def save_audio(
    audio,
    sample_rate: int,
    output_path: Path,
) -> None:
    """
    Save an audio clip as a WAV file.

    Parameters
    ----------
    audio : np.ndarray
        Audio waveform.

    sample_rate : int
        Sample rate.

    output_path : Path
        Destination path of the audio file.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    sf.write(output_path, audio, sample_rate)