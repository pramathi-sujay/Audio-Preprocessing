import librosa


def load_audio(file_path: str):
    """
    Load an audio file without modifying it.

    Returns:
        waveform (numpy.ndarray)
        sample_rate (int)
    """

    waveform, sample_rate = librosa.load(
        file_path,
        sr=None,      # Keep original sample rate
        mono=False    # Preserve original channels
    )

    return waveform, sample_rate