from pathlib import Path

from src.preprocessing.loader import load_audio
from src.preprocessing.mono import convert_to_mono
from src.preprocessing.normalizer import normalize_audio
from src.preprocessing.resampler import resample_audio
from src.preprocessing.saver import save_audio
from src.preprocessing.silence import trim_silence

audio_file = next(Path("Data Collection/Indoor/Baby Crying").glob("*"))

waveform, sr = load_audio(audio_file)
waveform = convert_to_mono(waveform)
waveform, sr = resample_audio(waveform, sr)
waveform = normalize_audio(waveform)
waveform = trim_silence(waveform)

save_audio(
    "Processed Data/test.wav",
    waveform,
    sr,
)

print("Audio saved successfully!")