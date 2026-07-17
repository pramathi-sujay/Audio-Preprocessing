import librosa


def convert_to_mono(waveform):
    """
    Convert stereo audio to mono.
    If already mono, return unchanged.
    """

    if waveform.ndim == 1:
        return waveform

    return librosa.to_mono(waveform)