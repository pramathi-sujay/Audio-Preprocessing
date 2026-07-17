import librosa


TARGET_SAMPLE_RATE = 16000


def resample_audio(waveform, sample_rate):
    """
    Resample audio to the target sample rate.
    """

    if sample_rate == TARGET_SAMPLE_RATE:
        return waveform, sample_rate

    waveform = librosa.resample(
        waveform,
        orig_sr=sample_rate,
        target_sr=TARGET_SAMPLE_RATE,
    )

    return waveform, TARGET_SAMPLE_RATE