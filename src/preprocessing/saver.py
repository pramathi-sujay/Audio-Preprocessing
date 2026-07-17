from pathlib import Path

import soundfile as sf


def save_audio(file_path, waveform, sample_rate):
    """
    Save a processed audio file.

    Parameters
    ----------
    file_path : str or Path
        Output path of the audio file.
    waveform : numpy.ndarray
        Audio waveform.
    sample_rate : int
        Sample rate of the audio.
    """

    file_path = Path(file_path)

    # Create parent directories if they don't exist
    file_path.parent.mkdir(parents=True, exist_ok=True)

    sf.write(
        file=file_path,
        data=waveform,
        samplerate=sample_rate,
        format="WAV",
    )