import librosa

from src.utils.constants import TRIM_TOP_DB


def trim_silence(waveform):
    """
    Remove leading and trailing silence.
    """

    trimmed_waveform, _ = librosa.effects.trim(
        waveform,
        top_db=TRIM_TOP_DB
    )

    return trimmed_waveform