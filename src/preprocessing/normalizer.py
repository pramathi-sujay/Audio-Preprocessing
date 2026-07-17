import numpy as np


def normalize_audio(waveform):
    """
    Normalize the waveform to the range [-1, 1].
    """

    peak = np.max(np.abs(waveform))

    if peak == 0:
        return waveform

    return waveform / peak